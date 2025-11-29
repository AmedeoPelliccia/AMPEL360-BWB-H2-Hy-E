# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Alert Processor
OFEC-23-95-67-24 - Ground Receiver

This module processes envelope data and generates alerts.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Callable
from enum import Enum
import time
import logging


# Set up module logger
logger = logging.getLogger(__name__)


class AlertSeverity(Enum):
    """Alert severity levels."""
    INFO = 0
    WARNING = 1
    CRITICAL = 2


class AlertType(Enum):
    """Alert type enumeration."""
    ADVISORY_CHANGE = "advisory_change"
    EXCEEDANCE = "exceedance"
    TREND_WARNING = "trend_warning"
    DATA_GAP = "data_gap"
    AIRCRAFT_OFFLINE = "aircraft_offline"


@dataclass
class Alert:
    """Alert record."""
    alert_id: str
    alert_type: AlertType
    severity: AlertSeverity
    aircraft_id: str
    flight_phase: str
    message: str
    details: Dict
    timestamp: float


class AlertProcessor:
    """
    Processes OFEC data and generates alerts.
    
    Monitors advisory levels, detects exceedances, and generates
    alerts for ground operators.
    """
    
    # Alert thresholds
    WARNING_MARGIN_PCT = 25.0
    CRITICAL_MARGIN_PCT = 10.0
    
    # Data gap threshold (seconds)
    DATA_GAP_THRESHOLD = 30.0
    
    def __init__(
        self,
        alert_callback: Optional[Callable[[Alert], None]] = None
    ):
        """
        Initialize the alert processor.
        
        Args:
            alert_callback: Function to call when alert is generated
        """
        self._alert_callback = alert_callback
        self._last_seen: Dict[str, float] = {}
        self._current_levels: Dict[str, str] = {}
        self._alerts: List[Alert] = []
        self._alert_count = 0
    
    def process(self, message: Dict) -> List[Alert]:
        """
        Process a message and generate any alerts.
        
        Args:
            message: Validated OFEC message
            
        Returns:
            List of generated alerts
        """
        aircraft_id = message["aircraft_id"]
        alerts = []
        
        # Update last seen
        self._last_seen[aircraft_id] = time.time()
        
        # Check advisory level changes
        advisory = message.get("advisory", {})
        new_level = advisory.get("level", "NORMAL")
        old_level = self._current_levels.get(aircraft_id, "NORMAL")
        
        if new_level != old_level:
            alert = self._create_advisory_alert(
                aircraft_id, message["flight_phase"],
                old_level, new_level, advisory
            )
            alerts.append(alert)
        
        self._current_levels[aircraft_id] = new_level
        
        # Check for exceedances in margins
        margins = message.get("margins", {})
        exceedance_alerts = self._check_exceedances(
            aircraft_id, message["flight_phase"], margins
        )
        alerts.extend(exceedance_alerts)
        
        # Store alerts and trigger callback
        for alert in alerts:
            self._alerts.append(alert)
            self._alert_count += 1
            if self._alert_callback:
                self._alert_callback(alert)
        
        return alerts
    
    def _create_advisory_alert(
        self,
        aircraft_id: str,
        flight_phase: str,
        old_level: str,
        new_level: str,
        advisory: Dict
    ) -> Alert:
        """Create an advisory level change alert."""
        severity = self._level_to_severity(new_level)
        
        return Alert(
            alert_id=f"ADV-{self._alert_count + 1}",
            alert_type=AlertType.ADVISORY_CHANGE,
            severity=severity,
            aircraft_id=aircraft_id,
            flight_phase=flight_phase,
            message=f"Advisory level changed: {old_level} → {new_level}",
            details={
                "old_level": old_level,
                "new_level": new_level,
                "active_advisories": advisory.get("active_advisories", []),
                "trend": advisory.get("trend", "UNKNOWN")
            },
            timestamp=time.time()
        )
    
    def _check_exceedances(
        self,
        aircraft_id: str,
        flight_phase: str,
        margins: Dict
    ) -> List[Alert]:
        """Check for margin exceedances."""
        alerts = []
        
        margin_checks = [
            ("alpha", "margin_pct"),
            ("speed", "margin_low_pct"),
            ("speed", "margin_high_pct"),
            ("load_factor", "margin_positive_pct"),
            ("bank_angle", "margin_pct"),
            ("altitude", "margin_pct")
        ]
        
        for margin_type, margin_field in margin_checks:
            margin_data = margins.get(margin_type, {})
            margin_pct = margin_data.get(margin_field)
            
            # Log warning if margin field is missing - may indicate sensor or pipeline issue
            if margin_pct is None:
                logger.warning(
                    f"Missing margin field '{margin_field}' for type '{margin_type}' - "
                    f"possible sensor or data pipeline issue"
                )
                continue  # Skip processing for missing data rather than masking it
            
            if margin_pct < 0:
                # Exceedance
                alerts.append(Alert(
                    alert_id=f"EXC-{self._alert_count + len(alerts) + 1}",
                    alert_type=AlertType.EXCEEDANCE,
                    severity=AlertSeverity.CRITICAL,
                    aircraft_id=aircraft_id,
                    flight_phase=flight_phase,
                    message=f"Exceedance: {margin_type} ({margin_pct:.1f}%)",
                    details={
                        "margin_type": margin_type,
                        "margin_pct": margin_pct,
                        "margin_data": margin_data
                    },
                    timestamp=time.time()
                ))
        
        return alerts
    
    def _level_to_severity(self, level: str) -> AlertSeverity:
        """Convert advisory level to alert severity."""
        mapping = {
            "NORMAL": AlertSeverity.INFO,
            "CAUTION": AlertSeverity.WARNING,
            "WARNING": AlertSeverity.WARNING,
            "CRITICAL": AlertSeverity.CRITICAL
        }
        return mapping.get(level, AlertSeverity.INFO)
    
    def check_data_gaps(self) -> List[Alert]:
        """
        Check for aircraft that haven't reported recently.
        
        Returns:
            List of data gap alerts
        """
        alerts = []
        current_time = time.time()
        
        for aircraft_id, last_time in self._last_seen.items():
            gap = current_time - last_time
            if gap > self.DATA_GAP_THRESHOLD:
                alerts.append(Alert(
                    alert_id=f"GAP-{self._alert_count + len(alerts) + 1}",
                    alert_type=AlertType.DATA_GAP,
                    severity=AlertSeverity.WARNING,
                    aircraft_id=aircraft_id,
                    flight_phase="UNKNOWN",
                    message=f"No data received for {gap:.0f} seconds",
                    details={"gap_seconds": gap},
                    timestamp=current_time
                ))
        
        return alerts
    
    @property
    def alert_count(self) -> int:
        """Get total alerts generated."""
        return self._alert_count
    
    @property
    def recent_alerts(self) -> List[Alert]:
        """Get recent alerts (last 100)."""
        return self._alerts[-100:]

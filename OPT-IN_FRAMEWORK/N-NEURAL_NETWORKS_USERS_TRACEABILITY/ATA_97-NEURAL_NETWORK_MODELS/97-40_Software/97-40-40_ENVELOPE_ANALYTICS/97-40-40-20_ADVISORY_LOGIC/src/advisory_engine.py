"""
Advisory Engine
OFEC-97-40-40-20 - Envelope Analytics

This module provides the main advisory generation logic.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional
import time


class AdvisoryLevel(Enum):
    """Advisory level enumeration."""
    NORMAL = 0
    CAUTION = 1
    WARNING = 2
    CRITICAL = 3


class TrendDirection(Enum):
    """Trend direction enumeration."""
    IMPROVING = -1
    STABLE = 0
    DEGRADING = 1


@dataclass
class Advisory:
    """Individual advisory information."""
    parameter: str
    level: AdvisoryLevel
    margin_pct: float
    message: str
    trend: TrendDirection
    timestamp: float


@dataclass
class AdvisoryState:
    """Complete advisory state."""
    overall_level: AdvisoryLevel
    active_advisories: List[Advisory]
    trend: TrendDirection
    timestamp: float


class AdvisoryEngine:
    """
    Main advisory generation engine.
    
    Processes margin data and generates appropriate advisories
    with hysteresis to prevent oscillation.
    """
    
    # Threshold percentages
    NORMAL_THRESHOLD = 50.0
    CAUTION_THRESHOLD = 25.0
    WARNING_THRESHOLD = 10.0
    
    # Hysteresis values (percentage points)
    HYSTERESIS_NORMAL = 5.0
    HYSTERESIS_CAUTION = 3.0
    HYSTERESIS_WARNING = 2.0
    
    # Message templates
    MESSAGES = {
        "alpha": {
            AdvisoryLevel.CAUTION: "AOA margin reduced - monitor airspeed",
            AdvisoryLevel.WARNING: "Low AOA margin - increase airspeed",
            AdvisoryLevel.CRITICAL: "AOA critical - take immediate action"
        },
        "speed_low": {
            AdvisoryLevel.CAUTION: "Approaching minimum speed",
            AdvisoryLevel.WARNING: "Low speed margin - increase thrust",
            AdvisoryLevel.CRITICAL: "Underspeed - add thrust immediately"
        },
        "speed_high": {
            AdvisoryLevel.CAUTION: "Approaching maximum speed",
            AdvisoryLevel.WARNING: "High speed - reduce thrust",
            AdvisoryLevel.CRITICAL: "Overspeed - reduce thrust now"
        },
        "load_factor": {
            AdvisoryLevel.CAUTION: "Elevated G-load",
            AdvisoryLevel.WARNING: "High G-load - reduce maneuver",
            AdvisoryLevel.CRITICAL: "G-limit - unload immediately"
        },
        "bank_angle": {
            AdvisoryLevel.CAUTION: "Steep bank angle",
            AdvisoryLevel.WARNING: "Bank approaching limit",
            AdvisoryLevel.CRITICAL: "Bank limit - reduce roll"
        },
        "altitude": {
            AdvisoryLevel.CAUTION: "Approaching service ceiling",
            AdvisoryLevel.WARNING: "Near altitude limit",
            AdvisoryLevel.CRITICAL: "At ceiling - descend"
        }
    }
    
    def __init__(self):
        """Initialize the advisory engine."""
        self._current_levels: Dict[str, AdvisoryLevel] = {}
        self._last_state: Optional[AdvisoryState] = None
    
    def process_margins(self, margins: Dict) -> AdvisoryState:
        """
        Process margin data and generate advisories.
        
        Args:
            margins: Dictionary containing all margin values
            
        Returns:
            Complete advisory state
        """
        advisories = []
        timestamp = time.time()
        
        # Process each margin type
        margin_params = [
            ("alpha", margins.get("alpha", {}).get("margin_pct", 100)),
            ("speed_low", margins.get("speed", {}).get("margin_low_pct", 100)),
            ("speed_high", margins.get("speed", {}).get("margin_high_pct", 100)),
            ("load_factor", min(
                margins.get("load_factor", {}).get("margin_positive_pct", 100),
                margins.get("load_factor", {}).get("margin_negative_pct", 100)
            )),
            ("bank_angle", margins.get("bank_angle", {}).get("margin_pct", 100)),
            ("altitude", margins.get("altitude", {}).get("margin_pct", 100))
        ]
        
        for param_name, margin_pct in margin_params:
            level = self._determine_level(param_name, margin_pct)
            
            if level != AdvisoryLevel.NORMAL:
                message = self.MESSAGES.get(param_name, {}).get(
                    level, f"{param_name} margin low"
                )
                
                advisories.append(Advisory(
                    parameter=param_name,
                    level=level,
                    margin_pct=margin_pct,
                    message=message,
                    trend=TrendDirection.STABLE,  # Trend set by TrendAnalyzer
                    timestamp=timestamp
                ))
        
        # Determine overall level (worst case)
        if advisories:
            max_level_value = max(a.level.value for a in advisories)
            overall_level = AdvisoryLevel(max_level_value)
        else:
            overall_level = AdvisoryLevel.NORMAL
        
        # Determine overall trend
        overall_trend = self._determine_overall_trend(advisories)
        
        state = AdvisoryState(
            overall_level=overall_level,
            active_advisories=advisories,
            trend=overall_trend,
            timestamp=timestamp
        )
        
        self._last_state = state
        return state
    
    def _determine_level(
        self, 
        param_name: str, 
        margin_pct: float
    ) -> AdvisoryLevel:
        """
        Determine advisory level with hysteresis.
        
        Args:
            param_name: Parameter name
            margin_pct: Current margin percentage
            
        Returns:
            Advisory level
        """
        current_level = self._current_levels.get(param_name, AdvisoryLevel.NORMAL)
        
        # Determine new level based on thresholds
        if margin_pct < 0:
            new_level = AdvisoryLevel.CRITICAL
        elif margin_pct < self.WARNING_THRESHOLD:
            new_level = AdvisoryLevel.WARNING
        elif margin_pct < self.CAUTION_THRESHOLD:
            new_level = AdvisoryLevel.CAUTION
        elif margin_pct < self.NORMAL_THRESHOLD:
            new_level = AdvisoryLevel.CAUTION
        else:
            new_level = AdvisoryLevel.NORMAL
        
        # Apply hysteresis for level reduction
        if new_level.value < current_level.value:
            # Require extra margin to reduce level
            hysteresis = {
                AdvisoryLevel.CAUTION: self.HYSTERESIS_WARNING,
                AdvisoryLevel.WARNING: self.HYSTERESIS_CAUTION,
                AdvisoryLevel.CRITICAL: self.HYSTERESIS_NORMAL
            }.get(current_level, 0)
            
            if margin_pct < self._get_threshold(current_level) + hysteresis:
                new_level = current_level
        
        self._current_levels[param_name] = new_level
        return new_level
    
    def _get_threshold(self, level: AdvisoryLevel) -> float:
        """Get threshold for a given level."""
        thresholds = {
            AdvisoryLevel.NORMAL: self.NORMAL_THRESHOLD,
            AdvisoryLevel.CAUTION: self.CAUTION_THRESHOLD,
            AdvisoryLevel.WARNING: self.WARNING_THRESHOLD,
            AdvisoryLevel.CRITICAL: 0
        }
        return thresholds.get(level, 0)
    
    def _determine_overall_trend(
        self, 
        advisories: List[Advisory]
    ) -> TrendDirection:
        """Determine overall trend from individual advisories."""
        if not advisories:
            return TrendDirection.STABLE
        
        trends = [a.trend.value for a in advisories]
        avg_trend = sum(trends) / len(trends)
        
        if avg_trend < -0.3:
            return TrendDirection.IMPROVING
        elif avg_trend > 0.3:
            return TrendDirection.DEGRADING
        else:
            return TrendDirection.STABLE
    
    @property
    def last_state(self) -> Optional[AdvisoryState]:
        """Get last advisory state."""
        return self._last_state

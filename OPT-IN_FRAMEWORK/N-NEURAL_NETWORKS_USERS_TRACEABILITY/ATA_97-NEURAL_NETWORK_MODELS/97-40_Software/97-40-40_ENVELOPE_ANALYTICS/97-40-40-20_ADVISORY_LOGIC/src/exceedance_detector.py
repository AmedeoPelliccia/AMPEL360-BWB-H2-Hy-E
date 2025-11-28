"""
Exceedance Detector
OFEC-97-40-40-20 - Envelope Analytics

This module detects and logs envelope exceedances.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional
import time


class ExceedanceSeverity(Enum):
    """Exceedance severity levels."""
    MINOR = 0      # At limit
    MODERATE = 1   # 5% beyond
    SEVERE = 2     # 10% beyond


@dataclass
class Exceedance:
    """Exceedance event record."""
    parameter: str
    severity: ExceedanceSeverity
    margin_pct: float
    peak_value: float
    limit_value: float
    start_time: float
    end_time: Optional[float] = None
    duration_sec: float = 0.0


class ExceedanceDetector:
    """
    Detects and logs envelope exceedances.
    
    Tracks when parameters exceed their limits and records
    the severity, duration, and peak values.
    """
    
    # Severity thresholds (margin percentage)
    MINOR_THRESHOLD = 0.0
    MODERATE_THRESHOLD = -5.0
    SEVERE_THRESHOLD = -10.0
    
    # Debounce time (seconds)
    DEBOUNCE_SEC = 0.1
    
    def __init__(self):
        """Initialize the exceedance detector."""
        self._active_exceedances: Dict[str, Exceedance] = {}
        self._history: List[Exceedance] = []
        self._last_detection: Dict[str, float] = {}
    
    def check(
        self,
        parameter: str,
        margin_pct: float,
        current_value: float,
        limit_value: float
    ) -> Optional[Exceedance]:
        """
        Check for exceedance and update state.
        
        Args:
            parameter: Parameter name
            margin_pct: Current margin percentage
            current_value: Current parameter value
            limit_value: Limit value
            
        Returns:
            Exceedance object if detected, None otherwise
        """
        timestamp = time.time()
        
        # Check debounce
        last_time = self._last_detection.get(parameter, 0)
        if timestamp - last_time < self.DEBOUNCE_SEC:
            return self._active_exceedances.get(parameter)
        
        self._last_detection[parameter] = timestamp
        
        if margin_pct < self.MINOR_THRESHOLD:
            # Exceedance detected
            severity = self._determine_severity(margin_pct)
            
            if parameter in self._active_exceedances:
                # Update existing exceedance
                exceedance = self._active_exceedances[parameter]
                
                # Track peak
                if margin_pct < (exceedance.limit_value - exceedance.peak_value):
                    exceedance.peak_value = current_value
                
                # Update severity if worse
                if severity.value > exceedance.severity.value:
                    exceedance.severity = severity
                
                exceedance.margin_pct = margin_pct
                exceedance.duration_sec = timestamp - exceedance.start_time
                
            else:
                # New exceedance
                exceedance = Exceedance(
                    parameter=parameter,
                    severity=severity,
                    margin_pct=margin_pct,
                    peak_value=current_value,
                    limit_value=limit_value,
                    start_time=timestamp
                )
                self._active_exceedances[parameter] = exceedance
            
            return exceedance
        
        else:
            # No exceedance - close any active one
            if parameter in self._active_exceedances:
                exceedance = self._active_exceedances.pop(parameter)
                exceedance.end_time = timestamp
                exceedance.duration_sec = timestamp - exceedance.start_time
                self._history.append(exceedance)
            
            return None
    
    def _determine_severity(self, margin_pct: float) -> ExceedanceSeverity:
        """Determine exceedance severity based on margin."""
        if margin_pct < self.SEVERE_THRESHOLD:
            return ExceedanceSeverity.SEVERE
        elif margin_pct < self.MODERATE_THRESHOLD:
            return ExceedanceSeverity.MODERATE
        else:
            return ExceedanceSeverity.MINOR
    
    @property
    def active_exceedances(self) -> Dict[str, Exceedance]:
        """Get currently active exceedances."""
        return self._active_exceedances.copy()
    
    @property
    def history(self) -> List[Exceedance]:
        """Get exceedance history."""
        return self._history.copy()
    
    def clear_history(self):
        """Clear exceedance history."""
        self._history.clear()
    
    def has_active_exceedance(self, parameter: str = None) -> bool:
        """
        Check if there are active exceedances.
        
        Args:
            parameter: Specific parameter to check (None = any)
        """
        if parameter is None:
            return len(self._active_exceedances) > 0
        return parameter in self._active_exceedances

"""
Trend Analyzer
OFEC-97-40-40-20 - Envelope Analytics

This module analyzes margin trends over time.
"""

from collections import deque
from dataclasses import dataclass
from enum import Enum
from typing import Dict
import time


class TrendDirection(Enum):
    """Trend direction enumeration."""
    IMPROVING = -1
    STABLE = 0
    DEGRADING = 1


@dataclass
class TrendResult:
    """Trend analysis result."""
    parameter: str
    direction: TrendDirection
    rate: float  # Change per second
    confidence: float  # 0-1
    window_seconds: float


class TrendAnalyzer:
    """
    Analyzes margin trends over configurable time windows.
    
    Uses moving average and linear regression to determine
    if margins are improving, stable, or degrading.
    """
    
    # Default configuration
    DEFAULT_WINDOW_SAMPLES = 50
    IMPROVING_THRESHOLD = -0.5  # pct/sec (negative = improving)
    DEGRADING_THRESHOLD = 0.5   # pct/sec (positive = degrading)
    
    def __init__(self, window_samples: int = DEFAULT_WINDOW_SAMPLES):
        """
        Initialize the trend analyzer.
        
        Args:
            window_samples: Number of samples to use for trend calculation
        """
        self.window_samples = window_samples
        self._history: Dict[str, deque] = {}
    
    def update(self, parameter: str, margin_pct: float, timestamp: float = None) -> TrendResult:
        """
        Update trend analysis with new margin value.
        
        Args:
            parameter: Parameter name
            margin_pct: Current margin percentage
            timestamp: Sample timestamp (uses current time if None)
            
        Returns:
            Trend analysis result
        """
        if timestamp is None:
            timestamp = time.time()
        
        # Initialize history for new parameters
        if parameter not in self._history:
            self._history[parameter] = deque(maxlen=self.window_samples)
        
        # Add sample to history
        self._history[parameter].append((timestamp, margin_pct))
        
        # Calculate trend
        return self._calculate_trend(parameter)
    
    def _calculate_trend(self, parameter: str) -> TrendResult:
        """
        Calculate trend for a parameter.
        
        Uses linear regression on the sample history.
        """
        history = self._history.get(parameter, deque())
        
        if len(history) < 2:
            return TrendResult(
                parameter=parameter,
                direction=TrendDirection.STABLE,
                rate=0.0,
                confidence=0.0,
                window_seconds=0.0
            )
        
        # Extract timestamps and values
        times = [s[0] for s in history]
        values = [s[1] for s in history]
        
        # Calculate time span
        time_span = times[-1] - times[0]
        if time_span <= 0:
            return TrendResult(
                parameter=parameter,
                direction=TrendDirection.STABLE,
                rate=0.0,
                confidence=0.0,
                window_seconds=0.0
            )
        
        # Simple linear regression
        n = len(times)
        t_mean = sum(times) / n
        v_mean = sum(values) / n
        
        numerator = sum((t - t_mean) * (v - v_mean) for t, v in zip(times, values))
        denominator = sum((t - t_mean) ** 2 for t in times)
        
        if denominator == 0:
            slope = 0.0
        else:
            slope = numerator / denominator
        
        # Slope represents margin change over time:
        # - Positive slope means margin is increasing (moving away from limit) = improving
        # - Negative slope means margin is decreasing (approaching limit) = degrading
        # The rate is kept as-is: positive rate = margin improving, negative rate = margin degrading
        # This aligns with the threshold interpretation where:
        # - rate < IMPROVING_THRESHOLD (negative threshold) triggers IMPROVING
        # - rate > DEGRADING_THRESHOLD (positive threshold) triggers DEGRADING
        margin_change_rate = slope
        
        # Calculate confidence (R-squared)
        if n > 2:
            ss_res = sum((v - (v_mean + slope * (t - t_mean))) ** 2 
                        for t, v in zip(times, values))
            ss_tot = sum((v - v_mean) ** 2 for v in values)
            confidence = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
            confidence = max(0, min(1, confidence))
        else:
            confidence = 0.5
        
        # Determine direction based on margin change rate:
        # - rate > DEGRADING_THRESHOLD (positive) means margin is increasing = IMPROVING
        # - rate < IMPROVING_THRESHOLD (negative) means margin is decreasing = DEGRADING
        if margin_change_rate > self.DEGRADING_THRESHOLD:
            direction = TrendDirection.IMPROVING
        elif margin_change_rate < self.IMPROVING_THRESHOLD:
            direction = TrendDirection.DEGRADING
        else:
            direction = TrendDirection.STABLE
        
        return TrendResult(
            parameter=parameter,
            direction=direction,
            rate=round(margin_change_rate, 3),
            confidence=round(confidence, 2),
            window_seconds=round(time_span, 1)
        )
    
    def get_all_trends(self) -> Dict[str, TrendResult]:
        """Get current trends for all tracked parameters."""
        return {param: self._calculate_trend(param) 
                for param in self._history}
    
    def clear(self, parameter: str = None):
        """
        Clear trend history.
        
        Args:
            parameter: Parameter to clear (None = clear all)
        """
        if parameter is None:
            self._history.clear()
        elif parameter in self._history:
            self._history[parameter].clear()

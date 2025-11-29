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
Rate Controller
OFEC-23-95-67-11 - Aircraft Publisher

This module manages sampling rate based on flight phase and system state.
"""

from enum import Enum
from typing import Dict
import time


class FlightPhase(Enum):
    """Flight phase enumeration."""
    GROUND = 0
    TAXI = 1
    TAKEOFF = 2
    CLIMB = 3
    CRUISE = 4
    DESCENT = 5
    APPROACH = 6
    LANDING = 7


class RatePriority(Enum):
    """Rate priority levels."""
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class RateController:
    """
    Controls sampling and publishing rates based on flight phase.
    
    Manages rate transitions, priority levels, and preemption logic.
    """
    
    # Phase rate configuration
    PHASE_CONFIG = {
        FlightPhase.GROUND: {
            "rate_hz": 0.1,
            "priority": RatePriority.LOW,
            "preemptible": True
        },
        FlightPhase.TAXI: {
            "rate_hz": 0.5,
            "priority": RatePriority.LOW,
            "preemptible": True
        },
        FlightPhase.TAKEOFF: {
            "rate_hz": 10.0,
            "priority": RatePriority.HIGH,
            "preemptible": False
        },
        FlightPhase.CLIMB: {
            "rate_hz": 5.0,
            "priority": RatePriority.MEDIUM,
            "preemptible": True
        },
        FlightPhase.CRUISE: {
            "rate_hz": 1.0,
            "priority": RatePriority.LOW,
            "preemptible": True
        },
        FlightPhase.DESCENT: {
            "rate_hz": 5.0,
            "priority": RatePriority.MEDIUM,
            "preemptible": True
        },
        FlightPhase.APPROACH: {
            "rate_hz": 10.0,
            "priority": RatePriority.HIGH,
            "preemptible": False
        },
        FlightPhase.LANDING: {
            "rate_hz": 10.0,
            "priority": RatePriority.HIGH,
            "preemptible": False
        }
    }
    
    # Rate override multipliers
    RATE_OVERRIDES = {
        "advisory_warning": 2.0,    # Double rate during warnings
        "advisory_critical": 5.0,   # 5x rate during critical
        "connectivity_poor": 0.5,   # Half rate on poor connection
    }
    
    def __init__(self):
        """Initialize the rate controller."""
        self._current_phase = FlightPhase.GROUND
        self._active_overrides: Dict[str, bool] = {}
        self._last_phase_change = time.time()
        self._transition_smoothing = True
    
    def set_phase(self, phase: FlightPhase) -> None:
        """
        Update the current flight phase.
        
        Args:
            phase: New flight phase
        """
        if phase != self._current_phase:
            self._current_phase = phase
            self._last_phase_change = time.time()
    
    def get_current_rate(self) -> float:
        """
        Get the current effective sampling rate.
        
        Returns:
            Rate in Hz
        """
        config = self.PHASE_CONFIG.get(self._current_phase, {})
        base_rate = config.get("rate_hz", 1.0)
        
        # Apply overrides
        effective_rate = base_rate
        for override_name, is_active in self._active_overrides.items():
            if is_active:
                multiplier = self.RATE_OVERRIDES.get(override_name, 1.0)
                effective_rate *= multiplier
        
        # Cap at maximum rate
        return min(effective_rate, 50.0)
    
    def get_current_priority(self) -> RatePriority:
        """Get current priority level."""
        config = self.PHASE_CONFIG.get(self._current_phase, {})
        return config.get("priority", RatePriority.LOW)
    
    def is_preemptible(self) -> bool:
        """Check if current transmission is preemptible."""
        config = self.PHASE_CONFIG.get(self._current_phase, {})
        return config.get("preemptible", True)
    
    def set_override(self, override_name: str, active: bool) -> None:
        """
        Set a rate override.
        
        Args:
            override_name: Name of the override
            active: Whether the override is active
        """
        self._active_overrides[override_name] = active
    
    def clear_overrides(self) -> None:
        """Clear all rate overrides."""
        self._active_overrides.clear()
    
    def get_interval(self) -> float:
        """
        Get the current sampling interval in seconds.
        
        Returns:
            Interval in seconds
        """
        rate = self.get_current_rate()
        return 1.0 / rate if rate > 0 else 1.0
    
    @property
    def current_phase(self) -> FlightPhase:
        """Get current flight phase."""
        return self._current_phase
    
    @property
    def time_in_phase(self) -> float:
        """Get time spent in current phase (seconds)."""
        return time.time() - self._last_phase_change

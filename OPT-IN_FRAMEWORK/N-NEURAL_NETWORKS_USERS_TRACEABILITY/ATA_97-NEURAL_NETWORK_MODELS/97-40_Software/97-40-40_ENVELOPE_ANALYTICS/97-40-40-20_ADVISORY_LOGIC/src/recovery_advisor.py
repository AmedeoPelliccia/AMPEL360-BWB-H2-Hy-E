"""
Recovery Advisor
OFEC-97-40-40-20 - Envelope Analytics

This module provides recovery suggestions for low margin conditions.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class RecoveryPriority(Enum):
    """Recovery action priority."""
    IMMEDIATE = 0
    PROMPT = 1
    WHEN_ABLE = 2


@dataclass
class RecoveryAction:
    """Suggested recovery action."""
    parameter: str
    priority: RecoveryPriority
    action: str
    rationale: str


class RecoveryAdvisor:
    """
    Provides recovery suggestions for low margin conditions.
    
    Generates actionable recommendations based on current
    envelope state and margin trends.
    """
    
    # Recovery action database
    RECOVERY_ACTIONS = {
        "alpha": {
            "low": [
                RecoveryAction(
                    parameter="alpha",
                    priority=RecoveryPriority.IMMEDIATE,
                    action="Reduce angle of attack - push nose down",
                    rationale="AOA approaching stall limit"
                ),
                RecoveryAction(
                    parameter="alpha",
                    priority=RecoveryPriority.PROMPT,
                    action="Increase airspeed",
                    rationale="Higher speed provides more AOA margin"
                )
            ]
        },
        "speed_low": {
            "low": [
                RecoveryAction(
                    parameter="speed_low",
                    priority=RecoveryPriority.IMMEDIATE,
                    action="Increase thrust / reduce drag",
                    rationale="Speed below minimum safe speed"
                ),
                RecoveryAction(
                    parameter="speed_low",
                    priority=RecoveryPriority.PROMPT,
                    action="Reduce pitch attitude",
                    rationale="Lower nose to gain airspeed"
                )
            ]
        },
        "speed_high": {
            "low": [
                RecoveryAction(
                    parameter="speed_high",
                    priority=RecoveryPriority.IMMEDIATE,
                    action="Reduce thrust",
                    rationale="Speed approaching Vmo/Mmo"
                ),
                RecoveryAction(
                    parameter="speed_high",
                    priority=RecoveryPriority.PROMPT,
                    action="Deploy speedbrakes if available",
                    rationale="Increase drag to reduce speed"
                ),
                RecoveryAction(
                    parameter="speed_high",
                    priority=RecoveryPriority.WHEN_ABLE,
                    action="Increase pitch attitude",
                    rationale="Trade speed for altitude"
                )
            ]
        },
        "load_factor": {
            "low": [
                RecoveryAction(
                    parameter="load_factor",
                    priority=RecoveryPriority.IMMEDIATE,
                    action="Reduce bank angle / pitch rate",
                    rationale="G-load approaching structural limit"
                ),
                RecoveryAction(
                    parameter="load_factor",
                    priority=RecoveryPriority.PROMPT,
                    action="Level wings, reduce maneuver intensity",
                    rationale="Minimize load factor"
                )
            ]
        },
        "bank_angle": {
            "low": [
                RecoveryAction(
                    parameter="bank_angle",
                    priority=RecoveryPriority.IMMEDIATE,
                    action="Reduce bank angle",
                    rationale="Bank approaching structural limit"
                )
            ]
        },
        "altitude": {
            "low": [
                RecoveryAction(
                    parameter="altitude",
                    priority=RecoveryPriority.PROMPT,
                    action="Begin descent",
                    rationale="Approaching service ceiling"
                ),
                RecoveryAction(
                    parameter="altitude",
                    priority=RecoveryPriority.WHEN_ABLE,
                    action="Consider weight reduction if able",
                    rationale="Lower weight increases ceiling"
                )
            ]
        }
    }
    
    # Margin thresholds for recovery suggestions
    SUGGESTION_THRESHOLD = 25.0  # Start suggesting below this margin %
    URGENT_THRESHOLD = 10.0      # Urgent suggestions below this
    
    def __init__(self):
        """Initialize the recovery advisor."""
        self._active_suggestions: Dict[str, List[RecoveryAction]] = {}
    
    def get_suggestions(
        self,
        parameter: str,
        margin_pct: float
    ) -> List[RecoveryAction]:
        """
        Get recovery suggestions for a parameter.
        
        Args:
            parameter: Parameter name
            margin_pct: Current margin percentage
            
        Returns:
            List of recovery actions
        """
        if margin_pct >= self.SUGGESTION_THRESHOLD:
            # Margin adequate - no suggestions
            if parameter in self._active_suggestions:
                del self._active_suggestions[parameter]
            return []
        
        # Get applicable recovery actions
        actions = self.RECOVERY_ACTIONS.get(parameter, {}).get("low", [])
        
        # Filter by urgency
        if margin_pct < self.URGENT_THRESHOLD:
            # Return all actions for urgent situation
            filtered = actions
        else:
            # Return only PROMPT and WHEN_ABLE for less urgent
            filtered = [a for a in actions 
                       if a.priority != RecoveryPriority.IMMEDIATE]
        
        self._active_suggestions[parameter] = filtered
        return filtered
    
    def get_all_suggestions(
        self,
        margins: Dict[str, float]
    ) -> List[RecoveryAction]:
        """
        Get all recovery suggestions for current state.
        
        Args:
            margins: Dictionary of parameter margins
            
        Returns:
            Combined list of recovery actions, sorted by priority
        """
        all_actions = []
        
        for parameter, margin_pct in margins.items():
            actions = self.get_suggestions(parameter, margin_pct)
            all_actions.extend(actions)
        
        # Sort by priority (IMMEDIATE first)
        all_actions.sort(key=lambda a: a.priority.value)
        
        return all_actions
    
    @property
    def active_suggestions(self) -> Dict[str, List[RecoveryAction]]:
        """Get currently active suggestions."""
        return self._active_suggestions.copy()
    
    def has_urgent_suggestions(self) -> bool:
        """Check if there are any IMMEDIATE priority suggestions."""
        for actions in self._active_suggestions.values():
            if any(a.priority == RecoveryPriority.IMMEDIATE for a in actions):
                return True
        return False

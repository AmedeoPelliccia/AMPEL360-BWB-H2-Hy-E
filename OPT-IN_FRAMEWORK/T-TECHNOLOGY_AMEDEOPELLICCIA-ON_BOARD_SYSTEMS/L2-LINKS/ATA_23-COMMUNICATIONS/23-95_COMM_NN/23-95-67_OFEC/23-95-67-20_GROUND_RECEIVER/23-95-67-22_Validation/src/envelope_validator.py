"""
Envelope Validator
OFEC-60-60-20-20 - Ground Receiver

This module validates decoded OFEC messages.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum


class ValidationResult(Enum):
    """Validation result codes."""
    VALID = 0
    SCHEMA_ERROR = 1
    RANGE_ERROR = 2
    TIMESTAMP_ERROR = 3
    AIRCRAFT_UNKNOWN = 4
    SIGNATURE_INVALID = 5


@dataclass
class ValidationReport:
    """Validation report for a message."""
    result: ValidationResult
    errors: List[str]
    warnings: List[str]


class EnvelopeValidator:
    """
    Validates OFEC envelope messages.
    
    Performs schema validation, range checks, and consistency validation.
    """
    
    # Required fields
    REQUIRED_FIELDS = [
        "envelope_id", "aircraft_id", "timestamp",
        "flight_phase", "margins", "advisory", "metadata"
    ]
    
    # Margin field requirements
    REQUIRED_MARGINS = ["alpha", "speed", "load_factor", "altitude", "bank_angle"]
    
    # Valid flight phases
    VALID_PHASES = [
        "GROUND", "TAXI", "TAKEOFF", "CLIMB",
        "CRUISE", "DESCENT", "APPROACH", "LANDING"
    ]
    
    # Range limits
    RANGES = {
        "alpha.margin_pct": (-100, 100),
        "speed.margin_low_pct": (-100, 100),
        "speed.margin_high_pct": (-100, 100),
        "load_factor.current_g": (-3, 6),
        "altitude.current_ft": (-2000, 60000),
        "bank_angle.current_deg": (-180, 180)
    }
    
    def __init__(self, known_aircraft: Optional[List[str]] = None):
        """
        Initialize the validator.
        
        Args:
            known_aircraft: List of known aircraft IDs (None = accept all)
        """
        self._known_aircraft = known_aircraft
        self._validation_count = 0
    
    def validate(self, message: Dict) -> ValidationReport:
        """
        Validate an envelope message.
        
        Args:
            message: Decoded message dictionary
            
        Returns:
            ValidationReport with results
        """
        self._validation_count += 1
        errors = []
        warnings = []
        
        # Check required fields
        for field in self.REQUIRED_FIELDS:
            if field not in message:
                errors.append(f"Missing required field: {field}")
        
        if errors:
            return ValidationReport(
                result=ValidationResult.SCHEMA_ERROR,
                errors=errors,
                warnings=warnings
            )
        
        # Check aircraft ID
        if self._known_aircraft is not None:
            if message["aircraft_id"] not in self._known_aircraft:
                errors.append(f"Unknown aircraft: {message['aircraft_id']}")
                return ValidationReport(
                    result=ValidationResult.AIRCRAFT_UNKNOWN,
                    errors=errors,
                    warnings=warnings
                )
        
        # Check flight phase
        if message["flight_phase"] not in self.VALID_PHASES:
            errors.append(f"Invalid flight phase: {message['flight_phase']}")
        
        # Check margins structure
        margins = message.get("margins", {})
        for margin_type in self.REQUIRED_MARGINS:
            if margin_type not in margins:
                warnings.append(f"Missing margin type: {margin_type}")
        
        # Range checks
        range_errors = self._check_ranges(message)
        errors.extend(range_errors)
        
        if errors:
            return ValidationReport(
                result=ValidationResult.RANGE_ERROR,
                errors=errors,
                warnings=warnings
            )
        
        return ValidationReport(
            result=ValidationResult.VALID,
            errors=[],
            warnings=warnings
        )
    
    def _check_ranges(self, message: Dict) -> List[str]:
        """Check value ranges."""
        errors = []
        margins = message.get("margins", {})
        
        for path, (min_val, max_val) in self.RANGES.items():
            parts = path.split(".")
            value = margins
            try:
                for part in parts:
                    value = value[part]
                
                if not isinstance(value, (int, float)):
                    continue
                
                if value < min_val or value > max_val:
                    errors.append(
                        f"Value out of range: {path} = {value} "
                        f"(expected {min_val} to {max_val})"
                    )
            except (KeyError, TypeError):
                # Field not present - handled elsewhere
                pass
        
        return errors
    
    @property
    def validation_count(self) -> int:
        """Get total validations performed."""
        return self._validation_count

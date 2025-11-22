"""
Q100 Configuration Item (CI) Validator

Validates CI numbers and effectivity codes against Q100 standards.

Format: CI-[ATA]-[ZONE]-[TYPE]-[ID]
Example: CI-53-400-SPAR-FWD
"""

import re
import logging
from typing import Dict, Optional, List
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class CIComponents:
    """Parsed components of a Q100 CI number."""
    ata: str
    zone: str
    type: str
    id: str


class CIValidator:
    """Validator for Q100 Configuration Item numbers."""
    
    # Valid ATA chapters for Q100
    VALID_ATA_CHAPTERS = [
        '00', '01', '04', '05', '06', '07', '08', '09', '12',  # O-P
        '20', '21', '24', '26', '27', '28', '29', '30', '31', '32',  # T (partial)
        '36', '37', '38', '41', '42', '47', '49', '50', '51', '52',
        '53', '54', '55', '56', '57', '60', '61', '70', '71', '72',
        '73', '74', '75', '76', '77', '78', '79', '80', '85', '95',
        '99', '100'
    ]
    
    # Valid effectivity codes
    VALID_EFFECTIVITY = ['ALL', 'SN0001-0003', 'SN0004', 'SN0005-0010', 
                         'SN0011-0099', 'SN0100UP']
    
    # Valid applicability codes
    VALID_APPLICABILITY = ['ALL', 'PAX', 'CGO', 'TEST', 'CERT']
    
    def __init__(self):
        """Initialize the CI validator."""
        # Pattern for CI number
        self.pattern = re.compile(
            r'^CI-(?P<ata>\d{2,3})-(?P<zone>\d{2,3})-(?P<type>[A-Z0-9_]+)-(?P<id>[A-Z0-9_]+)$'
        )
    
    def validate(self, ci_number: str) -> tuple[bool, Optional[str], Optional[CIComponents]]:
        """
        Validate a Q100 CI number.
        
        Args:
            ci_number: The CI number to validate
            
        Returns:
            Tuple of (is_valid, error_message, parsed_components)
            
        Example:
            >>> validator = CIValidator()
            >>> valid, err, components = validator.validate("CI-53-400-SPAR-FWD")
            >>> valid
            True
        """
        if not ci_number:
            return False, "CI number is empty", None
        
        # Must start with CI-
        if not ci_number.startswith('CI-'):
            return False, "CI number must start with 'CI-'", None
        
        # Match against pattern
        match = self.pattern.match(ci_number)
        if not match:
            return False, self._generate_format_error(ci_number), None
        
        # Extract components
        components = CIComponents(**match.groupdict())
        
        # Validate ATA chapter
        if components.ata not in self.VALID_ATA_CHAPTERS:
            return False, f"Invalid ATA chapter '{components.ata}'", None
        
        logger.info(f"✓ Validated CI number: {ci_number}")
        return True, None, components
    
    def validate_effectivity(self, effectivity: str) -> tuple[bool, Optional[str]]:
        """
        Validate effectivity code.
        
        Args:
            effectivity: Effectivity code to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check against known patterns
        if effectivity == 'ALL':
            return True, None
        
        # SN range pattern: SN0001-0003
        if re.match(r'^SN\d{4}-\d{4}$', effectivity):
            return True, None
        
        # SN from pattern: SN0100UP
        if re.match(r'^SN\d{4}UP$', effectivity):
            return True, None
        
        # SN exception pattern: SN0100UP-EXC0105
        if re.match(r'^SN\d{4}UP-EXC\d{4}$', effectivity):
            return True, None
        
        # Block pattern: BLK-A
        if re.match(r'^BLK-[A-Z]$', effectivity):
            return True, None
        
        return False, f"Invalid effectivity code: {effectivity}"
    
    def validate_applicability(self, applicability: str) -> tuple[bool, Optional[str]]:
        """
        Validate applicability code.
        
        Args:
            applicability: Applicability code to validate
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if applicability in self.VALID_APPLICABILITY:
            return True, None
        
        return False, f"Invalid applicability code: {applicability}. Must be one of: {self.VALID_APPLICABILITY}"
    
    def _generate_format_error(self, ci_number: str) -> str:
        """Generate a helpful error message for format violations."""
        return (
            f"Invalid CI number format: '{ci_number}'\n"
            f"Expected format: CI-[ATA]-[ZONE]-[TYPE]-[ID]\n"
            f"Example: CI-53-400-SPAR-FWD"
        )


def validate_ci_number(ci_number: str) -> bool:
    """
    Convenience function to validate CI number.
    
    Args:
        ci_number: CI number to validate
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If CI number is invalid
    """
    validator = CIValidator()
    is_valid, error, _ = validator.validate(ci_number)
    
    if not is_valid:
        raise ValueError(error)
    
    return True


def batch_validate_cis(ci_numbers: List[str]) -> Dict[str, tuple[bool, Optional[str]]]:
    """
    Validate multiple CI numbers.
    
    Args:
        ci_numbers: List of CI numbers to validate
        
    Returns:
        Dictionary mapping CI number to (is_valid, error_message)
    """
    validator = CIValidator()
    results = {}
    
    for ci_number in ci_numbers:
        is_valid, error, _ = validator.validate(ci_number)
        results[ci_number] = (is_valid, error)
    
    return results


if __name__ == '__main__':
    import sys
    
    logging.basicConfig(level=logging.INFO)
    
    if len(sys.argv) < 2:
        print("Usage: python ci_validator.py <ci_number1> [ci_number2] ...")
        sys.exit(1)
    
    validator = CIValidator()
    all_valid = True
    
    for ci_number in sys.argv[1:]:
        is_valid, error, components = validator.validate(ci_number)
        
        if is_valid:
            print(f"✓ {ci_number}")
            if components:
                print(f"  ATA: {components.ata}, Zone: {components.zone}, Type: {components.type}")
        else:
            print(f"✗ {ci_number}")
            print(f"  Error: {error}")
            all_valid = False
    
    sys.exit(0 if all_valid else 1)

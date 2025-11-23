"""
Q100 Drawing Filename Validator

Validates drawing filenames against the Q100 standard format:
[ATA]-[ZONE]-[SEQUENCE]-[VAR]_Rev[X]_[MODEL]_[EFF]_[APP]_Description.svg

SAFETY-CRITICAL: Correct naming is essential for traceability.
DO-178C Level C - Major failure condition.

Requirements:
- Python 3.9+ (uses tuple[...] type hint syntax)
- Model code is hardcoded to 'Q100' for this project
"""

import re
import logging
from typing import Dict, Optional, List
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class DrawingComponents:
    """Parsed components of a Q100 drawing filename."""
    ata: str
    zone: str
    sequence: str
    variant: Optional[str]
    revision: str
    model: str
    effectivity: str
    applicability: str
    description: str
    extension: str


class DrawingValidator:
    """Validator for Q100 drawing filenames."""
    
    # Valid effectivity codes
    VALID_EFFECTIVITY = [
        'ALL',
        r'SN\d{4}UP',  # e.g., SN0100UP
        r'SN\d{4}-\d{4}',  # e.g., SN0001-0050
        r'SN\d{4}UP-EXC\d{4}',  # e.g., SN0100UP-EXC0105
        r'BLK-[A-Z]',  # e.g., BLK-A
    ]
    
    # Valid applicability codes
    VALID_APPLICABILITY = ['ALL', 'PAX', 'CGO', 'TEST', 'CERT']
    
    # Valid models
    VALID_MODELS = ['Q100']
    
    # Valid extensions
    VALID_EXTENSIONS = ['.svg', '.step', '.iges', '.jt']
    
    def __init__(self):
        """Initialize the drawing validator."""
        # Pattern for Q100 drawing filename
        self.pattern = re.compile(
            r'^(?P<ata>\d{2})-(?P<zone>\d{2})-(?P<sequence>\d{4})(?:-(?P<variant>\d{2}|[A-Z]))?'
            r'_Rev(?P<revision>[A-Z]{1,2}|Draft)'
            r'_(?P<model>Q100)'
            r'_(?P<effectivity>[A-Z0-9\-]+)'
            r'_(?P<applicability>[A-Z]+)'
            r'_(?P<description>[A-Za-z0-9_]+)'
            r'(?P<extension>\.(svg|step|iges|jt))$'
        )
    
    def validate(self, filename: str) -> tuple[bool, Optional[str], Optional[DrawingComponents]]:
        """
        Validate a Q100 drawing filename.
        
        Args:
            filename: The filename to validate
            
        Returns:
            Tuple of (is_valid, error_message, parsed_components)
            
        Example:
            >>> validator = DrawingValidator()
            >>> valid, err, components = validator.validate(
            ...     "57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar.svg"
            ... )
            >>> valid
            True
        """
        if not filename:
            return False, "Filename is empty", None
        
        # Match against pattern
        match = self.pattern.match(filename)
        if not match:
            return False, self._generate_format_error(filename), None
        
        # Extract components
        components = DrawingComponents(**match.groupdict())
        
        # Validate model
        if components.model not in self.VALID_MODELS:
            return False, f"Invalid model '{components.model}'. Must be one of: {self.VALID_MODELS}", None
        
        # Validate effectivity
        if not self._validate_effectivity(components.effectivity):
            return False, f"Invalid effectivity code '{components.effectivity}'", None
        
        # Validate applicability
        if components.applicability not in self.VALID_APPLICABILITY:
            return False, f"Invalid applicability '{components.applicability}'. Must be one of: {self.VALID_APPLICABILITY}", None
        
        # Validate extension
        if components.extension not in self.VALID_EXTENSIONS:
            return False, f"Invalid extension '{components.extension}'. Must be one of: {self.VALID_EXTENSIONS}", None
        
        logger.info(f"✓ Validated Q100 drawing: {filename}")
        return True, None, components
    
    def _validate_effectivity(self, effectivity: str) -> bool:
        """Validate effectivity code against allowed patterns."""
        for pattern in self.VALID_EFFECTIVITY:
            if re.match(f'^{pattern}$', effectivity):
                return True
        return False
    
    def _generate_format_error(self, filename: str) -> str:
        """Generate a helpful error message for format violations."""
        return (
            f"Invalid Q100 drawing filename format: '{filename}'\n"
            f"Expected format: [ATA]-[ZONE]-[SEQUENCE]-[VAR]_Rev[X]_Q100_[EFF]_[APP]_Description.svg\n"
            f"Example: 57-40-1000_RevC_Q100_ALL_ALL_Forward_Wing_Spar_Assembly.svg"
        )


def validate_q100_drawing_filename(filename: str) -> bool:
    """
    Convenience function to validate Q100 drawing filename.
    
    Args:
        filename: Drawing filename to validate
        
    Returns:
        True if valid
        
    Raises:
        ValueError: If filename is invalid
        
    Example:
        >>> validate_q100_drawing_filename(
        ...     "57-40-1000_RevC_Q100_ALL_ALL_Spar.svg"
        ... )
        True
    """
    validator = DrawingValidator()
    is_valid, error, _ = validator.validate(filename)
    
    if not is_valid:
        raise ValueError(error)
    
    return True


def batch_validate_drawings(filenames: List[str]) -> Dict[str, tuple[bool, Optional[str]]]:
    """
    Validate multiple drawing filenames.
    
    Args:
        filenames: List of filenames to validate
        
    Returns:
        Dictionary mapping filename to (is_valid, error_message)
    """
    validator = DrawingValidator()
    results = {}
    
    for filename in filenames:
        is_valid, error, _ = validator.validate(filename)
        results[filename] = (is_valid, error)
    
    return results


if __name__ == '__main__':
    import sys
    
    logging.basicConfig(level=logging.INFO)
    
    if len(sys.argv) < 2:
        print("Usage: python drawing_validator.py <filename1> [filename2] ...")
        sys.exit(1)
    
    validator = DrawingValidator()
    all_valid = True
    
    for filename in sys.argv[1:]:
        is_valid, error, components = validator.validate(filename)
        
        if is_valid:
            print(f"✓ {filename}")
            if components:
                print(f"  ATA: {components.ata}, Zone: {components.zone}, Model: {components.model}")
        else:
            print(f"✗ {filename}")
            print(f"  Error: {error}")
            all_valid = False
    
    sys.exit(0 if all_valid else 1)

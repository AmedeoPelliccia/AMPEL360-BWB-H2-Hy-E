"""
Bank Angle Margin Calculation
OFEC-97-40-40-10 - Envelope Analytics

This module calculates bank angle margins relative to roll limits.
"""

from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .margin_calculator import Configuration


# Bank angle limits
BANK_LIMIT_CLEAN_DEG = 67.0   # Clean configuration (structural)
BANK_LIMIT_FLAPS_DEG = 30.0   # With flaps deployed


def get_bank_limit(config: "Configuration") -> float:
    """
    Get bank angle limit based on configuration.
    
    Args:
        config: Aircraft configuration
        
    Returns:
        Bank angle limit in degrees
    """
    if config.flap_deg > 0 or config.gear_down:
        return BANK_LIMIT_FLAPS_DEG
    else:
        return BANK_LIMIT_CLEAN_DEG


def calculate_bank_margin(
    current_bank: float,
    config: "Configuration"
) -> Dict:
    """
    Calculate bank angle margin.
    
    Args:
        current_bank: Current bank angle in degrees (can be positive or negative)
        config: Aircraft configuration
        
    Returns:
        Dictionary with margin values
    """
    limit = get_bank_limit(config)
    
    # Use absolute value for margin calculation
    bank_abs = abs(current_bank)
    
    margin_deg = limit - bank_abs
    margin_pct = (margin_deg / limit) * 100 if limit > 0 else 0
    
    return {
        "current_deg": round(current_bank, 1),
        "limit_deg": round(limit, 0),
        "margin_deg": round(margin_deg, 1),
        "margin_pct": round(margin_pct, 1)
    }


def is_bank_exceedance(current_bank: float, config: "Configuration") -> bool:
    """
    Check if bank angle exceeds limit.
    
    Args:
        current_bank: Current bank angle
        config: Aircraft configuration
        
    Returns:
        True if bank limit exceeded
    """
    limit = get_bank_limit(config)
    return abs(current_bank) > limit


def classify_bank_angle(bank_deg: float) -> str:
    """
    Classify the current bank angle.
    
    Args:
        bank_deg: Bank angle in degrees
        
    Returns:
        Classification string
    """
    bank_abs = abs(bank_deg)
    
    if bank_abs < 5:
        return "WINGS_LEVEL"
    elif bank_abs < 15:
        return "SHALLOW"
    elif bank_abs < 30:
        return "MODERATE"
    elif bank_abs < 45:
        return "STEEP"
    else:
        return "EXTREME"


def calculate_load_factor_for_bank(bank_deg: float) -> float:
    """
    Calculate load factor resulting from coordinated turn.
    
    In a coordinated turn: n = 1 / cos(bank)
    
    Args:
        bank_deg: Bank angle in degrees
        
    Returns:
        Load factor (G)
    """
    import math
    
    bank_rad = math.radians(abs(bank_deg))
    
    # Avoid division by zero at 90 degrees
    if abs(bank_deg) >= 89:
        return 99.0  # Effectively infinite
    
    return 1.0 / math.cos(bank_rad)

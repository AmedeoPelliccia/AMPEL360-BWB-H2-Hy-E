"""
Load Factor (G-Load) Margin Calculation
OFEC-97-40-40-10 - Envelope Analytics

This module calculates load factor margins relative to structural limits.
"""

from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .margin_calculator import Configuration


# Structural limits
LIMIT_POSITIVE_CLEAN = 2.5   # +2.5g clean configuration
LIMIT_NEGATIVE_CLEAN = -1.0  # -1.0g clean configuration
LIMIT_POSITIVE_FLAPS = 2.0   # +2.0g with flaps
LIMIT_NEGATIVE_FLAPS = 0.0   # 0.0g with flaps (no negative G)


def get_load_factor_limits(config: "Configuration") -> tuple:
    """
    Get load factor limits based on configuration.
    
    Args:
        config: Aircraft configuration
        
    Returns:
        Tuple of (positive_limit, negative_limit)
    """
    if config.flap_deg > 0 or config.gear_down:
        return LIMIT_POSITIVE_FLAPS, LIMIT_NEGATIVE_FLAPS
    else:
        return LIMIT_POSITIVE_CLEAN, LIMIT_NEGATIVE_CLEAN


def calculate_load_factor_margin(
    current_g: float,
    config: "Configuration"
) -> Dict:
    """
    Calculate load factor (G) margins.
    
    Args:
        current_g: Current normal load factor
        config: Aircraft configuration
        
    Returns:
        Dictionary with margin values
    """
    limit_positive, limit_negative = get_load_factor_limits(config)
    
    # Calculate absolute margins
    margin_positive_g = limit_positive - current_g
    margin_negative_g = current_g - limit_negative
    
    # Calculate percentage margins
    # Positive margin as percentage of positive limit
    margin_positive_pct = (margin_positive_g / limit_positive) * 100 if limit_positive > 0 else 0
    
    # Negative margin as percentage of negative limit range
    if limit_negative < 0:
        # Normal case with negative G capability
        neg_range = 1.0 - limit_negative  # Range from 1g to negative limit
        margin_negative_pct = (margin_negative_g / neg_range) * 100
    else:
        # Flaps out - no negative G allowed
        margin_negative_pct = 100 if current_g >= limit_negative else 0
    
    return {
        "current_g": round(current_g, 2),
        "limit_positive_g": round(limit_positive, 1),
        "limit_negative_g": round(limit_negative, 1),
        "margin_positive_g": round(margin_positive_g, 2),
        "margin_negative_g": round(margin_negative_g, 2),
        "margin_positive_pct": round(margin_positive_pct, 1),
        "margin_negative_pct": round(margin_negative_pct, 1)
    }


def is_g_exceedance(current_g: float, config: "Configuration") -> bool:
    """
    Check if load factor exceeds limits.
    
    Args:
        current_g: Current load factor
        config: Aircraft configuration
        
    Returns:
        True if G-limit exceeded
    """
    limit_positive, limit_negative = get_load_factor_limits(config)
    return current_g > limit_positive or current_g < limit_negative


def classify_g_load(current_g: float) -> str:
    """
    Classify the current G-load condition.
    
    Args:
        current_g: Current load factor
        
    Returns:
        Classification string
    """
    if current_g < 0:
        return "NEGATIVE_G"
    elif current_g < 0.5:
        return "LOW_G"
    elif current_g < 1.5:
        return "NORMAL"
    elif current_g < 2.0:
        return "ELEVATED"
    else:
        return "HIGH_G"

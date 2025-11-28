"""
Alpha (Angle of Attack) Margin Calculation
OFEC-97-40-40-10 - Envelope Analytics

This module calculates angle of attack margins relative to the stall limit.
"""

from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .margin_calculator import Configuration


# Reference values
STALL_ALPHA_BASE_DEG = 14.0  # Clean configuration stall alpha
PROTECTION_MARGIN_DEG = 2.0   # Buffer before actual stall
FLAP_EFFECT_PER_DEG = 0.15    # Alpha increase per degree of flap
SLAT_EFFECT_PER_DEG = 0.20    # Alpha increase per degree of slat


def get_stall_alpha(
    config: "Configuration",
    mach: float,
    altitude: float
) -> float:
    """
    Determine stall angle of attack based on configuration.
    
    Args:
        config: Aircraft configuration (flaps, slats, gear)
        mach: Current Mach number
        altitude: Pressure altitude in feet
        
    Returns:
        Stall alpha in degrees
    """
    # Base stall alpha (clean configuration)
    alpha_stall = STALL_ALPHA_BASE_DEG
    
    # Flap effect (increases stall alpha - allows higher AOA)
    alpha_stall += config.flap_deg * FLAP_EFFECT_PER_DEG
    
    # Slat effect (increases stall alpha)
    alpha_stall += config.slat_deg * SLAT_EFFECT_PER_DEG
    
    # Mach correction (stall alpha reduces at high Mach)
    if mach > 0.6:
        mach_factor = 1.0 - (mach - 0.6) * 0.5
        alpha_stall *= max(0.7, mach_factor)
    
    # Altitude correction (Reynolds number effect)
    if altitude > 20000:
        alt_factor = 1.0 - (altitude - 20000) / 200000
        alpha_stall *= max(0.9, alt_factor)
    
    return alpha_stall


def calculate_alpha_margin(
    current_aoa: float,
    config: "Configuration",
    mach: float,
    altitude: float
) -> Dict:
    """
    Calculate angle of attack margin.
    
    Args:
        current_aoa: Current AOA in degrees
        config: Aircraft configuration
        mach: Current Mach number
        altitude: Pressure altitude in feet
        
    Returns:
        Dictionary with margin values:
        - current_deg: Current angle of attack
        - limit_deg: Maximum permissible AOA (with protection margin)
        - margin_deg: Margin in degrees
        - margin_pct: Margin as percentage of limit
    """
    # Get stall alpha for current configuration
    stall_alpha = get_stall_alpha(config, mach, altitude)
    
    # Apply protection margin
    limit_alpha = stall_alpha - PROTECTION_MARGIN_DEG
    
    # Calculate margin
    margin_deg = limit_alpha - current_aoa
    
    # Calculate percentage (relative to usable range)
    # Assumes negative AOA limit around -5 degrees
    usable_range = limit_alpha - (-5.0)
    margin_pct = (margin_deg / usable_range) * 100 if usable_range > 0 else 0
    
    return {
        "current_deg": round(current_aoa, 2),
        "limit_deg": round(limit_alpha, 2),
        "margin_deg": round(margin_deg, 2),
        "margin_pct": round(margin_pct, 1)
    }


def is_approaching_stall(margin_pct: float, threshold_pct: float = 25.0) -> bool:
    """
    Check if aircraft is approaching stall condition.
    
    Args:
        margin_pct: Current margin percentage
        threshold_pct: Warning threshold
        
    Returns:
        True if approaching stall
    """
    return margin_pct < threshold_pct


def get_alpha_trend(
    current_margin: float,
    previous_margin: float,
    time_delta: float
) -> str:
    """
    Determine alpha margin trend.
    
    Args:
        current_margin: Current margin in degrees
        previous_margin: Previous margin in degrees
        time_delta: Time between samples in seconds
        
    Returns:
        Trend string: "IMPROVING", "STABLE", or "DEGRADING"
    """
    if time_delta <= 0:
        return "STABLE"
    
    rate = (previous_margin - current_margin) / time_delta  # deg/s
    
    if rate > 0.5:
        return "DEGRADING"
    elif rate < -0.5:
        return "IMPROVING"
    else:
        return "STABLE"

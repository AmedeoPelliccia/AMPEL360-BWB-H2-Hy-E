"""
Altitude Margin Calculation
OFEC-97-40-40-10 - Envelope Analytics

This module calculates altitude margins relative to service ceiling.
"""

from typing import Dict


# Altitude limits
MAX_CERTIFIED_ALTITUDE_FT = 43000  # Maximum certified altitude
MIN_ALTITUDE_FT = -1000            # Minimum (below sea level airports)


def calculate_service_ceiling(
    weight: float,
    oat: float,
    weight_reference: float = 80000.0
) -> float:
    """
    Calculate performance-limited service ceiling.
    
    Args:
        weight: Current weight in kg
        oat: Outside air temperature in Celsius
        weight_reference: Reference weight in kg
        
    Returns:
        Service ceiling in feet
    """
    # Weight effect (heavier = lower ceiling)
    if weight > weight_reference:
        weight_factor = 1.0 - (weight - weight_reference) / weight_reference * 0.2
    else:
        weight_factor = 1.0 + (weight_reference - weight) / weight_reference * 0.1
    
    weight_factor = max(0.7, min(1.1, weight_factor))
    
    # Temperature effect (ISA deviation)
    # Hot day = lower ceiling, cold day = higher ceiling
    isa_deviation = oat - 15.0  # ISA at sea level is 15°C
    temp_factor = 1.0 - isa_deviation / 100
    temp_factor = max(0.9, min(1.1, temp_factor))
    
    # Calculate performance ceiling
    performance_ceiling = MAX_CERTIFIED_ALTITUDE_FT * weight_factor * temp_factor
    
    # Cannot exceed certified limit
    return min(MAX_CERTIFIED_ALTITUDE_FT, performance_ceiling)


def calculate_altitude_margin(
    current_alt: float,
    weight: float,
    oat: float
) -> Dict:
    """
    Calculate altitude margin to service ceiling.
    
    Args:
        current_alt: Current pressure altitude in feet
        weight: Current weight in kg
        oat: Outside air temperature in Celsius
        
    Returns:
        Dictionary with margin values
    """
    ceiling = calculate_service_ceiling(weight, oat)
    
    margin_ft = ceiling - current_alt
    margin_pct = (margin_ft / ceiling) * 100 if ceiling > 0 else 0
    
    return {
        "current_ft": round(current_alt, 0),
        "ceiling_ft": round(ceiling, 0),
        "margin_ft": round(margin_ft, 0),
        "margin_pct": round(margin_pct, 1)
    }


def is_above_ceiling(current_alt: float, ceiling: float) -> bool:
    """Check if aircraft is above service ceiling."""
    return current_alt > ceiling


def get_altitude_band(altitude: float) -> str:
    """
    Classify altitude into operational bands.
    
    Args:
        altitude: Current altitude in feet
        
    Returns:
        Band classification string
    """
    if altitude < 0:
        return "BELOW_SEA_LEVEL"
    elif altitude < 10000:
        return "LOW_ALTITUDE"
    elif altitude < 25000:
        return "MEDIUM_ALTITUDE"
    elif altitude < 35000:
        return "HIGH_ALTITUDE"
    else:
        return "VERY_HIGH_ALTITUDE"

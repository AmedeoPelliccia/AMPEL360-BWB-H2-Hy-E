"""
Speed Margin Calculation
OFEC-97-40-40-10 - Envelope Analytics

This module calculates speed envelope margins (Vmin and Vmax).
"""

import math
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .margin_calculator import Configuration


# Reference values
VMO_KTS = 350.0           # Maximum operating speed (knots CAS)
MMO = 0.85                # Maximum operating Mach
VS_REFERENCE_KTS = 120.0  # Reference stall speed
WEIGHT_REFERENCE_KG = 80000.0  # Reference weight


def mach_to_cas(mach: float, altitude: float) -> float:
    """
    Convert Mach number to calibrated airspeed.
    
    Args:
        mach: Mach number
        altitude: Pressure altitude in feet
        
    Returns:
        Equivalent CAS in knots
    """
    # Simplified conversion using ISA atmosphere
    # Sea level speed of sound: 661.5 kts
    # Temperature lapse rate effect on speed of sound
    
    if altitude < 36089:
        # Troposphere
        temp_ratio = 1 - altitude / 145442
        pressure_ratio = temp_ratio ** 5.2559
    else:
        # Stratosphere (simplified)
        temp_ratio = 0.7519
        pressure_ratio = 0.2234 * math.exp((36089 - altitude) / 20806)
    
    speed_of_sound = 661.5 * math.sqrt(temp_ratio)
    tas = mach * speed_of_sound
    
    # Convert TAS to CAS (simplified)
    cas = tas * math.sqrt(pressure_ratio)
    
    return cas


def calculate_vmin(
    config: "Configuration",
    weight: float,
    altitude: float
) -> float:
    """
    Calculate minimum operating speed.
    
    Args:
        config: Aircraft configuration
        weight: Current weight in kg
        altitude: Pressure altitude in feet
        
    Returns:
        Vmin in knots CAS
    """
    # Weight effect on stall speed
    weight_factor = math.sqrt(weight / WEIGHT_REFERENCE_KG)
    
    # Configuration effect (flaps reduce stall speed)
    config_factors = {
        0: 1.00,   # Flaps 0 (clean)
        1: 0.95,   # Flaps 1
        5: 0.90,   # Flaps 5
        15: 0.85,  # Flaps 15
        25: 0.80,  # Flaps 25
        40: 0.75   # Flaps FULL
    }
    
    # Find closest flap setting
    flap_settings = sorted(config_factors.keys())
    flap_key = min(flap_settings, key=lambda x: abs(x - config.flap_deg))
    config_factor = config_factors[flap_key]
    
    # Calculate stall speed
    vs = VS_REFERENCE_KTS * weight_factor * config_factor
    
    # Add margin for Vmin
    # 1.23 * Vs for takeoff/approach, 1.13 * Vs for landing
    if config.flap_deg >= 25 and config.gear_down:
        margin_factor = 1.13  # Landing configuration
    else:
        margin_factor = 1.23  # Other configurations
    
    return vs * margin_factor


def calculate_vmax(altitude: float) -> float:
    """
    Calculate maximum operating speed.
    
    Args:
        altitude: Pressure altitude in feet
        
    Returns:
        Vmax in knots CAS
    """
    # Convert MMO to CAS at current altitude
    mmo_cas = mach_to_cas(MMO, altitude)
    
    # Vmax is the lower of VMO and MMO-equivalent CAS
    return min(VMO_KTS, mmo_cas)


def calculate_speed_margins(
    cas: float,
    config: "Configuration",
    altitude: float,
    weight: float
) -> Dict:
    """
    Calculate speed envelope margins.
    
    Args:
        cas: Current calibrated airspeed in knots
        config: Aircraft configuration
        altitude: Pressure altitude in feet
        weight: Current weight in kg
        
    Returns:
        Dictionary with margin values
    """
    vmin = calculate_vmin(config, weight, altitude)
    vmax = calculate_vmax(altitude)
    
    margin_low_kts = cas - vmin
    margin_high_kts = vmax - cas
    
    # Calculate percentages relative to usable speed range
    speed_range = vmax - vmin
    if speed_range > 0:
        margin_low_pct = (margin_low_kts / speed_range) * 100
        margin_high_pct = (margin_high_kts / speed_range) * 100
    else:
        margin_low_pct = 0
        margin_high_pct = 0
    
    return {
        "current_kts": round(cas, 1),
        "vmin_kts": round(vmin, 1),
        "vmax_kts": round(vmax, 1),
        "margin_low_kts": round(margin_low_kts, 1),
        "margin_high_kts": round(margin_high_kts, 1),
        "margin_low_pct": round(margin_low_pct, 1),
        "margin_high_pct": round(margin_high_pct, 1)
    }


def is_overspeed(cas: float, vmax: float) -> bool:
    """Check if aircraft is in overspeed condition."""
    return cas > vmax


def is_underspeed(cas: float, vmin: float) -> bool:
    """Check if aircraft is in underspeed condition."""
    return cas < vmin

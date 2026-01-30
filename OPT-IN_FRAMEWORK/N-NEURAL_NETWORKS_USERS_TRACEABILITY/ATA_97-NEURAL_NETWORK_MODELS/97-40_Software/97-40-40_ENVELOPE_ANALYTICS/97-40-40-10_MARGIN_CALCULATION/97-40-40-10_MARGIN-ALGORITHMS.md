# Margin Calculation Algorithms

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | OFEC-97-40-40-10-ALG-001 |
| **Version** | 1.0 |
| **Status** | DRAFT |

---

## 1. Alpha Margin Algorithm

### 1.1 Stall Alpha Determination

```python
def get_stall_alpha(config: Configuration, mach: float, altitude: float) -> float:
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
    alpha_stall_base = 14.0  # degrees
    
    # Flap effect (increases stall alpha)
    flap_effect = config.flap_deg * 0.15  # ~0.15 deg per deg flap
    
    # Slat effect (increases stall alpha)
    slat_effect = config.slat_deg * 0.2  # ~0.2 deg per deg slat
    
    # Mach correction (reduces at high Mach)
    mach_factor = 1.0 - max(0, (mach - 0.6) * 0.5)
    
    # Altitude correction (reduces at high altitude due to Reynolds)
    altitude_factor = 1.0 - (altitude / 100000) * 0.1
    
    alpha_stall = (alpha_stall_base + flap_effect + slat_effect) * mach_factor * altitude_factor
    
    return alpha_stall
```

### 1.2 Margin Calculation

```python
def calculate_alpha_margin(current_alpha: float, stall_alpha: float) -> dict:
    """
    Calculate angle of attack margin.
    
    Args:
        current_alpha: Current AOA in degrees
        stall_alpha: Stall AOA in degrees
        
    Returns:
        Dictionary with margin values
    """
    # Protection margin (buffer before stall)
    PROTECTION_MARGIN = 2.0  # degrees
    
    limit_alpha = stall_alpha - PROTECTION_MARGIN
    margin_deg = limit_alpha - current_alpha
    margin_pct = (margin_deg / limit_alpha) * 100 if limit_alpha > 0 else 0
    
    return {
        "current_deg": current_alpha,
        "limit_deg": limit_alpha,
        "margin_deg": margin_deg,
        "margin_pct": margin_pct
    }
```

---

## 2. Speed Margin Algorithm

### 2.1 Minimum Speed (Vmin)

```python
def calculate_vmin(config: Configuration, weight: float, altitude: float) -> float:
    """
    Calculate minimum operating speed.
    
    Args:
        config: Aircraft configuration
        weight: Current weight in kg
        altitude: Pressure altitude in feet
        
    Returns:
        Vmin in knots CAS
    """
    # Base stall speed (reference weight, sea level)
    VS_REFERENCE = 120.0  # knots
    WEIGHT_REFERENCE = 80000  # kg
    
    # Weight effect
    weight_factor = math.sqrt(weight / WEIGHT_REFERENCE)
    
    # Configuration effect
    config_factor = {
        0: 1.0,    # Flaps 0
        1: 0.95,   # Flaps 1
        5: 0.90,   # Flaps 5
        15: 0.85,  # Flaps 15
        25: 0.80,  # Flaps 25
        40: 0.75   # Flaps FULL
    }.get(config.flap_deg, 1.0)
    
    # Calculate stall speed
    vs = VS_REFERENCE * weight_factor * config_factor
    
    # Add margin for Vmin (1.23 * Vs for takeoff, 1.13 * Vs for landing)
    margin_factor = 1.23 if config.flap_deg < 25 else 1.13
    
    return vs * margin_factor
```

### 2.2 Maximum Speed (Vmax)

```python
def calculate_vmax(altitude: float, mach: float) -> float:
    """
    Calculate maximum operating speed.
    
    Args:
        altitude: Pressure altitude in feet
        mach: Current Mach number
        
    Returns:
        Vmax in knots CAS
    """
    # Limiting speeds
    VMO = 350  # knots CAS
    MMO = 0.85  # Mach
    
    # Convert MMO to CAS at current altitude
    mmo_cas = mach_to_cas(MMO, altitude)
    
    # Vmax is the lower of VMO and MMO-equivalent CAS
    return min(VMO, mmo_cas)
```

### 2.3 Speed Margin Calculation

```python
def calculate_speed_margins(cas: float, vmin: float, vmax: float) -> dict:
    """
    Calculate speed envelope margins.
    """
    margin_low_kts = cas - vmin
    margin_high_kts = vmax - cas
    
    speed_range = vmax - vmin
    margin_low_pct = (margin_low_kts / speed_range) * 100 if speed_range > 0 else 0
    margin_high_pct = (margin_high_kts / speed_range) * 100 if speed_range > 0 else 0
    
    return {
        "current_kts": cas,
        "vmin_kts": vmin,
        "vmax_kts": vmax,
        "margin_low_kts": margin_low_kts,
        "margin_high_kts": margin_high_kts,
        "margin_low_pct": margin_low_pct,
        "margin_high_pct": margin_high_pct
    }
```

---

## 3. Load Factor Margin Algorithm

```python
def calculate_load_factor_margin(current_g: float, config: Configuration) -> dict:
    """
    Calculate load factor (G) margins.
    
    Args:
        current_g: Current normal load factor
        config: Aircraft configuration
        
    Returns:
        Dictionary with margin values
    """
    # Structural limits (clean configuration)
    LIMIT_POSITIVE_CLEAN = 2.5  # +2.5g
    LIMIT_NEGATIVE_CLEAN = -1.0  # -1.0g
    
    # Reduced limits with flaps
    if config.flap_deg > 0:
        limit_positive = 2.0
        limit_negative = 0.0
    else:
        limit_positive = LIMIT_POSITIVE_CLEAN
        limit_negative = LIMIT_NEGATIVE_CLEAN
    
    margin_positive = limit_positive - current_g
    margin_negative = current_g - limit_negative
    
    return {
        "current_g": current_g,
        "limit_positive_g": limit_positive,
        "limit_negative_g": limit_negative,
        "margin_positive_g": margin_positive,
        "margin_negative_g": margin_negative,
        "margin_positive_pct": (margin_positive / limit_positive) * 100,
        "margin_negative_pct": (margin_negative / abs(limit_negative)) * 100 if limit_negative != 0 else 100
    }
```

---

## 4. Altitude Margin Algorithm

```python
def calculate_altitude_margin(
    current_alt: float, 
    weight: float, 
    oat: float
) -> dict:
    """
    Calculate altitude margin to service ceiling.
    
    Args:
        current_alt: Current pressure altitude in feet
        weight: Current weight in kg
        oat: Outside air temperature in Celsius
        
    Returns:
        Dictionary with margin values
    """
    # Maximum certified altitude
    MAX_ALTITUDE = 43000  # feet
    
    # Calculate performance-limited ceiling
    # (Simplified - actual would use complex engine/aero model)
    weight_factor = 1.0 - (weight - 60000) / 40000 * 0.15
    temp_factor = 1.0 + (15 - oat) / 100 * 0.05  # ISA deviation effect
    
    performance_ceiling = MAX_ALTITUDE * weight_factor * temp_factor
    ceiling = min(MAX_ALTITUDE, performance_ceiling)
    
    margin_ft = ceiling - current_alt
    margin_pct = (margin_ft / ceiling) * 100 if ceiling > 0 else 0
    
    return {
        "current_ft": current_alt,
        "ceiling_ft": ceiling,
        "margin_ft": margin_ft,
        "margin_pct": margin_pct
    }
```

---

## 5. Bank Angle Margin Algorithm

```python
def calculate_bank_margin(current_bank: float, config: Configuration) -> dict:
    """
    Calculate bank angle margin.
    
    Args:
        current_bank: Current bank angle in degrees (absolute value)
        config: Aircraft configuration
        
    Returns:
        Dictionary with margin values
    """
    # Bank limits by configuration
    if config.flap_deg > 0:
        limit_bank = 30.0  # degrees with flaps
    else:
        limit_bank = 67.0  # degrees clean (structural limit)
    
    bank_abs = abs(current_bank)
    margin_deg = limit_bank - bank_abs
    margin_pct = (margin_deg / limit_bank) * 100 if limit_bank > 0 else 0
    
    return {
        "current_deg": current_bank,
        "limit_deg": limit_bank,
        "margin_deg": margin_deg,
        "margin_pct": margin_pct
    }
```

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-28_.

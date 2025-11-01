# Overview: 06-30-01 - Fuel Tank Volumes (LH₂)

## Purpose
This component documents the volumetric capacity and dimensional specifications of the liquid hydrogen (LH₂) fuel storage system for the AMPEL360 aircraft.

## LH₂ Tank System Overview

### Primary Tank Specifications
| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| **Total Volume** | 13,000 | liters | Inner vessel total capacity |
| **Usable Volume** | 12,500 | liters | Available for fuel |
| **Ullage Volume** | 500 | liters | Vapor space (4% of total) |
| **Maximum Fuel Mass** | 9,000 | kg | At LH₂ density 71.2 kg/m³ |
| **Tank Type** | Type C | - | Double-wall vacuum-insulated |

### Dimensional Specifications
| Dimension | Value | Tolerance | Reference |
|-----------|-------|-----------|-----------|
| **Inner Vessel Length** | 6,000 mm | ±20 mm | Cylindrical section |
| **Inner Vessel Diameter** | 3,600 mm | ±20 mm | Maximum diameter |
| **Outer Vessel Length** | 6,200 mm | ±50 mm | Including vacuum jacket |
| **Outer Vessel Diameter** | 3,800 mm | ±50 mm | Including insulation |
| **Insulation Thickness** | 150 mm | ±10 mm | Multi-layer insulation (MLI) |

### Tank Location (BRS Coordinates)
| Feature | X (FS) | Y (BL) | Z (WL) | Description |
|---------|--------|--------|--------|-------------|
| Tank Forward End | 16,000 | 0 | 5,200 | Forward bulkhead |
| Tank Center | 18,500 | 0 | 5,200 | Geometric center |
| Tank Aft End | 21,000 | 0 | 5,200 | Aft bulkhead |
| Fill Port | 22,000 | -2,500 | 4,800 | External access |
| Vent Port | 21,800 | +2,500 | 6,200 | Pressure relief |

## Tank Geometry

### Configuration
- **Type:** Cylindrical with hemispherical end caps
- **Orientation:** Longitudinal (along aircraft X-axis)
- **Installation:** Within BWB center body, below cabin floor
- **Attachment:** 4-point suspension system (allows thermal contraction)

### Internal Configuration
- **Baffles:** 3 anti-slosh baffles (perforated plates)
- **Instrumentation:** 5 level sensors, 8 temperature sensors, 4 pressure sensors
- **Piping:** Feed lines, fill lines, vent lines, boil-off recovery
- **Insulation:** 75 layers of MLI in annular vacuum space

## Clearance Envelopes

### Structural Clearances
| Surface | Clearance | Purpose |
|---------|-----------|---------|
| Top (cabin floor) | 800 mm | Thermal protection + access |
| Bottom (lower skin) | 600 mm | Thermal protection + access |
| Sides (lateral structure) | 500 mm | Thermal protection + safety zone |
| Forward (forward bulkhead) | 400 mm | Thermal protection |
| Aft (aft bulkhead) | 400 mm | Thermal protection |

### Safety Zones
- **Hot Work Prohibited:** 10m radius from tank center (no welding, grinding, etc.)
- **Personnel Access:** Restricted to certified LH₂ technicians within 5m
- **Equipment Exclusion:** No electrical equipment (non-ATEX rated) within 3m
- **Fire Protection:** Foam deluge system coverage within 15m radius

## Volume Calculations

### Geometric Volume
**Cylindrical Section:**
- Volume = π × r² × L
- V_cyl = π × (1.8m)² × 4.5m = 45.8 m³

**Hemispherical End Caps (2×):**
- Volume = (4/3) × π × r³ × 0.5 × 2
- V_caps = (4/3) × π × (1.8m)³ = 24.4 m³

**Total Geometric Volume:**
- V_total = V_cyl + V_caps = 45.8 + 24.4 = 70.2 m³ (theoretical)

**Accounting for Internals:**
- Baffles, piping, instrumentation: -6.2 m³
- **Net Internal Volume:** 64.0 m³ (64,000 liters)

**Tank Design Volume:**
- Inner vessel: 13,000 liters (20% of geometric for safety margin)
- Ullage space: 500 liters (4% of total)
- Usable fuel volume: 12,500 liters

### Fuel Mass Calculation
- **LH₂ Density:** 71.2 kg/m³ at -253°C, 1 atm
- **Maximum Fuel Mass:** 12,500 L × 0.0712 kg/L = **890 kg** per tank
- **Total Fuel (10 tanks):** 890 kg × 10 = **9,000 kg LH₂**
- **Energy Content:** 9,000 kg × 120 MJ/kg = **1,080 GJ** (300 MWh)

## Thermal Considerations

### Thermal Contraction
- **Temperature Change:** +20°C (ambient) to -253°C (LH₂)
- **Aluminum Alloy (2219-T87):** α = 23 × 10⁻⁶ /°C
- **Length Contraction:** ΔL = L × α × ΔT = 6.0m × 23×10⁻⁶ × 273 = **37.7 mm**
- **Diameter Contraction:** ΔD = D × α × ΔT = 3.6m × 23×10⁻⁶ × 273 = **22.6 mm**

**Design Accommodation:**
- Flexible attachment points (allow 50mm movement)
- Thermal expansion joints on piping
- Clearance envelope accounts for thermal movement

### Boil-Off Rate
- **Heat Leak:** ~5 W (excellent MLI insulation)
- **Boil-Off Rate:** 5 W / (450 kJ/kg) = **0.04 kg/hour**
- **Daily Boil-Off:** 0.04 × 24 = **1.0 kg/day** (0.01% of total fuel)
- **7-Day Mission:** 7 kg boil-off (0.08% of total fuel) → negligible

## Operational Constraints

### Fueling Constraints
- **Maximum Fill Rate:** 200 kg/hour (safety limitation)
- **Minimum Fill Time:** 9,000 kg / 200 kg/hr = **45 hours** (full fuel load)
- **Typical Fill:** 6,000 kg / 200 kg/hr = **30 hours** (typical mission)

### Center of Gravity Impact
- **Empty Tank CG:** FS 18,500 (tank center)
- **Full Tank CG:** FS 18,500 (no shift, symmetric fill)
- **CG Range:** 9,000 kg fuel × 0.5m / 85,000 kg MTOW = ±0.05% MAC (negligible)

## Interface Requirements

### ATA 28 (Fuel System)
- **Interface:** Tank volume → Fuel system capacity
- **Critical Data:** 12,500 L usable volume per tank
- **Feed System:** 2 feed lines per tank (redundancy)

### ATA 06-10 (Overall Dimensions)
- **Interface:** Tank dimensions → Overall aircraft volume allocation
- **Critical Data:** Tank clearance envelope (FS 16,000 to 21,000)

### ATA 21 (Air Conditioning)
- **Interface:** Tank thermal protection → HVAC cooling requirements
- **Critical Data:** 5W heat leak per tank × 10 tanks = 50W cooling load

### ATA 26 (Fire Protection)
- **Interface:** Tank safety zones → Fire suppression system coverage
- **Critical Data:** 15m radius foam deluge system

## Certification Requirements

### CS-25 (Applicable)
- **CS-25.963:** Fuel tanks (general requirements)
- **CS-25.965:** Fuel tank tests (pressure, leak, structural)
- **CS-25.967:** Fuel tank installation (crashworthiness)

### Hydrogen-Specific Standards
- **ISO 21013:** Cryogenic vessels (design requirements)
- **SAE AS6858:** Cryogenic Hydrogen Storage for Aircraft
- **NFPA 2:** Hydrogen Technologies Code

## Document Status
**Status:** In Development  
**Last Review:** 2025-11-01  
**Next Review:** 2026-05-01

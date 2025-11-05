# H2 Tank Placement Strategy

## Executive Summary

The AMPEL360 BWB configuration provides unique advantages for hydrogen storage through its thick center body and wing structure, enabling safe, efficient H2 integration with optimal CG control.

## Tank Configuration

### Center Body Tanks
**Location:** Upper deck, centerline, station 12-22m  
**Capacity:** 4,000 kg H2 (two tanks @ 2,000 kg each)  
**CG Position:** 25% MAC (near optimal)

**Advantages:**
- Maximum volumetric efficiency
- Minimal CG shift as fuel depletes
- Optimal thermal insulation
- Separated from passenger cabin

**Design Features:**
- Cylindrical pressure vessels (Type IV composite)
- Vacuum-insulated double wall
- Venting to upper surface
- Crash-resistant mounting

### Wing Tanks
**Location:** Outboard of center body, station Y=8-18m  
**Capacity:** 2,500 kg H2 (two tanks @ 1,250 kg each)  
**CG Position:** Adjustable (18-32% MAC)

**Advantages:**
- CG trim capability
- Load distribution
- Structural integration
- Additional volumetric capacity

**Design Features:**
- Conformal to wing contour
- Multi-chamber configuration
- Independent fill/drain capability
- Emergency dump provisions

## Safety Integration

### Separation Requirements
- **Passenger Cabin:** Minimum 2.0m clearance
- **Fire Zones:** Class D fire suppression
- **Electrical Systems:** Isolated routing

### Ventilation Strategy
- Natural convection to upper surface
- Forced ventilation during ground operations
- H2 detection sensors (4 ppm threshold)
- Automatic isolation on leak detection

### Crash Protection
- Frangible couplings
- Pressure relief to safe direction (upward)
- Post-crash fire prevention
- Emergency services access

## CG Control Strategy

### Fuel Loading Sequence
1. **Center tanks first:** Establishes baseline CG
2. **Wing tanks as required:** Trim to target CG
3. **Top-off center:** Maximize range

### In-Flight Management
- **CAOS Monitoring:** Real-time CG calculation
- **Automated Transfer:** Center ↔ wing as needed
- **Optimal Cruise:** Maintain 24-28% MAC (best L/D)
- **Landing Prep:** Transfer to center tanks (stable CG)

### Depletion Pattern
- Consume wing tanks first (move CG forward)
- Center tanks provide reserve and CG stability
- Automated sequencing via fuel management system

## Weight and Balance Impacts

### CG Envelope Utilization
- **Full Fuel:** 27% MAC ± 8% (depending on passenger load)
- **Empty Fuel:** 25% MAC ± 6%
- **Usable Range:** 19-35% MAC (accommodates all loading)

### Tank Weight Summary
| Component | Weight (kg) | CG (% MAC) |
|-----------|-------------|------------|
| Center Tanks (empty) | 1,200 | 25% |
| Wing Tanks (empty) | 800 | 28% |
| H2 Fuel (max) | 6,500 | Variable |
| **Total System** | **8,500** | **26%** |

## Operational Procedures

### Ground Refueling
- Truck connection at underwing stations
- Automated fill sequence per load sheet
- CG verification before taxi
- Safety zone enforcement (15m radius)

### Pre-Flight
- Tank pressure verification
- Leak check (automatic)
- CG position confirmation
- Fuel quantity cross-check

### In-Flight
- Continuous tank monitoring (CAOS)
- Automatic transfer as required
- Temperature and pressure trending
- Leak detection system active

### Post-Flight
- Tank pressure stabilization
- Boil-off capture (if applicable)
- System safing procedures
- Maintenance logging

## Design Validation

### Analysis Performed
- CFD thermal analysis
- FEA structural loads
- CG sensitivity studies
- Safety hazard analysis (SHA)

### Testing Planned
- Ground vibration testing
- Crash simulation
- Pressure cycling
- Thermal performance
- Emergency scenarios

---

**References:**
- H2 System Architecture: ATA 28-00-00
- Tank Design Specification: ISO-19881 compliance
- Safety Analysis: SHA-H2-2025-001
- Weight & Balance: WBM-003 H2 Supplement

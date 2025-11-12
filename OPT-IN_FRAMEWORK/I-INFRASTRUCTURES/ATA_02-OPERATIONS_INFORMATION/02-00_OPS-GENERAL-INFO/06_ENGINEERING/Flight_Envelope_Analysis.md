# Flight Envelope Analysis
**Component Code:** 02-00-00  
**Component Name:** GENERAL  
**Document Type:** Flight Envelope Analysis

---

## Overview

This document defines the flight envelope analysis for the AMPEL360 BWB H₂ Hy-E Q100 aircraft, including operational limits, performance boundaries, and safety margins across all flight conditions.

---

## Flight Envelope Definition

### Operating Envelope

| Parameter | Minimum | Maximum | Units |
|-----------|---------|---------|-------|
| **Altitude** | -1,000 ft | 41,000 ft | ft MSL |
| **Airspeed** | 120 KIAS | 330 KIAS | kt |
| **Mach Number** | 0.20 | 0.85 | Mach |
| **Load Factor** | -1.0 g | +2.5 g | g |
| **Bank Angle** | -60° | +60° | degrees |
| **Pitch Angle** | -15° | +30° | degrees |

---

## V-n Diagram

### Design Load Factors

**Positive Load Factors:**
- Limit load: +2.5 g (normal operations)
- Ultimate load: +3.75 g (1.5 × limit)
- Maneuvering speed (VA): 250 KIAS

**Negative Load Factors:**
- Limit load: -1.0 g
- Ultimate load: -1.5 g

### Speed Limitations

**Critical Speeds:**
```
VS0 (Stall, landing config):  120 KIAS
VS1 (Stall, clean):          135 KIAS
VFE (Max flaps extended):    200 KIAS
VLE (Max landing gear ext):  220 KIAS
VLO (Max landing gear op):   200 KIAS
VMO (Max operating speed):   330 KIAS
MMO (Max operating Mach):    0.85
VNE (Never exceed):          350 KIAS
```

---

## Altitude Performance

### Service Ceiling
- Maximum: 41,000 ft
- Optimum cruise: 35,000-39,000 ft
- Single engine ceiling: 25,000 ft (fuel cell stack out)

### Climb Performance
- Rate of climb (SL, MTOW): 2,500 ft/min
- Time to FL350: 22 minutes
- Fuel to FL350: 180 kg H₂

---

## BWB-Specific Characteristics

### Stall Characteristics
- Benign stall behavior
- Excellent stall warning
- Good post-stall controllability
- No wing drop tendency
- Effective stall recovery

### High-Speed Characteristics
- Flutter cleared to VD + 15%
- No adverse compressibility effects
- Good high-speed stability
- Mach buffet margin: 0.03 Mach

---

## Environmental Limits

### Temperature
- Minimum: -54°C (standard atmosphere)
- Maximum: ISA +35°C

### Wind
- Crosswind: 35 kt
- Tailwind: 15 kt
- Headwind: No limit

---

## CG Effects on Envelope

### Forward CG Impact
- Higher stall speed (+5 KIAS at 25% MAC)
- Increased control forces
- Reduced maneuverability

### Aft CG Impact
- Lower stall speed (-3 KIAS at 42% MAC)
- Reduced stability
- Potential for pitch oscillations

---

## Simulation Models

Flight envelope simulations maintained in:
- `/SIMULATIONS/Flight_Envelope_Simulations/`
- SIM-02-00-001: Flight Envelope Model
- SIM-02-00-002: BWB Handling Characteristics
- SIM-02-00-003: CG Range Effects
- SIM-02-00-004: Emergency Scenarios

---

## Related Documents

- Performance Engineering
- BWB Operations Engineering
- Safety Engineering Analysis
- Weight & Balance Engineering

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-05 | Flight Dynamics Team | Initial release |

---

**Status:** Active  
**Next Review:** 2026-02-05  
**Owner:** AMPEL360 Flight Dynamics Engineering

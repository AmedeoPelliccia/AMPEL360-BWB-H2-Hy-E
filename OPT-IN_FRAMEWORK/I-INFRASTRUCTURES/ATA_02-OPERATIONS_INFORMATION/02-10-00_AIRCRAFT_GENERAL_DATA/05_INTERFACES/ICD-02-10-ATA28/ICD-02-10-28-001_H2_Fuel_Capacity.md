# ICD-02-10-28-001: H₂ Fuel Capacity Interface

**From:** ATA 02-10 Aircraft General Data  
**To:** ATA 28 Fuel (SAF and Cryogenic)

**ICD ID:** ICD-02-10-28-001  
**Version:** 1.0  
**Date:** 2025-11-05  
**Status:** Active

## Purpose

This Interface Control Document defines the hydrogen fuel capacity specifications that are fundamental to aircraft performance, range calculations, and operational planning.

## Data Exchange

### H₂ Fuel Capacity Specifications

**Provided by ATA 02-10:**
- **Total Usable Fuel Capacity:** 8,000 kg liquid H₂
- **Total Tank Volume:** 112,700 liters
- **Fuel Density (LH₂):** 71 kg/m³ @ -253°C
- **Unusable Fuel:** 120 kg (1.5% of capacity)
- **Boil-off Rate:** 0.5% per hour (ground), 0.2% per hour (flight)

**Data Format:** Fuel capacity specification table  
**Update Frequency:** Static (certified values)  
**Criticality:** Critical

### Tank Distribution

**Four Main Tanks:**
1. **Forward Center Tank:** 2,400 kg capacity
2. **Aft Center Tank:** 2,400 kg capacity
3. **Left Wing Tank:** 1,600 kg capacity
4. **Right Wing Tank:** 1,600 kg capacity

**Tank Configuration:**
- Symmetrical wing tank distribution
- Center tanks for CG management
- All tanks Type IV composite with vacuum insulation
- Redundant pressure and level sensors

### Fuel System Performance

**Feed Rates:**
- Maximum feed rate: 80 kg/hour per fuel cell
- Cruise feed rate: 400 kg/hour total
- Emergency feed capability: 120% nominal

**Pressure Parameters:**
- Storage pressure: 1.5-4.0 bar
- Feed pressure: 8-10 bar (after pump)
- Maximum pressure (safety): 12 bar

## BWB Integration Advantages

The Blended Wing Body configuration provides optimal fuel storage:
- **Large center body volume** accommodates tanks efficiently
- **Low-pressure differential** reduces tank weight
- **Thermal management** via wing surface heat exchangers
- **CG control** through selective tank usage

## Fuel Weight and CG Interface

**Critical for Weight & Balance (ATA 08):**
- Fuel load significantly affects CG (42% of fuel at center)
- Tank sequencing controls CG during flight
- Real-time fuel quantity/CG calculation required

**Fuel Loading Sequence:**
1. Center tanks to 50%
2. Wing tanks to 100%
3. Center tanks to 100%

**Fuel Usage Sequence:**
1. Wing tanks first (maintain CG)
2. Forward center tank
3. Aft center tank (maintain CG aft of forward limit)

## Performance Impact

**Range Calculations:**
- Specific energy: 33.3 kWh/kg (H₂) vs 11.9 kWh/kg (Jet-A)
- With 8,000 kg H₂: 266,400 kWh total energy
- Design range: 4,000 km (with reserves)
- Cruise altitude: 35,000-41,000 ft

**Reserve Fuel Requirements:**
- Alternate airport: 600 kg
- Holding (45 min): 300 kg
- Final reserve (30 min): 200 kg
- Contingency: 5% of trip fuel

## Safety Considerations

**Fuel Capacity Monitoring:**
- Continuous quantity indication per tank
- Low fuel warning: 1,500 kg remaining
- Critical fuel warning: 800 kg remaining
- Automatic tank switching on low level

**Boil-off Management:**
- Predicted boil-off calculated pre-flight
- Boil-off venting system: 20 kg/hour capacity
- Extended ground time procedures
- Return-to-gate fuel recalculation

## Dependencies

- Tank structural certification (ATA 20)
- Fuel cell power requirements (ATA 71)
- Flight performance calculations (ATA 02)
- Weight and balance (ATA 08)
- CAOS fuel monitoring (ATA 95)

## Responsibilities

**ATA 02-10 (Provider):**
- Define fuel capacity requirements
- Specify tank quantities and locations
- Maintain fuel specifications database

**ATA 28 (Consumer):**
- Design fuel system to meet capacity
- Implement fuel management system
- Provide accurate fuel quantity indication
- Manage boil-off and venting

## Change Control

Fuel capacity changes require:
1. Performance analysis and certification
2. Tank structural re-qualification if volume changes
3. Weight and balance revalidation
4. Range and endurance recalculation
5. Update to Aircraft Flight Manual Section 5

## CAOS Integration

**Real-time Monitoring:**
- Fuel quantity per tank
- Predicted range remaining
- Optimal fuel sequence
- Boil-off prediction
- Temperature monitoring

## References

- ISO 19881: Gaseous Hydrogen - Land Vehicle Fuel Containers
- SAE AS8691: Minimum Performance Standards for Hydrogen Fuel Systems
- EASA SC-H2 Special Condition: Hydrogen Fuel Systems

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Review Cycle: Annual or per modification

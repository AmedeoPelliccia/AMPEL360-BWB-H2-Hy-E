# 02-70-00 PROPULSION - Hydrogen Fuel Operations Data

**AMPEL360 BWB H2 Hy-E Q100 INTEGRA Platform**

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | AMPEL360-02-70-00-OVW-001 |
| **Version** | 1.0 |
| **Date** | 2025-11-12 |
| **Status** | Active |
| **Classification** | Operations Critical |

## Overview

This origin block contains all operational data related to hydrogen fuel and fuel cell propulsion systems. Following the AMPEL360_DOCUMENTATION_STANDARD, this directory organizes H2 fuel operations, safety procedures, and propulsion-related operational information.

## Structure

### Hydrogen Fuel System Data (02-70-10 to 02-70-18)
- **02-70-10**: Hydrogen Fuel Data
- **02-70-11**: H2 Fuel Capacity Data
- **02-70-12**: H2 Weight CG Effects
- **02-70-13**: H2 System Limitations
- **02-70-14**: H2 Fuel Planning Data
- **02-70-15**: H2 Temperature Effects
- **02-70-16**: H2 Quantity Indication
- **02-70-17**: H2 Emergency Procedures
- **02-70-18**: H2 Ground Operations

### H2 Refueling Operations (02-70-30)
- **02-70-30**: H2 Refueling Procedures

## Hydrogen Fuel System Characteristics

### Fuel Properties

**Liquid Hydrogen (LH2)**:
- **Chemical Formula**: H₂
- **Storage State**: Cryogenic liquid at -253°C (20K)
- **Density**: 70.8 kg/m³ (vs 804 kg/m³ for Jet-A)
- **Energy Content**: 120 MJ/kg (vs 43 MJ/kg for Jet-A)
- **Energy by Volume**: 8.5 MJ/L (vs 34.7 MJ/L for Jet-A)

### Operational Implications

**Advantages**:
- 3× energy per mass vs Jet-A
- Zero direct emissions (H₂O only)
- Excellent high-altitude performance
- No carbon footprint
- Renewable production potential

**Challenges**:
- 1/11th density requires larger tanks
- Cryogenic handling complexity
- Boil-off management required
- Specialized ground infrastructure
- Unique safety considerations

## Fuel System Capacity

### Tank Configuration

**Total Capacity**: 8,000 kg LH₂ (equivalent to ~28,000 kg Jet-A energy)

**Tank Distribution**:
- Wing tanks (primary): 6,400 kg (80%)
- Center body tank: 1,600 kg (20%)
- Total volume: ~113 m³

**Usable Fuel**: 7,800 kg (97.5%)
**Unusable Fuel**: 200 kg (2.5%)

### Weight and CG Effects

**Empty to Full Weight Change**: 8,000 kg
**CG Travel**: 2.5% MAC (due to distributed tanks)
**Fuel Burn Rate**: 380 kg/hr cruise @ M0.82

### Mission Fuel Planning

**Typical Mission** (4,000 km range):
- Taxi: 80 kg
- Takeoff/Climb: 620 kg
- Cruise: 2,850 kg
- Descent/Landing: 150 kg
- Reserve (45 min): 280 kg
- Alternate (200 km): 180 kg
- **Total Required**: 4,160 kg

## H2 Refueling Operations

### Refueling Procedures

**Ground Refueling**:
- **Method**: Single-point pressure refueling
- **Rate**: 180 kg/min maximum
- **Time**: 45 minutes (full tank from empty)
- **Pressure**: 4-6 bar transfer pressure
- **Temperature**: Maintained at -253°C

**Safety Procedures**:
1. Establish 25m safety zone
2. Connect grounding cable
3. Deploy H2 leak detectors (4 zones minimum)
4. Attach refueling coupling with leak check
5. Pre-cool transfer lines
6. Begin refueling at reduced rate (30%)
7. Increase to full rate after stabilization
8. Monitor boil-off and vent system
9. Complete refueling, purge lines
10. Disconnect and secure

### Refueling Safety Zones

| Zone | Radius | Restrictions |
|------|--------|--------------|
| Hot Zone | 0-25m | Essential personnel only, no ignition sources |
| Warm Zone | 25-50m | Limited access, safety equipment required |
| Cold Zone | 50m+ | Normal operations, awareness required |

## H2 System Limitations

### Operating Limits

**Tank Pressure**:
- Normal: 1.2-4.0 bar
- Maximum: 6.0 bar
- Minimum (vapor space): 0.8 bar

**Temperature**:
- Nominal: -253°C (20K)
- Maximum: -250°C (23K)
- Minimum: -259°C (14K - near triple point)

**Boil-Off**:
- Rate: 0.5% per day (ground), 0.3% per day (flight)
- Vent capacity: 10 kg/hr maximum
- Management: Auto-recompression or controlled vent

### Fuel Cell Interface

**Fuel Delivery**:
- Supply pressure: 3.5-4.5 bar
- Flow rate: 2.8 kg/hr per MW (nominal)
- Temperature: -20°C to +20°C (vaporized/warmed)
- Purity: 99.999% (5N grade)

## Emergency Procedures

### H2 System Emergencies

**Leak Detection**:
- Automatic: 4% LEL (Lower Explosive Limit) alarm
- Response: <2 seconds to isolate
- Crew action: Emergency H2 shutdown checklist

**Fire**:
- Detection: UV/IR flame detectors
- Suppression: Inert gas (nitrogen flood)
- Crew action: Emergency landing preparation

**Fuel Cell Malfunction**:
- Degraded mode: <3 MW per stack
- Response: Reduce power, consider diversion
- Emergency: Isolate affected stack, use backup power

**Tank Overpressure**:
- Automatic relief: 6.0 bar
- Crew action: Monitor venting, reduce climb rate
- Emergency: Emergency descent if uncontrolled

## Ground Operations

### Pre-Flight
- Fuel quantity check (visual + gauges)
- Tank pressure verification
- Leak detection system test
- Vent system check
- Fuel cell readiness check

### Post-Flight
- Fuel remaining calculation
- Boil-off assessment
- System status check
- Defueling if required (maintenance)

### Cold Soak
For aircraft parked >24 hours:
- Fuel stabilization monitoring
- Boil-off management (recompress or controlled vent)
- Tank pressure trending
- Safety zone maintenance

## Integration with Fuel Cells

### Fuel Cell Stacks
- **Configuration**: 4 × 2.5 MW PEM fuel cell stacks
- **Total Power**: 10 MW
- **Efficiency**: 55-60% (vs 40% turbofan)
- **H2 Consumption**: 280-320 kg/hr cruise
- **Operating Temperature**: 60-80°C

### Performance Benefits
- Instant response: 3 seconds to full power
- No altitude degradation
- Silent operation (75% quieter than turbofan)
- Zero emissions (H₂O only)
- Lower maintenance (fewer moving parts)

## Design-Driven Structure

Each system under this origin block contains:

- Fuel system operational procedures
- Performance data and charts
- Safety analyses and emergency procedures
- Refueling procedures and ground operations
- Integration with propulsion systems
- Training materials

## Cross-References

This origin block integrates with:

- **02-00-00_GENERAL**: Overall operations safety framework
- **02-20-00_SYSTEMS**: Performance planning, fuel planning
- **02-40-00_PROGRAMMING_ALGORITHMS**: Fuel optimization algorithms
- **02-50-00_STRUCTURES**: Refueling infrastructure
- **ATA 28**: Fuel (H2 Storage and Distribution)
- **ATA 71**: Power Plant (Fuel Cells)
- **ATA 73**: Engine Fuel and Control

## Compliance

All systems within this origin block comply with:
- ISO 19881 (Gaseous Hydrogen - Land Vehicle Fuel Containers)
- ISO 19880-8 (Hydrogen Refueling Protocols)
- SAE J2719 (Hydrogen Fuel Quality)
- EN 17127 (Hydrogen Refueling Stations)
- EASA CS-25 (Fuel System Requirements)
- FAA AC 25-8 (Fuel Tank System Safety)
- AMPEL360_DOCUMENTATION_STANDARD v1.4

## Safety

**H2 Safety Classification**: High-Risk  
**Boil-off Management**: Mandatory  
**Leak Detection**: Redundant (4 zones minimum)  
**Emergency Response**: <2 seconds isolation

---

**Status**: ✅ Active  
**Last Updated**: 2025-11-12  
**Safety Level**: High-Risk (Cryogenic Hydrogen)

# 03-00-05-03-04A - Air Conditioning GSE

## 1. Purpose
This document specifies the interface requirements for ground-based air conditioning units servicing the AMPEL360 BWB H₂ Hy-E aircraft cabin and electronics cooling systems.

## 2. Scope
This specification covers the air conditioning connection interface, cooling capacity requirements, operational procedures, and environmental considerations for ground pre-conditioning operations.

## 3. Applicable Documents
- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- ARP4754A (Guidelines for Development of Civil Aircraft and Systems)
- SAE ARP85 (Air Conditioning Equipment for Aircraft)
- ASHRAE Standard 55 (Thermal Environmental Conditions)
- ISO 7730 (Ergonomics of the Thermal Environment)
- SAE AS1241 (Air Start Units and Accessories)

## 4. Interface Description

### 4.1 Overview
Ground-based air conditioning units provide conditioned air to the aircraft cabin and electronics bays during ground operations when aircraft environmental control systems are not operating. This maintains passenger comfort and prevents equipment overheating.

### 4.2 Physical Characteristics
| Parameter | Specification | Tolerance |
|-----------|---------------|-----------|
| Connector Type | 12-inch flexible duct | Expandable 3-6m |
| Connection Location | Forward entry door L1, Aft door L4 | Port side |
| Supply Temperature | 18°C to 24°C | Cooling mode |
| Heating Temperature | 20°C to 30°C | Heating mode (cold weather) |
| Air Flow Rate | 400-600 CFM per connection | Adjustable |
| Supply Pressure | 0.5-2.0 inches H₂O | Positive pressure |
| Relative Humidity | 30% to 60% | Target range |
| Air Quality | HEPA filtered | 99.97% @ 0.3 micron |
| Noise Level | < 70 dBA | At 1m from unit |
| Duct Material | PVC-coated fabric | Fire-retardant |

### 4.3 Connection Procedure
1. **Pre-Connection Setup**
   - Position air conditioning unit within 10m of aircraft
   - Verify unit operational and parameters set correctly
   - Inspect flexible duct for damage or contamination
   - Check aircraft door opening dimensions
   - Verify electrical power supply available
   - Confirm weather conditions suitable for door opening

2. **Connection Sequence**
   - Open aircraft entry door per procedures
   - Extend flexible duct to aircraft door opening
   - Secure duct with provided clamps or straps
   - Ensure air seal around duct perimeter
   - Activate air conditioning unit
   - Gradually increase flow rate
   - Verify positive cabin pressure (0.5-1.0 inches H₂O)
   - Monitor cabin temperature and humidity

3. **Operating Monitoring**
   - Check cabin temperature every 15 minutes
   - Verify air flow rate remains stable
   - Monitor for condensation in duct
   - Check duct connections periodically
   - Adjust temperature setpoint as needed
   - Document operating parameters hourly

4. **Disconnection Procedure**
   - Reduce air flow gradually
   - Allow cabin temperature to stabilize
   - Shut down air conditioning unit
   - Remove duct from aircraft door
   - Close and secure aircraft door
   - Inspect duct and store properly
   - Document final cabin conditions

## 5. GSE Equipment Requirements
| Equipment | Specification | Notes |
|-----------|---------------|-------|
| Air Conditioning Unit | 60,000 BTU cooling capacity | Mobile, self-contained |
| Heating Capability | 40,000 BTU heating | For cold weather ops |
| Flexible Duct | 12-inch diameter, 6m length | Fire-retardant material |
| HEPA Filter | 99.97% efficiency | Replace per schedule |
| Humidity Control | Dehumidification capable | For tropical operations |
| Temperature Controller | Digital, ±1°C accuracy | Automatic regulation |
| Remote Monitor | Wireless display | For operator convenience |

## 6. Safety Requirements
- **Cabin Comfort and Safety**
  - Maintain temperature 18-24°C for passenger comfort
  - Avoid rapid temperature changes (< 5°C per hour)
  - Monitor humidity to prevent condensation
  - Ensure adequate air circulation throughout cabin
  - Verify no obstruction of emergency exits
  - Maintain communication with ground crew inside aircraft

- **Equipment Safety**
  - Electronics cooling: maintain temperature < 35°C
  - Prevent overheating of avionics equipment
  - Monitor for excessive condensation
  - Verify air supply is clean and filtered
  - Check for proper duct sealing to prevent air loss
  - Position unit on stable, level ground

- **H2 Aircraft Considerations**
  - Air intake positioned away from H2 vent areas
  - No recirculation of potentially H2-contaminated air
  - Unit electrical systems intrinsically safe rated
  - Enhanced ventilation requirements
  - Monitor for H2 presence before activating AC unit
  - Position unit upwind of aircraft

- **Environmental Considerations**
  - Energy-efficient operation to minimize fuel consumption
  - Use of environmentally friendly refrigerants (R-134a or R-1234yf)
  - Noise abatement per airport regulations
  - Exhaust discharge directed away from personnel and aircraft
  - Cold weather: prevent ice formation on ducts and aircraft

- **Operational Safety**
  - Verify aircraft door properly secured when duct connected
  - Two-person operation recommended
  - Unit operator maintains visual contact with aircraft
  - Emergency shutdown capability readily accessible
  - Fire extinguisher positioned near unit
  - Regular maintenance per manufacturer schedule

## 7. Cross-References
- Related ATA Chapters: 
  - ATA 21 (Air Conditioning)
  - ATA 52 (Doors)
  - ATA 24 (Electrical Power - for AC unit power)
- Parent Document: [03-00-05_Interfaces](../README.md)
- Related GSE Operations: 03-10_Operations
- Related Interface: [03-00-05-03-02A_Bleed_Air_Interface](./03-00-05-03-02A_Bleed_Air_Interface.md)
- Related Interface: [03-00-05-03-03A_Pneumatic_Pressure_Standards](./03-00-05-03-03A_Pneumatic_Pressure_Standards.md)
- Related Interface: [03-00-05-07-02A_Boarding_Bridge_Interface](../03-00-05-07_Passenger_Service_Interfaces/03-00-05-07-02A_Boarding_Bridge_Interface.md)

## 8. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 GSE Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

---

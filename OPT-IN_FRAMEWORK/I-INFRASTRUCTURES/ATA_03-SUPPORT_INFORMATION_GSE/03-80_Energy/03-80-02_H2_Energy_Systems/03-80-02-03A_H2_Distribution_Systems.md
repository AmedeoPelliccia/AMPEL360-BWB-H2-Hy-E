# 03-80-02-03A - H2 Distribution Systems

## 1. Purpose
This document specifies hydrogen distribution systems for Ground Support Equipment (GSE) operations, including piping networks, mobile transport, and safety systems for moving H2 from production/storage to end-use points.

## 2. Scope
This specification covers:
- Fixed piping distribution networks
- Mobile H2 transport (tube trailers, liquid tankers)
- Compression and pressure management
- Safety systems and leak detection
- Distribution optimization and control
- Maintenance and inspection requirements

## 3. Applicable Documents
- ISO 15649 (Petroleum and Natural Gas Industries - Piping)
- ASME B31.12 (Hydrogen Piping and Pipelines)
- SAE AS6968 (Hydrogen Aircraft Refueling Standards)
- ISO 19880-5 (Gaseous Hydrogen Fueling Stations - Dispenser Hoses and Hose Assemblies)
- NFPA 2 (Hydrogen Technologies Code)
- ADR/RID (Transport of Dangerous Goods by Road/Rail)
- ISO 11114 (Gas Cylinders - Compatibility of Materials with Gas Contents)

## 4. Energy System Description

### 4.1 Overview
The H2 distribution system safely and efficiently transports hydrogen from production facilities or bulk storage to refueling dispensers and other end-use points within airport GSE operations.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Distribution Pressure | 50-900 bar | Multi-pressure zones |
| Piping Material | 316L Stainless Steel, Composite | H2-compatible materials |
| Leak Detection | <1% LEL sensitivity | Continuous monitoring |
| Pressure Drop | <5% end-to-end | At maximum flow |
| Mobile Transport Capacity | 500-4000 kg per delivery | Tube trailers or liquid tankers |
| Distribution Availability | 99.5% minimum | With redundancy |

### 4.3 Performance Requirements

#### 4.3.1 Fixed Piping Systems
- **Flow Capacity**: Support peak GSE refueling demand + 25% margin
- **Pressure Stability**: ±5% of nominal operating pressure
- **Response Time**: Pressure recovery within 30 seconds after demand surge
- **Leak Rate**: <0.1% of throughput annually
- **Material Compatibility**: Resistance to H2 embrittlement per ISO 11114

#### 4.3.2 Mobile Distribution
- **Delivery Frequency**: Match consumption with 1-2 day safety margin
- **Capacity**: Single delivery covers 1-3 days of operation
- **Turnaround Time**: <2 hours from arrival to departure
- **Safety**: Full compliance with ADR/RID transport regulations

### 4.4 Fixed Piping Distribution Systems

#### 4.4.1 System Architecture
**Hub-and-Spoke Configuration**:
- Central hub: Main H2 production/storage facility
- Primary distribution: High-pressure trunk lines (200-900 bar)
- Secondary distribution: Medium-pressure branch lines (50-200 bar)
- Local distribution: Low-pressure service lines (20-50 bar)
- Refueling stations: Multiple dispensing points throughout airport

**Ring Configuration** (for larger facilities):
- Redundant piping loops for high reliability
- Multiple feed points for load balancing
- Isolation valves for sectional maintenance

#### 4.4.2 Piping Materials and Design
**Material Selection**:
- Primary choice: 316L austenitic stainless steel
  - Excellent H2 compatibility
  - Resistance to embrittlement
  - Wide availability and familiarity
- Alternative: Composite piping (HDPE liner with fiber overwrap)
  - Lower weight
  - Corrosion immunity
  - Suitable for moderate pressures (<200 bar)

**Design Considerations**:
- Wall thickness: Per ASME B31.12 for operating pressure + safety factor
- Welding: Full penetration welds, 100% radiographic inspection
- Joints: Minimize joints; use welded connections preferred over threaded
- Expansion compensation: Flexible sections or expansion loops
- Supports: Designed to prevent stress concentration and vibration

#### 4.4.3 Valves and Fittings
- **Isolation Valves**: Manual and/or automated, fail-safe design
- **Pressure Regulating Valves**: Maintain downstream pressure within tolerances
- **Check Valves**: Prevent backflow and maintain system integrity
- **Pressure Relief Devices**: Thermally activated PRDs and spring-loaded relief valves
- **Emergency Shutdown Valves**: Rapid closure (<2 seconds) on safety signal

#### 4.4.4 Compression Stations
- **Purpose**: Boost pressure for high-pressure zones or refueling stations
- **Technology**: Multi-stage reciprocating or diaphragm compressors
- **Capacity**: Match local demand + compression losses
- **Efficiency**: >85% isentropic efficiency
- **Cooling**: Intercoolers between stages, final aftercooler
- **Safety**: Intrinsically safe design, pressure relief, leak detection

### 4.5 Mobile H2 Distribution

#### 4.5.1 Tube Trailers (Gaseous H2)
**Specifications**:
- Pressure: 200-500 bar Type III/IV composite cylinders
- Capacity: 500-1,200 kg H2 per trailer
- Trailer configuration: 10-12 large-diameter tubes in frame
- Manifold system: Quick-connect couplings for fast transfer
- Transport: Road transport per ADR/RID regulations

**Operations**:
- Delivery schedule: Based on consumption rate and storage capacity
- Transfer time: 30-60 minutes per trailer
- Safety: Grounding, bonding, leak checks before transfer
- Parking: Designated safe area with adequate ventilation and setbacks

#### 4.5.2 Liquid H2 Tankers (Cryogenic)
**Specifications**:
- Temperature: -253°C (20 K)
- Capacity: 3,000-5,000 kg H2 per tanker
- Tank: Vacuum-insulated cryogenic vessel
- Boil-off rate: <1% per day during transport
- Transfer: Cryogenic pumps or pressure-driven transfer

**Operations**:
- Delivery schedule: Less frequent than tube trailers due to higher capacity
- Transfer time: 60-120 minutes including cooldown and warm-up
- Safety: Cryogenic hazards (cold burns, embrittlement), vapor management
- Parking: Designated area with adequate spacing and ventilation

### 4.6 Safety Systems

#### 4.6.1 Leak Detection
- **Sensor Types**: Catalytic bead, electrochemical, thermal conductivity
- **Sensitivity**: <1% LEL (Lower Explosive Limit for H2 = 4% by volume)
- **Coverage**: All enclosed and semi-enclosed areas, valve stations
- **Response**: Automatic alerts, emergency shutdown if >25% LEL
- **Maintenance**: Calibration every 6 months, sensor replacement per manufacturer

#### 4.6.2 Ventilation
- **Natural Ventilation**: Preferred for outdoor installations
  - High points: H2 is lighter than air and rises
  - Openings: Minimum 1% of enclosed area
- **Forced Ventilation**: For enclosed or semi-enclosed spaces
  - Air change rate: Minimum 6 air changes per hour
  - Activation: Continuous or triggered by leak detection

#### 4.6.3 Fire Protection
- **Detection**: Flame detectors (UV/IR) and heat detectors
- **Suppression**: Water deluge systems for cooling, not extinguishing
  - H2 fires: Allow to burn in controlled manner
  - Water cooling: Prevent escalation to adjacent equipment
- **Emergency Response**: Trained personnel, fire brigade notification

#### 4.6.4 Pressure Monitoring and Control
- **Pressure Sensors**: Redundant sensors at critical points
- **High Pressure Alarm**: Alert at 105% of maximum operating pressure
- **Pressure Relief**: Automatic venting at 110% of maximum operating pressure
- **Emergency Depressurization**: Controlled venting to safe location in emergency

### 4.7 Distribution Optimization

**Optimization Objectives**:
- Minimize pressure losses (energy efficiency)
- Balance load across multiple feed points
- Prioritize critical refueling stations
- Coordinate production, storage, and distribution

**Control Strategy**:
- Real-time monitoring of pressure, flow, temperature at all key points
- Predictive algorithms for demand forecasting
- Dynamic pressure regulation based on demand
- Integration with energy management system (EMS)

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Piping Design | ASME B31.12, ISO 15649 | Design, fabrication, testing, inspection |
| Material Compatibility | ISO 11114 | Material selection and testing |
| Pressure Equipment | ASME BPVC, EN 13445 | Vessel and component certification |
| Transport Safety | ADR/RID | Mobile H2 transport compliance |
| Leak Detection | NFPA 2, ISO 26142 | Detection systems and response |
| Fire Safety | NFPA 2, ISO 22734-3 | Fire detection, suppression, emergency response |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Related GSE ANCHORS: 03-30_ANCHORS
- Related GSE Propulsion: 03-70_Propulsion
- Related GSE Storages: 03-60_Storages
- H2 Infrastructure: 03-80-02-01A_H2_Energy_Infrastructure
- Green H2 Production: 03-80-02-02A_Green_H2_Production
- H2 Energy Conversion: 03-80-02-04A_H2_Energy_Conversion
- H2 Safety: 03-80-08-02A_H2_Energy_Safety

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 GSE Energy WG | Initial release |

---

## Document Control

- **Status**: DRAFT – Subject to review and approval
- **Classification**: Internal Use
- **Owner**: AMPEL360 GSE Energy Working Group
- **Next Review**: 2026-03-08
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-08

---

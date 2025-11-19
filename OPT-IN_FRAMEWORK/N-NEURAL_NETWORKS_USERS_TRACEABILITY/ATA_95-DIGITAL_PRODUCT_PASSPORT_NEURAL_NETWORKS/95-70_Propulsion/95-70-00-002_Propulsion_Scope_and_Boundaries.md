# 95-70-00-002: Propulsion Scope and Boundaries

## 1. Executive Summary

This document defines the precise scope and boundaries of the Propulsion Digital Product Passport (DPP) within the AMPEL360 BWB H₂ Hy-E Q100 aircraft. It clarifies what is included, what is excluded, and where interfaces with other systems occur.

## 2. Scope Definition

### 2.1 In-Scope Systems

The Propulsion DPP encompasses:

#### 2.1.1 Core Propulsion Systems (ATA 70-79)

- **Standard Practices (ATA 70)**: Propulsion installation practices, safety margins, configuration baselines
- **Power Plant (ATA 71)**: Nacelle, pylon, mounting structures, access provisions
- **Engines/Propulsors (ATA 72)**: Open-fan propulsors, hybrid electric motors, core engine modules
- **Fuel Supply to Engine (ATA 73)**: Feed lines, pumps, valves, metering devices (engine side only)
- **Bleed Air (ATA 75)**: Bleed sources, manifolds, valves, energy recovery
- **Engine Controls (ATA 76)**: FADEC, hybrid control units, actuators, safety limits
- **Engine Indicating (ATA 77)**: Sensors, instruments, health monitoring channels
- **Exhaust (ATA 78)**: Exhaust ducting, noise treatment, emissions sensing
- **Lubrication (ATA 79)**: Oil tanks, pumps, filters, monitoring systems

#### 2.1.2 AMPEL360-Specific Propulsion Features

- **Hybrid Architecture**: Integration of H₂ fuel cells, electric motors, and mechanical propulsors
- **Open-Fan Technology**: Counter-rotating open-fan propulsors for efficiency
- **Cryogenic Interfaces**: H₂ fuel line connections at engine feed points
- **CO₂ Integration**: Links to CO₂ capture waste heat recovery
- **Neural Network Control**: CAOS-based thrust optimization and health monitoring

### 2.2 Out-of-Scope Systems

The following are explicitly **NOT** included in Propulsion DPP:

#### 2.2.1 Aircraft Fuel System (ATA 28)

- H₂ storage tanks (covered in 95-60-28 Storage DPP)
- Aircraft fuel distribution (covered in 95-20-28 Systems DPP)
- Fuel quantity indication (covered in 95-30-31 Instruments DPP)
- **Boundary**: Engine fuel inlet flange

#### 2.2.2 Electrical Power Generation (ATA 24)

- Fuel cell stacks (covered in 95-20-24 Electrical Power DPP)
- Power distribution (covered in 95-30-24)
- Battery systems (covered in 95-60-24 Storage DPP)
- **Boundary**: Generator output terminals

#### 2.2.3 Structures (ATA 50-57)

- Wing primary structure (covered in 95-50-57 Wing DPP)
- Fuselage integration points (covered in 95-50-53 Fuselage DPP)
- Structural load paths (covered in 95-50 Structures DPP)
- **Boundary**: Pylon-to-wing attach fittings

#### 2.2.4 Environmental Control (ATA 21, 36)

- Cabin air conditioning (covered in 95-30-21 ECS DPP)
- Pneumatic distribution beyond bleed manifold (covered in 95-30-36)
- **Boundary**: Bleed air outlet port on engine

#### 2.2.5 Flight Controls (ATA 27)

- Thrust reverser actuation (interface documented, control in 95-30-27)
- Thrust lever hardware (covered in 95-30-27 Flight Controls DPP)
- **Boundary**: Thrust command signal at FADEC input

## 3. Interface Boundaries

### 3.1 Physical Interfaces

| Interface | In-Scope | Out-of-Scope | Boundary Definition |
|-----------|----------|--------------|---------------------|
| **Fuel Supply** | Engine fuel pump inlet | H₂ distribution manifold | Engine fuel inlet flange |
| **Electrical** | Generator rotor | Power distribution bus | Generator terminal box |
| **Bleed Air** | Bleed port to first valve | Pneumatic distribution | Bleed air outlet flange |
| **Mounting** | Pylon structure | Wing primary structure | Pylon-to-wing bolt line |
| **Control** | FADEC and actuators | Flight control computers | MIL-STD-1553 bus connection |
| **Exhaust** | Nozzle to 3m downstream | Atmospheric dispersion | 3-meter plane aft of nozzle |

### 3.2 Functional Interfaces

| Function | Propulsion DPP Responsibility | Other System Responsibility |
|----------|------------------------------|----------------------------|
| **Thrust Generation** | Engine/propulsor performance | Flight control laws (ATA 22) |
| **Fuel Management** | Engine fuel metering | Aircraft fuel quantity (ATA 28) |
| **Power Generation** | Mechanical shaft power | Electrical conversion (ATA 24) |
| **Thermal Management** | Engine oil cooling | Heat sink distribution (ATA 21) |
| **Health Monitoring** | Engine sensor data | Centralized diagnostics (ATA 45) |

### 3.3 Data Interfaces

| Data Type | Propulsion DPP | Consuming System |
|-----------|---------------|------------------|
| **Thrust Demand** | Receives from FCC | Flight Control (ATA 22) |
| **Fuel Flow** | Provides to FMS | Flight Management (ATA 34) |
| **Health Data** | Provides to CAOS | Maintenance System (ATA 45) |
| **Emissions** | Provides to ESG reporting | Operations (ATA 02) |
| **Performance** | Provides to digital twin | Neural Networks (ATA 95) |

## 4. Geographical Scope

### 4.1 Aircraft Stations

The Propulsion DPP covers components located in:

- **Engine Nacelles**: Stations 100-300 (forward nacelles)
- **Pylons**: Vertical attachment structures
- **Aft Fuselage**: Stations 800-900 (if aft-mounted engines apply)
- **Wing Integration**: Spanwise stations 200-500 (underwing or embedded)

### 4.2 BWB-Specific Considerations

For the Blended Wing Body configuration:

- **Embedded Engines**: Propulsion systems integrated within center body
- **Distributed Propulsion**: Multiple smaller propulsors vs. traditional podded engines
- **Inlet Integration**: Boundary layer ingestion considerations
- **Exhaust Integration**: Upper surface exhaust for noise shielding

## 5. Lifecycle Scope

### 5.1 Design Phase

- Requirements capture and traceability
- Conceptual and detailed design
- Interface control documents (ICDs)
- Trade studies and optimization
- Digital twin model creation

### 5.2 Manufacturing Phase

- Supplier qualification
- Component manufacturing
- Assembly integration
- Ground testing and validation
- Quality assurance documentation

### 5.3 Operations Phase

- Flight operations procedures
- Performance monitoring
- Health management
- Predictive maintenance
- Operational data collection for NN training

### 5.4 End-of-Life Phase

- Decommissioning procedures
- Component removal and tagging
- Material sorting and recycling
- Circularity metrics tracking
- Lessons learned documentation

## 6. Regulatory Scope

### 6.1 Applicable Regulations

- **EASA CS-E**: Engine certification (if applicable)
- **EASA CS-25**: Integration into large aircraft
- **FAA FAR Part 33**: Engine airworthiness standards
- **FAA FAR Part 25**: Aircraft certification
- **EU AI Act**: Annex III high-risk systems (propulsion control)
- **EU DPP Regulation**: Product passport requirements

### 6.2 Certification Interfaces

| Certification Area | Lead Authority | Propulsion DPP Role |
|-------------------|----------------|---------------------|
| **Engine Type Certificate** | EASA/FAA Engine Section | Provide design and test data |
| **Aircraft Type Certificate** | EASA/FAA Aircraft Section | Provide integration evidence |
| **AI System Assessment** | EU Notified Body | Provide NN safety case |
| **Environmental Compliance** | ICAO CAEP | Provide emissions data |

## 7. Data Ownership and Governance

### 7.1 Propulsion DPP Data

- **Owner**: AMPEL360 Propulsion Systems Engineering
- **Custodian**: Digital Product Passport Team
- **Access**: Role-based (design, operations, maintenance, certification)

### 7.2 Shared Data

- **Interface Data**: Co-owned with interfacing system owners
- **Performance Data**: Shared with Flight Operations and CAOS
- **Health Data**: Shared with Maintenance and NN teams

### 7.3 External Data

- **Supplier Data**: Licensed from propulsion system suppliers
- **Regulatory Data**: Maintained per authority requirements
- **Industry Standards**: Referenced from SAE, AIAA, ASME

## 8. Change Management

### 8.1 Scope Change Process

1. **Request**: Stakeholder submits scope change request
2. **Analysis**: Impact assessment on interfaces and systems
3. **Review**: Configuration Control Board (CCB) review
4. **Approval**: CCB approves/rejects scope change
5. **Implementation**: Update DPP and notify affected parties
6. **Verification**: Confirm interfaces remain valid

### 8.2 Interface Change Notification

When propulsion interfaces change:

- Notify affected system owners (ATA 28, 24, 27, etc.)
- Update Interface Control Documents (ICDs)
- Revise traceability matrix
- Conduct integration testing

## 9. Limitations and Assumptions

### 9.1 Current Limitations

- **Technology Maturity**: Some hybrid propulsion technologies at TRL 6-7
- **Data Availability**: Limited operational fleet data (pre-entry into service)
- **Certification Precedent**: Novel propulsion configurations require authority collaboration

### 9.2 Key Assumptions

- H₂ fuel system provides fuel at specified pressure and temperature
- Electrical power system can handle generator transients
- FADEC software complies with DO-178C DAL A
- Neural network models achieve target accuracy (≥95%)

## 10. Future Scope Considerations

### 10.1 Potential Expansions

- **Advanced Propulsion**: Hydrogen combustion engines, electric-only modes
- **Distributed Propulsion**: Additional smaller propulsors for redundancy
- **Propulsion-Airframe Integration**: Active flow control, morphing nacelles
- **Autonomous Operations**: Fully automated thrust management

### 10.2 Emerging Technologies

- **Additive Manufacturing**: 3D-printed engine components
- **Digital Thread**: Blockchain-based traceability
- **Edge AI**: On-engine neural network inference
- **Quantum Optimization**: Quantum algorithms for control tuning

## 11. Related Documents

- [95-70-00-001: Propulsion DPP Overview](95-70-00-001_Propulsion_DPP_Overview.md)
- [95-70-00-003: Cross-ATA Propulsion Map](95-70-00-003_Cross_ATA_Propulsion_Map.csv)
- [95-70-00-005: Propulsion Traceability Matrix](00_META/95-70-00-005_Propulsion_Traceability_Matrix.csv)

## 12. Version History

| Version | Date       | Author               | Changes                    |
|---------|------------|----------------------|----------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Doc Team    | Initial creation           |

---

**Document ID**: 95-70-00-002  
**Status**: Active  
**Classification**: Internal Use  
**Next Review**: 2026-02-17

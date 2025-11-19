# 95-70-00-004: Propulsion Taxonomy

## 1. Introduction

This document defines the taxonomy and classification system for all propulsion components, systems, and subsystems within the AMPEL360 BWB H₂ Hy-E Q100 aircraft. The taxonomy provides a structured vocabulary for consistent naming, categorization, and traceability across all propulsion-related documentation.

## 2. Top-Level Classification

### 2.1 Propulsion System Types

```
Propulsion Systems
├── Primary Propulsion
│   ├── Open-Fan Propulsors
│   ├── Hybrid Electric Motors
│   └── Core Engine Modules (if applicable)
├── Energy Conversion
│   ├── H₂ Fuel Cells (covered in ATA 24)
│   ├── Shaft-Driven Generators
│   └── Power Electronics
├── Fuel Supply
│   ├── Engine Feed Systems
│   ├── Fuel Metering and Control
│   └── H₂ Cryogenic Interfaces
├── Auxiliary Systems
│   ├── Bleed Air Extraction
│   ├── Lubrication Systems
│   └── Thermal Management
└── Control and Monitoring
    ├── FADEC Systems
    ├── Health Monitoring
    └── Neural Network Integration
```

## 3. Detailed Taxonomy by ATA Chapter

### 3.1 ATA 70: Standard Practices - Propulsion

**Category**: Standards and Practices

**Components**:
- Installation Standards
- Safety Margins and Limits
- Configuration Baselines
- Maintenance Practices
- Documentation Standards

**Classification**: Non-Physical (Documentation)

---

### 3.2 ATA 71: Power Plant Integration

**Category**: Mechanical Integration

**Major Assemblies**:

#### 3.2.1 Nacelle Structure
- **Type**: Aerodynamic Housing
- **Materials**: Composite (CFRP), Aluminum Alloys
- **Functions**: Aerodynamic shaping, noise attenuation, fire protection
- **Criticality**: High

#### 3.2.2 Pylon Structure
- **Type**: Load-Bearing Structure
- **Materials**: Titanium, Aluminum Alloys, CFRP
- **Functions**: Engine mounting, load transfer, systems routing
- **Criticality**: Critical

#### 3.2.3 Mounting Hardware
- **Type**: Attachment Interface
- **Components**: Thrust links, side links, vertical links, failsafe provisions
- **Criticality**: Critical

#### 3.2.4 Access Provisions
- **Type**: Maintenance Interface
- **Components**: Cowling doors, access panels, inspection ports
- **Criticality**: Medium

---

### 3.3 ATA 72: Engines and Propulsors

**Category**: Thrust Generation

#### 3.3.1 Open-Fan Propulsor
- **Type**: Counter-Rotating Open Rotor
- **Subcomponents**:
  - Forward Rotor Assembly (12-14 blades)
  - Aft Rotor Assembly (12-14 blades)
  - Hub and Spinner
  - Pitch Control Mechanism
  - Gearbox (if applicable)
- **Power Source**: Electric Motor or Core Engine
- **Diameter**: 4.5-5.5 meters
- **Criticality**: Critical

#### 3.3.2 Hybrid Electric Motor
- **Type**: High-Power Density Electric Motor
- **Subcomponents**:
  - Stator Assembly
  - Rotor Assembly
  - Cooling System (liquid or air)
  - Power Electronics Interface
  - Position Sensors
- **Power Rating**: 2-3 MW per motor
- **Criticality**: Critical

#### 3.3.3 Core Engine Module (if applicable)
- **Type**: Gas Turbine or H₂ Combustion Engine
- **Subcomponents**:
  - Compressor Section
  - Combustion Chamber (if applicable)
  - Turbine Section
  - Accessory Gearbox
- **Note**: May be omitted in fully electric configuration
- **Criticality**: Critical (if present)

---

### 3.4 ATA 73: Engine Fuel and Supply

**Category**: Fuel Management (Engine Side)

#### 3.4.1 Engine Fuel Pump
- **Type**: Cryogenic-Compatible Pump
- **Function**: H₂ pressure boost for injection
- **Temperature Range**: -253°C to -240°C
- **Pressure**: 5-15 bar
- **Criticality**: Critical

#### 3.4.2 Fuel Metering Unit (FMU)
- **Type**: Electronic Control Valve
- **Function**: Precise fuel flow regulation
- **Control Signal**: FADEC digital commands
- **Redundancy**: Dual-channel
- **Criticality**: Critical

#### 3.4.3 Fuel Lines and Manifolds
- **Type**: Cryogenic Transfer Lines
- **Materials**: Stainless steel, vacuum-insulated
- **Connections**: Quick-disconnect couplings
- **Criticality**: Critical

#### 3.4.4 Fuel Filters
- **Type**: Cryogenic Filters
- **Function**: Remove contaminants, ice crystals
- **Criticality**: High

---

### 3.5 ATA 75: Bleed Air and Air Management

**Category**: Pneumatic Energy Extraction

#### 3.5.1 Bleed Air Source
- **Type**: Compressor Bleed Port (if turbine engine)
- **Alternative**: Electric compressor (if pure electric)
- **Pressure**: 30-45 psi
- **Temperature**: 200-400°C
- **Criticality**: High

#### 3.5.2 Bleed Air Manifold
- **Type**: Distribution Manifold
- **Function**: Route bleed air to aircraft systems
- **Interfaces**: ATA 21 (ECS), ATA 30 (Ice Protection)
- **Criticality**: High

#### 3.5.3 Bleed Control Valves
- **Type**: Pneumatic Control Valves
- **Function**: Regulate bleed flow and pressure
- **Control**: FADEC or pneumatic controller
- **Criticality**: High

#### 3.5.4 Waste Heat Recovery
- **Type**: Heat Exchanger
- **Function**: Recover exhaust heat for CO₂ capture system
- **Interface**: ATA 21-80 (CO₂ Capture)
- **Criticality**: Medium

---

### 3.6 ATA 76: Propulsion Control Systems

**Category**: Digital Control

#### 3.6.1 FADEC (Full Authority Digital Engine Control)
- **Type**: Dual-Channel Digital Controller
- **Functions**: Thrust control, fuel metering, health monitoring, protection logic
- **Software Level**: DO-178C DAL A
- **Criticality**: Critical

#### 3.6.2 Hybrid Control Unit (HCU)
- **Type**: Integrated Power Management Controller
- **Functions**: Coordinate fuel cell, battery, and motor operations
- **Interface**: FADEC, Battery Management System, CAOS
- **Criticality**: Critical

#### 3.6.3 Actuators
- **Types**:
  - Fuel metering valve actuators
  - Variable geometry actuators (if applicable)
  - Bleed valve actuators
  - Thrust reverser actuators (if applicable)
- **Control**: FADEC commands
- **Criticality**: Critical

#### 3.6.4 Neural Network Optimization Module
- **Type**: Real-Time AI Inference Engine
- **Functions**: Thrust optimization, fuel efficiency, thermal management
- **Interface**: CAOS, FADEC
- **Safety**: Advisory only (FADEC has override)
- **Criticality**: High

---

### 3.7 ATA 77: Propulsion Indications and Health Monitoring

**Category**: Sensing and Diagnostics

#### 3.7.1 Engine Sensors
- **Temperature Sensors**:
  - Exhaust Gas Temperature (EGT)
  - Oil Temperature
  - H₂ Fuel Temperature
- **Pressure Sensors**:
  - Engine Pressure Ratio (EPR)
  - Oil Pressure
  - Fuel Pressure
- **Speed Sensors**:
  - N1 (Fan/Propulsor RPM)
  - N2 (Core RPM, if applicable)
- **Vibration Sensors**:
  - Accelerometers on bearings
  - Shaft position sensors

#### 3.7.2 Health Monitoring Channels
- **Data Bus**: ARINC 429, MIL-STD-1553, Ethernet
- **Sample Rate**: 10-100 Hz
- **Data Volume**: ~1 MB/flight hour per engine
- **Neural Network Input**: Real-time anomaly detection

#### 3.7.3 Cockpit Indications
- **Primary Displays**:
  - Thrust indication (% or EPR)
  - Fuel flow
  - EGT
  - Oil pressure and temperature
  - Alerts and advisories

---

### 3.8 ATA 78: Exhaust and Emissions

**Category**: Exhaust Management

#### 3.8.1 Exhaust Nozzle
- **Type**: Fixed or Variable Geometry
- **Function**: Optimize exhaust velocity, noise reduction
- **Materials**: Titanium alloys, ceramics
- **Criticality**: High

#### 3.8.2 Noise Treatment
- **Type**: Acoustic Liners, Chevrons
- **Function**: Reduce jet noise
- **Compliance**: ICAO Annex 16 Chapter 14
- **Criticality**: Medium

#### 3.8.3 Emissions Sensing
- **Sensors**: NOx, CO, H₂O, particulates (if combustion)
- **Function**: Compliance monitoring, ESG reporting
- **Interface**: CAOS, ATA 45 (Maintenance System)
- **Criticality**: Medium

#### 3.8.4 Exhaust Heat Recovery
- **Type**: Heat Exchanger
- **Function**: Provide thermal energy to CO₂ capture system
- **Interface**: ATA 21-80
- **Criticality**: Medium

---

### 3.9 ATA 79: Lubrication and Oil Systems

**Category**: Lubrication and Cooling

#### 3.9.1 Oil Tank
- **Type**: Integral or Remote Tank
- **Capacity**: 10-20 liters per engine
- **Materials**: Aluminum, stainless steel
- **Criticality**: Critical

#### 3.9.2 Oil Pumps
- **Types**: Scavenge pumps, pressure pumps
- **Function**: Circulate oil, return oil to tank
- **Redundancy**: Dual pumps
- **Criticality**: Critical

#### 3.9.3 Oil Filters
- **Type**: Full-flow and bypass filters
- **Function**: Remove contaminants
- **Monitoring**: Differential pressure sensor
- **Criticality**: High

#### 3.9.4 Oil Cooler
- **Type**: Air-oil or fuel-oil heat exchanger
- **Function**: Maintain oil temperature within limits
- **Criticality**: High

#### 3.9.5 Oil Quality Monitoring
- **Sensors**: Metal particle detectors, oil quality sensors
- **Function**: Early detection of wear or contamination
- **Interface**: Health monitoring system, CAOS
- **Criticality**: Medium

---

## 4. Classification Attributes

Each propulsion component is classified with the following attributes:

| Attribute | Values | Description |
|-----------|--------|-------------|
| **Type** | Physical, Logical, Documentation | Nature of the component |
| **ATA Chapter** | 70-79 | Primary ATA classification |
| **Criticality** | Critical, High, Medium, Low | Safety and operational impact |
| **Redundancy** | None, Dual, Triple, N+1 | Fault tolerance level |
| **Maintainability** | On-wing, On-ground, Shop | Maintenance location |
| **TRL** | 1-9 | Technology Readiness Level |
| **Heritage** | New, Modified, Existing | Design maturity |
| **Supplier** | OEM, Third-party, In-house | Source of component |

---

## 5. Naming Conventions

### 5.1 Component Identifiers

**Format**: `[ATA]-[System]-[Subsystem]-[Part]-[Instance]`

**Examples**:
- `72-PROP-FAN-BLADE-L1-001`: Left engine, propulsor, fan blade #1
- `76-FADEC-CPU-A`: FADEC channel A CPU
- `79-OIL-PUMP-SCAVENGE-R1`: Right engine, scavenge oil pump

### 5.2 Document Identifiers

**Format**: `95-70-[ATA]-[Sequence]_[Title]`

**Examples**:
- `95-70-72-001_Engines_and_Propulsors_Overview.md`
- `95-70-76-A-003_Control_IF_Spec_OpenAPI.yaml` (ASSET)

---

## 6. Taxonomy Extensions

### 6.1 AMPEL360-Specific Additions

The following categories are unique to AMPEL360:

- **H₂ Cryogenic Interfaces**: Components operating at -253°C
- **Hybrid Control Logic**: Integration of fuel cells, batteries, and motors
- **Neural Network Integration**: AI/ML components in control loop
- **CO₂ Circularity Links**: Waste heat and energy recovery
- **BWB Propulsion Integration**: Embedded or distributed propulsion

### 6.2 Future Extensions

- **Hydrogen Combustion**: If H₂ combustion engines are adopted
- **Boundary Layer Ingestion**: If BLI propulsors are added
- **Morphing Nacelles**: Adaptive geometry for efficiency
- **Distributed Electric Propulsion**: Multiple smaller propulsors

---

## 7. Taxonomy Governance

- **Owner**: AMPEL360 Propulsion Systems Engineering
- **Review Cycle**: Semi-Annual
- **Change Process**: Configuration Control Board (CCB) approval required
- **Tool Support**: Taxonomy managed in structured database, exported to JSON

---

## 8. Related Documents

- [95-70-00-001: Propulsion DPP Overview](../95-70-00-001_Propulsion_DPP_Overview.md)
- [95-70-00-006: Propulsion Assets Registry](95-70-00-006_Propulsion_Assets_Registry.json)
- [AMPEL360 Documentation Standard](../../../../AMPEL360_DOCUMENTATION_STANDARD.md)

---

## 9. Version History

| Version | Date       | Author               | Changes                    |
|---------|------------|----------------------|----------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Doc Team    | Initial taxonomy           |

---

**Document ID**: 95-70-00-004  
**Status**: Active  
**Classification**: Internal Use  
**Next Review**: 2026-05-17

# 03-80-02-02A - Green H2 Production

## 1. Purpose
This document specifies green hydrogen production systems for Ground Support Equipment (GSE) operations, focusing on water electrolysis powered by renewable energy sources.

## 2. Scope
This specification covers:
- Electrolysis technologies (PEM, Alkaline, AEM)
- Renewable energy integration
- Water supply and treatment
- H2 purification and drying
- System efficiency and performance
- Production capacity planning

## 3. Applicable Documents
- ISO 22734-1 (Hydrogen Generators Using Water Electrolysis)
- IEC 62282-3-201 (Fuel Cell Technologies - Stationary Fuel Cell Power Systems - Performance Test Methods)
- ISO 14687 (Hydrogen Fuel Quality - Product Specification)
- ISO 50001 (Energy Management Systems)
- ASME BPVC Section VIII (Pressure Vessels)
- IEC 61508 (Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems)

## 4. Energy System Description

### 4.1 Overview
Green hydrogen production via water electrolysis is the cornerstone of sustainable GSE energy systems. This process uses renewable electricity to split water into hydrogen and oxygen, producing zero-carbon hydrogen fuel for GSE operations.

### 4.2 Specifications
| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Production Technology | PEM and/or Alkaline Electrolysis | Multi-technology approach |
| Production Capacity | 500-5000 kg H2/day | Scalable modular design |
| H2 Purity | ≥99.97% (ISO 14687 Type I Grade D) | Direct fuel cell grade |
| System Efficiency | >60% (HHV), >70% (LHV) | Stack efficiency |
| Water Consumption | 9-10 L/kg H2 | Including process losses |
| Renewable Energy Source | Solar PV, Wind, Grid Renewable | 100% renewable electricity |

### 4.3 Performance Requirements

#### 4.3.1 Production Rate and Capacity
- Nominal production: Match daily GSE fleet H2 demand + 20% margin
- Peak production: 150% of nominal for demand variability
- Minimum load: 10% of nominal capacity
- Ramp rate: 0-100% in <5 minutes (PEM), <30 minutes (Alkaline)
- Start-up time: <5 minutes (PEM), <60 minutes (Alkaline)

#### 4.3.2 Output Quality
- H2 purity: ≥99.97% per ISO 14687 Type I Grade D
- Moisture content: <5 ppm (dewpoint -70°C)
- Total particulates: <1 mg/kg
- Oxygen content: <5 ppm
- Other contaminants: Per ISO 14687 limits

### 4.4 Electrolysis Technologies

#### 4.4.1 Proton Exchange Membrane (PEM) Electrolysis
**Description**: Uses a solid polymer electrolyte membrane to conduct protons while blocking gases.

**Characteristics**:
- Operating temperature: 50-80°C
- Operating pressure: 30-80 bar (high-pressure variant)
- Current density: 1-3 A/cm²
- Efficiency: 60-70% (HHV)
- Response time: Seconds to minutes
- Part-load capability: 10-100% of nominal

**Advantages**:
- Compact design, high power density
- Fast dynamic response (renewable energy compatibility)
- High purity H2 output
- High-pressure output option (reduces compression needs)

**Limitations**:
- Higher capital cost
- Requires noble metal catalysts (Pt, Ir)
- Membrane degradation over time

**Applications**:
- Primary technology for variable renewable energy integration
- Fast-response, load-following applications
- Compact installations with space constraints

#### 4.4.2 Alkaline Electrolysis
**Description**: Uses liquid alkaline electrolyte (KOH or NaOH) between two electrodes.

**Characteristics**:
- Operating temperature: 60-80°C
- Operating pressure: 1-30 bar
- Current density: 0.2-0.5 A/cm²
- Efficiency: 60-70% (HHV)
- Response time: Minutes to tens of minutes
- Part-load capability: 20-100% of nominal

**Advantages**:
- Mature, proven technology
- Lower capital cost
- Long operational lifetime (>80,000 hours)
- No noble metal catalysts required

**Limitations**:
- Larger footprint
- Slower dynamic response
- Lower current density
- Maintenance requirements for liquid electrolyte

**Applications**:
- Base-load H2 production
- Large-scale installations
- Grid-connected systems with stable power supply

#### 4.4.3 Anion Exchange Membrane (AEM) Electrolysis
**Description**: Emerging technology combining advantages of PEM and Alkaline.

**Characteristics**:
- Operating temperature: 40-60°C
- Current density: 0.5-2 A/cm²
- Efficiency: Target >65% (HHV)
- Noble-metal-free catalysts

**Status**: Development/early commercialization (not primary choice for near-term deployments)

### 4.5 System Components

#### 4.5.1 Water Supply and Treatment
- Source: Municipal water supply or on-site well
- Treatment: Reverse osmosis + deionization (conductivity <0.1 µS/cm)
- Capacity: 1.2x nominal consumption (includes cooling, cleaning)
- Storage: 24-hour supply buffer tank
- Quality monitoring: Continuous conductivity, pH, and particulate sensors

#### 4.5.2 Electrolyzer Stack
- Core component: Electrode assemblies, membrane/electrolyte, bipolar plates
- Cooling: Deionized water circulation system
- Temperature control: ±2°C stability
- Pressure control: Pressure sensors and relief devices
- Gas separation: Integrated or external gas-liquid separators

#### 4.5.3 Power Supply and Control
- AC/DC converter: High-efficiency rectifier (>96% efficiency)
- Power quality: Low ripple (<5%), stable output
- Control system: PLC-based with SCADA integration
- Safety interlocks: Multiple redundant safety systems
- Grid interface: Power factor correction, harmonic filtering

#### 4.5.4 H2 Purification and Conditioning
- Oxygen removal: Catalytic deoxidizer (if required)
- Moisture removal: Desiccant dryers or pressure swing adsorption (PSA)
- Compression: Multi-stage compression to storage pressure (if low-pressure electrolyzer)
- Quality monitoring: Online analyzers for purity verification
- Buffer storage: Small on-skid H2 buffer for process stability

### 4.6 Renewable Energy Integration

#### 4.6.1 Direct Coupling
- On-site solar PV or wind turbines directly powering electrolyzers
- Benefits: Minimal grid dependence, lowest carbon intensity
- Challenges: Variable production, requires H2 storage buffering

#### 4.6.2 Grid-Connected with Renewable Power Purchase Agreement (PPA)
- Electrolyzers powered by grid electricity from certified renewable sources
- Benefits: Stable power supply, predictable production
- Verification: Renewable Energy Certificates (RECs) or Guarantees of Origin (GOs)

#### 4.6.3 Hybrid Configuration
- Combination of on-site renewables + grid backup
- Energy management system optimizes electrolyzer operation
- Maximizes use of low-cost/renewable electricity

### 4.7 Production Planning and Optimization

**Factors**:
- GSE fleet H2 demand profile (daily, weekly, seasonal)
- Renewable energy availability (solar/wind generation patterns)
- Electricity pricing (time-of-use rates)
- H2 storage capacity and state of charge
- Electrolyzer efficiency curve (load-dependent)

**Strategy**:
- Operate electrolyzers during periods of high renewable generation
- Shift production to off-peak hours if grid electricity is used
- Maintain H2 storage at optimal levels for operational resilience
- Balance production smoothness with efficiency optimization

## 5. Safety and Environmental Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Electrolyzer Safety | ISO 22734-1, IEC 61508 | Design, operation, functional safety |
| Pressure Equipment | ASME BPVC Section VIII | Vessel design, testing, certification |
| Electrical Safety | IEC 61508, NFPA 70 | Electrical systems, grounding, protection |
| H2 Quality | ISO 14687 | Continuous monitoring and certification |
| Water Quality | ASTM D5127 | Water treatment and monitoring |
| Environmental Management | ISO 14001, ISO 50001 | EMS, energy efficiency, waste management |

## 6. Cross-References
- Related ATA Chapters: ATA 03 (Support Information/GSE)
- Parent Document: 03-80_Energy
- Related GSE ANCHORS: 03-30_ANCHORS
- Related GSE Propulsion: 03-70_Propulsion
- Related GSE Storages: 03-60_Storages
- Energy Strategy: 03-80-01-01A_GSE_Energy_Strategy
- H2 Infrastructure: 03-80-02-01A_H2_Energy_Infrastructure
- H2 Distribution: 03-80-02-03A_H2_Distribution_Systems
- Renewable Energy: 03-80-04_Renewable_Energy_GSE
- Power-to-H2 Systems: 03-80-04-04A_Power_To_H2_Systems

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

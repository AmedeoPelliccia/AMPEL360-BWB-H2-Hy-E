# 95-20-00-004 — Subsystems Taxonomy

## Document Information

- **Document ID**: 95-20-00-004
- **Title**: Neural Network Subsystems Taxonomy
- **Version**: 1.0
- **Date**: 2025-11-17
- **Status**: Active
- **Classification**: Technical Reference

## Purpose

This document defines the taxonomic classification system for AMPEL360 Neural Network subsystems, providing a standardized hierarchy for organizing, discovering, and managing NN capabilities across the aircraft systems landscape.

## Taxonomy Overview

The 95-20 subsystems taxonomy is organized along multiple dimensions:

1. **Functional Domain** (What the subsystem does)
2. **ATA Chapter Alignment** (Which aircraft system it serves)
3. **Criticality Level** (Design Assurance Level)
4. **AI/ML Architecture Type** (Technical approach)
5. **Deployment Context** (Where it runs)

## Taxonomy Structure

### Level 1: Core vs. Application Subsystems

```
95-20_Subsystems
├── CORE (Infrastructure)
│   ├── 95-20-01: NN_Core_Platform
│   └── 95-20-02: NN_DPP_Blockchain
└── APPLICATION (ATA-Specific)
    ├── ENVIRONMENT: 95-20-21
    ├── FLIGHT: 95-20-27, 95-20-57
    ├── PROPULSION_FUEL: 95-20-28, 95-20-70
    ├── DATA: 95-20-31
    ├── AVIONICS: 95-20-42
    ├── MAINTENANCE: 95-20-45
    ├── AUXILIARY: 95-20-49
    ├── STRUCTURES: 95-20-53
    └── ENERGY: 95-20-80
```

### Level 2: Functional Domain Classification

| Domain | Subsystems | Primary Function | Examples |
|--------|-----------|------------------|----------|
| **Infrastructure** | 01, 02 | Platform services | Model registry, blockchain |
| **Environmental Control** | 21 | Climate management | Cabin temp, air quality |
| **Flight Dynamics** | 27, 57 | Flight control & safety | Gust alleviation, flutter |
| **Fuel & Propulsion** | 28, 70 | Energy generation | H₂ management, thrust |
| **Data & Recording** | 31 | Information capture | Anomaly detection, logging |
| **Avionics Integration** | 42 | Compute infrastructure | IMA partitions, AFDX |
| **Predictive Maintenance** | 45 | Health management | RUL, fault diagnosis |
| **Auxiliary Systems** | 49 | Backup power | APU health |
| **Structural Health** | 53 | Load monitoring | SHM, fatigue estimation |
| **Energy Management** | 80 | Electrical systems | Load prediction, battery SOH |

### Level 3: ATA Chapter Mapping

Each application subsystem directly maps to its parent ATA chapter:

```
95-20-XX ↔ ATA XX

95-20-21 ↔ ATA 21 (Air Conditioning)
95-20-27 ↔ ATA 27 (Flight Controls)
95-20-28 ↔ ATA 28 (Fuel)
95-20-31 ↔ ATA 31 (Recording)
95-20-42 ↔ ATA 42 (IMA)
95-20-45 ↔ ATA 45 (Maintenance)
95-20-49 ↔ ATA 49 (APU)
95-20-53 ↔ ATA 53 (Fuselage)
95-20-57 ↔ ATA 57 (Wings)
95-20-70 ↔ ATA 70-79 (Propulsion)
95-20-80 ↔ ATA 80 (Electrical)
```

**Exception**: Core subsystems (01, 02) are cross-cutting and serve all ATA chapters.

## Criticality Taxonomy

### Design Assurance Levels (DAL)

| Level | Failure Impact | Subsystems | Verification Requirements |
|-------|---------------|------------|---------------------------|
| **DAL-A** | Catastrophic | 27, 57, 70, 01 | DO-178C Level A + DO-333 |
| **DAL-B** | Hazardous | 28, 42, 53, 80, 02 | DO-178C Level B + DO-333 |
| **DAL-C** | Major | 21, 31, 45 | DO-178C Level C + DO-333 |
| **DAL-D** | Minor | 49 | DO-178C Level D + DO-333 |

### Criticality Rationale

**DAL-A Subsystems (Flight-Critical)**:
- **95-20-27 (Flight Controls)**: Direct control of flight path
- **95-20-57 (Wing Systems)**: Flutter prevention is flight-critical
- **95-20-70 (Propulsion)**: Engine performance affects flight safety
- **95-20-01 (Core Platform)**: Hosts all DAL-A models

**DAL-B Subsystems (Safety-Significant)**:
- **95-20-28 (Fuel)**: H₂ leak could be hazardous
- **95-20-42 (IMA)**: Avionics failure impacts multiple systems
- **95-20-53 (Structures)**: Structural failure is hazardous
- **95-20-80 (Energy)**: Total power loss is hazardous
- **95-20-02 (Blockchain)**: Certification evidence integrity

**DAL-C Subsystems (Operationally Important)**:
- **95-20-21 (ECS)**: Cabin environment affects passenger comfort
- **95-20-31 (Recording)**: Important for investigation, not flight safety
- **95-20-45 (Maintenance)**: Affects dispatch reliability

**DAL-D Subsystems (Minor Impact)**:
- **95-20-49 (APU)**: Failure only inconveniences operations

## AI/ML Architecture Taxonomy

### Model Type Classification

| Architecture | Subsystems | Use Cases | Characteristics |
|-------------|-----------|-----------|-----------------|
| **Feedforward NN** | 21, 28, 49, 80 | Prediction, estimation | Fast inference, deterministic |
| **LSTM/RNN** | 27, 45, 57 | Time-series, sequences | Temporal dependencies |
| **CNN** | 57 | Image processing | Ice detection, visual inspection |
| **GNN** | 53 | Graph structures | Mesh-based SHM |
| **Ensemble** | 45, 70 | High reliability | Multiple models voting |
| **Physics-Informed NN** | 27, 28, 70 | Physical constraints | Embeds domain knowledge |
| **Reinforcement Learning** | 80 | Optimization | Energy management |
| **Surrogate Models** | 27 | CFD replacement | Fast approximation |

### Model Complexity Levels

| Level | Parameters | Inference Time | Subsystems | Use Cases |
|-------|-----------|----------------|------------|-----------|
| **Light** | <1M | <1ms | 21, 31, 49 | Simple predictions |
| **Medium** | 1M-10M | 1-10ms | 28, 42, 45, 80 | Standard tasks |
| **Heavy** | 10M-100M | 10-100ms | 27, 53, 57, 70 | Complex modeling |
| **Ultra** | >100M | >100ms | None (ground only) | Training, validation |

## Deployment Context Taxonomy

### Runtime Environment

| Context | Subsystems | Platform | Constraints |
|---------|-----------|----------|-------------|
| **Real-Time Critical** | 27, 57 | IMA P1 | <10ms latency, deterministic |
| **Real-Time Standard** | 21, 28, 70, 80 | IMA P2-P3 | <100ms latency |
| **Near Real-Time** | 31, 42, 45, 53 | IMA P4+ | <1s latency acceptable |
| **Ground Only** | 01, 02 (training) | Data center | No latency constraint |
| **Hybrid** | All | Aircraft + Ground | In-flight inference + ground training |

### Compute Allocation

Based on 95-20-42 (IMA Integration):

```
IMA Partition Allocation:
├── P1 (30% CPU, 256MB): 95-20-27 (Flight Controls)
├── P2 (15% CPU, 128MB): 95-20-28 (Fuel)
├── P3 (10% CPU, 64MB):  95-20-21 (ECS)
├── P4 (20% CPU, 128MB): 95-20-45 (Maintenance)
├── P5 (10% CPU, 128MB): 95-20-70 (Propulsion)
├── P6 (5% CPU, 64MB):   95-20-57 (Wings)
├── P7 (5% CPU, 64MB):   95-20-80 (Energy)
└── P8-P10 (5%): Shared for 31, 42, 49, 53
```

## Data Source Taxonomy

### Input Data Categories

| Category | Subsystems | Data Types | Sources |
|----------|-----------|-----------|---------|
| **Flight State** | 27, 57, 70 | Position, velocity, attitude | Air data, IMU |
| **System Sensors** | 21, 28, 42, 49, 80 | Temperature, pressure, voltage | System sensors |
| **Structural** | 53, 57 | Strain, acceleration, acoustics | SHM sensors |
| **Visual** | 57 | Images, video | Cameras |
| **Historical** | 31, 45 | Time-series, events | FDR, logs |
| **Computed** | All | Derived parameters | Other subsystems |

### Output Data Categories

| Category | Subsystems | Output Types | Consumers |
|----------|-----------|--------------|-----------|
| **Control Commands** | 27, 28, 70, 80 | Actuator setpoints | ATA XX systems |
| **Predictions** | 21, 45, 49, 80 | Future states | Operators, CAOS |
| **Classifications** | 31, 57 | Event labels | Maintenance, safety |
| **Estimations** | 28, 53, 80 | State estimates | Control systems |
| **Alerts** | All | Warnings, advisories | Flight crew, maintenance |

## Lifecycle State Taxonomy

### Maturity Levels

| Level | Description | Criteria | Subsystems at Level |
|-------|-------------|----------|---------------------|
| **TRL 3** | Concept validated | Proof of concept | None (all beyond this) |
| **TRL 6** | Prototype demonstrated | Lab validation | 49 (APU) |
| **TRL 7** | Operational prototype | Ground test complete | 21, 31, 42, 45, 53, 80 |
| **TRL 8** | Flight qualified | Flight test complete | 28, 70 |
| **TRL 9** | Flight proven | In-service operation | 27, 57 (target for cert) |

### Certification Status

| Status | Subsystems | Next Milestone | Timeline |
|--------|-----------|----------------|----------|
| **Conceptual** | 49 | Lab testing | 2026 Q1 |
| **Development** | 21, 31, 42, 45, 53, 80 | Ground validation | 2026 Q2-Q3 |
| **Validation** | 28, 70 | Flight test | 2026 Q4 |
| **Certification** | 27, 57 | Type certificate | 2027-2028 |
| **Operational** | 01, 02 | EIS | 2029 |

## Integration Pattern Taxonomy

### Interface Types

| Pattern | Subsystems | Description | Protocol |
|---------|-----------|-------------|----------|
| **Sensor Fusion** | 27, 53, 57 | Multiple sensors → single estimate | Custom |
| **Control Loop** | 21, 27, 28, 70, 80 | Sense → Predict → Actuate | ARINC 429 |
| **Event Detection** | 31, 45, 57 | Stream → Classify → Alert | AFDX |
| **Batch Processing** | 45, 53 | Accumulate → Analyze → Report | REST |
| **Pub/Sub** | All | Asynchronous messaging | MQTT/AFDX |

## Naming Convention Taxonomy

### Document Naming

```
95-20-SS-XXX_Description.md

SS  = Subsystem code (01-80)
XXX = Document sequence (001-999)
      001-099: Overview/architecture
      100-199: Component details
      200-299: Integration
      300-999: Specialized topics
```

### Asset Naming

```
95-20-SS-A-XXX_Description.ext

A   = Asset indicator
XXX = Asset sequence
      001-099: Diagrams (drawio, svg)
      100-199: Data files (json, csv, xml)
      200-299: Model cards (yaml)
      300-399: Smart contracts (sol)
      400-999: Other artifacts
```

## Metadata Tags

### Standard Tags for Discovery

Each subsystem SHALL include these metadata tags in its README.md:

```yaml
metadata:
  subsystem_id: "95-20-XX"
  name: "NN_Subsystem_Name"
  domain: [Infrastructure|Environment|Flight|FuelPropulsion|Data|Avionics|Maintenance|Auxiliary|Structures|Energy]
  parent_ata: "ATA XX"
  criticality: [DAL-A|DAL-B|DAL-C|DAL-D]
  architecture: [FeedForward|LSTM|CNN|GNN|Ensemble|PINN|RL|Surrogate]
  complexity: [Light|Medium|Heavy|Ultra]
  deployment: [RealTimeCritical|RealTimeStandard|NearRealTime|GroundOnly|Hybrid]
  maturity: [TRL3|TRL6|TRL7|TRL8|TRL9]
  certification: [Conceptual|Development|Validation|Certification|Operational]
  dependencies: ["95-20-01", "95-20-02", ...]
  interfaces: ["ATA XX", ...]
```

### Example: 95-20-27 Metadata

```yaml
metadata:
  subsystem_id: "95-20-27"
  name: "NN_Flight_Controls"
  domain: "Flight"
  parent_ata: "ATA 27"
  criticality: "DAL-A"
  architecture: ["PINN", "Surrogate"]
  complexity: "Heavy"
  deployment: "RealTimeCritical"
  maturity: "TRL9"
  certification: "Certification"
  dependencies: ["95-20-01", "95-20-02", "95-20-42", "95-20-53", "95-20-57", "95-20-70"]
  interfaces: ["ATA 27-10", "ATA 27-30", "ATA 27-40"]
```

## Query & Discovery

### CAOS/MCP Query Examples

Using the taxonomy for programmatic discovery:

```json
{
  "query": "Find all DAL-A subsystems with real-time critical deployment",
  "result": ["95-20-01", "95-20-27", "95-20-57", "95-20-70"]
}
```

```json
{
  "query": "Find subsystems serving ATA 42",
  "result": ["95-20-42"]
}
```

```json
{
  "query": "Find subsystems using LSTM architecture",
  "result": ["95-20-27", "95-20-45", "95-20-57"]
}
```

## Taxonomy Extensions

### Future Classifications

Planned taxonomy dimensions:

1. **AI Safety Level** (per EASA MOC SC-AI)
   - Level 1: Assistive
   - Level 2: Human-AI collaborative
   - Level 3: Human-supervised autonomy
   - Level 4: Autonomous

2. **Explainability Level**
   - Glass box (fully explainable)
   - Gray box (partially explainable)
   - Black box (limited explainability)

3. **Data Sharing Level** (for fleet learning)
   - Private (aircraft-specific)
   - Fleet (shared across operator)
   - Public (anonymized research)

## References

- [95-20-00-001_Subsystems_Overview.md](../95-20-00-001_Subsystems_Overview.md) — Architecture
- [95-20-00-002_Subsystems_Integration_Map.md](../95-20-00-002_Subsystems_Integration_Map.md) — Integration
- [95-20-00-006_Subsystem_Registry.json](./95-20-00-006_Subsystem_Registry.json) — Registry implementation
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials) — Software DAL
- [DO-333](https://www.rtca.org/content/standards-guidance-materials) — Model-based development
- [EASA MOC SC-AI](https://www.easa.europa.eu/document-library/general-publications/means-compliance-special-condition-sc-ai) — AI certification
- [ISO/IEC 5338:2023](https://www.iso.org/standard/81118.html) — AI system lifecycle

## Document Control

- **Author**: AMPEL360 NN Architecture Team
- **Reviewer**: Chief Systems Architect
- **Approver**: Technical Director
- **Change Log**:
  - 2025-11-17: v1.0 — Initial taxonomy framework

---

**Classification**: Technical Reference  
**Distribution**: Internal + Standards Bodies

# 95-00-13-00-003: Subsystems Taxonomy

## Document Information
- **Document ID**: 95-00-13-00-003
- **Title**: Subsystems Taxonomy
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Purpose

This document defines the hierarchical taxonomy for classifying and organizing subsystems within the AMPEL360 BWB H₂ Hy-E aircraft system.

## Taxonomy Structure

### Level 1: Domain Categories

#### 1. Functional Subsystems
Subsystems organized by primary mission functions and operational capabilities.

**Categories**:
- Flight Control
- Navigation
- Communication
- Mission Management
- Crew Interface

#### 2. Hardware Components
Physical subsystems organized by technology and form factor.

**Categories**:
- Compute Platforms
- Sensors & Actuators
- Power Systems
- Thermal Management
- Networking Hardware

#### 3. Software Components
Software subsystems organized by architectural layer and purpose.

**Categories**:
- Operating Systems
- Middleware
- Applications
- Services
- Libraries

#### 4. Data Subsystems
Data management subsystems organized by storage type and purpose.

**Categories**:
- Databases
- Data Lakes
- Feature Stores
- Caches
- Log Systems

#### 5. Model Components
AI/ML subsystems organized by model architecture and function.

**Categories**:
- Neural Networks
- Ensemble Models
- Feature Extractors
- Inference Engines
- Training Pipelines

#### 6. Safety & Monitoring
Safety-critical subsystems for monitoring and fault management.

**Categories**:
- Runtime Monitors
- Safety Guards
- Fallback Systems
- Health Management
- Diagnostics

#### 7. Integration & Testing
Subsystems supporting integration, testing, and validation.

**Categories**:
- Integration Kits
- Test Harnesses
- Simulators
- HIL/SIL Rigs
- Emulators

#### 8. Lifecycle & Support
Subsystems for lifecycle management and field support.

**Categories**:
- Configuration Management
- Field Replaceable Units
- Diagnostic Tools
- Update Mechanisms
- Documentation Systems

### Level 2: Functional Classification

#### By Operational Mode
- **Ground**: Pre-flight, post-flight, maintenance
- **Taxi**: Surface operations
- **Takeoff**: Departure phase
- **Climb**: Ascent to cruise
- **Cruise**: Normal flight
- **Descent**: Approach preparation
- **Approach**: Landing preparation
- **Landing**: Touchdown and rollout
- **Emergency**: Abnormal operations

#### By Criticality
- **Critical (DAL-A)**: Loss causes catastrophic failure
- **Essential (DAL-B)**: Loss causes hazardous failure
- **Important (DAL-C)**: Loss causes major failure
- **Standard (DAL-D)**: Loss causes minor failure
- **Optional (DAL-E)**: Loss has no safety effect

#### By Lifecycle Phase
- **Development**: Engineering and prototyping
- **Production**: Manufacturing support
- **Operational**: In-service systems
- **Maintenance**: Support and repair
- **Decommissioning**: End-of-life

### Level 3: Technology Classification

#### Hardware Technology
- **Analog**: Continuous signal processing
- **Digital**: Discrete signal processing
- **Hybrid**: Mixed analog/digital
- **Mechanical**: Physical actuators
- **Electromechanical**: Electric actuators
- **Optical**: Fiber optic systems
- **Wireless**: Radio frequency systems

#### Software Architecture
- **Monolithic**: Single integrated application
- **Modular**: Componentized architecture
- **Microservices**: Distributed services
- **Event-Driven**: Message-based
- **Real-Time**: Time-critical systems
- **Batch**: Offline processing

#### Data Architecture
- **Relational**: SQL databases
- **NoSQL**: Document, key-value, graph
- **Time-Series**: Temporal data
- **Streaming**: Real-time data flows
- **File-Based**: Traditional file systems

#### Model Architecture
- **Feedforward**: Standard neural networks
- **Recurrent**: Temporal processing
- **Convolutional**: Spatial processing
- **Transformer**: Attention-based
- **Ensemble**: Multiple models
- **Hybrid**: Mixed architectures

### Level 4: ATA Chapter Mapping

Each subsystem shall be mapped to applicable ATA chapters:

| ATA Chapter | Title | Applicable Subsystems |
|-------------|-------|----------------------|
| ATA 02 | Weight and Balance | Configuration management, sensors |
| ATA 21 | Air Conditioning | Environmental control hardware |
| ATA 22 | Auto Flight | Flight control software, autopilot |
| ATA 23 | Communications | Communication hardware/software |
| ATA 24 | Electrical Power | Power management systems |
| ATA 27 | Flight Controls | Control surfaces, actuators |
| ATA 28 | Fuel | H₂ fuel cell management |
| ATA 31 | Indicating/Recording | Displays, data recording |
| ATA 34 | Navigation | Navigation sensors and software |
| ATA 42 | Integrated Modular Avionics | Core computing platforms |
| ATA 45 | Central Maintenance System | Diagnostic subsystems |
| ATA 95 | Digital Product Passport | AI/ML, traceability systems |

### Level 5: Interface Classification

#### Physical Interfaces
- **Power**: Voltage, current, protection
- **Data**: Serial, parallel, network
- **Analog**: Sensor inputs/outputs
- **Mechanical**: Mounting, cooling
- **Optical**: Fiber connections

#### Logical Interfaces
- **API**: Application programming interfaces
- **Protocol**: Communication protocols
- **Message**: Asynchronous messaging
- **Event**: Event notification
- **Stream**: Data streaming

#### Integration Interfaces
- **Standard**: Industry standards
- **Custom**: Project-specific
- **Proprietary**: Vendor-specific
- **Open**: Open-source protocols

## Taxonomy Application Rules

### Rule T1: Single Primary Classification
Each subsystem shall have one primary classification in Level 1-2.

### Rule T2: Multiple Secondary Classifications
Subsystems may have multiple classifications in Level 3-5.

### Rule T3: Explicit Mapping
All classifications shall be explicitly documented in subsystem catalogs.

### Rule T4: Consistent Terminology
Standard terms from this taxonomy shall be used in all documentation.

### Rule T5: Extensibility
New categories may be added following change management process.

## Cross-Reference Matrix

### Subsystem to ATA Mapping
See: 95-00-13-02-005_HW_Components_to_ATA_Systems_Map.md

### Subsystem to Requirements Mapping
See: 95-00-13-14-002_Subsystems_to_RQ_Map.md

### Subsystem to V&V Mapping
See: 95-00-13-14-003_Subsystems_to_VV_Cases_Map.md

## Taxonomy Maintenance

### Update Frequency
- Review annually
- Update with major architecture changes
- Revise for new technology categories

### Change Process
1. Proposal submitted to Architecture Board
2. Impact analysis conducted
3. Documentation updated
4. Stakeholders notified
5. Training provided (if needed)

### Version Control
- Taxonomy version tracked separately
- Changes logged in revision history
- Backward compatibility maintained

## Related Documents

- 95-00-13-00-001: Subsystems Components Strategy
- 95-00-13-00-002: Decomposition Principles and Rules
- 95-00-13-00-004: Components Taxonomy
- 95-00-13-00-005: Subsys_Comp_Traceability_Matrix.csv
- 95-00-13-00-006: Subsys_Registry.json

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |

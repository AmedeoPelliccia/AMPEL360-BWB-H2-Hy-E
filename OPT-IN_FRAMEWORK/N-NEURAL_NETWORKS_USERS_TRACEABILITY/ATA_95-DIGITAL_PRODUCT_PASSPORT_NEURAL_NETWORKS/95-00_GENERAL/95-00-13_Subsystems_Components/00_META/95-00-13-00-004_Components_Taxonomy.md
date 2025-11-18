# [95-00-13-00-004](95-00-13-00-004.md): Components Taxonomy

## Document Information
- **Document ID**: [95-00-13-00-004](95-00-13-00-004.md)
- **Title**: Components Taxonomy
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Purpose

This document defines the detailed taxonomy for classifying individual components within subsystems of the AMPEL360 BWB H₂ Hy-E aircraft.

## Component Classification Framework

### 1. Hardware Components

#### 1.1 Compute Components
- **Processors**: CPUs, GPUs, TPUs, FPGAs
- **Memory**: RAM, ROM, Flash, NVRAM
- **Storage**: SSD, HDD, SD cards
- **Accelerators**: AI accelerators, DSPs
- **Boards**: Single-board computers, cards

#### 1.2 Sensor Components
- **Inertial**: Accelerometers, gyroscopes, IMUs
- **Positioning**: GNSS, INS, DME
- **Environmental**: Temperature, pressure, humidity
- **Optical**: Cameras, LiDAR, infrared
- **Acoustic**: Microphones, ultrasonic
- **Proximity**: Radar, ultrasonic distance

#### 1.3 Actuator Components
- **Electric Motors**: Servo, stepper, brushless
- **Hydraulic**: Pumps, valves, cylinders
- **Pneumatic**: Compressors, valves
- **Piezoelectric**: High-precision actuators
- **Linear**: Ball screws, lead screws
- **Rotary**: Geared motors, direct drive

#### 1.4 Power Components
- **Distribution**: Buses, switches, contactors
- **Conversion**: AC/DC, DC/DC converters
- **Protection**: Fuses, breakers, surge protection
- **Storage**: Batteries, supercapacitors
- **Generation**: Fuel cells, generators
- **Management**: Battery management systems

#### 1.5 Communication Components
- **Wired**: Ethernet, CAN, [ARINC 429](https://www.aviation-ia.com/cf/aeec.html)
- **Wireless**: WiFi, Bluetooth, cellular
- **Optical**: Fiber transceivers
- **Radio**: VHF, UHF, satcom
- **Antennas**: Various frequency bands

#### 1.6 Interface Components
- **Displays**: LCD, OLED, HUD
- **Input Devices**: Keyboards, touchscreens, controls
- **Indicators**: LEDs, gauges, annunciators
- **Connectors**: Electrical, optical, mechanical
- **Adapters**: Protocol converters, level shifters

### 2. Software Components

#### 2.1 Operating Systems
- **RTOS**: Real-time operating systems
- **Linux**: Standard and embedded variants
- **Hypervisors**: Virtualization platforms
- **Bare-Metal**: Direct hardware control

#### 2.2 Middleware
- **Communication**: Message brokers, RPC frameworks
- **Database**: ORMs, connection pools
- **Security**: Authentication, encryption
- **Logging**: Log aggregation, forwarding
- **Monitoring**: Metrics, tracing

#### 2.3 Application Components
- **Services**: Microservices, daemons
- **Applications**: User-facing programs
- **Scripts**: Automation scripts
- **Plugins**: Extensible modules
- **Agents**: Background processes

#### 2.4 Library Components
- **Utilities**: Helper functions, tools
- **Mathematical**: Linear algebra, statistics
- **Signal Processing**: FFT, filtering
- **AI/ML**: ML frameworks, inference engines
- **Graphics**: Rendering, visualization
- **Network**: Protocol implementations

#### 2.5 Data Processing
- **ETL**: Extract, transform, load pipelines
- **Stream Processing**: Real-time data processing
- **Batch Processing**: Offline analysis
- **Data Validation**: Schema validation, checks
- **Data Transformation**: Format conversion

### 3. Data Components

#### 3.1 Storage Components
- **Databases**: SQL, NoSQL variants
- **File Systems**: Local, distributed
- **Object Stores**: S3-compatible stores
- **Block Storage**: Raw block devices
- **Cache Systems**: In-memory caches

#### 3.2 Data Pipeline Components
- **Ingestion**: Data collectors, receivers
- **Processing**: Transformation, enrichment
- **Routing**: Data routing, filtering
- **Output**: Sinks, exporters

#### 3.3 Feature Components
- **Feature Stores**: Feature repositories
- **Feature Engineering**: Transformations
- **Feature Serving**: Real-time serving
- **Feature Monitoring**: Drift detection

#### 3.4 Metadata Components
- **Catalogs**: Data catalogs, registries
- **Schemas**: Schema definitions, validation
- **Lineage**: Data lineage tracking
- **Governance**: Data policies, rules

### 4. Model Components

#### 4.1 Model Architecture Components
- **Layers**: Neural network layers
- **Blocks**: Reusable building blocks
- **Heads**: Task-specific outputs
- **Backbones**: Feature extractors
- **Embeddings**: Vector representations

#### 4.2 Training Components
- **Optimizers**: Gradient descent variants
- **Loss Functions**: Training objectives
- **Metrics**: Performance measures
- **Callbacks**: Training hooks
- **Schedulers**: Learning rate scheduling

#### 4.3 Inference Components
- **Model Servers**: Serving infrastructure
- **Preprocessing**: Input preparation
- **Postprocessing**: Output formatting
- **Batching**: Request batching
- **Caching**: Result caching

#### 4.4 Model Management
- **Registry**: Model version registry
- **Metadata**: Model documentation
- **Lineage**: Training lineage
- **Monitoring**: Performance monitoring

### 5. Safety Components

#### 5.1 Monitor Components
- **Runtime Monitors**: Execution monitoring
- **Watchdogs**: Timeout detection
- **Boundary Checkers**: Value validation
- **Anomaly Detectors**: Outlier detection
- **Health Checks**: System health monitoring

#### 5.2 Guard Components
- **Input Guards**: Input validation
- **Output Guards**: Output validation
- **State Guards**: State consistency
- **Resource Guards**: Resource limits
- **Access Guards**: Permission checks

#### 5.3 Fallback Components
- **Backup Systems**: Redundant systems
- **Degraded Modes**: Reduced functionality
- **Safe States**: Fail-safe configurations
- **Recovery Procedures**: Automatic recovery
- **Manual Overrides**: Human intervention

### 6. Integration Components

#### 6.1 Adapter Components
- **Protocol Adapters**: Protocol translation
- **Data Adapters**: Format conversion
- **Interface Adapters**: API adaptation
- **Legacy Adapters**: Legacy system integration

#### 6.2 Test Components
- **Test Harnesses**: Test frameworks
- **Mocks**: Simulated components
- **Stubs**: Placeholder implementations
- **Drivers**: Test drivers
- **Fixtures**: Test data, setup

#### 6.3 Bridge Components
- **System Bridges**: System interconnects
- **Domain Bridges**: Domain translation
- **Version Bridges**: Version compatibility
- **Format Bridges**: Data format conversion

## Component Attributes

### Required Attributes
- **ID**: Unique identifier
- **Name**: Descriptive name
- **Type**: Component type from taxonomy
- **Version**: Component version
- **Owner**: Responsible party
- **Status**: Lifecycle status

### Optional Attributes
- **Description**: Detailed description
- **Dependencies**: Other components required
- **Interfaces**: Exposed interfaces
- **Configuration**: Configuration parameters
- **Certification**: Certification level (DAL)
- **FRU**: Field replaceable unit flag
- **COTS**: Commercial off-the-shelf flag

## Component Lifecycle States

1. **Concept**: Initial design phase
2. **Development**: Under active development
3. **Testing**: In test/validation
4. **Qualified**: Passed qualification
5. **Production**: In production use
6. **Maintenance**: In-service support
7. **Deprecated**: Being phased out
8. **Obsolete**: No longer supported
9. **Archived**: Historical record only

## Component Relationships

### Dependency Types
- **Required**: Must be present
- **Optional**: Enhances functionality
- **Recommended**: Best practice
- **Conflicts**: Cannot coexist
- **Supersedes**: Replaces older component

### Interface Types
- **Provides**: Services offered
- **Requires**: Services needed
- **Publishes**: Events published
- **Subscribes**: Events consumed
- **Extends**: Extension points

## Component Documentation Requirements

### Minimum Documentation
1. Component specification
2. Interface definition
3. Configuration guide
4. Test procedures
5. Certification evidence (if applicable)

### Recommended Documentation
1. Design rationale
2. Usage examples
3. Performance characteristics
4. Known limitations
5. Troubleshooting guide

## Component Naming Conventions

### Format
`<Type>_<Function>_<Variant>_<Version>`

### Examples
- `CPU_FlightControl_Primary_v2.1`
- `SW_NavService_Standard_v1.5.3`
- `DB_FlightData_Timeseries_v3.0`
- `NN_ObjectDetection_YOLO_v4.2`

## Component Registry

### Registry Structure
See: [95-00-13-00-006_Subsys_Registry](95-00-13-00-006_Subsys_Registry.md).json

### Registry Fields
- Component ID
- Type classification
- Version information
- Dependencies
- Interface contracts
- Certification status
- Lifecycle state

## Cross-References

### To Requirements
See: [95-00-13-14-002_Subsystems_to_RQ_Map](../14_SUBSYSTEMS_REQUIREMENTS_VV_MAP/95-00-13-14-002_Subsystems_to_RQ_Map.md).md

### To Verification
See: [95-00-13-14-003_Subsystems_to_VV_Cases_Map](../14_SUBSYSTEMS_REQUIREMENTS_VV_MAP/95-00-13-14-003_Subsystems_to_VV_Cases_Map.md).md

### To Certification
See: [95-00-13-14-004_Subsystems_to_Cert_Evidence_Map](../14_SUBSYSTEMS_REQUIREMENTS_VV_MAP/95-00-13-14-004_Subsystems_to_Cert_Evidence_Map.md).md

## Maintenance and Updates

### Review Schedule
- Quarterly review of component registry
- Annual taxonomy update
- On-demand for new technologies

### Change Process
1. Proposal submission
2. Technical review
3. Impact assessment
4. Documentation update
5. Registry update
6. Stakeholder notification

## Related Documents

- [95-00-13-00-003](95-00-13-00-003.md): Subsystems Taxonomy
- [95-00-13-00-005](95-00-13-00-005.md): Subsys_Comp_Traceability_Matrix.csv
- [95-00-13-00-006](95-00-13-00-006.md): Subsys_Registry.json
- Component-specific catalogs in each subsystem folder

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |

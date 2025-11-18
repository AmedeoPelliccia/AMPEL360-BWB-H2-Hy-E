# 95-10-00-01-002 Operational Scope and Actors

## Document Information

- **Document ID**: 95-10-00-01-002
- **Title**: Operational Scope and Actors
- **Version**: 1.0
- **Date**: 2025-11-17
- **Status**: Active
- **Category**: Operations
- **ATA Chapter**: 95 - Digital Product Passport and Neural Networks

## Purpose

This document defines the operational scope of Neural Network systems and the Digital Product Passport within aircraft operations, and identifies all actors involved in operational activities.

## Operational Scope

### In-Scope Activities

The 95-10 Operations domain covers:

#### 1. Flight Operations
- Pre-flight NN system checks and briefings
- In-flight NN system monitoring and override
- NN-assisted flight envelope management
- Operational decision support
- Post-flight data capture and event recording

#### 2. Maintenance Operations
- Predictive maintenance alerts and scheduling
- Component health monitoring via NN systems
- DPP-based maintenance history access
- Maintenance task execution and validation
- Maintenance data feedback to DPP

#### 3. Ground Operations
- Turnaround procedure execution with NN support
- Ground safety monitoring with NN advisories
- GSE (Ground Support Equipment) integration
- Ramp operations and aircraft handling
- Operational data capture during ground ops

#### 4. Data Operations
- Data pipeline management (flight-to-ground)
- Real-time and batch data processing
- Data quality monitoring and validation
- Operational data retention and archiving
- Data governance and compliance

#### 5. AI/MLOps Operations
- NN model deployment to operational aircraft
- Runtime configuration and parameter tuning
- Model performance monitoring in service
- Operational approval workflows for model updates
- Rollback procedures for model issues

### Out-of-Scope Activities

The following are NOT covered by 95-10 Operations:

- **Model Development**: Covered by 95-00-06 Engineering
- **Model Training**: Covered by 95-00-08 Prototyping
- **Requirements Definition**: Covered by 95-00-03 Requirements
- **Certification Activities**: Covered by 95-00-10 Certification
- **Research Activities**: Covered by dedicated R&D chapters

## Operational Actors

### Primary Actors

#### 1. Flight Crew

**Roles**:
- Pilot in Command (PIC)
- First Officer (FO)
- Relief Pilots (for extended operations)

**Responsibilities**:
- Monitor NN system status and recommendations
- Execute NN-assisted procedures per FCOM/FCTM
- Override NN systems when necessary (per ODD boundaries)
- Document NN system behavior and anomalies
- Update DPP with operational events

**Interfaces**:
- Flight deck displays (EICAS, MFD, ND)
- DPP operational view (read/annotate)
- OM-A/OM-B procedures
- QRH (Quick Reference Handbook)

#### 2. Maintenance Personnel

**Roles**:
- Licensed Aircraft Maintenance Engineers (LAME)
- Line Maintenance Technicians
- Base Maintenance Technicians
- Avionics Specialists

**Responsibilities**:
- Execute predictive maintenance tasks
- Validate NN system health predictions
- Access component history via DPP
- Perform NN system diagnostics
- Update DPP with maintenance actions

**Interfaces**:
- DPP maintenance view (read/write)
- ATA 45 Onboard Maintenance Systems
- Maintenance manuals and task cards
- Predictive maintenance dashboards

#### 3. Ground Operations Staff

**Roles**:
- Ramp Agents
- Turnaround Coordinators
- Fueling Technicians (H₂ specialists)
- GSE Operators

**Responsibilities**:
- Execute turnaround procedures with NN support
- Monitor ground safety with NN advisories
- Operate GSE integrated with aircraft systems
- Capture operational data during ground ops
- Report ground-side events to DPP

**Interfaces**:
- Ground operations tablets/displays
- DPP ground view (limited read/annotate)
- GSE control interfaces
- Airport operations systems

#### 4. Operations Control Center (OCC)

**Roles**:
- Flight Dispatchers
- Operations Controllers
- Fuel Planning Specialists
- Technical Operations Support

**Responsibilities**:
- Monitor fleet-wide NN system performance
- Coordinate operational changes with aircraft
- Approve/deny operational configuration changes
- Manage operational data flows
- Coordinate with maintenance control

**Interfaces**:
- Fleet operations dashboards
- DPP fleet view (read-only, aggregated)
- Airline operations systems (e.g., Sabre, Amadeus)
- Weather and route planning systems

#### 5. Data Operations Team

**Roles**:
- Data Engineers
- Data Quality Analysts
- Data Governance Officers
- Operations Data Scientists

**Responsibilities**:
- Maintain data pipelines (aircraft-to-ground)
- Monitor data quality and completeness
- Enforce data retention policies
- Support operational analytics
- Manage DPP data infrastructure

**Interfaces**:
- Data operations platforms
- DPP data layer (backend access)
- Cloud data storage (AWS/Azure/GCP)
- Data quality monitoring tools

#### 6. AI/MLOps Team

**Roles**:
- ML Engineers
- MLOps Specialists
- AI Safety Officers
- Model Deployment Managers

**Responsibilities**:
- Deploy NN models to operational fleet
- Monitor runtime model performance
- Configure operational parameters
- Coordinate model updates with stakeholders
- Manage model rollback if needed

**Interfaces**:
- MLOps platforms (e.g., MLflow, Kubeflow)
- DPP model registry
- CI/CD pipelines for model deployment
- Model monitoring dashboards

### Secondary Actors

#### 7. Training Department

**Responsibilities**:
- Develop NN system training programs
- Conduct simulator sessions with NN models
- Assess crew competence on NN operations
- Maintain training records in DPP

#### 8. Safety Department

**Responsibilities**:
- Define safety boundaries for NN operations
- Monitor operational safety metrics
- Investigate NN-related incidents/events
- Update safety assessments based on operational data

#### 9. Regulatory Affairs

**Responsibilities**:
- Ensure regulatory compliance in operations
- Interface with EASA, FAA, and other authorities
- Manage operational approvals and authorizations
- Maintain regulatory documentation

#### 10. Quality Assurance

**Responsibilities**:
- Audit operational procedures
- Verify compliance with standards
- Review operational data quality
- Support continuous improvement initiatives

### External Actors

#### 11. Airline Operators

**Roles**:
- Airline Operations Management
- Airline Maintenance Management
- Airline Training Departments

**Responsibilities**:
- Define operator-specific operational profiles
- Customize procedures per airline needs
- Manage airline-specific data and configurations
- Interface with AMPEL360 support

#### 12. Airport Authorities

**Responsibilities**:
- Provide ground infrastructure
- Coordinate aircraft movements
- Support H₂ refueling operations
- Integrate with airport systems

#### 13. Regulatory Authorities

**Roles**:
- EASA (European Union Aviation Safety Agency)
- FAA (Federal Aviation Administration)
- National aviation authorities

**Responsibilities**:
- Approve operational procedures
- Conduct operational audits/inspections
- Issue operational authorizations
- Review operational safety data

## Actor Interaction Matrix

| Actor                 | Flight Ops | Maint Ops | Ground Ops | Data Ops | AI/MLOps | DPP Access |
|-----------------------|------------|-----------|------------|----------|----------|------------|
| Flight Crew           | Primary    | Read      | Coordinate | Capture  | Monitor  | Read/Write |
| Maintenance Personnel | Coordinate | Primary   | Coordinate | Capture  | Validate | Read/Write |
| Ground Operations     | Coordinate | Report    | Primary    | Capture  | Monitor  | Read/Write |
| OCC                   | Monitor    | Coordinate| Monitor    | Analyze  | Approve  | Read       |
| Data Ops Team         | Support    | Support   | Support    | Primary  | Support  | Backend    |
| AI/MLOps Team         | Monitor    | Validate  | Monitor    | Analyze  | Primary  | Backend    |
| Training Department   | Develop    | Develop   | Develop    | Review   | Review   | Read       |
| Safety Department     | Oversee    | Oversee   | Oversee    | Audit    | Oversee  | Read       |

**Legend**:
- **Primary**: Main responsibility
- **Coordinate**: Active coordination required
- **Monitor**: Monitoring and oversight
- **Support**: Support role
- **Read/Write**: DPP access permissions
- **Backend**: Backend system access

## Operational Boundaries

### Geographical Scope
- Operations within approved Operational Design Domain (ODD)
- International operations per ICAO standards
- Regional variations per local authority requirements

### Temporal Scope
- 24/7/365 operational support
- Real-time and near-real-time operations
- Batch processing during maintenance windows

### Functional Scope
- NN systems operating within certified envelopes
- DPP accessible per role-based access control
- Data operations compliant with GDPR and data sovereignty

## References

- ATA 02: Operations Information
- FCOM (Flight Crew Operations Manual)
- FCTM (Flight Crew Training Manual)
- OM-A/OM-B (Operations Manual)
- ATA 45: Onboard Maintenance Systems
- 95-10-00-01-001: Operations Overview
- 95-10-00-01-005: Operational Roles Registry

## Version History

| Version | Date       | Author              | Changes                |
|---------|------------|---------------------|------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Ops Team   | Initial release        |

---

**Classification**: Internal Use  
**Owner**: AMPEL360 Operations Working Group  
**Next Review**: 2026-02-17

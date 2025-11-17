# Functional Subsystems Catalog Template

## Subsystem Identification
- **Subsystem ID**: [FS-XXX]
- **Subsystem Name**: [Name]
- **Version**: [X.Y.Z]
- **Owner**: [Team/Person]
- **Status**: [Concept|Development|Testing|Qualified|Production|Deprecated]

## Primary Function
[One sentence description of the primary mission capability]

## Scope and Boundaries
### Included Functions
- [Function 1]
- [Function 2]
- [Function 3]

### Excluded Functions
- [What this subsystem does NOT do]

## Operational Modes
| Mode | Status | Key Functions | Notes |
|------|--------|---------------|-------|
| Ground | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Taxi | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Takeoff | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Climb | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Cruise | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Descent | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Approach | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Landing | [Active/Standby/Inactive] | [Functions active in this mode] | |
| Emergency | [Active/Standby/Inactive] | [Functions active in this mode] | |

## Interfaces

### Input Interfaces
| Interface ID | Source Subsystem | Data Type | Rate (Hz) | Criticality |
|--------------|------------------|-----------|-----------|-------------|
| [IF-XXX-IN-001] | [Source] | [Type] | [Rate] | [DAL-X] |

### Output Interfaces
| Interface ID | Destination Subsystem | Data Type | Rate (Hz) | Criticality |
|--------------|----------------------|-----------|-----------|-------------|
| [IF-XXX-OUT-001] | [Destination] | [Type] | [Rate] | [DAL-X] |

### Control Interfaces
| Interface ID | Type | Direction | Purpose |
|--------------|------|-----------|---------|
| [IF-XXX-CTL-001] | [Command/Config] | [In/Out] | [Purpose] |

## Allocated Components

### Hardware Components
- [HW-XXX]: [Component Name] - [Purpose]

### Software Components
- [SW-XXX]: [Component Name] - [Purpose]

### Data Components
- [DS-XXX]: [Component Name] - [Purpose]

### Model Components
- [ML-XXX]: [Component Name] - [Purpose]

## Requirements Traceability
| Requirement ID | Requirement Title | Verification Method |
|----------------|-------------------|---------------------|
| [REQ-XXX-001] | [Title] | [Test/Analysis/Inspection] |

## Performance Characteristics
- **Update Rate**: [X Hz]
- **Latency**: [X ms]
- **Accuracy**: [Specification]
- **Reliability**: [MTBF or failure rate]
- **Availability**: [X.XXXX]

## Safety Characteristics
- **Criticality Level**: [DAL-A through DAL-E]
- **Failure Modes**: [List key failure modes]
- **Mitigation Strategies**: [How failures are handled]
- **Fallback Behavior**: [What happens in degraded mode]

## Degraded Operation Modes
| Degraded Mode | Trigger Condition | Capabilities | Limitations |
|---------------|-------------------|--------------|-------------|
| [Mode Name] | [What causes this mode] | [What still works] | [What doesn't work] |

## Certification Basis
- **Applicable Standards**: [DO-178C, DO-254, etc.]
- **Certification Level**: [DAL-X]
- **Certification Status**: [Not Started|In Progress|Complete]
- **Certification Authority**: [FAA/EASA/etc.]

## Testing Strategy
- **Unit Testing**: [Approach]
- **Integration Testing**: [Approach]
- **System Testing**: [Approach]
- **Certification Testing**: [Approach]

## Configuration Management
- **Configuration Items**: [List CIs]
- **Version Control**: [Repository/Branch]
- **Change Control**: [Process reference]

## Documentation
- **Design Documents**: [List]
- **Interface Specifications**: [List]
- **Test Plans**: [List]
- **User Manuals**: [List]

## Related Subsystems
- [FS-XXX]: [Relationship description]
- [FS-YYY]: [Relationship description]

## Revision History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | [Author] | Initial release |

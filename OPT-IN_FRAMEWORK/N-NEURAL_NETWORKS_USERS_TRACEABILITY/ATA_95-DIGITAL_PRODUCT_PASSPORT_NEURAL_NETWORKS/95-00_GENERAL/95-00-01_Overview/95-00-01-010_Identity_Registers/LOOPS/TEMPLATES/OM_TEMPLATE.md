---
document_id: OM_<bb_id>
title: Operational Mission for <bb_id>
subtitle: Predicted Operational Manifestation
version: 1.0
date: YYYY-MM-DD
status: TEMPLATE
owner: AMPEL360 / ATA 95 Governance
classification: INTERNAL
primary_ata: "<Body_ATA>"
related_ata: ["<Brain_ATA>", "95"]
---

# OM_<bb_id> — Operational Mission

## 1. Purpose

This document defines the **Operational Mission (OM)** for `<bb_id>` — `<Artifact_Name>`.

The OM describes the **predicted operational manifestation** — what the artifact is expected to do in the fleet, based on the design (AM) and validated by design evidence (DV).

**Key concept**: The DPP predicts this OM. OAV will validate whether this OM holds true in the unique operational context.

---

## 2. Artifact Identity

| Field | Value |
|---|---|
| **BB ID** | `<bb_id>` |
| **Artifact Name** | `<Artifact_Name>` |
| **OM Class** | `<om_class>` |
| **Body ATA** | `<Body_ATA>` |
| **Brain ATA** | `<Brain_ATA>` |
| **DPP Reference** | `<dpp_ref>` |

---

## 3. Operational Mission Description

### 3.1 Mission Statement
```
<High-level statement of operational purpose: what the artifact does in service>
Example: "Provide real-time cabin temperature optimization across all flight phases
to maintain passenger comfort within Q80/Q100 targets while minimizing energy consumption."
```

### 3.2 Operational Context
- **Operational Domain**: `<airborne | ground | hybrid>`
- **Mission Phases**: `<list phases: ground, taxi, takeoff, climb, cruise, descent, landing, etc.>`
- **Operational Modes**: `<list modes: normal, degraded, emergency, etc.>`
- **Crew Interaction**: `<describe crew interaction model>`
- **Fleet Type**: `<aircraft types where deployed>`

---

## 4. Operational Functions

### 4.1 Primary Operational Functions
| Function ID | Description | Operational Mode | Performance Target | Priority |
|---|---|---|---|---|
| `<func_id>` | `<description>` | `<mode>` | `<target>` | `<critical/standard/optional>` |

### 4.2 Secondary/Support Functions
| Function ID | Description | Operational Mode | Performance Target | Priority |
|---|---|---|---|---|
| `<func_id>` | `<description>` | `<mode>` | `<target>` | `<standard/optional>` |

---

## 5. Operational Envelope

### 5.1 Environmental Envelope
| Parameter | Minimum | Maximum | Nominal | Units |
|---|---|---|---|---|
| Altitude | `<min>` | `<max>` | `<nominal>` | `<ft/m>` |
| Temperature | `<min>` | `<max>` | `<nominal>` | `<°C>` |
| Pressure | `<min>` | `<max>` | `<nominal>` | `<psi/bar>` |
| Humidity | `<min>` | `<max>` | `<nominal>` | `<%>` |
| Vibration | `<min>` | `<max>` | `<nominal>` | `<g>` |

### 5.2 Operational Load Cases
| Load Case ID | Description | Frequency | Severity | Expected Behavior |
|---|---|---|---|---|
| `<case_id>` | `<description>` | `<frequent/occasional/rare>` | `<low/medium/high>` | `<behavior>` |

---

## 6. Operational Behavior Model

### 6.1 Normal Operations
```
<Describe expected behavior under normal conditions:
- Inputs processed
- Outputs generated
- State transitions
- Performance characteristics>
```

### 6.2 Degraded Operations
```
<Describe expected behavior under degraded conditions:
- Failure modes
- Graceful degradation
- Fallback strategies
- Crew alerts/notifications>
```

### 6.3 Emergency Operations
```
<Describe expected behavior under emergency conditions:
- Emergency responses
- Safety prioritization
- Fail-safe behaviors>
```

---

## 7. Operational Performance Expectations

### 7.1 Performance Targets (Operational Context)
| Performance Parameter | Target | Units | Tolerance | Measurement Method |
|---|---|---|---|---|
| `<param>` | `<target>` | `<units>` | `<tolerance>` | `<method>` |

### 7.2 Availability and Reliability
- **Required Availability**: `<percentage>%`
- **MTBF (Mean Time Between Failures)**: `<value>` `<hours/cycles>`
- **MTTR (Mean Time To Repair)**: `<value>` `<hours>`
- **Dispatch Reliability Target**: `<percentage>%`

---

## 8. Operational Limitations and Constraints

### 8.1 Operational Limitations
```
<Define operational limitations:
- Prohibited uses
- Restricted operational modes
- Environmental limitations
- Configuration dependencies>
```

### 8.2 Crew Procedures and Constraints
```
<Define crew procedures and constraints:
- Normal operating procedures
- Abnormal procedures
- Emergency procedures
- Crew training requirements>
```

---

## 9. Safety-Critical Operational Behaviors (if applicable)

### 9.1 Safety Functions in Operations
| Safety Function ID | Hazard Mitigated | Operational Scenario | Expected Behavior | Evidence |
|---|---|---|---|---|
| `<sf_id>` | `<hazard>` | `<scenario>` | `<behavior>` | `<evidence_ref>` |

### 9.2 Failure Conditions and Responses
| Failure Condition | Classification | Operational Response | Crew Action | Evidence |
|---|---|---|---|---|
| `<failure>` | `<catastrophic/hazardous/major/minor>` | `<response>` | `<action>` | `<evidence_ref>` |

---

## 10. ML/NN Operational Behavior (if applicable)

### 10.1 ML/NN Operational Domain (ODD)
```
<Define the operational domain definition for ML/NN:
- Valid input ranges
- Environmental conditions
- Operational modes where ML/NN is active
- Out-of-distribution detection and handling>
```

### 10.2 ML/NN Performance in Operations
| Metric | Operational Target | Monitoring Method | Alert Threshold |
|---|---|---|---|
| `<metric>` | `<target>` | `<method>` | `<threshold>` |

### 10.3 ML/NN Drift Monitoring
- **Drift Detection Method**: `<method>`
- **Drift Alert Threshold**: `<threshold>`
- **Drift Response**: `<response_procedure>`

---

## 11. Human-Machine Interface (HMI)

### 11.1 Crew Interface
```
<Describe crew interface:
- Control inputs
- Display outputs
- Alerts and warnings
- Mode annunciations>
```

### 11.2 Maintenance Interface
```
<Describe maintenance interface:
- BITE (Built-In Test Equipment)
- Maintenance menus
- Diagnostic data access
- Configuration management>
```

---

## 12. Operational Data Collection

### 12.1 Data Logged to DT
| Data Parameter | Type | Frequency | Storage | Purpose |
|---|---|---|---|---|
| `<param>` | `<sensor/derived/event>` | `<freq>` | `<storage>` | `<purpose>` |

### 12.2 Operational Telemetry
```
<Define operational telemetry requirements:
- Real-time monitoring
- Post-flight analysis
- Trend monitoring
- Anomaly detection>
```

---

## 13. Operational Validation Requirements

### 13.1 OAV Success Criteria
```
<Define criteria for OAV to validate this OM:
- What must be demonstrated operationally
- What measurements must be taken
- What acceptance thresholds must be met>
```

### 13.2 Predicted vs Actual Comparison
| OM Prediction | Validation Method | Acceptance Criteria | OAV Reference |
|---|---|---|---|
| `<prediction>` | `<method>` | `<criteria>` | `<oav_ref>` |

---

## 14. Fleet Operational Context

### 14.1 Fleet Integration
```
<Describe how artifact integrates into fleet operations:
- Installation considerations
- Fleet-wide procedures
- Commonality with other variants
- Fleet configuration management>
```

### 14.2 Operational Variability
```
<Describe expected variability across fleet:
- Aircraft-specific configurations
- Route-specific considerations
- Seasonal/environmental factors
- Operational procedure differences>
```

---

## 15. Operational Change Management

### 15.1 OM Update Policy
```
<Define when and how OM can be updated:
- Triggers for OM update (new operational experience, incident data, etc.)
- Authority required for OM updates
- Impact on DPP and OAV>
```

### 15.2 OM Version History
| Version | Date | Change Description | Authority | DPP Version |
|---|---|---|---|---|
| 1.0 | YYYY-MM-DD | Initial OM definition | `<authority>` | `<dpp_version>` |

---

## 16. Traceability

### 16.1 AM Traceability
- **AM Reference**: `<am_ref>`
- **AM Version**: `<version>`
- **Requirements Traced**: `<requirement_list>`

### 16.2 DPP Traceability
- **DPP Reference**: `<dpp_ref>`
- **DPP Version**: `<version>`
- **Predicted by DPP**: `[YES]`

### 16.3 OAV Traceability
- **OAV Reference**: `<oav_ref>` (to be populated after OAV)
- **OAV Status**: `<status>`
- **Validated in Operations**: `[YES | NO | PENDING]`

---

## 17. Open Items

| Item ID | Description | Impact on OM | Target Date | Owner | Status |
|---|---|---|---|---|---|
| `<item_id>` | `<description>` | `<impact>` | `<target_date>` | `<owner>` | `<open/closed>` |

---

## 18. Document Control

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | AMPEL360/ATA 95 Governance | Template creation |

---

**End of OM_<bb_id>**

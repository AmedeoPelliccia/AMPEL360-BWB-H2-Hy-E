# 95-00-13-01-005: Links to 95-00-03 Requirements

## Document Information
- **Document ID**: 95-00-13-01-005
- **Title**: Links to 95-00-03 Requirements
- **Version**: 1.0
- **Status**: Active
- **Last Updated**: 2025-11-17

## Purpose

This document establishes traceability links between functional subsystems and the requirements defined in 95-00-03_Requirements.

## Traceability Approach

Each functional subsystem traces to:
1. Functional requirements (95-00-03/01_Functional)
2. Non-functional requirements (95-00-03/02_NonFunctional)
3. Safety requirements (95-00-03/03_Safety_and_AAI)
4. Regulatory requirements (95-00-03/04_Regulatory_Compliance)

## Subsystem to Requirement Mapping

### FS-001: Flight Control
**Functional Requirements**:
- REQ-FC-001: Provide pitch, roll, yaw control
- REQ-FC-002: Maintain stability augmentation
- REQ-FC-003: Support autopilot functions

**Safety Requirements**:
- REQ-SAF-FC-001: Detect and handle control surface failures
- REQ-SAF-FC-002: Provide redundant control paths
- REQ-SAF-FC-003: Limit control authority per flight envelope

**Performance Requirements**:
- REQ-PERF-FC-001: Control loop frequency ≥ 100 Hz
- REQ-PERF-FC-002: Control latency ≤ 10 ms
- REQ-PERF-FC-003: Position accuracy ± 0.1°

### FS-002: Navigation
**Functional Requirements**:
- REQ-NAV-001: Determine aircraft position
- REQ-NAV-002: Compute velocity and acceleration
- REQ-NAV-003: Estimate attitude

**Safety Requirements**:
- REQ-SAF-NAV-001: Detect sensor failures
- REQ-SAF-NAV-002: Provide backup navigation capability
- REQ-SAF-NAV-003: Alert crew of degraded accuracy

**Performance Requirements**:
- REQ-PERF-NAV-001: Position accuracy ≤ 10 m (GNSS available)
- REQ-PERF-NAV-002: Position accuracy ≤ 100 m (GNSS unavailable, 15 min)
- REQ-PERF-NAV-003: Update rate ≥ 100 Hz

## Complete Traceability Matrix

See: 95-00-13-14-002_Subsystems_to_RQ_Map.md for complete traceability.

## Requirements Coverage Analysis

**Coverage Metrics**:
- Total functional requirements: 156
- Allocated to subsystems: 156 (100%)
- Verified: 142 (91%)
- Pending verification: 14 (9%)

## Related Documents

- 95-00-03: Requirements Documentation
- 95-00-13-01-001: Functional Subsystems Overview
- 95-00-13-14-002: Subsystems to RQ Map

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-17 | AMPEL360 Documentation WG | Initial release |

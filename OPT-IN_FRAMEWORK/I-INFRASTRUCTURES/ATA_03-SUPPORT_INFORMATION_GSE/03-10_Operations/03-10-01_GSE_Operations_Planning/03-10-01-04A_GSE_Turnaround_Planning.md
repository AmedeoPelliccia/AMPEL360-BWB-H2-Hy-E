---
Title: "GSE Turnaround Planning"
Identifier: "AMPEL360-03-10-01-04A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Documentation Team"
ResponsibleOrg: "I-INFRASTRUCTURES GSE Operations"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
ReviewDue: "2026-06-07"
Effectivity: "Q100 INTEGRA GSE Operations"
Abstract: "Planning procedures for aircraft turnaround operations including GSE sequencing, timing, and coordination."
Keywords: ["GSE","Turnaround","Planning","Ground Operations","Sequencing","ATA 03"]
Compliance:
  - "ATA iSpec 2200"
  - "IATA Airport Handling Manual (AHM)"
  - "IATA Ground Operations Manual (IGOM)"
Links:
  ParentDoc: "./03-10-01-01A_GSE_Ops_Planning_Overview.md"
  Siblings:
    - "./03-10-01-02A_GSE_Ops_Scheduling.md"
    - "./03-10-01-03A_GSE_Resource_Planning.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Documentation Team", change: "Initial release" }
---

# 03-10-01-04A — GSE Turnaround Planning

## 1. Purpose

This document defines procedures for planning aircraft turnaround operations, including GSE sequencing, timing, critical path analysis, and coordination of multiple ground service activities to achieve target turnaround times for AMPEL360 BWB aircraft.

## 2. Scope

This document covers:
- Turnaround operation planning and sequencing
- GSE arrival and positioning timing
- Critical path analysis for turnaround operations
- H₂ refueling integration into turnaround sequence
- Contingency planning for turnaround delays
- Performance monitoring and optimization

## 3. Applicable Documents

- ATA iSpec 2200 (Information Standards for Aviation Maintenance)
- IATA Airport Handling Manual (AHM)
- IATA Ground Operations Manual (IGOM)
- SAE AS6968 (Hydrogen Aircraft Refueling Ground Support Equipment)
- `03-10-01-01A_GSE_Ops_Planning_Overview.md`
- `03-10-02_H2_GSE_Operations`

## 4. Operations Description

### 4.1 Overview

Aircraft turnaround planning coordinates the sequencing and timing of all GSE operations from aircraft arrival to departure. For H₂-powered aircraft, turnaround planning must integrate hydrogen refueling operations, which require special safety considerations and timing constraints.

### 4.2 Operating Procedures

#### 4.2.1 Standard Turnaround Sequence

| Step | Operation | GSE Required | Duration | Can Parallel | Notes |
|------|-----------|--------------|----------|--------------|-------|
| 1 | Aircraft arrival & parking | Marshallers, chocks | 3 min | No | Safety critical |
| 2 | Passenger disembarkation | Passenger stairs/jetway | 8-15 min | No | Complete before fueling |
| 3 | Cargo/baggage unloading | Cargo loaders, tugs | 15-25 min | Yes | Can parallel with other ops |
| 4 | H₂ safety zone establishment | Safety barriers, monitors | 5 min | No | Before H₂ connection |
| 5 | H₂ refueling operations | LH₂ bowser, transfer equip | 20-40 min | Limited | Critical path item |
| 6 | Cabin cleaning & servicing | Cleaning crew, supplies | 15-25 min | Yes | During or after H₂ ops |
| 7 | Catering service | Catering truck, loaders | 10-15 min | Yes | After H₂ ops complete |
| 8 | Water & lavatory service | Service trucks | 8-12 min | Yes | After H₂ ops complete |
| 9 | Ground power connection | GPU | 2 min | Yes | Early in turnaround |
| 10 | Cargo/baggage loading | Cargo loaders, tugs | 15-25 min | Yes | After H₂ ops complete |
| 11 | Passenger boarding | Passenger stairs/jetway | 15-25 min | No | After all servicing |
| 12 | Pre-departure checks | Ground crew | 5 min | No | Final safety check |
| 13 | Pushback & taxi | Pushback tug | 3-5 min | No | Departure |

**Total Turnaround Time: 45-90 minutes** (depending on aircraft configuration and services required)

#### 4.2.2 Critical Path Analysis

The critical path for AMPEL360 BWB turnaround operations typically includes:

1. **Passenger Disembarkation** (must complete before H₂ refueling)
2. **H₂ Refueling Operations** (longest duration, limited parallelization)
3. **Passenger Boarding** (must wait for all servicing completion)

**Optimization Strategy:**
- Maximize parallel operations during non-H₂ portions of turnaround
- Pre-position H₂ GSE to minimize connection time
- Streamline safety zone establishment procedures
- Coordinate catering/servicing to begin immediately after H₂ completion

#### 4.2.3 H₂ Refueling Integration

Special considerations for H₂ operations in turnaround:

- **Safety Zone**: 7.5m radius exclusion zone during H₂ transfer
- **Personnel Restrictions**: Only qualified H₂ handlers in safety zone
- **Equipment Restrictions**: No ignition sources, ATEX-certified equipment only
- **Monitoring**: Continuous H₂ leak detection during refueling
- **Weather Constraints**: Wind speed <15 kt, no precipitation during connection

### 4.3 Safety Considerations

- **Pre-Turnaround Safety Briefing**: All personnel briefed on H₂ hazards
- **Safety Zone Enforcement**: Physical barriers and signage for H₂ exclusion zone
- **Emergency Equipment**: Fire suppression equipment positioned nearby
- **Communication Protocol**: Dedicated radio channel for H₂ operations
- **Abort Procedures**: Clear protocols for stopping turnaround if safety concerns arise

## 5. Equipment Requirements

| Equipment | Specification | Quantity |
|-----------|---------------|----------|
| Turnaround Planning Software | Gantt chart, critical path analysis | 1 system |
| GSE Tracking System | Real-time location, status monitoring | Per GSE unit |
| H₂ Safety Monitoring | Leak detection, environmental sensors | Per H₂ operation |
| Communication Devices | Hands-free radio, digital messaging | Per crew member |

## 6. Cross-References

- Related ATA Chapters: ATA 02 (Operations Information), ATA 28 (Fuel/H₂)
- Parent Document: 03-10-01-01A_GSE_Ops_Planning_Overview
- Related H₂ Operations: 03-10-02_H2_GSE_Operations
- Related Safety: 03-10-05_GSE_Safety_Operations

## 7. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-07_.

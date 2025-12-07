# 03-00-09-06-02A - Work Order Management

**Version:** A  
**Date:** 2025-12-07  
**Status:** DRAFT  
**Document ID:** 03-00-09-06-02A

---

## 1. Purpose

This document establishes the work order management system for the AMPEL360 BWB-H2-Hy-E aircraft production program, defining how production activities are authorized, tracked, and closed.

## 2. Scope

This document covers:
- Work order structure and hierarchy
- Work order creation and release
- Status tracking and updates
- Material allocation and kitting
- Labor charging and reporting
- Work order closure and archival

## 3. Applicable Documents

- **ATA 03:** Support Information/Ground Support Equipment
- **AS9100:** Quality Management Systems - Aerospace
- **ATA 03-00-09-06-01A:** Master Schedule
- **ATA 03-00-09-06-03A:** Resource Allocation
- **ATA 03-00-09-04-02A:** Assembly Sequences

## 4. Description

### 4.1 Overview

Work orders are the fundamental production control documents that authorize manufacturing activities. The work order management system provides the structure for planning, executing, and tracking all production work.

### 4.2 Requirements

**Work Order Management Objectives:**
- Clear production authorization
- Accurate resource allocation
- Real-time status visibility
- Traceability of all activities
- Cost collection and control
- Quality integration

**Work Order Hierarchy:**
- **Program Work Order:** Overall aircraft
- **Assembly Work Orders:** Major assemblies
- **Component Work Orders:** Sub-assemblies
- **Operation Work Orders:** Individual operations
- **Rework Work Orders:** Corrective work

### 4.3 Methodology

**Work Order Management Process:**

1. **Work Order Creation**
   - Master schedule decomposition
   - Bill of materials (BOM) integration
   - Routing/sequence definition
   - Resource requirement calculation
   - Quality checkpoint insertion
   - Release date determination

2. **Work Order Release**
   - Material availability verification
   - Tooling availability confirmation
   - Labor availability check
   - Prerequisite work completion
   - Quality approval
   - System release

3. **Material Management**
   - Material allocation
   - Kit preparation
   - Material issue
   - Shortage management
   - Excess material handling
   - Material traceability

4. **Execution Tracking**
   - Operation start/stop times
   - Labor hours recording
   - Material usage tracking
   - Quality inspection results
   - Non-conformance documentation
   - Progress updates

5. **Status Management**
   - Not Released
   - Released
   - In Progress
   - On Hold
   - Completed
   - Closed

6. **Work Order Closure**
   - Completion verification
   - Quality sign-off
   - Cost reconciliation
   - Document collection
   - Archival
   - Lessons learned capture

## 5. Deliverables

| Deliverable | Format | Responsible | Due |
|-------------|--------|-------------|-----|
| Work Order Procedures | PDF | Production Control | 2025-Q3 |
| Work Order Templates | System/PDF | IT/Production | 2025-Q3 |
| MES System Configuration | Software | IT/Production | 2025-Q4 |
| Work Order Reports | Dashboard | Production Control | Ongoing |

## 6. Key Performance Indicators

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| Work Order On-Time Completion | >90% | Schedule tracking |
| Work Order Accuracy | >98% | Error tracking |
| Average Work Order Cycle Time | Per standard | Time tracking |
| Work Order Closure Time | <5 days | Process tracking |
| Material Shortage Rate | <2% | Material tracking |

## 7. Cross-References

- **Related ATA Chapters:**
  - ATA 03-00-06 (Engineering)
  - ATA 05 (Time Limits/Maintenance Checks)
- **Parent Document:** 03-00-09_Production_Planning
- **Related Subsections:**
  - 03-00-09-04-02A (Assembly Sequences)
  - 03-00-09-06-01A (Master Schedule)
  - 03-00-09-06-03A (Resource Allocation)
  - 03-00-09-03-03A (Inventory Management)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | Production Planning Team | Initial release |

---

**Document Control Information:**
- **Status:** DRAFT - Subject to review and approval
- **Classification:** Internal - Production
- **Distribution:** Production Control, Manufacturing, Materials Management, IT

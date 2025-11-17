# 02_NonFunctional — Non-Functional Requirements

## Purpose

This folder contains **non-functional requirements** (NFRs) — quality attributes that define **how well** the system must perform.

## Scope

### ID Range: RQ-95-00-03-100 to RQ-95-00-03-199

Non-functional requirements address:
- **Performance**: Latency, throughput, response time
- **Reliability**: Availability, fault tolerance, MTBF
- **Scalability**: Capacity, growth handling
- **Maintainability**: Ease of updates, diagnostics
- **Usability**: User experience, API ergonomics

## Requirements Summary

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-101 | DPP Availability ≥ 99.5% | APPROVED |
| RQ-95-00-03-102 | DPP Read Latency Under 500ms | APPROVED |
| RQ-95-00-03-103 | DPP SHALL Support Concurrent Access | DRAFT |
| ... | (Additional requirements as defined) | ... |

---

## What Belongs Here

**Non-functional requirements** define system quality attributes. Examples:
- "The system SHALL have 99.5% availability"
- "Read operations SHALL complete in < 500ms at 95th percentile"
- "The system SHALL support 1000+ concurrent users"

## What Doesn't Belong Here

- **Functional capabilities** → 01_Functional
- **Safety-specific attributes** → 03_Safety_and_AAI
- **Compliance mandates** → 04_Regulatory_Compliance

---

## Document Control

- **Folder**: 02_NonFunctional
- **ID Range**: 100-199
- **Owner**: Requirements WG / Quality Assurance
- **Last Updated**: 2025-11-17

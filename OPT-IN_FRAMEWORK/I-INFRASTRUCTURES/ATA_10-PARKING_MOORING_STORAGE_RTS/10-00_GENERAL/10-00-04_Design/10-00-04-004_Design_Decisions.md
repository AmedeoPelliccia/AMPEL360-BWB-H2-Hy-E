# 10-00-04-004 — Design Decisions

**ATA Chapter:** 10 — Parking, Mooring, Storage & RTS  
**Document ID:** 10-00-04-004  
**Version:** 1.0  
**Status:** DRAFT  

---

## 1. Purpose

This document records key design decisions made during the development of parking, mooring, storage, and RTS provisions for the Q100 aircraft, including rationale and alternatives considered.

---

## 2. Decision Log

### DD-10-001: Mooring Point Configuration

**Decision:** Five mooring points — forward, aft, tail, left wing, right wing

**Rationale:**
- BWB configuration requires distributed load paths
- Five-point system provides redundancy and stability in crosswinds
- Wing mooring points necessary due to wide span (80.4 m)

**Alternatives Considered:**
- Three-point system (nose, tail, centerline) — insufficient for BWB geometry
- Seven-point system — added complexity with marginal stability benefit

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-002: Towing Lug Location

**Decision:** Main towing lug at nose gear, auxiliary lugs at wing root

**Rationale:**
- Standard nose gear towing maintains compatibility with existing GSE
- Auxiliary wing root lugs provide backup capability
- Emergency towing provisions at reinforced attachment points

**Alternatives Considered:**
- Center fuselage towing only — poor visibility and limited maneuverability
- Wing tip towing — excessive structural loads and ground crew risk

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-003: H₂ Storage Isolation Strategy

**Decision:** Multi-layer isolation: manual valve + automated isolation + pressure relief

**Rationale:**
- Fail-safe design required for cryogenic LH₂
- Manual isolation for long-term storage
- Automated isolation for emergency scenarios
- Pressure relief prevents tank over-pressure during extended storage

**Alternatives Considered:**
- Single manual isolation — insufficient safety margin
- Fully automated only — requires continuous power, less reliable for long-term storage

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-004: HV Isolation Architecture

**Decision:** Distributed isolation points with central lockout panel

**Rationale:**
- Main disconnect at battery packs (primary HV source)
- Secondary isolation at fuel cell stacks and motor controllers
- Central LOTO panel for simplified maintenance procedures
- Ground fault interrupter (GFI) protection at all isolation points

**Alternatives Considered:**
- Single master disconnect — lacks zone-based maintenance capability
- Fully distributed with no central panel — complex procedures, higher error risk

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-005: Ground Power Interface Type

**Decision:** Hybrid interface: 400Hz AC + High-power DC (CCS2/MCS compatible)

**Rationale:**
- 400Hz AC for legacy GSE compatibility
- High-power DC (up to 800V, 350 kW) for rapid battery charging
- CCS2/MCS connector standard adopted for future-proofing
- Automatic transfer switch for seamless source switching

**Alternatives Considered:**
- 400Hz AC only — insufficient for rapid battery charging
- DC only — incompatible with existing airport infrastructure

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-006: Jacking Point Distribution

**Decision:** Five primary jacking points aligned with main structural frames

**Rationale:**
- Distributed loads to match BWB structural design
- Forward jacking point at nose gear bay
- Two main jacking points under wing-fuselage blend (LH/RH)
- Aft jacking point at rear spar
- Emergency jacking provisions at reinforced hard points

**Alternatives Considered:**
- Three-point system — insufficient for BWB weight distribution
- Seven-point system — overconstrained, higher alignment complexity

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-007: Protective Cover Material

**Decision:** Multi-layer fabric covers with reflective outer layer

**Rationale:**
- UV-resistant outer layer with high reflectivity (reduce thermal load)
- Breathable middle layer (prevent condensation)
- Soft inner lining (protect painted surfaces)
- Custom fit for H₂ vents and HV connectors

**Alternatives Considered:**
- Rigid covers — difficult to handle, storage challenges
- Single-layer tarps — inadequate UV and thermal protection

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-008: H₂ Leak Detection Technology

**Decision:** Redundant sensor arrays: electrochemical + thermal conductivity

**Rationale:**
- Electrochemical sensors for high sensitivity (ppm range)
- Thermal conductivity sensors for wide range (0-100% H₂)
- Redundant arrays at tank boundaries, vents, and connection points
- Continuous monitoring during storage with remote alert capability

**Alternatives Considered:**
- Single sensor technology — insufficient redundancy for critical safety function
- Manual inspection only — cannot detect slow leaks or monitor continuously

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-009: Tie-Down Hardware Quick Release Mechanism

**Decision:** Spring-loaded pin with secondary safety latch

**Rationale:**
- Tool-less release for rapid deployment/removal
- Secondary latch prevents inadvertent release
- Visual indicator (red/green) for engagement status
- Tension indicator integrated into strap assembly

**Alternatives Considered:**
- Threaded turnbuckles — slow, requires tools
- Cam-lock only — potential for accidental release

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

### DD-10-010: Environmental Monitoring System Architecture

**Decision:** Standalone monitoring unit with wireless connectivity

**Rationale:**
- Independent of aircraft power systems
- Battery-powered (30-day autonomy minimum)
- Wireless connection to facility management systems
- Sensor suite: temperature, humidity, H₂ concentration, HV voltage presence
- Data logging with trend analysis and predictive alerts

**Alternatives Considered:**
- Aircraft-powered system — requires ground power, less reliable
- Manual monitoring — labor-intensive, delayed response to issues

**Status:** Approved  
**Date:** TBD  
**Approver:** TBD

---

## 3. Pending Decisions

### PD-10-001: RTS Kit Tool Selection

**Issue:** Selection of specific tools for H₂ system test kit

**Options:**
1. Custom-designed tools specific to Q100
2. Adapt existing aerospace H₂ tools (space industry)
3. Combination approach

**Target Decision Date:** TBD  
**Responsible:** TBD

---

### PD-10-002: Boil-Off Capture vs. Vent

**Issue:** Whether to capture H₂ boil-off during long-term storage or vent safely

**Options:**
1. Vent to atmosphere via controlled release point
2. Capture and liquify for reuse
3. Burn-off with catalytic converter

**Target Decision Date:** TBD  
**Responsible:** TBD

---

## 4. Design Decision Traceability

| Decision ID | Related Requirements | Related Assemblies | Verification Method |
|-------------|---------------------|-------------------|---------------------|
| DD-10-001 | REQ-10-XXX | ASM-10-001 | Load testing |
| DD-10-002 | REQ-10-XXX | ASM-10-002 | Towing trials |
| DD-10-003 | REQ-10-XXX | ASM-10-007 | Isolation testing |
| DD-10-004 | REQ-10-XXX | ASM-10-008 | HV isolation verification |
| DD-10-005 | REQ-10-XXX | ASM-10-009 | Charging tests |
| DD-10-006 | REQ-10-XXX | ASM-10-003 | Jacking load tests |
| DD-10-007 | REQ-10-XXX | ASM-10-006 | Environmental testing |
| DD-10-008 | REQ-10-XXX | ASM-10-007, ASM-10-011 | Leak detection calibration |
| DD-10-009 | REQ-10-XXX | ASM-10-004 | Release mechanism testing |
| DD-10-010 | REQ-10-XXX | ASM-10-011 | System integration test |

---

## 5. Change History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | 2025-12-09 | Initial draft | TBD |

---

## Document Control

- **Generated with assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT – Subject to human review and approval
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---

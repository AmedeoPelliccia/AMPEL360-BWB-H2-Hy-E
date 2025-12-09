# ASM-10-099-A — Assembly Index

**Document ID:** ASM-10-099-A  
**Version:** 1.0  
**Status:** DRAFT  
**Last Updated:** 2025-12-09

---

## Purpose

This document provides a master index of all assembly definitions in ATA Chapter 10 — Parking, Mooring, Storage & RTS.

---

## Assembly Master List

| Assembly ID | Title | Components | Status | Safety Criticality | H₂ | HV | Notes |
|-------------|-------|------------|--------|-------------------|----|----|-------|
| ASM-10-001 | Mooring Points | 5 | Planned | Critical | ❌ | ❌ | BWB-specific distribution |
| ASM-10-002 | Towing Fittings | 4 | Planned | Critical | ❌ | ❌ | High-load capacity required |
| ASM-10-003 | Jacking Points | 5 | Planned | Critical | ❌ | ❌ | BWB weight distribution |
| ASM-10-004 | Tie-Down Hardware | 5 | Planned | High | ❌ | ❌ | Quick-release mechanism |
| ASM-10-005 | Ground Locks | 5 | Planned | Critical | ❌ | ❌ | Safety interlock system |
| ASM-10-006 | Protective Covers | 8 | Planned | Medium | ✅ | ✅ | Includes H₂ and HV covers |
| ASM-10-007 | H₂ Storage Provisions | 6 | Planned | Critical | ✅ | ❌ | Cryogenic-specific design |
| ASM-10-008 | HV Isolation Provisions | 6 | Planned | Critical | ❌ | ✅ | 800V+ electrical systems |
| ASM-10-009 | Ground Power Interface | 5 | Planned | High | ❌ | ✅ | Dual-mode (AC + DC) |
| ASM-10-010 | Environmental Protection | 6 | Planned | Medium | ❌ | ❌ | Storage preservation |
| ASM-10-011 | Monitoring Systems | 6 | Planned | High | ✅ | ✅ | H₂ + battery monitoring |
| ASM-10-012 | RTS Kit | 6 | Planned | Low | ✅ | ✅ | Return-to-service tools |

**Legend:**  
✅ = Yes, ❌ = No  
H₂ = Hydrogen-specific, HV = High-voltage-specific

---

## Assembly Details

### ASM-10-001: Mooring Points

**Path:** [`ASM-10-001_Mooring_Points/`](../ASM-10-001_Mooring_Points/)

**Components:**
1. Forward Mooring Point
2. Aft Mooring Point
3. Wing Mooring Point (LH)
4. Wing Mooring Point (RH)
5. Tail Mooring Point

**Key Interfaces:**
- ATA 53 (Fuselage structure)
- ATA 57 (Wings)

---

### ASM-10-002: Towing Fittings

**Path:** [`ASM-10-002_Towing_Fittings/`](../ASM-10-002_Towing_Fittings/)

**Components:**
1. Main Towing Lug
2. Auxiliary Towing Lug
3. Emergency Towing Point
4. Towing Adapter Interface

**Key Interfaces:**
- ATA 09 (Towing & Taxiing)
- ATA 32 (Landing Gear)

---

### ASM-10-003: Jacking Points

**Path:** [`ASM-10-003_Jacking_Points/`](../ASM-10-003_Jacking_Points/)

**Components:**
1. Forward Jacking Point
2. Main Jacking Point (LH)
3. Main Jacking Point (RH)
4. Aft Jacking Point
5. Emergency Jacking Provisions

**Key Interfaces:**
- ATA 07 (Lifting & Shoring)
- ATA 53 (Fuselage structure)

---

### ASM-10-004: Tie-Down Hardware

**Path:** [`ASM-10-004_Tie_Down_Hardware/`](../ASM-10-004_Tie_Down_Hardware/)

**Components:**
1. Tie-Down Ring
2. Tie-Down Anchor
3. Tie-Down Strap Assembly
4. Quick Release Mechanism
5. Tension Indicator

**Key Interfaces:**
- ATA 53 (Attachment points)

---

### ASM-10-005: Ground Locks

**Path:** [`ASM-10-005_Ground_Locks/`](../ASM-10-005_Ground_Locks/)

**Components:**
1. Landing Gear Ground Lock
2. Control Surface Lock
3. Propeller Lock
4. Door Hold-Open Lock
5. Throttle Lock

**Key Interfaces:**
- ATA 27 (Flight Controls)
- ATA 32 (Landing Gear)
- ATA 52 (Doors)
- ATA 71 (Powerplant)

---

### ASM-10-006: Protective Covers

**Path:** [`ASM-10-006_Protective_Covers/`](../ASM-10-006_Protective_Covers/)

**Components:**
1. Pitot-Static Covers
2. Engine Inlet Covers
3. Exhaust Covers
4. Sensor Covers
5. Window Covers
6. Landing Gear Covers
7. H₂ Vent Covers 🧊
8. HV Connector Covers ⚡

**Key Interfaces:**
- ATA 28 (Fuel - H₂ vents)
- ATA 24 (Electrical - HV connectors)
- ATA 71 (Powerplant)

---

### ASM-10-007: H₂ Storage Provisions 🧊

**Path:** [`ASM-10-007_H2_Storage_Provisions/`](../ASM-10-007_H2_Storage_Provisions/)

**Components:**
1. Tank Isolation System
2. Vent Management System
3. Pressure Relief Interface
4. Leak Detection Provisions
5. Boil-Off Management
6. Ground Vent Connection

**Key Interfaces:**
- ATA 28 (Fuel Systems)
- ATA 73 (Engine Fuel Systems)
- ASM-10-011 (Monitoring Systems)

**Safety Note:** Critical safety system for cryogenic LH₂ storage.

---

### ASM-10-008: HV Isolation Provisions ⚡

**Path:** [`ASM-10-008_HV_Isolation_Provisions/`](../ASM-10-008_HV_Isolation_Provisions/)

**Components:**
1. Main HV Disconnect
2. Battery Isolation Switch
3. Fuel Cell Isolation
4. Motor Isolation Contactors
5. Ground Fault Interrupter
6. LOTO Provisions

**Key Interfaces:**
- ATA 24 (Electrical Power)
- ATA 80 (Starting)
- ASM-10-009 (Ground Power)

**Safety Note:** Critical for 800V+ electrical system safety and maintenance.

---

### ASM-10-009: Ground Power Interface

**Path:** [`ASM-10-009_Ground_Power_Interface/`](../ASM-10-009_Ground_Power_Interface/)

**Components:**
1. External Power Receptacle
2. Power Transfer Switch
3. Ground Power Controller
4. Battery Charging Interface
5. Shore Power Connector

**Key Interfaces:**
- ATA 24 (Electrical Power)
- ASM-10-008 (HV Isolation)

---

### ASM-10-010: Environmental Protection

**Path:** [`ASM-10-010_Environmental_Protection/`](../ASM-10-010_Environmental_Protection/)

**Components:**
1. Weather Sealing Kit
2. Desiccant System
3. Corrosion Protection Kit
4. UV Protection Covers
5. Thermal Blankets
6. Humidity Control System

**Key Interfaces:**
- All ATA chapters (general protection)

---

### ASM-10-011: Monitoring Systems

**Path:** [`ASM-10-011_Monitoring_Systems/`](../ASM-10-011_Monitoring_Systems/)

**Components:**
1. Storage Monitoring Unit
2. H₂ Leak Detection System 🧊
3. Battery Monitoring System ⚡
4. Environmental Sensors
5. Remote Monitoring Interface
6. Alert Notification System

**Key Interfaces:**
- ASM-10-007 (H₂ Storage)
- ASM-10-008 (HV Isolation)
- ATA 24 (Electrical Power)

---

### ASM-10-012: RTS Kit

**Path:** [`ASM-10-012_RTS_Kit/`](../ASM-10-012_RTS_Kit/)

**Components:**
1. Inspection Tools
2. Fluid Sampling Kit
3. Electrical Test Kit
4. H₂ System Test Kit 🧊
5. Functional Test Equipment
6. Calibration References

**Key Interfaces:**
- All ATA 10 assemblies (test/inspection support)

---

## Summary Statistics

- **Total Assemblies:** 12
- **Total Components:** 66
- **Critical Safety Assemblies:** 6
- **H₂-Specific Assemblies:** 4
- **HV-Specific Assemblies:** 5
- **Dual (H₂+HV) Assemblies:** 3

---

## Change History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | 2025-12-09 | Initial index created | TBD |

---

## Document Control

- **Generated with assistance of AI** (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT – Subject to human review and approval
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---

# DWG-10-099-D — Cross References

**Document ID:** DWG-10-099-D  
**Title:** Drawing Cross References  
**ATA Chapter:** 10 – Parking, Mooring, Storage, RTS  
**Status:** DRAFT  
**Version:** A  
**Date:** 2025-12-09

---

## 1. Purpose

This document provides cross-references between ATA 10 drawings and other project documents, including requirements, assemblies, and related ATA chapters.

---

## 2. Related ATA Chapters

### 2.1 Primary Interfaces

| ATA Chapter | Title | Interface Points | Related Drawings |
|-------------|-------|------------------|------------------|
| 06 | Dimensions & Areas | Aircraft dimensions, clearances | DWG-10-100 series |
| 07 | Lifting & Shoring | Jacking points, lifting provisions | DWG-10-400 series |
| 09 | Towing & Taxiing | Towing lugs, ground movement | DWG-10-300 series |
| 12 | Servicing | Ground service connections | DWG-10-1000 series |
| 24 | Electrical Power | Ground power, HV systems | DWG-10-900, DWG-10-1000 |
| 28 | Fuel | H₂ storage and handling | DWG-10-800 series |
| 73 | Fuel System | H₂ system interfaces | DWG-10-800 series |

### 2.2 Secondary Interfaces

| ATA Chapter | Title | Interface Points | Related Drawings |
|-------------|-------|------------------|------------------|
| 05 | Time Limits/Maintenance Checks | RTS procedures | DWG-10-1300 series |
| 25 | Equipment/Furnishings | Interior access during storage | DWG-10-700 series |
| 30 | Ice and Rain Protection | Protective covers | DWG-10-700 series |
| 32 | Landing Gear | Ground locks, jacking | DWG-10-400, DWG-10-600 |
| 45 | Central Maintenance System | Monitoring interfaces | DWG-10-1200 series |

---

## 3. Assembly Cross-References

### 3.1 Drawing Series to Assembly Mapping

| Drawing Series | Assembly Reference | Description |
|----------------|-------------------|-------------|
| DWG-10-200 | ASM-10-001 | Mooring Points Assembly |
| DWG-10-300 | ASM-10-002 | Towing Fittings Assembly |
| DWG-10-400 | ASM-10-003 | Jacking Points Assembly |
| DWG-10-500 | ASM-10-004 | Tie-Down Hardware Assembly |
| DWG-10-600 | ASM-10-005 | Ground Locks Assembly |
| DWG-10-700 | ASM-10-006 | Protective Covers Assembly |
| DWG-10-800 | ASM-10-007 | H₂ Storage Provisions |
| DWG-10-900 | ASM-10-008 | HV Isolation Provisions |
| DWG-10-1000 | ASM-10-009 | Ground Power Interface |
| DWG-10-1100 | ASM-10-010 | Environmental Protection |
| DWG-10-1200 | ASM-10-011 | Monitoring Systems |
| DWG-10-1300 | ASM-10-012 | RTS Kit Assembly |

---

## 4. Requirements Traceability

### 4.1 Safety Requirements

| Requirement ID | Title | Related Drawings |
|----------------|-------|------------------|
| REQ-10-SAF-001 | H₂ Leak Detection | DWG-10-800-004, DWG-10-1200-002 |
| REQ-10-SAF-002 | HV Isolation | DWG-10-900-001, DWG-10-900-010 |
| REQ-10-SAF-003 | Emergency Shutoff | DWG-10-800-050, DWG-10-900-050 |
| REQ-10-SAF-004 | Exclusion Zones | DWG-10-100-006, DWG-10-800-040 |
| REQ-10-SAF-005 | Arc Flash Protection | DWG-10-900-040, DWG-10-900-060 |
| REQ-10-SAF-006 | Load Distribution | DWG-10-400-040 |
| REQ-10-SAF-007 | Warning Labels | DWG-10-1400 series |

### 4.2 Functional Requirements

| Requirement ID | Title | Related Drawings |
|----------------|-------|------------------|
| REQ-10-FUN-001 | Parking Zones | DWG-10-100-001 |
| REQ-10-FUN-002 | Mooring Capability | DWG-10-200 series |
| REQ-10-FUN-003 | Towing Capability | DWG-10-300 series |
| REQ-10-FUN-004 | Jacking Capability | DWG-10-400 series |
| REQ-10-FUN-005 | Ground Power | DWG-10-1000 series |
| REQ-10-FUN-006 | Environmental Protection | DWG-10-1100 series |
| REQ-10-FUN-007 | Storage Monitoring | DWG-10-1200 series |

### 4.3 Interface Requirements

| Requirement ID | Title | Related Drawings |
|----------------|-------|------------------|
| REQ-10-INT-001 | H₂ Ground Connection | DWG-10-800-006 |
| REQ-10-INT-002 | HV Ground Connection | DWG-10-1000-005 |
| REQ-10-INT-003 | GSE Interface | DWG-10-100-008 |
| REQ-10-INT-004 | Monitoring Interface | DWG-10-1200-005 |

---

## 5. Structural Zone References

### 5.1 Fuselage Zones

| Zone | Description | Related Drawings |
|------|-------------|------------------|
| Zone 100 | Nose section | DWG-10-200-001 (Forward mooring) |
| Zone 200 | Forward fuselage | DWG-10-400-001 (Forward jacking) |
| Zone 300 | Center fuselage | DWG-10-400-002, DWG-10-400-003 (Main jacking) |
| Zone 400 | Aft fuselage | DWG-10-200-002 (Aft mooring) |
| Zone 500 | Tail section | DWG-10-200-005 (Tail mooring) |
| Zone 600 | Wing sections | DWG-10-200-003, DWG-10-200-004 (Wing mooring) |

---

## 6. System Interface Matrix

### 6.1 H₂ System Interfaces

| System | Interface Point | Drawing Reference |
|--------|----------------|-------------------|
| H₂ Storage | Tank isolation | DWG-10-800-001 |
| H₂ Venting | Vent management | DWG-10-800-002 |
| H₂ Safety | Leak detection | DWG-10-800-004, DWG-10-1200-002 |
| H₂ Ground Service | Ground connection | DWG-10-800-006 |

### 6.2 HV System Interfaces

| System | Interface Point | Drawing Reference |
|--------|----------------|-------------------|
| HV Distribution | Main disconnect | DWG-10-900-001 |
| Battery System | Isolation switch | DWG-10-900-002 |
| Fuel Cell | Isolation | DWG-10-900-003 |
| Ground Power | Charging port | DWG-10-1000-004 |

---

## 7. Procedure Cross-References

### 7.1 Operational Procedures

| Procedure | Related Drawings |
|-----------|------------------|
| Aircraft Parking | DWG-10-100-001 |
| Mooring Setup | DWG-10-200-020 |
| Towing Operation | DWG-10-300-040 |
| Jacking Procedure | DWG-10-400-020, DWG-10-400-030 |
| Tie-Down Installation | DWG-10-500-020 |
| Ground Lock Application | DWG-10-600-020 |
| Cover Installation | DWG-10-700-020 |
| H₂ System Isolation | DWG-10-800-020 |
| HV System Isolation | DWG-10-900-020 |
| Ground Power Connection | DWG-10-1000-020 |
| RTS Inspection | DWG-10-1300-020, DWG-10-1300-030 |

---

## 8. Standards and Regulations

### 8.1 Applicable Standards

| Standard | Title | Related Drawings |
|----------|-------|------------------|
| CS-25 | Certification Specifications for Large Aeroplanes | All series |
| ISO 7010 | Safety Signs and Symbols | DWG-10-1400 series |
| SAE AS8015 | Jacking and Shoring | DWG-10-400 series |
| NFPA 2 | Hydrogen Technologies Code | DWG-10-800 series |
| IEEE 1584 | Arc Flash Hazard Calculation | DWG-10-900 series |

---

## 9. Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---

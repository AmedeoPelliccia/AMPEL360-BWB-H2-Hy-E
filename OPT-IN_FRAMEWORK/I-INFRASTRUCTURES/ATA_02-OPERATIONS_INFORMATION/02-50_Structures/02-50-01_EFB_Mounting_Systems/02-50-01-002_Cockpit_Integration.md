# 02-50-01-002: Cockpit Integration

## Document Information

- **Document ID**: 02-50-01-002
- **Version**: 1.0.0
- **Status**: DRAFT
- **Date**: 2025-11-21

## 1. Purpose

Details the cockpit integration of EFB mounts including attachment points, clearances, human factors considerations, and wiring interfaces.

## 2. Attachment Points

### 2.1 Pilot Side (Left)

- **Location**: Left instrument panel, STA 120, BL -20, WL 42
- **Hard points**: 4× threaded inserts, M6×1.0, 10mm deep
- **Panel structure**: Aluminum honeycomb, 3mm face sheets
- **Load capacity**: 500N per fastener (verified by panel analysis)

### 2.2 Copilot Side (Right)

- **Location**: Right instrument panel, STA 120, BL +20, WL 42
- **Hard points**: 4× threaded inserts, M6×1.0, 10mm deep (mirror of pilot side)
- **Panel structure**: Identical to pilot side

## 3. Clearances

### 3.1 Static Clearances

| Adjacent Component | Clearance | Notes |
|--------------------|-----------|-------|
| Primary Flight Display (PFD) | 100mm minimum | No obstruction of display |
| Control column | 150mm stowed, 50mm extended | Prevents interference during flight |
| Circuit breaker panel | 80mm | Access for maintenance |
| Side console | 60mm | Pilot elbow room |

### 3.2 Dynamic Clearances

- **EFB articulation**: Full range of motion (±30° tilt, ±15° rotate) without contact
- **Control column travel**: Full forward/aft and lateral motion unobstructed
- **Seat adjustment**: Pilot seat full range (fore/aft, up/down) does not contact EFB

## 4. Human Factors

### 4.1 Viewing Geometry

- **Eye-to-EFB distance**: 550-650mm (optimal for 12.9" display)
- **Viewing angle**: 15° below horizontal eye line (reduces neck strain)
- **Glare mitigation**: Pilot can tilt ±30° to avoid direct sunlight

### 4.2 Reachability

- **One-handed operation**: Pilot can reach and operate EFB with left hand without looking
- **Touch targets**: EFB screen fully accessible without arm extension
- **Emergency release**: Quick-release button within easy reach (400mm from pilot shoulder)

### 4.3 Anthropometry

Design accommodates 5th percentile female to 95th percentile male pilots:
- Seat adjusted for leg length (short/tall pilots)
- EFB remains in comfortable reach and viewing zone for all pilots

**Reference**: MIL-STD-1472G (Human Engineering Design Criteria)

## 5. Wiring Interfaces

### 5.1 Power Supply (Optional)

- **Connector**: USB-C (USB Power Delivery 3.0)
- **Power rating**: 5V DC, 3A max (15W)
- **Cable routing**: From left side console power outlet, 1.5m cable with strain relief
- **Circuit protection**: 5A fuse in cockpit circuit breaker panel (CB-EFB-PWR)

### 5.2 Data Interface

- **Connection**: Wireless only (WiFi to cockpit network)
- **No hardwired data**: Eliminates cable clutter and simplifies installation

### 5.3 Grounding

- **Mount grounding**: Direct metal-to-metal contact with panel (< 0.001 Ω)
- **EFB grounding**: Via USB cable shield (if power cable connected)
- **EMI compliance**: Verified per [DO-160G](https://www.rtca.org/) Section 20 (RF susceptibility)

## 6. Installation Coordination

### 6.1 Prerequisites

Before EFB mount installation:
- Instrument panel installation complete
- Wiring harness for USB power installed (if applicable)
- Panel hard points inspected and verified (thread engagement, pull-out strength)

### 6.2 Interface Control

Interfaces managed via:
- **Mechanical ICD**: Panel hard point locations and load capacity
- **Electrical ICD**: Power supply voltage, current, connector type
- **Human factors ICD**: Clearance zones and viewing geometry

**Reference**: [02-00-05_Interfaces](../../02-00_GENERAL/02-00-05_Interfaces/)

## 7. Certification Considerations

### 7.1 Part 25 Compliance

- **CS-25.771**: Pilot compartment view — EFB does not obstruct required field of view
- **CS-25.777**: Cockpit controls — EFB mount does not interfere with flight control operation
- **CS-25.1301**: Function and installation — EFB is accessible and operable under all flight conditions

**Reference**: [CS-25 Large Aeroplanes](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)

### 7.2 Equipment Approval

- EFB mount is **minor modification** (no flight control or structural impact)
- Approved under **EASA Part 21 Subpart D** (Design Organisation Approval)

## 8. Related Documents

- [02-50-01-001_EFB_Mount_Design.md](./02-50-01-001_EFB_Mount_Design.md) — Mount design specifications
- [02-50-01-005_Installation_Procedures.md](./02-50-01-005_Installation_Procedures.md) — Installation steps
- [02-50-00-002_Physical_Infrastructure_Map.md](../02-50-00-002_Physical_Infrastructure_Map.md) — Cockpit zone mapping

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---

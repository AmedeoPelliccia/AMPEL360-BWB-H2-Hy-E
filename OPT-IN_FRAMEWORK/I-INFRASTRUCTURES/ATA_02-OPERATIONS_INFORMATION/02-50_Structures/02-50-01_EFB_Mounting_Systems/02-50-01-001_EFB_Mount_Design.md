# 02-50-01-001: EFB Mount Design

## Document Information

- **Document ID**: 02-50-01-001
- **Version**: 1.0.0
- **Status**: DRAFT
- **Date**: 2025-11-21

## 1. Purpose

Describes the design of Electronic Flight Bag (EFB) mounting systems for pilot and copilot positions, including geometry, materials, interfaces, constraints, and design rationale.

## 2. Design Overview

### 2.1 Mount Types

| Mount ID | Position | Device Compatibility | Adjustability |
|----------|----------|---------------------|---------------|
| PILOT-EFB-01 | Left instrument panel | iPad Pro 12.9", Surface Pro | Tilt ±30°, rotate ±15° |
| COPILOT-EFB-01 | Right instrument panel | iPad Pro 12.9", Surface Pro | Tilt ±30°, rotate ±15° |

### 2.2 Design Requirements

Derived from [CS-25.561](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) and operational requirements:

| Requirement | Value | Rationale |
|-------------|-------|-----------|
| Ultimate load | 16g forward, 8g lateral, 14g down | Emergency landing per CS-25.561 |
| Vibration | Per DO-160G Section 8, Category S | Cockpit environment |
| Temperature | -20°C to +55°C operating | Cockpit temperature range |
| Weight (mount only) | < 0.5 kg | Weight optimization |
| Device retention | Positive locking, no tools to release | Safety and usability |

## 3. Geometry and Dimensions

### 3.1 Mounting Interface

- **Attachment**: 4× M6 bolts to instrument panel hard points
- **Bolt spacing**: 100mm × 80mm rectangular pattern
- **Panel thickness**: 3mm aluminum
- **Clearance**: Minimum 50mm to adjacent components

### 3.2 Articulation

- **Tilt axis**: Horizontal, ±30° from vertical
- **Rotation axis**: Vertical, ±15° from centerline
- **Friction adjustment**: Thumbscrew, no tools required

### 3.3 Device Cradle

- **Width**: Adjustable 200-280mm (iPad to Surface Pro range)
- **Depth**: 15mm grip on device edges
- **Padding**: Soft-touch thermoplastic elastomer (TPE), 2mm thick

## 4. Materials and Construction

### 4.1 Bill of Materials

| Part | Material | Specification | Finish |
|------|----------|---------------|--------|
| Base bracket | Aluminum 6061-T6 | [AMS 4027](https://www.sae.org/standards/content/ams4027/) | Anodize Type II, clear |
| Arm tube | Aluminum 7075-T6 | [AMS 4045](https://www.sae.org/standards/content/ams4045/) | Anodize Type II, black |
| Pivot bushings | Bronze alloy | SAE 660 | As-cast |
| Fasteners | Stainless A286 | NAS screws | Passivated |
| Cradle springs | Music wire | ASTM A228 | Zinc plated |

### 4.2 Mass Budget

- Base bracket: 180g
- Articulating arm: 150g
- Device cradle: 120g
- **Total mount mass**: ~450g (within 0.5kg limit)

## 5. Interface Specifications

### 5.1 Mechanical Interface

- **Panel hard points**: Existing instrument panel structure at STA 120, FR 10
- **Fastener torque**: 10 Nm (M6 bolts) per [02-50-00-003_Installation_Standards.md](../02-50-00-003_Installation_Standards.md)
- **Grounding**: Direct metal-to-metal contact, < 0.001 Ω resistance

### 5.2 Electrical Interface

- **Power**: Optional USB-C charging port (5V, 3A max)
- **Data**: None (wireless EFB connection via cockpit WiFi)
- **Cable routing**: Integrated strain relief and cable clips

## 6. Design Rationale

### 6.1 Material Selection

- **Aluminum 6061-T6 base**: Good strength-to-weight, easy to machine, corrosion resistant
- **Aluminum 7075-T6 arm**: Higher strength for crash loads in thin-wall tube
- **Bronze bushings**: Low friction, no lubrication required

### 6.2 Articulation Design

- **Friction hold**: Allows pilot to position EFB and maintains position under vibration
- **Range of motion**: Covers all pilot viewing angles and stowage positions
- **Tool-free adjustment**: Operational requirement for in-flight repositioning

### 6.3 Device Retention

- **Spring-loaded cradle**: Accommodates device thickness variation (8-13mm)
- **Corner grips**: Four-point contact prevents rotation or ejection under crash loads
- **Quick-release button**: Single-action release for emergency egress

## 7. Load Paths and Structural Concept

### 7.1 Load Path

Under 16g forward crash load:
1. Device (max 1kg) applies 160N force to cradle
2. Cradle transfers load to arm via pivot pin (Ø8mm, double shear)
3. Arm transfers load to base bracket via second pivot (Ø10mm, double shear)
4. Base bracket transfers load to panel via 4× M6 bolts (tension and shear)

### 7.2 Margins of Safety

From FEA analysis [02-50-01-A-101_Static_Load_Analysis.pdf](./ASSETS/FEA_Analysis/02-50-01-A-101_Static_Load_Analysis.pdf):

| Component | Critical Load Case | Margin of Safety |
|-----------|-------------------|------------------|
| Base bracket | 16g forward | MS = +0.85 |
| Arm tube | 16g forward | MS = +1.12 |
| Pivot pins | 16g forward, double shear | MS = +2.30 |
| M6 fasteners | 16g forward, pull-out | MS = +0.52 |

*(MS > 0 required, all components positive margin)*

## 8. Human Factors and Ergonomics

### 8.1 Viewing Angles

- **Normal operation**: EFB tilted 15° from vertical, eye point ~600mm
- **Glare mitigation**: Tilt adjustment allows pilot to avoid sun/light reflections
- **No obstruction**: Mount does not obstruct primary flight display (PFD) view

### 8.2 Reach Envelope

- **Pilot shoulder to mount**: 450mm (within easy reach)
- **One-handed operation**: Release button accessible without looking
- **Emergency egress**: Mount does not impede pilot exit or obstruct escape path

## 9. Design Verification

Design verified through:

1. **CAD modeling**: [02-50-01-A-001_Pilot_EFB_Mount.step](./ASSETS/CAD_Models/02-50-01-A-001_Pilot_EFB_Mount.step)
2. **FEA analysis**: Static loads, vibration modes (see ASSETS/FEA_Analysis)
3. **Prototype testing**: Physical mockup in cockpit simulator for ergonomics
4. **Certification testing**: DO-160G and 16g crash tests (see ASSETS/Test_Reports)

## 10. Configuration Control

### 10.1 Effectivity

- **Aircraft**: AMPEL360 BWB H2-Hy-E, S/N 001 onward
- **Retrofit**: Not applicable (new aircraft only)

### 10.2 Interchangeability

- Pilot and copilot mounts are **mirror images**, not interchangeable
- Device cradles are **common** and interchangeable (left/right)

## 11. Related Documents

- [02-50-01-002_Cockpit_Integration.md](./02-50-01-002_Cockpit_Integration.md) — Detailed cockpit installation
- [02-50-01-003_Vibration_Analysis.md](./02-50-01-003_Vibration_Analysis.md) — Dynamic analysis
- [02-50-01-005_Installation_Procedures.md](./02-50-01-005_Installation_Procedures.md) — Installation instructions
- [02-50-00-003_Installation_Standards.md](../02-50-00-003_Installation_Standards.md) — General standards

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---

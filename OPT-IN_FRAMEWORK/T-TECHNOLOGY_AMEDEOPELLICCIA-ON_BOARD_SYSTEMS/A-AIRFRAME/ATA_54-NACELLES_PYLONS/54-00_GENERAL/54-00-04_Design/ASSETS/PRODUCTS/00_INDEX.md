# PRODUCTS — Top-Level Product Definitions
## ATA 54-00-04 Design Assets

> **Purpose:** This folder contains the highest-level product definitions for ATA 54 Nacelles & Pylons. Products represent complete deliverable systems that are shipped to customers or integrated into the aircraft.

---

## 📂 Folder Structure

| Folder | Purpose | Count |
|--------|---------|-------|
| **NACELLE/** | Complete nacelle system products | 2 |
| **PYLON/** | Complete pylon assembly products | 2 |
| **INTEGRATION/** | Integration kits and interface hardware | 1 |
| **LRU/** | Line Replaceable Units | 2 |
| **TEMPLATES/** | Product definition templates | 1 |

---

## 📋 Product Register

### Nacelle Products

| Product ID | Title | Type | Mass (kg) | Lead Time | Status |
|------------|-------|------|-----------|-----------|--------|
| 54-00-04-PR001 | Left Nacelle System | Ship Set | 450 | 26 weeks | Draft |
| 54-00-04-PR002 | Right Nacelle System | Ship Set | 450 | 26 weeks | Draft |

**Description:** Complete nacelle systems including inlet structure, fan cowl, core cowl, exhaust nozzle, acoustic treatment, and thrust reverser integration points. Delivered fully assembled and tested.

**Key Features:**
- CFRP composite construction with titanium high-temperature sections
- Integrated acoustic treatment (≥15 dB reduction)
- Bird strike and lightning protection
- Fan cowl access doors for maintenance
- Design life: 90,000 FH / 60,000 FC

---

### Pylon Products

| Product ID | Title | Type | Mass (kg) | Lead Time | Status |
|------------|-------|------|-----------|-----------|--------|
| 54-00-04-PR003 | Left Pylon Assembly | Ship Set | 180 | 24 weeks | Draft |
| 54-00-04-PR004 | Right Pylon Assembly | Ship Set | 180 | 24 weeks | Draft |

**Description:** Complete pylon assemblies providing structural connection between wing and engine/nacelle. Includes primary load-carrying structure, wing attachment fittings, engine mount interfaces, and systems routing provisions.

**Key Features:**
- Primary load path for thrust, vertical, and gyroscopic loads
- CFRP pylon box with steel and titanium fittings
- Precision alignment for engine positioning (±0.2mm)
- Integrated systems routing for fuel, hydraulic, electrical
- Design life: 90,000 FH / 60,000 FC

---

### Integration Products

| Product ID | Title | Type | Mass (kg) | Lead Time | Status |
|------------|-------|------|-----------|-----------|--------|
| 54-00-04-PR005 | Nacelle-Pylon Integration Kit | Ship Set | 25 | 8 weeks | Draft |

**Description:** Complete hardware package enabling installation and integration of nacelle and pylon systems. Includes mounting hardware, interface seals, quick-disconnect fittings, and installation aids.

**Key Features:**
- Traceable aerospace-grade fasteners
- High-temperature seals and gaskets
- Quick-disconnect fittings for systems
- Installation time: 8 hours per integration
- Supports both left and right installations

---

### Line Replaceable Units (LRU)

| Product ID | Title | Type | Mass (kg) | Lead Time | Status |
|------------|-------|------|-----------|-----------|--------|
| 54-00-04-PR006 | Thrust Reverser System - Left | LRU | 120 | 22 weeks | Draft |
| 54-00-04-PR007 | Thrust Reverser System - Right | LRU | 120 | 22 weeks | Draft |

**Description:** Complete thrust reverser systems delivered as Line Replaceable Units. Includes reverser doors, hydraulic actuation, control electronics, and position sensors.

**Key Features:**
- Cascade-type thrust reverser with translating cowl
- Dual hydraulic actuators for redundancy
- Deployment time: ≤1.5 seconds
- Thrust reversal efficiency: ≥45%
- MTTR: 3.5 hours (line maintenance)
- Design life: 90,000 FH / 60,000 FC

---

## 📊 Statistics Summary

### Total Inventory
- **Total Products:** 7
- **Ship Sets:** 5
- **LRUs:** 2
- **Total Mass (complete aircraft set):** 1,525 kg
  - Nacelles: 900 kg (2×450 kg)
  - Pylons: 360 kg (2×180 kg)
  - Integration Kits: 25 kg (shared)
  - Thrust Reversers: 240 kg (2×120 kg)

### Lead Times
- **Shortest:** 8 weeks (Integration Kit)
- **Longest:** 26 weeks (Nacelle Systems)
- **Average:** 21.1 weeks

### Status Distribution
- **Draft:** 7 products
- **In Review:** 0 products
- **Approved:** 0 products
- **Released:** 0 products

---

## 🔄 Product Hierarchy

```
AMPEL360-AIR-T Aircraft
│
├── Left Propulsion System
│   ├── PR001: Left Nacelle System
│   │   ├── ASM-54-NAC-001: Primary Nacelle Structure
│   │   ├── ASM-54-TR-001: Thrust Reverser Assembly
│   │   └── ASM-54-COW-001: Fan Cowl Door Assembly
│   ├── PR003: Left Pylon Assembly
│   │   ├── ASM-54-PYL-001: Forward Pylon Structure
│   │   ├── ASM-54-PYL-002: Aft Pylon Structure
│   │   └── ASM-54-PYL-003: Systems Integration Assembly
│   ├── PR005: Integration Kit (shared)
│   └── PR006: Thrust Reverser System - Left (LRU)
│
└── Right Propulsion System
    ├── PR002: Right Nacelle System
    │   ├── ASM-54-NAC-001: Primary Nacelle Structure
    │   ├── ASM-54-TR-001: Thrust Reverser Assembly
    │   └── ASM-54-COW-001: Fan Cowl Door Assembly
    ├── PR004: Right Pylon Assembly
    │   ├── ASM-54-PYL-001: Forward Pylon Structure
    │   ├── ASM-54-PYL-002: Aft Pylon Structure
    │   └── ASM-54-PYL-003: Systems Integration Assembly
    ├── PR005: Integration Kit (shared)
    └── PR007: Thrust Reverser System - Right (LRU)
```

---

## 🔗 Product → Assembly Traceability Matrix

| Product ID | Child Assembly | Assembly ID | Quantity | Notes |
|------------|----------------|-------------|----------|-------|
| PR001 | Primary Nacelle Structure | ASM-54-NAC-001 | 1 | Main structural assembly |
| PR001 | Thrust Reverser Assembly | ASM-54-TR-001 | 1 | Integration points only |
| PR001 | Fan Cowl Door Assembly | ASM-54-COW-001 | 2 | Access doors |
| PR002 | Primary Nacelle Structure | ASM-54-NAC-001 | 1 | Main structural assembly |
| PR002 | Thrust Reverser Assembly | ASM-54-TR-001 | 1 | Integration points only |
| PR002 | Fan Cowl Door Assembly | ASM-54-COW-001 | 2 | Access doors |
| PR003 | Forward Pylon Structure | ASM-54-PYL-001 | 1 | Primary load path |
| PR003 | Aft Pylon Structure | ASM-54-PYL-002 | 1 | Fairing and structure |
| PR003 | Systems Integration Assembly | ASM-54-PYL-003 | 1 | Routing and brackets |
| PR004 | Forward Pylon Structure | ASM-54-PYL-001 | 1 | Primary load path |
| PR004 | Aft Pylon Structure | ASM-54-PYL-002 | 1 | Fairing and structure |
| PR004 | Systems Integration Assembly | ASM-54-PYL-003 | 1 | Routing and brackets |
| PR005 | Mounting Hardware Kit | 54-00-04-KIT-001 | 1 | Fasteners and hardware |
| PR005 | Interface Seals Kit | 54-00-04-KIT-002 | 1 | Seals and gaskets |
| PR005 | Systems Quick-Disconnect Kit | 54-00-04-KIT-003 | 1 | Quick-disconnect fittings |
| PR006 | Thrust Reverser Door Assembly | ASM-54-TR-001 | 2 | Cascade doors |
| PR006 | Hydraulic Actuation Assembly | ASM-54-TR-ACT-001 | 2 | Actuators and linkages |
| PR006 | Control and Sensor Assembly | ASM-54-TR-CTRL-001 | 1 | Electronics and sensors |
| PR007 | Thrust Reverser Door Assembly | ASM-54-TR-001 | 2 | Cascade doors |
| PR007 | Hydraulic Actuation Assembly | ASM-54-TR-ACT-001 | 2 | Actuators and linkages |
| PR007 | Control and Sensor Assembly | ASM-54-TR-CTRL-001 | 1 | Electronics and sensors |

---

## 📦 Delivery Summary

| Product ID | Delivery State | Packaging | Shelf Life | Documentation |
|------------|----------------|-----------|------------|---------------|
| PR001 | Fully Integrated | Custom shipping fixture | 24 months | CoC, Test records, AMM, IPC |
| PR002 | Fully Integrated | Custom shipping fixture | 24 months | CoC, Test records, AMM, IPC |
| PR003 | Fully Integrated | Custom shipping fixture | 36 months | CoC, Test records, AMM, IPC, ICDs |
| PR004 | Fully Integrated | Custom shipping fixture | 36 months | CoC, Test records, AMM, IPC, ICDs |
| PR005 | Kit Form | Modular kit boxes | 60 months | Contents list, Installation instructions |
| PR006 | Fully Integrated and Tested | Protective container | 48 months | CoC, Test records, AMM, IPC, Rigging |
| PR007 | Fully Integrated and Tested | Protective container | 48 months | CoC, Test records, AMM, IPC, Rigging |

**Legend:**
- CoC: Certificate of Conformity
- AMM: Aircraft Maintenance Manual extract
- IPC: Illustrated Parts Catalog extract
- ICD: Interface Control Document

---

## 🔍 Requirements Traceability

All products trace to requirements in:
- `../../54-00-03_Requirements/` (ATA 54 requirements)
- Related ATA chapter requirements (29, 30, 71, 76, 78)

Key requirement areas:
- Structural requirements (54-00-03-01-XXX)
- Thermal requirements (54-00-03-02-XXX)
- Aerodynamic requirements (54-00-03-03-XXX)
- Interface requirements (54-00-03-05-XXX)
- Actuation requirements (54-00-03-08-XXX)

---

## 🛠️ Manufacturing & Quality

### Manufacturing Status
- All products currently in preliminary design phase
- Final assembly locations: TBD
- Production rate target: 2-3 products per month

### Quality Control
- 100% inspection for all critical characteristics
- Acceptance test procedures defined for each product
- Quality plans established (54-00-08-QP-00X series)
- Conformity inspection procedures in place

---

## ✅ Certification Status

All products are being developed under:
- **Certification Basis:** CS-25 Amendment 27
- **Type Certificate:** EASA TC (pending)
- **Compliance Status:** In Progress

Key regulations:
- CS-25.571 (Damage tolerance)
- CS-25.581 (Lightning protection)
- CS-25.933 (Reversing systems - thrust reversers)
- CS-25.1309 (Equipment systems)

Individual certification plans: 54-00-10-CP-00X series

---

## 📁 Related Documents

### Design Documents
- Drawings in `../DRAWINGS/`
- Models in `../MODELS/`
- Assemblies in `../ASSEMBLIES/`

### Requirements
- Requirements in `../../54-00-03_Requirements/`

### Analysis
- Stress analysis models (54-00-04-M70X series)
- Thermal analysis (54-00-04-M71X series)
- Aerodynamic analysis (54-00-04-M72X series)

### Test & Verification
- Test reports in `../../54-00-07_V_AND_V/`

### Manufacturing
- Manufacturing plans in `../../54-00-09_Production_Planning/`

---

## 📝 Notes

### Product Development Philosophy
Products represent the highest level of the design hierarchy - complete systems ready for customer delivery. Each product is:
- **Self-contained:** Fully functional with all required components
- **Tested:** Undergoes acceptance testing before delivery
- **Documented:** Complete documentation package included
- **Traceable:** Full traceability to requirements and certification basis

### Naming Convention
Products follow the naming pattern:
```
54-00-04-PR<nnn>_PROD_<Descriptive_Name>.<ext>
```
Where:
- `54-00-04` = ATA reference for Design phase
- `PR<nnn>` = Product number (PR001, PR002, etc.)
- `PROD` = Category identifier for products
- `<Descriptive_Name>` = PascalCase description

### Maintenance Philosophy
- **Ship Sets:** Delivered as complete systems, maintained as assemblies
- **LRUs:** Designed for rapid removal/replacement at line maintenance level
- **Integration Kits:** Consumable/serviceable items for installation

### Symmetry
Left and right products (PR001/PR002, PR003/PR004, PR006/PR007) are symmetrical designs with mirrored geometry but separate part numbers for traceability and configuration management.

---

## 🔄 Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1.0 | 2026-01-02 | Product Engineering | Initial product definitions created |

---

## Document Control

- **Document ID:** 54-00-04-PROD-00-INDEX
- **Version:** 0.1.0
- **Status:** Draft
- **Owner:** Product Engineering
- **Last Updated:** 2026-01-02
- **Next Review:** 2026-03-01

---

*For questions or updates to product definitions, contact the ATA 54 Configuration Control Board.*

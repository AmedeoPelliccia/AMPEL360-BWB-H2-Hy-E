# BOM + LMP — Rotor Assembly (LRI-61-20-02-01)

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-02_01_BOM_LMP                    |
| **LRI ID**         | LRI-61-20-02-01                        |
| **Part Number**    | PN-DF-ROT-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Bill of Materials (BOM)

### 1.1 Major Components

| Item | Part Number     | Description                  | Material            | Qty | Unit Mass (kg) | Illustrated |
|------|-----------------|------------------------------|---------------------|-----|----------------|-------------|
| 1    | PN-DF-ROT-001   | Rotor Assembly (Complete)    | —                   | 1   | 85.0           | Y           |
| 1.1  | PN-DF-BLD-001   | Fan Blade                    | Ti-6Al-4V / CFRP    | 14  | 3.8            | Y           |
| 1.2  | PN-DF-HUB-001   | Rotor Hub                    | Ti-6Al-4V forging   | 1   | 28.0           | Y           |
| 1.3  | PN-DF-SPN-001   | Spinner Cone                 | Al-7075-T6          | 1   | 4.2            | Y           |
| 1.4  | PN-DF-LES-001   | Leading Edge Shield          | Titanium            | 14  | 0.15           | Y           |
| 1.5  | PN-DF-BAL-001   | Balance Weights              | Tungsten Alloy      | AR  | 0.05           | N           |

### 1.2 Fasteners and Hardware

| Item | Part Number     | Description                  | Specification       | Qty | Illustrated |
|------|-----------------|------------------------------|---------------------|-----|-------------|
| 2.1  | PN-DF-BLT-001   | Blade Retention Bolt         | NAS 6304            | 56  | N           |
| 2.2  | PN-DF-NUT-001   | Self-Locking Nut             | NAS 1291            | 56  | N           |
| 2.3  | PN-DF-WSH-001   | Blade Washer                 | AN 960              | 56  | N           |
| 2.4  | PN-DF-PIN-001   | Locating Dowel Pin           | NAS 561             | 28  | N           |

### 1.3 Consumables

| Item | Part Number     | Description                  | Specification       | Qty      | Maintenance Marking |
|------|-----------------|------------------------------|---------------------|----------|---------------------|
| 3.1  | PN-DF-LUB-001   | Blade Root Lubricant         | MIL-PRF-23827       | 0.5 L    | Y                   |
| 3.2  | PN-DF-SEA-001   | Hub Seal Compound            | MIL-S-8802          | 0.2 L    | Y                   |
| 3.3  | PN-DF-ADH-001   | Blade Bond Adhesive          | FM-300              | Per req. | N                   |

---

## 2. Lubrication and Maintenance Plan (LMP)

### 2.1 Lubrication Schedule

| Task ID       | Description                          | Lubricant           | Interval    | Marking Required |
|---------------|--------------------------------------|---------------------|-------------|------------------|
| LMP-ROT-001   | Blade Root Lubrication               | MIL-PRF-23827       | 2,500 FH    | Y                |
| LMP-ROT-002   | Hub Bearing Inspection / Re-grease   | MIL-PRF-81322       | 5,000 FH    | Y                |
| LMP-ROT-003   | Spinner Attachment Lubrication       | MIL-PRF-23827       | 2,500 FH    | N                |

### 2.2 Inspection Schedule

| Task ID       | Description                          | Method              | Interval    | Acceptance Criteria           |
|---------------|--------------------------------------|---------------------|-------------|-------------------------------|
| INS-ROT-001   | Visual Inspection (FOD, erosion)     | Visual / 10× mag    | Pre-flight  | No visible damage             |
| INS-ROT-002   | Blade Tip Clearance                  | Feeler gauge        | 1,000 FH    | 1.5 mm ± 0.3 mm               |
| INS-ROT-003   | Eddy Current (Leading Edge)          | EC probe            | 2,500 FH    | No cracks > 0.5 mm            |
| INS-ROT-004   | Ultrasonic (Blade Spar)              | UT A-scan           | 5,000 FH    | No delamination               |
| INS-ROT-005   | Borescope (Hub/Root Interface)       | Flexible borescope  | 2,500 FH    | No fretting > 0.2 mm depth    |

### 2.3 Replacement Criteria

| Component            | Life Limit (FH) | Life Limit (Cycles) | Condition-Based Trigger           |
|----------------------|-----------------|---------------------|-----------------------------------|
| Fan Blade            | 25,000          | 30,000              | Erosion depth > 0.5 mm            |
| Leading Edge Shield  | 12,500          | 15,000              | Erosion through > 20% area        |
| Hub Assembly         | 50,000          | 60,000              | Crack indication (any)            |
| Balance Weights      | On-condition    | —                   | Vibration > 0.5 IPS               |

---

## 3. Maintenance Procedures Reference

| Procedure ID   | Description                          | AMM Reference         |
|----------------|--------------------------------------|-----------------------|
| MP-61-20-02-01 | Rotor Assembly Removal / Installation| AMM 61-20-02-01       |
| MP-61-20-02-02 | Blade Replacement                    | AMM 61-20-02-02       |
| MP-61-20-02-03 | Rotor Balancing                      | AMM 61-20-02-03       |
| MP-61-20-02-04 | Leading Edge Shield Replacement      | AMM 61-20-02-04       |
| MP-61-20-02-05 | Hub Inspection / Overhaul            | AMM 61-20-02-05       |

---

## 4. Illustrated Parts Breakdown

See Central Illustration Repository:
- `61-90-20_02-01-FIG_001` — Rotor Assembly Exploded View
- `61-90-20_02-01-FIG_003` — Hub Assembly Detail
- `61-90-20_02-01-FIG_004` — Blade Root Attachment

---

## 5. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01

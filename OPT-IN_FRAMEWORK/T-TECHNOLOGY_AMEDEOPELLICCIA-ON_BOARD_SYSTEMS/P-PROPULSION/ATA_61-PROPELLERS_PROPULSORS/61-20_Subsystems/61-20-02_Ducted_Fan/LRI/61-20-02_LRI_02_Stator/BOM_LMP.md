# BOM + LMP — Stator Assembly (LRI-61-20-02-02)

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-02_02_BOM_LMP                    |
| **LRI ID**         | LRI-61-20-02-02                        |
| **Part Number**    | PN-DF-STA-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Bill of Materials (BOM)

### 1.1 Major Components

| Item | Part Number     | Description                  | Material            | Qty | Unit Mass (kg) | Illustrated |
|------|-----------------|------------------------------|---------------------|-----|----------------|-------------|
| 1    | PN-DF-STA-001   | Stator Assembly (Complete)   | —                   | 1   | 45.0           | Y           |
| 1.1  | PN-DF-VAN-001   | Stator Vane                  | CFRP (AS4/8552)     | 21  | 1.2            | Y           |
| 1.2  | PN-DF-HBR-001   | Hub Ring                     | Al-7050-T7451       | 1   | 8.5            | Y           |
| 1.3  | PN-DF-OTR-001   | Outer Ring                   | Al-7050-T7451       | 1   | 10.2           | Y           |
| 1.4  | PN-DF-LES-002   | Vane Leading Edge Strip      | Titanium            | 21  | 0.08           | Y           |
| 1.5  | PN-DF-TES-001   | Serrated Trailing Edge       | CFRP                | 21  | 0.05           | N           |

### 1.2 Fasteners and Hardware

| Item | Part Number     | Description                  | Specification       | Qty | Illustrated |
|------|-----------------|------------------------------|---------------------|-----|-------------|
| 2.1  | PN-DF-BLT-002   | Vane Attachment Bolt         | NAS 6303            | 84  | N           |
| 2.2  | PN-DF-NUT-002   | Self-Locking Nut             | NAS 1291            | 84  | N           |
| 2.3  | PN-DF-INS-001   | Nutplate Insert              | NAS 1832            | 84  | N           |
| 2.4  | PN-DF-SHM-001   | Shim Set (Assembly)          | Per drawing         | AR  | N           |

### 1.3 Consumables

| Item | Part Number     | Description                  | Specification       | Qty      | Maintenance Marking |
|------|-----------------|------------------------------|---------------------|----------|---------------------|
| 3.1  | PN-DF-SEA-002   | Ring Seal Compound           | MIL-S-8802          | 0.1 L    | N                   |
| 3.2  | PN-DF-ADH-002   | Vane Bond Adhesive           | FM-300              | Per req. | N                   |
| 3.3  | PN-DF-CLN-001   | Cleaning Solvent             | MIL-PRF-680         | Per req. | N                   |

---

## 2. Lubrication and Maintenance Plan (LMP)

### 2.1 Lubrication Schedule

| Task ID       | Description                          | Lubricant           | Interval    | Marking Required |
|---------------|--------------------------------------|---------------------|-------------|------------------|
| LMP-STA-001   | Ring Interface Lubrication           | MIL-PRF-23827       | 5,000 FH    | N                |

### 2.2 Inspection Schedule

| Task ID       | Description                          | Method              | Interval    | Acceptance Criteria           |
|---------------|--------------------------------------|---------------------|-------------|-------------------------------|
| INS-STA-001   | Visual Inspection (FOD, erosion)     | Visual / 10× mag    | Pre-flight  | No visible damage             |
| INS-STA-002   | Leading Edge Inspection              | Visual              | 500 FH      | No erosion > 0.3 mm           |
| INS-STA-003   | Ultrasonic (Vane Body)               | UT A-scan           | 5,000 FH    | No delamination               |
| INS-STA-004   | Ring Attachment Torque Check         | Torque wrench       | 2,500 FH    | Per specification             |
| INS-STA-005   | Borescope (Vane Root)                | Flexible borescope  | 5,000 FH    | No cracking                   |

### 2.3 Replacement Criteria

| Component            | Life Limit (FH) | Life Limit (Cycles) | Condition-Based Trigger           |
|----------------------|-----------------|---------------------|-----------------------------------|
| Stator Vane          | 50,000          | 60,000              | Delamination > 5 mm²              |
| Leading Edge Strip   | 25,000          | 30,000              | Erosion > 0.3 mm depth            |
| Hub Ring             | On-condition    | —                   | Crack indication (any)            |
| Outer Ring           | On-condition    | —                   | Crack indication (any)            |

---

## 3. Maintenance Procedures Reference

| Procedure ID   | Description                          | AMM Reference         |
|----------------|--------------------------------------|-----------------------|
| MP-61-20-02-10 | Stator Assembly Removal / Installation| AMM 61-20-02-10      |
| MP-61-20-02-11 | Vane Replacement                     | AMM 61-20-02-11       |
| MP-61-20-02-12 | Leading Edge Strip Replacement       | AMM 61-20-02-12       |
| MP-61-20-02-13 | Ring Inspection / Repair             | AMM 61-20-02-13       |

---

## 4. Illustrated Parts Breakdown

See Central Illustration Repository:
- `61-90-20_02-02-FIG_001` — Stator Assembly Exploded View
- `61-90-20_02-02-FIG_003` — Ring Assembly Detail
- `61-90-20_02-02-FIG_004` — Vane Attachment Detail

---

## 5. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01

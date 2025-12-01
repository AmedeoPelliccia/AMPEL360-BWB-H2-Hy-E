# BOM + LMP — Nacelle Duct Assembly (LRI-61-20-02-03)

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-02_03_BOM_LMP                    |
| **LRI ID**         | LRI-61-20-02-03                        |
| **Part Number**    | PN-DF-NAC-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Bill of Materials (BOM)

### 1.1 Major Components

| Item | Part Number     | Description                  | Material            | Qty | Unit Mass (kg) | Illustrated |
|------|-----------------|------------------------------|---------------------|-----|----------------|-------------|
| 1    | PN-DF-NAC-001   | Nacelle Duct Assembly        | —                   | 1   | 55.0           | Y           |
| 1.1  | PN-DF-INL-001   | Inlet Cowl                   | CFRP (T800/3900)    | 1   | 12.5           | Y           |
| 1.2  | PN-DF-FNC-001   | Fan Case                     | CFRP/Kevlar hybrid  | 1   | 18.0           | Y           |
| 1.3  | PN-DF-IMC-001   | Intermediate Case            | Ti-6Al-4V           | 1   | 14.5           | Y           |
| 1.4  | PN-DF-EXD-001   | Exhaust Duct                 | CFRP (AS4/8552)     | 1   | 8.0            | Y           |
| 1.5  | PN-DF-ACL-001   | Acoustic Liner (Inlet)       | Al honeycomb        | 1   | 1.2            | Y           |
| 1.6  | PN-DF-ACL-002   | Acoustic Liner (Exhaust)     | Al honeycomb        | 1   | 0.8            | Y           |

### 1.2 Fasteners and Hardware

| Item | Part Number     | Description                  | Specification       | Qty | Illustrated |
|------|-----------------|------------------------------|---------------------|-----|-------------|
| 2.1  | PN-DF-BLT-003   | Case Attachment Bolt         | NAS 6305            | 48  | N           |
| 2.2  | PN-DF-NUT-003   | Self-Locking Nut             | NAS 1291            | 48  | N           |
| 2.3  | PN-DF-FLG-001   | Flange Segment               | Ti-6Al-4V           | 8   | Y           |
| 2.4  | PN-DF-GSK-001   | Seal Gasket                  | Silicone            | 4   | N           |

### 1.3 Consumables

| Item | Part Number     | Description                  | Specification       | Qty      | Maintenance Marking |
|------|-----------------|------------------------------|---------------------|----------|---------------------|
| 3.1  | PN-DF-SEA-003   | Flange Sealant               | MIL-S-8802          | 0.5 L    | N                   |
| 3.2  | PN-DF-ADH-003   | Liner Bond Adhesive          | FM-300              | Per req. | N                   |
| 3.3  | PN-DF-CLN-002   | Composite Cleaning Solvent   | MIL-PRF-680         | Per req. | N                   |

---

## 2. Lubrication and Maintenance Plan (LMP)

### 2.1 Lubrication Schedule

| Task ID       | Description                          | Lubricant           | Interval    | Marking Required |
|---------------|--------------------------------------|---------------------|-------------|------------------|
| LMP-NAC-001   | Flange Interface Lubrication         | MIL-PRF-23827       | 5,000 FH    | N                |
| LMP-NAC-002   | Hinge/Access Panel Lubrication       | MIL-PRF-81322       | 2,500 FH    | N                |

### 2.2 Inspection Schedule

| Task ID       | Description                          | Method              | Interval    | Acceptance Criteria           |
|---------------|--------------------------------------|---------------------|-------------|-------------------------------|
| INS-NAC-001   | Visual Inspection (FOD, damage)      | Visual              | Pre-flight  | No visible damage             |
| INS-NAC-002   | Inlet Lip Inspection                 | Visual / 10× mag    | 500 FH      | No dents > 3 mm               |
| INS-NAC-003   | Fan Case Visual (Interior)           | Borescope           | 2,500 FH    | No rub marks > 0.5 mm         |
| INS-NAC-004   | Acoustic Liner Inspection            | Visual / Tap test   | 2,500 FH    | No disbond > 25 mm diameter   |
| INS-NAC-005   | Containment Case UT                  | Ultrasonic          | 10,000 FH   | No delamination               |

### 2.3 Replacement Criteria

| Component            | Life Limit (FH) | Life Limit (Cycles) | Condition-Based Trigger           |
|----------------------|-----------------|---------------------|-----------------------------------|
| Inlet Cowl           | On-condition    | —                   | Dent > 10 mm or crack             |
| Fan Case             | 100,000         | 120,000             | Any containment breach            |
| Intermediate Case    | 75,000          | 90,000              | Crack indication (any)            |
| Acoustic Liner       | 25,000          | 30,000              | Disbond > 100 mm² total           |

---

## 3. Maintenance Procedures Reference

| Procedure ID   | Description                          | AMM Reference         |
|----------------|--------------------------------------|-----------------------|
| MP-61-20-02-20 | Nacelle Assembly Removal / Install   | AMM 61-20-02-20       |
| MP-61-20-02-21 | Inlet Cowl Replacement               | AMM 61-20-02-21       |
| MP-61-20-02-22 | Fan Case Inspection                  | AMM 61-20-02-22       |
| MP-61-20-02-23 | Acoustic Liner Replacement           | AMM 61-20-02-23       |

---

## 4. Illustrated Parts Breakdown

See Central Illustration Repository:
- `61-90-20_02-03-FIG_001` — Nacelle Assembly Exploded View
- `61-90-20_02-03-FIG_002` — Inlet Cowl Detail
- `61-90-20_02-03-FIG_003` — Fan Case Cross-Section

---

## 5. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01

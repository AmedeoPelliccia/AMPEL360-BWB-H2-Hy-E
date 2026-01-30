# BOM + LMP — Rotor Assembly (LRI-61-20-01-02)

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_02_BOM_LMP                    |
| **LRI ID**         | LRI-61-20-01-02                        |
| **Part Number**    | PN-EM-ROT-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Bill of Materials (BOM)

### 1.1 Major Components

| Item | Part Number     | Description                  | Material              | Qty | Unit Mass (kg) | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|----------------|-------------|
| 1    | PN-EM-ROT-001   | Rotor Assembly (Complete)    | —                     | 1   | 125.0          | Y           |
| 1.1  | PN-EM-SHF-001   | Motor Shaft                  | 4340 Steel Q&T        | 1   | 42.0           | Y           |
| 1.2  | PN-EM-RCR-001   | Rotor Core Stack             | M19 Silicon Steel     | 1   | 48.0           | Y           |
| 1.3  | PN-EM-MAG-001   | Permanent Magnet Set         | NdFeB N48UH           | 24  | 1.4            | Y           |
| 1.4  | PN-EM-RET-001   | Magnet Retention Sleeve      | Carbon Fiber          | 1   | 1.2            | Y           |
| 1.5  | PN-EM-BAL-001   | Balance Weight Set           | Tungsten Alloy        | AR  | 0.05           | N           |
| 1.6  | PN-EM-KEY-001   | Shaft Key                    | 4340 Steel            | 2   | 0.15           | N           |

### 1.2 Hardware

| Item | Part Number     | Description                  | Specification         | Qty | Illustrated |
|------|-----------------|------------------------------|-----------------------|-----|-------------|
| 2.1  | PN-EM-RBT-001   | Rotor End Plate Bolt         | NAS 6304-8            | 12  | N           |
| 2.2  | PN-EM-EPL-001   | Rotor End Plate (DE)         | Al-7075-T6            | 1   | Y           |
| 2.3  | PN-EM-EPL-002   | Rotor End Plate (NDE)        | Al-7075-T6            | 1   | Y           |
| 2.4  | PN-EM-WSH-002   | Washer Set                   | AN 960                | 12  | N           |

### 1.3 Consumables

| Item | Part Number     | Description                  | Specification         | Qty      | Maintenance Marking |
|------|-----------------|------------------------------|-----------------------|----------|---------------------|
| 3.1  | PN-EM-ADH-002   | Magnet Bonding Adhesive      | FM-300                | 2.0 L    | N                   |
| 3.2  | PN-EM-LOC-001   | Thread Locking Compound      | Loctite 242           | 0.05 L   | N                   |
| 3.3  | PN-EM-COR-001   | Corrosion Inhibitor          | MIL-PRF-16173         | 0.5 L    | N                   |

---

## 2. Lubrication and Maintenance Plan (LMP)

### 2.1 Maintenance Schedule

| Task ID       | Description                          | Method                    | Interval    | Marking Required |
|---------------|--------------------------------------|---------------------------|-------------|------------------|
| LMP-ROT-001   | Rotor Visual Inspection              | Borescope (air gap)       | 2,500 FH    | Y                |
| LMP-ROT-002   | Vibration Signature Analysis         | Accelerometer             | 1,000 FH    | Y                |
| LMP-ROT-003   | Balance Check                        | In-situ balancing         | 5,000 FH    | Y                |
| LMP-ROT-004   | Magnetic Flux Check                  | Gaussmeter                | 10,000 FH   | Y                |
| LMP-ROT-005   | Shaft Runout Measurement             | Dial indicator            | 5,000 FH    | Y                |

### 2.2 Condition Monitoring Parameters

| Parameter                  | Normal Range      | Warning Threshold | Critical Threshold |
|----------------------------|-------------------|-------------------|---------------------|
| **Vibration (radial)**     | < 2.5 mm/s RMS    | > 4.0 mm/s        | > 6.0 mm/s          |
| **Vibration (axial)**      | < 1.5 mm/s RMS    | > 2.5 mm/s        | > 4.0 mm/s          |
| **Rotor Temperature**      | < 100°C           | > 120°C           | > 140°C             |
| **Shaft Runout**           | < 0.025 mm        | > 0.040 mm        | > 0.060 mm          |
| **Magnetic Flux**          | ±3% of nominal    | ±5% of nominal    | ±10% of nominal     |

### 2.3 Replacement Criteria

| Component            | Life Limit (FH) | Life Limit (Cycles) | Condition-Based Trigger           |
|----------------------|-----------------|---------------------|-----------------------------------|
| Rotor Assembly       | 50,000          | 60,000              | Vibration > 6 mm/s, flux loss > 10%|
| Permanent Magnets    | 50,000          | —                   | Flux loss > 5% (irreversible)     |
| Retention Sleeve     | 50,000          | —                   | Cracking, delamination            |
| Balance Weights      | On-condition    | —                   | Vibration > 4 mm/s                |
| Shaft                | 75,000          | 90,000              | Runout > 0.050 mm, fatigue crack  |

---

## 3. Maintenance Procedures Reference

| Procedure ID   | Description                          | AMM Reference         |
|----------------|--------------------------------------|-----------------------|
| MP-61-20-01-10 | Rotor Removal / Installation         | AMM 61-20-01-10       |
| MP-61-20-01-11 | Rotor Balancing (In-Situ)            | AMM 61-20-01-11       |
| MP-61-20-01-12 | Magnet Inspection                    | AMM 61-20-01-12       |
| MP-61-20-01-13 | Shaft Runout Check                   | AMM 61-20-01-13       |
| MP-61-20-01-14 | Rotor Complete Overhaul              | AMM 61-20-01-14       |

---

## 4. Illustrated Parts Breakdown

See Central Illustration Repository:
- `61-90-20_01-02-FIG_001` — Rotor Assembly Exploded View
- `61-90-20_01-02-FIG_002` — Shaft Detail
- `61-90-20_01-02-FIG_003` — Magnet Configuration (V-shaped)
- `61-90-20_01-02-FIG_004` — Retention Sleeve Detail

---

## 5. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01

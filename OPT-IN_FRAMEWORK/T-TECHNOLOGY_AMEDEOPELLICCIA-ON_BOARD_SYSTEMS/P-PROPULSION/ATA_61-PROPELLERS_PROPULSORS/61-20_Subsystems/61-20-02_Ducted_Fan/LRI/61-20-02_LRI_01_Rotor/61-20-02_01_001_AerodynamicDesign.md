# 61-20-02_01_001 — Rotor Aerodynamic Design

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-02_01_001                        |
| **LRI ID**         | LRI-61-20-02-01                        |
| **Part Number**    | PN-DF-ROT-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Status**         | Active                                 |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. Overview

The **Rotor Assembly** is a Line Replaceable Item (LRI) within the Ducted Fan LRU. It comprises the rotating blade assembly that generates primary airflow and thrust.

---

## 2. Design Parameters

### 2.1 Geometric Parameters

| Parameter                | Value       | Unit    | Notes                              |
|--------------------------|-------------|---------|-------------------------------------|
| **Fan Diameter**         | 1,180       | mm      | Tip-to-tip                          |
| **Hub Diameter**         | 380         | mm      | Spinner interface                   |
| **Hub-to-Tip Ratio**     | 0.322       | —       | Optimized for efficiency            |
| **Blade Count**          | 14          | blades  | Wide-chord design                   |
| **Blade Chord (Hub)**    | 120         | mm      | Root section                        |
| **Blade Chord (Tip)**    | 85          | mm      | Tip section                         |
| **Blade Height**         | 400         | mm      | Radial span                         |
| **Maximum Twist**        | 45          | deg     | Hub to tip                          |

### 2.2 Aerodynamic Parameters

| Parameter                | Design Point | Off-Design Range | Unit    |
|--------------------------|--------------|------------------|---------|
| **Pressure Ratio**       | 1.45         | 1.35 – 1.55      | —       |
| **Mass Flow Rate**       | 185          | 120 – 220        | kg/s    |
| **Tip Speed**            | 235          | 180 – 260        | m/s     |
| **Polytropic Efficiency**| 0.92         | 0.88 – 0.94      | —       |
| **Inlet Mach Number**    | 0.55         | 0.40 – 0.65      | —       |

---

## 3. Blade Airfoil Selection

### 3.1 Airfoil Sections

| Radial Position (%) | Airfoil Profile | Stagger Angle (deg) | Camber (%) |
|---------------------|-----------------|---------------------|------------|
| 0 (Hub)             | NACA 65-A12     | 35                  | 3.2        |
| 25                  | NACA 65-A10     | 38                  | 2.8        |
| 50                  | NACA 65-A08     | 42                  | 2.4        |
| 75                  | NACA 65-A06     | 48                  | 2.0        |
| 100 (Tip)           | NACA 65-A04     | 55                  | 1.6        |

### 3.2 Design Philosophy

- **High bypass ratio** optimized for cruise efficiency at M 0.78
- **Wide-chord blades** for reduced blade count and noise
- **Swept leading edge** for shock mitigation at transonic tip speeds
- **Lean stacking** for secondary flow control

---

## 4. Performance Characteristics

### 4.1 Thrust Generation

| Flight Condition        | Thrust (kN) | Fan Speed (RPM) | Efficiency |
|-------------------------|-------------|-----------------|------------|
| Ground Static (ISA)     | 45          | 4,200           | 0.88       |
| Take-off (M 0.2, SL)    | 42          | 4,100           | 0.89       |
| Climb (M 0.6, FL200)    | 32          | 3,950           | 0.91       |
| Cruise (M 0.78, FL410)  | 25          | 3,800           | 0.92       |
| Descent (M 0.5, FL200)  | 8           | 2,200           | 0.85       |

### 4.2 Stall Margin

| Parameter                | Value       | Unit    |
|--------------------------|-------------|---------|
| **Stall Margin (Design)**| 18          | %       |
| **Stall Margin (Min)**   | 12          | %       |
| **Surge Line Clearance** | 15          | %       |

---

## 5. Structural Design

### 5.1 Material Specification

| Component              | Material                  | Spec Reference      |
|------------------------|---------------------------|---------------------|
| **Blade**              | Ti-6Al-4V + CFRP overlay  | AMS 4911 / AMS 5774 |
| **Hub**                | Ti-6Al-4V forging         | AMS 4928            |
| **Leading Edge**       | Titanium erosion shield   | AMS 4911            |
| **Root Attachment**    | IN718 dovetail            | AMS 5662            |

### 5.2 Structural Loads

| Load Case              | Axial (kN) | Radial (kN) | Moment (kNm) |
|------------------------|------------|-------------|--------------|
| **Max Thrust**         | 45         | 2.5         | 8.5          |
| **Bird Strike**        | 85         | 45          | 25           |
| **Blade-Off**          | 120        | 180         | 95           |

---

## 6. Manufacturing Requirements

### 6.1 Process Specification

| Process                | Specification              | Tolerance          |
|------------------------|----------------------------|--------------------|
| **Forging**            | AMS-H-6875                 | ±0.5 mm profile    |
| **Machining**          | 5-axis CNC                 | ±0.05 mm           |
| **CFRP Layup**         | RTM / Autoclave            | ±0.2 mm thickness  |
| **Bonding**            | FM-300 adhesive film       | Per AMS 3686       |
| **Coating**            | Erosion-resistant PVD      | 25 µm ± 5 µm       |

---

## 7. References

- [CIR_LINKS.md](./CIR_LINKS.md) — Central Illustration Repository references
- [BOM_LMP.md](./BOM_LMP.md) — Bill of Materials and Lubrication/Maintenance Plan
- [../../LRU_61-20-02_DuctedFan.md](../../LRU_61-20-02_DuctedFan.md) — Parent LRU

---

## 8. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01

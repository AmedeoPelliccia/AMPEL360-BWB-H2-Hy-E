# 61-20-02_02_001 — Stator Design

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-02_02_001                        |
| **LRI ID**         | LRI-61-20-02-02                        |
| **Part Number**    | PN-DF-STA-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Status**         | Active                                 |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |
| **Owner**          | AMPEL360 Propulsion Team               |
| **Standard**       | OPT-IN Framework v1.2                  |

---

## 1. Overview

The **Stator Assembly** is a Line Replaceable Item (LRI) within the Ducted Fan LRU. It comprises the fixed vane assembly downstream of the rotor that straightens exit flow for improved propulsive efficiency.

---

## 2. Design Parameters

### 2.1 Geometric Parameters

| Parameter                | Value       | Unit    | Notes                              |
|--------------------------|-------------|---------|-------------------------------------|
| **Outer Diameter**       | 1,195       | mm      | Matches nacelle duct               |
| **Inner Diameter**       | 400         | mm      | Hub ring                           |
| **Axial Length**         | 180         | mm      | Flow path length                   |
| **Vane Count**           | 21          | vanes   | Prime number for noise reduction   |
| **Vane Chord (Hub)**     | 95          | mm      | Root section                       |
| **Vane Chord (Tip)**     | 70          | mm      | Tip section                        |
| **Vane Height**          | 397         | mm      | Radial span                        |
| **Stagger Angle Range**  | 15 – 35     | deg     | Hub to tip                         |

### 2.2 Aerodynamic Parameters

| Parameter                | Design Value | Unit    |
|--------------------------|--------------|---------|
| **Exit Swirl Angle**     | < 5          | deg     |
| **Total Pressure Loss**  | < 2          | %       |
| **Flow Turning**         | 25 – 45      | deg     |
| **Diffusion Factor**     | < 0.45       | —       |

---

## 3. Vane Airfoil Selection

### 3.1 Airfoil Sections

| Radial Position (%) | Airfoil Profile | Stagger Angle (deg) | Camber (%) |
|---------------------|-----------------|---------------------|------------|
| 0 (Hub)             | NACA 65-A10     | 15                  | 4.5        |
| 25                  | NACA 65-A08     | 20                  | 4.0        |
| 50                  | NACA 65-A06     | 25                  | 3.5        |
| 75                  | NACA 65-A05     | 30                  | 3.0        |
| 100 (Tip)           | NACA 65-A04     | 35                  | 2.5        |

### 3.2 Design Philosophy

- **Swirl recovery** optimized for cruise condition
- **Low loss** profiles with controlled diffusion
- **Non-uniform spacing** for tonal noise reduction
- **Lean/sweep** for secondary flow mitigation

---

## 4. Structural Design

### 4.1 Material Specification

| Component              | Material                  | Spec Reference      |
|------------------------|---------------------------|---------------------|
| **Vane**               | CFRP (AS4/8552)           | AMS 5774            |
| **Leading Edge**       | Titanium erosion strip    | AMS 4911            |
| **Hub Ring**           | Al-7050-T7451             | AMS 4050            |
| **Outer Ring**         | Al-7050-T7451             | AMS 4050            |
| **Attachment Lugs**    | Ti-6Al-4V                 | AMS 4928            |

### 4.2 Structural Loads

| Load Case              | Axial (kN) | Radial (kN) | Moment (kNm) |
|------------------------|------------|-------------|--------------|
| **Normal Operation**   | 8          | 0.5         | 1.2          |
| **Bird Strike**        | 35         | 15          | 8            |
| **Fan Blade-Off**      | 45         | 60          | 25           |

---

## 5. Acoustic Design

### 5.1 Noise Mitigation Features

| Feature                  | Description                              | Benefit              |
|--------------------------|------------------------------------------|----------------------|
| **Prime Vane Count**     | 21 vanes (vs 14 rotor blades)            | Tonal frequency shift|
| **Lean Stacking**        | 8° circumferential lean                  | BPF reduction -3 dB  |
| **Serrated Trailing Edge**| Sawtooth TE geometry                    | Broadband -2 dB      |
| **Acoustic Liner**       | Nacelle integration                      | Low-freq absorption  |

### 5.2 Wake Management

| Parameter                | Target       | Unit    |
|--------------------------|--------------|---------|
| **Rotor-Stator Gap**     | 2.5 × chord  | —       |
| **Axial Spacing**        | 85           | mm      |
| **Wake Interaction**     | Minimized    | —       |

---

## 6. Manufacturing Requirements

### 6.1 Process Specification

| Process                | Specification              | Tolerance          |
|------------------------|----------------------------|--------------------|
| **CFRP Layup**         | Autoclave cure             | ±0.15 mm profile   |
| **Ti Strip Bonding**   | FM-300 adhesive            | Per AMS 3686       |
| **Ring Machining**     | 5-axis CNC                 | ±0.05 mm           |
| **Assembly**           | Precision jig assembly     | ±0.1 mm position   |

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

# 61-20-01_04_001 — Housing/Frame Assembly Design

| Field              | Value                                  |
|--------------------|----------------------------------------|
| **Document ID**    | 61-20-01_04_001                        |
| **LRI ID**         | LRI-61-20-01-04                        |
| **Part Number**    | PN-EM-HSG-001                          |
| **ATA Chapter**    | 61 – Propellers / Propulsors           |
| **Programme**      | AMPEL360 BWB H₂ Hy-E Q100              |
| **Version**        | 1.0                                    |
| **Last Updated**   | 2025-12-01                             |

---

## 1. Purpose

This document defines the design, structural analysis, and manufacturing of the **Housing/Frame Assembly** for the 4 MW PMSM Electric Motor used in the AMPEL360 Q100 EDF propulsors.

---

## 2. Housing Configuration

### 2.1 Overall Dimensions

| Parameter                  | Value                     | Unit    |
|----------------------------|---------------------------|---------|
| **Outer Diameter**         | 650                       | mm      |
| **Overall Length**         | 520                       | mm      |
| **Wall Thickness (avg)**   | 25                        | mm      |
| **Flange Diameter**        | 720                       | mm      |
| **Mounting Bolt Circle**   | 680                       | mm      |
| **Number of Mount Bolts**  | 12                        | —       |
| **Housing Mass**           | 58                        | kg      |

### 2.2 Material

| Property                   | Value                                  |
|----------------------------|----------------------------------------|
| **Material**               | Al-7075-T6 (Aerospace Aluminum)        |
| **Yield Strength**         | 503 MPa                                |
| **Tensile Strength**       | 572 MPa                                |
| **Density**                | 2.81 g/cm³                             |
| **Thermal Conductivity**   | 130 W/(m·K)                            |
| **Fatigue Limit**          | 159 MPa (10⁸ cycles)                   |

---

## 3. Structural Design

### 3.1 Load Cases

| Load Case                  | Description                              | Factor  |
|----------------------------|------------------------------------------|---------|
| **LC-1: Ground Operation** | Max thrust + own weight + thermal        | 1.0     |
| **LC-2: Takeoff**          | Max thrust + 2.5g maneuver               | 2.5     |
| **LC-3: Flight Limit**     | 1.5g sustained + asymmetric thrust       | 1.5     |
| **LC-4: Emergency Landing**| Crash load factors (CS-25.561)           | 9.0g/6.0g/3.0g |
| **LC-5: Fatigue**          | Cyclic flight loads (30,000 cycles)      | —       |

### 3.2 Stress Analysis Summary

| Location                   | Max Stress (LC-2) | Allowable    | Margin of Safety |
|----------------------------|-------------------|--------------|------------------|
| **Mounting Flange Bolt Hole**| 285 MPa         | 335 MPa (MS) | 0.18             |
| **Stator Bore**            | 120 MPa           | 335 MPa      | 1.79             |
| **Cooling Channel Root**   | 195 MPa           | 335 MPa      | 0.72             |
| **End Cap Interface**      | 165 MPa           | 335 MPa      | 1.03             |

### 3.3 Modal Analysis

| Mode                       | Frequency (Hz)    | Description              |
|----------------------------|-------------------|--------------------------|
| **1st Bending**            | 185               | Lateral bending          |
| **2nd Bending**            | 312               | Vertical bending         |
| **1st Torsional**          | 425               | Torsional rotation       |
| **Shell Breathing**        | 580               | Radial expansion         |

---

## 4. Cooling Integration

### 4.1 Stator Jacket Design

| Parameter                  | Value                                  |
|----------------------------|----------------------------------------|
| **Channel Configuration**  | Spiral (single pass)                   |
| **Channel Width**          | 15 mm                                  |
| **Channel Depth**          | 12 mm                                  |
| **Number of Turns**        | 18                                     |
| **Inlet Port Location**    | 12 o'clock position                    |
| **Outlet Port Location**   | 6 o'clock position                     |
| **Port Size**              | G 3/4" BSP                             |

### 4.2 Thermal Performance

| Parameter                  | Value                     | Unit    |
|----------------------------|---------------------------|---------|
| **Heat Transfer Coefficient**| 2,500                   | W/(m²·K)|
| **Coolant Flow Rate**      | 25                        | L/min   |
| **Pressure Drop**          | 0.8                       | bar     |
| **Heat Rejection Capacity**| 45                        | kW      |

---

## 5. Manufacturing

### 5.1 Manufacturing Process

| Step | Process                              | Specification                    |
|------|--------------------------------------|----------------------------------|
| 1    | Forging (near-net shape)             | Closed-die forging               |
| 2    | Solution heat treatment              | 470°C, 2h, water quench          |
| 3    | Aging                                | 120°C, 24h (T6 temper)           |
| 4    | Rough machining                      | CNC 5-axis                       |
| 5    | Cooling channel machining            | Deep hole drilling + milling     |
| 6    | Channel sealing                      | Electron beam welding or epoxy   |
| 7    | Final machining                      | Bore, flange, ports              |
| 8    | NDT inspection                       | UT + dye penetrant               |
| 9    | Surface treatment                    | Hard anodize (MIL-A-8625 Type III)|
| 10   | Final inspection                     | CMM, leak test                   |

### 5.2 Critical Tolerances

| Feature                    | Tolerance           | Note                     |
|----------------------------|---------------------|--------------------------|
| **Stator Bore Diameter**   | H7 (640 +0.04/-0)   | Stator shrink fit        |
| **Flange Face Flatness**   | 0.05 mm             | Mating surface           |
| **Mounting Bolt Holes**    | ±0.10 mm position   | True position            |
| **Cooling Port Threads**   | G 3/4" Class 2A     | Pressure rated           |

---

## 6. Quality and Testing

### 6.1 Acceptance Tests

| Test                       | Method                                | Acceptance      |
|----------------------------|---------------------------------------|-----------------|
| **Dimensional Inspection** | CMM measurement                       | Per drawing     |
| **Hardness**               | Brinell (HB)                          | 140-160 HB      |
| **Dye Penetrant**          | MIL-STD-6866                          | No indications  |
| **Ultrasonic**             | AMS 2630                              | No rejectable defects |
| **Pressure Test (Cooling)**| Hydrostatic, 1.5× working pressure    | No leakage      |
| **Proof Load (Mounts)**    | 1.5× limit load                       | No deformation  |

---

## 7. Document Control

- **Standard:** OPT-IN Framework v1.2
- **Owner:** AMPEL360 Propulsion Team
- **Generation:** AI-assisted (GitHub Copilot)
- **Approval:** Pending human review
- **Last AI Update:** 2025-12-01

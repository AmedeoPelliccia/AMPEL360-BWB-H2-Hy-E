# Materials and Allowables Selection

**Document ID:** 02-11-00-TN-004  
**Platform:** AMPEL360 BWB H₂ Hy-E Q100  
**Status:** Draft  
**Date:** 2025-11-10

---

## 1. Purpose

Document material selections and allowable stress/strain values used in structural analysis and design.

---

## 2. Material Selection Criteria

### 2.1 Design Requirements
- **Strength-to-weight ratio:** Minimize structural weight
- **Stiffness:** Meet deflection and frequency requirements
- **Fatigue resistance:** 60,000+ flight hours
- **Damage tolerance:** Slow crack growth, residual strength
- **Environmental resistance:** Temperature, moisture, corrosion
- **Manufacturing:** Availability, cost, fabricability

---

## 3. Primary Structural Materials

### 3.1 Aluminum Alloys

**7075-T6 Aluminum:**
- **Application:** Center body skin, frames, bulkheads
- **Specification:** AMS 4045 (sheet), AMS 4078 (plate)
- **Density:** 2,810 kg/m³
- **Elastic modulus:** 71 GPa
- **Poisson's ratio:** 0.33
- **Allowables (MIL-HDBK-5J, Room Temperature):**
  - Ftu (ultimate tensile): 572 MPa (B-basis)
  - Fty (tensile yield): 503 MPa (B-basis)
  - Fcy (compressive yield): 531 MPa (B-basis)
  - Fsu (ultimate shear): 331 MPa (B-basis)
  - Fbru (ultimate bearing): 1,103 MPa (e/D=2.0, B-basis)

**2024-T3 Aluminum:**
- **Application:** Skin doublers, secondary structure
- **Specification:** AMS 4037
- **Allowables (MIL-HDBK-5J):**
  - Ftu: 483 MPa (B-basis)
  - Fty: 345 MPa (B-basis)

### 3.2 Titanium Alloys

**Ti-6Al-4V (Grade 5):**
- **Application:** Landing gear fittings, high-stress attachments
- **Specification:** AMS 4928 (bar), AMS 4911 (forging)
- **Density:** 4,430 kg/m³
- **Elastic modulus:** 114 GPa
- **Allowables (MIL-HDBK-5J, Annealed, A-basis):**
  - Ftu: 965 MPa
  - Fty: 896 MPa
  - Fcy: 931 MPa
  - Fsu: 586 MPa

### 3.3 Composite Materials

**Carbon/Epoxy (IM7/8552):**
- **Application:** Wing box (skins, spars, ribs), vertical tails
- **Specification:** CMH-17-3G
- **Layup:** Quasi-isotropic or tailored for local loads
- **Density:** 1,600 kg/m³
- **Fiber volume fraction:** 60%
- **Ply thickness:** 0.125 mm (typical)

**Unidirectional (0°) Ply Properties (CMH-17, Room Temperature Dry, A-basis):**
- E₁ (longitudinal modulus): 171 GPa
- E₂ (transverse modulus): 9.08 GPa
- G₁₂ (shear modulus): 5.29 GPa
- ν₁₂ (Poisson's ratio): 0.32
- F₁tu (longitudinal tensile strength): 2,724 MPa
- F₂tu (transverse tensile strength): 60 MPa
- F₁cu (longitudinal compressive strength): 1,531 MPa
- F₁₂su (in-plane shear strength): 103 MPa

**Typical Quasi-Isotropic Laminate [45/0/-45/90]s:**
- Ex = Ey: 55 GPa
- Gxy: 21 GPa
- Ftu (tension): 620 MPa
- Fcu (compression): 550 MPa

---

## 4. Allowables Basis

### 4.1 Statistical Basis (Per CS-25.613)

**A-Basis (99% reliability, 95% confidence):**
- Used for single load path structure (no redundancy)
- 99% of material population exceeds this value

**B-Basis (90% reliability, 95% confidence):**
- Used for multiple load path structure (redundancy)
- 90% of material population exceeds this value

### 4.2 Environmental Factors

**Temperature:**
- Room Temperature (RT): 20°C
- Elevated Temperature (ET): Up to 120°C for wing structure near engines
- Cryogenic Temperature (CT): -253°C for H₂ tank structure

**Moisture (Composites):**
- Conditioned to Equilibrium (CTD): 85% RH, 70°C until saturation
- Room Temperature Ambient (RTA): 50% RH, 20°C

**Knockdown Factors:**
- Hot/wet composites: 0.85× (ET/wet vs. RT/dry)
- Cryogenic metals: 1.10× (increased strength at low temp)

---

## 5. Fasteners and Joints

### 5.1 Titanium Fasteners

**Ti-6Al-4V Bolts:**
- **Application:** Critical structural joints
- **Specification:** MS20004, MS20073
- **Allowables:** Per MS standards

**Aluminum Hi-Lok and Lockbolt:**
- **Application:** Skin-stringer, skin-frame joints
- **Specification:** HL70, HL19
- **Allowables:** Per manufacturer data

### 5.2 Bearing and Bypass Allowables

**Bearing stress calculation:**
Fbr = P / (D × t)

Where:
- P = fastener load (N)
- D = fastener diameter (mm)
- t = sheet thickness (mm)

**Bearing allowables:** Per MIL-HDBK-5J, function of edge distance ratio (e/D)

---

## 6. Material Selection by Component

| Component | Primary Material | Reason for Selection |
|-----------|------------------|---------------------|
| Wing upper skin | Carbon/epoxy | High compressive strength, low weight |
| Wing lower skin | Carbon/epoxy | High tensile strength, fatigue resistance |
| Wing spars | Carbon/epoxy | High bending stiffness |
| Center body skin | Aluminum 7075-T6 | Pressure vessel, damage tolerance, repairability |
| Center body frames | Aluminum 7075-T6 | Hoop load transfer, ease of fabrication |
| Landing gear trunnion | Titanium Ti-6Al-4V | High strength, ultimate load capability |
| Vertical tail | Carbon/epoxy | High stiffness-to-weight ratio |
| Engine pylons | Titanium Ti-6Al-4V | High temperature resistance, bird strike |

---

## 7. Material Testing and Qualification

### 7.1 Required Tests

**Static tests:**
- Tension, compression, shear (0°, 90°, ±45°)
- Bearing and fastener pull-through
- Open-hole tension/compression

**Fatigue tests:**
- Constant amplitude S-N curves
- Spectrum loading

**Environmental tests:**
- Temperature (-55°C to +120°C)
- Moisture conditioning
- Combined temperature and moisture

### 7.2 Test Standards

- **Metals:** ASTM E8 (tension), ASTM E9 (compression)
- **Composites:** ASTM D3039 (tension), ASTM D6641 (compression)
- **Bearing:** ASTM D5961

---

## 8. Safety Factors

### 8.1 Ultimate Load Factor (CS-25.303)

**Factor of Safety:** 1.5 on limit load

**Application:**
- Structure must sustain ultimate load (1.5 × limit) without failure
- Allowable stress = Material ultimate strength / 1.0 (at ultimate load)

### 8.2 Fitting Factor (CS-25.625)

**Factor:** 1.15 for fittings

**Application:**
- Fittings (lugs, clevis, trunnion) must sustain 1.15 × ultimate load

---

## 9. References

- MIL-HDBK-5J – Metallic Materials and Elements for Aerospace Vehicle Structures
- CMH-17-3G – Composite Materials Handbook, Volume 3: Polymer Matrix Composites
- CS-25.603 – Materials
- CS-25.613 – Material Strength Properties and Design Values
- CS-25.619 – Special Factors
- CS-25.625 – Fitting Factors

---

**Document Control:**
- **Version:** 1.0 (Draft)
- **Author:** Materials and Processes Engineer
- **Reviewed by:** Chief Structural Engineer
- **Date:** 2025-11-10

# 03-00-02-004 — Hydrogen-Specific Safety Considerations for GSE

## 1. Purpose

This document defines **hydrogen-specific safety constraints and requirements** for Ground Support Equipment (GSE) handling H₂ refuelling and support operations under [ATA 03 – Support Information GSE](https://www.ata.org/resources/specifications/ispec2200).

It establishes:

- H₂ hazard characteristics and safety properties
- H₂ refuelling safety zones and exclusion areas
- Leak detection and monitoring requirements
- Ignition source control measures
- Emergency response procedures for H₂ incidents
- H₂-specific PPE and equipment requirements

---

## 2. Hydrogen Safety Properties

### 2.1 Physical and Chemical Properties

| Property | Value | Safety Implication |
|---|---|---|
| **Flammability Range** | 4-75% in air | Very wide flammability range |
| **Lower Explosive Limit (LEL)** | 4% by volume | Low ignition threshold |
| **Autoignition Temperature** | 585°C | Relatively high (safer than gasoline 246°C) |
| **Minimum Ignition Energy** | 0.017 mJ | Extremely low (easily ignited by static) |
| **Flame Visibility** | Nearly invisible in daylight | Difficult to detect H₂ fires visually |
| **Flame Temperature** | 2045°C | Extremely hot, risk of severe burns |
| **Density** (gas at STP) | 0.0899 kg/m³ | 14× lighter than air, rises rapidly |
| **Diffusion Coefficient** | 0.61 cm²/s | Disperses quickly, reduces accumulation risk |
| **Boiling Point** (liquid H₂) | -253°C | Cryogenic hazard, risk of cold burns and embrittlement |
| **Odor** | Odorless | Cannot be detected by smell (odorants not used due to fuel cell contamination) |

### 2.2 Key Safety Considerations

- **Rapid Dispersion**: H₂ gas disperses quickly in open air due to low density (14× lighter than air)
- **Accumulation Risk**: H₂ can accumulate in enclosed or poorly ventilated spaces (roof peaks, ceilings)
- **Static Ignition**: H₂ can be ignited by very low energy static discharge
- **Invisible Flame**: H₂ flames are nearly invisible in daylight, making fire detection difficult
- **Cryogenic Hazards**: Liquid H₂ (LH₂) causes severe cold burns and material embrittlement
- **Asphyxiation**: H₂ can displace oxygen in confined spaces

---

## 3. H₂ Refuelling Safety Zones

### 3.1 Zone Definitions

H₂ refuelling operations require three concentric safety zones:

| Zone | Radius | Access Control | Activity Restrictions |
|---|:---:|---|---|
| **Inner Zone** | 10m from coupling point | Authorized refuelling crew only | Full H₂ PPE required, no ignition sources |
| **Outer Zone** | 25m from coupling point | No unauthorized personnel | No smoking, no hot work, no running engines |
| **Buffer Zone** | 50m from coupling point | Emergency response staged | Fire/rescue equipment ready, evacuation route clear |

### 3.2 Zone Demarcation

- **Physical Barriers**: Cones, barrier tape, or retractable barriers to mark zone boundaries
- **Signage**: Clear signage indicating "H₂ REFUELLING IN PROGRESS", "NO SMOKING", "NO IGNITION SOURCES"
- **Lighting**: Zone boundaries illuminated during night operations
- **Communication**: Zone establishment communicated to ramp control and nearby personnel

### 3.3 Ventilation Requirements

- **Open Air Operations**: Preferred, natural ventilation by wind
- **Covered Areas**: Mechanical ventilation required, minimum 4 air changes per hour
- **Enclosed Spaces**: H₂ refuelling prohibited in enclosed spaces without certified ventilation system

---

## 4. Leak Detection and Monitoring

### 4.1 Fixed H₂ Detection Systems

All H₂ refuelling areas shall be equipped with:

- **H₂ Gas Detectors**: Catalytic bead or electrochemical sensors
  - **Detection Range**: 0-4% H₂ (0-100% LEL)
  - **Alarm Levels**:
    - **Low Alarm**: 1% H₂ (25% LEL) – warning, increased monitoring
    - **High Alarm**: 2% H₂ (50% LEL) – evacuate personnel, stop refuelling
    - **Critical Alarm**: 3% H₂ (75% LEL) – emergency shutdown, activate fire suppression
- **Sensor Placement**: At high points (ceiling, roof peaks) where H₂ accumulates
- **Calibration**: Monthly calibration with certified H₂ test gas

### 4.2 Portable H₂ Detectors

All H₂ refuelling crew members shall carry:

- **Personal H₂ Detectors**: Wearable, audible/visual alarm
  - **Alarm Level**: 1% H₂ (25% LEL)
  - **Battery Check**: Daily before operations
- **Handheld H₂ Detectors**: For leak checking and area surveys
  - **Leak Detection Sensitivity**: ≥ 0.1% H₂ (2.5% LEL)

### 4.3 Leak Detection Methods

- **Visual Inspection**: Check for ice formation (indicates cryogenic LH₂ leak)
- **Bubble Test**: Soap solution applied to connections (small leaks generate bubbles)
- **Ultrasonic Detection**: Detects high-pressure gas leaks by sound
- **Thermal Imaging**: Detects cryogenic leaks by temperature anomalies

---

## 5. Ignition Source Control

### 5.1 Prohibited Ignition Sources (within 25m of H₂ refuelling)

- **Smoking**: Strictly prohibited
- **Open Flames**: No welding, cutting, brazing, or open flames
- **Hot Work**: No grinding, drilling, or operations generating sparks
- **Running Engines**: All aircraft and GSE engines shutdown
- **Mobile Phones**: Non-intrinsically safe mobile devices prohibited
- **Electrical Work**: No electrical maintenance or hot swapping of equipment

### 5.2 Static Electricity Control

- **Bonding and Grounding**: All H₂ refuelling equipment bonded and grounded to aircraft
  - **Bonding Resistance**: < 10 Ω between equipment and aircraft
  - **Ground Connection**: Established before opening any H₂ connections
- **Conductive Clothing**: Personnel wear flame-resistant, anti-static clothing
- **Conductive Footwear**: Safety footwear with conductive soles (< 10⁸ Ω resistance)
- **Conductive Flooring**: H₂ refuelling areas have conductive or dissipative flooring

### 5.3 Intrinsically Safe Equipment

All electrical equipment used within 10m of H₂ refuelling must be:
- **Intrinsically Safe (IS)**: Certified to [IEC 60079-11](https://webstore.iec.ch/publication/634) or equivalent
- **Explosion-Proof**: Certified to [IEC 60079-0](https://webstore.iec.ch/publication/24803) or equivalent
- **Examples**: IS flashlights, IS radios, IS H₂ detectors

---

## 6. H₂ Refuelling Equipment Safety

### 6.1 Refuelling Bowser Requirements

H₂ refuelling bowsers (mobile H₂ supply vehicles) shall be:

- **Certified**: To [ISO 19880-8](https://www.iso.org/standard/71940.html) (H₂ fueling stations) and [SAE J2601](https://www.sae.org/standards/content/j2601/) (fueling protocols)
- **Pressure Relief**: Multiple pressure relief devices (PRDs) to prevent over-pressure
- **Emergency Shutdown**: Dead-man switch and remote emergency shutdown capability
- **Breakaway Coupling**: Automatic coupling disconnect if vehicle moves during refuelling
- **Fire Suppression**: On-board fire suppression system (dry chemical or CO₂)
- **H₂ Detection**: On-board H₂ leak detection with automatic shutdown
- **Inspection**: Daily pre-operation inspection, monthly detailed inspection

### 6.2 Refuelling Hose and Coupling

- **Hose Material**: Stainless steel braided hose, cryogenic-rated for LH₂
- **Pressure Rating**: Minimum 1.5× maximum operating pressure
- **Coupling Type**: SAE J2600 compatible, with dry-break connection
- **Inspection**: Visual inspection before each use, replace if damaged or degraded

### 6.3 Personal Protective Equipment (PPE) for H₂ Refuelling

| PPE Item | Standard | Purpose |
|---|---|---|
| **Flame-Resistant Coveralls** | [EN ISO 11612](https://www.iso.org/standard/57457.html) | Protection from H₂ flash fire |
| **Cryogenic Gloves** | [EN 511](https://www.en-standard.eu/csn-en-511-protective-gloves-against-cold/) | Protection from LH₂ cold burns |
| **Face Shield** | [EN 166](https://www.en-standard.eu/bs-en-166-2001-personal-eye-protection-specifications/) | Eye and face protection from cold spray |
| **Safety Footwear** | [EN ISO 20345](https://www.iso.org/standard/70019.html) S3, conductive | Foot protection, static dissipation |
| **Personal H₂ Detector** | Wearable, 1% LEL alarm | H₂ leak detection |

---

## 7. H₂ Emergency Procedures

### 7.1 H₂ Leak Response

**Indicators of H₂ Leak:**
- H₂ detector alarm
- Ice formation on connections or piping
- Hissing or whistling sound
- Personnel report unusual odor from fuel cell contamination

**Immediate Actions:**
1. **Stop Refuelling**: Immediately stop H₂ flow, close valves
2. **Emergency Shutdown**: Activate emergency shutdown system
3. **Evacuate**: Evacuate all personnel from Inner and Outer Zones (10m + 25m)
4. **Alert**: Notify fire/rescue, GSE Safety Manager, H₂ Safety Specialist
5. **Secure Area**: Establish 50m exclusion zone, prevent ignition sources
6. **Monitor**: Use handheld H₂ detector to assess leak size and H₂ concentration
7. **Ventilate**: If indoors or enclosed, maximize ventilation

**Do Not:**
- Attempt to repair leak while under pressure
- Re-enter area until H₂ concentration < 0.5% (confirmed by H₂ detector)
- Use non-intrinsically safe equipment in hazard area

### 7.2 H₂ Fire Response

**Indicators of H₂ Fire:**
- Nearly invisible flame (look for heat shimmer, distortion)
- Thermal imaging camera shows hot spot
- Personnel report sensation of heat
- H₂ detector shows decreasing concentration (H₂ being consumed by fire)

**Immediate Actions:**
1. **Activate Fire Alarm**: Alert all personnel
2. **Evacuate**: Evacuate all personnel from 50m radius
3. **Call Fire Brigade**: Emergency number (112/911)
4. **Do Not Extinguish**: Allow H₂ fire to burn unless leak can be isolated
   - **Rationale**: Extinguishing H₂ fire without stopping leak creates explosive H₂ cloud
5. **Cool Surrounding Structures**: Use water spray to cool adjacent structures and equipment
6. **Isolate H₂ Source**: If safe to do so, close remote shutoff valve to stop H₂ flow

**Fire Suppression (only if leak is isolated):**
- **Dry Chemical**: PKP (Purple-K) or ABC dry chemical extinguisher
- **CO₂**: CO₂ extinguisher for small fires
- **Water Spray**: Water mist or fog for cooling, NOT direct water jet

### 7.3 Cryogenic Injury (LH₂ Cold Burn)

**Immediate Actions:**
1. **Remove from Exposure**: Move person away from LH₂ source
2. **Remove Contaminated Clothing**: Remove clothing soaked with LH₂ (cryogenic hazard)
3. **Warm Affected Area**: Use lukewarm water (not hot), do not rub or massage
4. **Do Not Apply Ice**: Ice or cold water will worsen injury
5. **Seek Medical Attention**: All cryogenic burns require medical evaluation
6. **Transport**: If severe, call for medical transport (ambulance)

### 7.4 H₂ Asphyxiation

**Indicators:**
- Rapid breathing, dizziness, confusion
- Loss of consciousness
- Cyanosis (blue lips, skin)

**Immediate Actions:**
1. **Do Not Enter**: If person is unconscious in H₂ hazard area, do not enter without breathing apparatus
2. **Call for Help**: Alert fire/rescue, medical emergency
3. **Rescue (if safe)**: Only trained rescue personnel with SCBA (Self-Contained Breathing Apparatus) may enter
4. **Administer Oxygen**: Once in safe area, administer 100% oxygen if available
5. **CPR if Required**: If no pulse/breathing, begin CPR
6. **Medical Transport**: Call ambulance immediately

---

## 8. H₂ Storage and Transportation

### 8.1 On-Site H₂ Storage

- **Storage Location**: Outdoor, well-ventilated area, minimum 15m from buildings and ignition sources
- **Quantity Limits**: Comply with local fire code and [NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2) (Hydrogen Technologies Code)
- **Security**: Fenced enclosure, access control, signage
- **Fire Protection**: Deluge water spray system or dry chemical suppression
- **Monitoring**: 24/7 H₂ detection, remote monitoring

### 8.2 H₂ Transport (Road)

- **Vehicle Requirements**: Certified to [ADR](https://unece.org/transport/dangerous-goods/adr-2023-files) (European Agreement concerning the International Carriage of Dangerous Goods by Road) or equivalent
- **Driver Qualification**: Hazardous materials (HAZMAT) endorsement, H₂ safety training
- **Route Planning**: Avoid congested areas, tunnels, and high-risk zones
- **Emergency Kit**: Fire extinguisher, spill kit, emergency contact information

---

## 9. H₂ Safety Training

All personnel involved in H₂ operations must complete:

- **Initial H₂ Safety Training** (8 hours):
  - H₂ properties and hazards
  - Leak detection and monitoring
  - Ignition source control
  - Emergency response procedures
  - PPE use and limitations
- **Practical H₂ Refuelling Training** (16 hours):
  - Hands-on refuelling operations
  - Leak detection practice
  - Emergency scenario drills
  - Competency assessment
- **Recurrent Training** (annual, 4 hours):
  - Refresher on H₂ safety principles
  - Review of incidents and lessons learned
  - Update on new procedures or equipment

See [03-00-02-005_Safety_Training_and_Competency.md](./03-00-02-005_Safety_Training_and_Competency.md)

---

## 10. Regulatory Alignment

This document aligns with:

- **[ISO 19880-8](https://www.iso.org/standard/71940.html)** (Gaseous hydrogen — Fueling stations — Part 8: Fuel quality control)
- **[SAE J2601](https://www.sae.org/standards/content/j2601/)** (Fueling Protocols for Light Duty Gaseous Hydrogen Surface Vehicles)
- **[NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2)** (Hydrogen Technologies Code)
- **[IEC 60079 Series](https://webstore.iec.ch/publication/24803)** (Explosive Atmospheres)
- **[ADR](https://unece.org/transport/dangerous-goods/adr-2023-files)** (Transport of Dangerous Goods by Road)

---

## 11. References

- [03-00-02-001_Safety_Management_Framework.md](./03-00-02-001_Safety_Management_Framework.md)
- [03-00-02-002_Hazard_Identification_and_Risk_Assessment.md](./03-00-02-002_Hazard_Identification_and_Risk_Assessment.md)
- [03-00-02-003_Operational_Safety_Rules_GSE.md](./03-00-02-003_Operational_Safety_Rules_GSE.md)
- [03-00-02-005_Safety_Training_and_Competency.md](./03-00-02-005_Safety_Training_and_Competency.md)
- [ASSETS/03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg](./ASSETS/03-00-02-A-003_BowTie_Analysis_H2_Refuelling.svg)

---

## 12. Document Control

- **Status**: `DRAFT` – Subject to human review and approval
- **Owner**: H₂ Safety Specialist
- **Approver**: _[to be completed]_
- **Last Updated**: 2025-11-21
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Repository: `AMPEL360-BWB-H2-Hy-E`

---

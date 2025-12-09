---
Title: "Cryogenic Operations Standards"
Identifier: "AMPEL360-03-00-14-02-02A"
Version: "1.0.0"
Status: "Draft"
AccessLevel: "Internal"
Author: "AMPEL360 Cryogenic Operations Team"
ResponsibleOrg: "I-INFRASTRUCTURES Cryogenic GSE Authority"
Language: "en"
CreatedAt: "2025-12-07"
ModifiedAt: "2025-12-07"
Abstract: "Operational standards for cryogenic liquid hydrogen handling at -253°C."
Keywords: ["ATA 03","GSE","Cryogenic","LH2","Hydrogen","Cold","Operations","Standards"]
Compliance:
  - "ISO 13985"
  - "ISO 21013"
  - "NFPA 2"
  - "ATA iSpec 2200"
  - "AMPEL360 Documentation Standard v1.1"
Links:
  ParentGeneral: "../../"
  Siblings:
    - "./03-00-14-02-01A_LH2_Fueling_Ops_Standards.md"
    - "./03-00-14-02-03A_H2_Safety_Ops_Standards.md"
    - "./03-00-14-02-04A_H2_Emergency_Ops_Standards.md"
ChangeLog:
  - { version: "1.0.0", date: "2025-12-07", author: "AMPEL360 Cryogenic Team", change: "Initial release" }
---

# 03-00-14-02-02A — Cryogenic Operations Standards

## 1. Purpose

This document establishes **operational standards for cryogenic liquid hydrogen (LH₂) handling** at -253°C (-423°F) for AMPEL360 aircraft ground operations. It defines cryogenic safety requirements, material compatibility, thermal management, and operational procedures for ultra-low temperature LH₂ handling.

## 2. Scope

### 2.1 Coverage

Cryogenic operations standards for:

1. **Cryogenic Equipment Operations**
   - LH₂ storage and transfer equipment
   - Cryogenic piping and hoses
   - Cryogenic valves and fittings
   - Vacuum-insulated components

2. **Personnel Protection**
   - Cryogenic personal protective equipment (PPE)
   - Cold burn prevention
   - Frostbite protection
   - Emergency response for cryogenic exposure

3. **Material Considerations**
   - Material compatibility at cryogenic temperatures
   - Thermal contraction management
   - Embrittlement prevention
   - Insulation requirements

4. **Thermal Management**
   - Cooldown procedures
   - Boil-off management
   - Ice formation prevention
   - Thermal stress control

## 3. Applicable Documents

### 3.1 Cryogenic Standards

| Standard | Title | Application |
|----------|-------|-------------|
| **[ISO 13985:2020](https://www.iso.org/standard/63534.html)** | Liquid Hydrogen — Land Vehicle Fuel Tanks | LH₂ handling |
| **[ISO 21013](https://www.iso.org/standard/71555.html)** | Cryogenic Vessels | Equipment design and operation |
| **[NFPA 2](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=2)** | Hydrogen Technologies Code | Cryogenic H₂ safety |
| **[CGA P-12](https://www.cganet.com/)** | Safe Handling of Cryogenic Liquids | Handling procedures |

### 3.2 Internal References

- [03-00-14-02-01A_LH2_Fueling_Ops_Standards.md](./03-00-14-02-01A_LH2_Fueling_Ops_Standards.md)
- [03-00-14-02-03A_H2_Safety_Ops_Standards.md](./03-00-14-02-03A_H2_Safety_Ops_Standards.md)

## 4. Operations/Sustainment Requirements

### 4.1 Cryogenic Hazards Overview

| Hazard | Description | Risk Level | Primary Controls |
|--------|-------------|------------|------------------|
| **Cold Burns/Frostbite** | Skin contact with LH₂ or cold surfaces | Critical | Cryogenic PPE, no skin exposure |
| **Embrittlement** | Material failure due to extreme cold | High | Use qualified materials only |
| **Asphyxiation** | H₂ vaporization displacing oxygen | High | Ventilation, O₂ monitoring |
| **Thermal Shock** | Rapid temperature changes causing failure | High | Controlled cooldown procedures |
| **Ice Formation** | Atmospheric moisture freezing | Medium | Dry environment, insulation |
| **Oxygen Enrichment** | Liquid air condensation on cold surfaces | Medium | Regular inspection, defrosting |

### 4.2 Cryogenic Personal Protective Equipment (PPE)

#### 4.2.1 Mandatory Cryogenic PPE

| PPE Item | Specification | Replacement Criteria |
|----------|---------------|---------------------|
| **Cryogenic Gloves** | Rated to -260°C minimum, 5-finger articulation | Damage, stiffness, or annually |
| **Face Shield** | Full-face, anti-fog, impact-resistant | Scratches or damage |
| **Insulated Coveralls** | Multi-layer, loose-fitting, non-absorbent | Tears, stains, or annually |
| **Safety Boots** | Steel toe, non-porous, slip-resistant | Sole wear or damage |
| **Safety Goggles** | Indirect venting, anti-fog | Scratches or quarterly |
| **Apron (optional)** | Cryogenic-rated, used for spill response | Damage or stiffness |

#### 4.2.2 PPE Donning Procedure

**Proper Sequence:**
1. Inspect all PPE before use (no damage, proper ratings)
2. Don insulated coveralls (loose fit to trap air)
3. Don safety boots (ensure pants cover boot tops)
4. Don safety goggles or face shield
5. Don cryogenic gloves (ensure cuff over coverall sleeve)
6. Buddy check before approaching cryogenic equipment

**Critical Don'ts:**
- Never tuck gloves inside sleeves (liquid can run down)
- Never wear absorbent materials (cotton, wool) as base layer
- Never wear jewelry or watches (conducts cold)
- Never wear laced shoes (liquid can enter)

### 4.3 Material Compatibility at Cryogenic Temperatures

#### 4.3.1 Approved Materials for LH₂ Service

| Material | Application | Temperature Range | Notes |
|----------|-------------|-------------------|-------|
| **Stainless Steel 304/316** | Piping, tanks, fittings | -270°C to +500°C | Excellent cryogenic properties |
| **Aluminum 5083/6061** | Tanks, structures | -270°C to +200°C | Good strength retention |
| **Inconel 718** | High-stress components | -270°C to +700°C | Superior low-temp performance |
| **PTFE (Teflon)** | Seals, gaskets | -270°C to +260°C | Flexible at cryogenic temps |
| **G-10 Fiberglass** | Electrical insulation | -270°C to +180°C | Low thermal conductivity |
| **Perlite** | Vacuum insulation | -270°C to +200°C | Excellent insulator |

#### 4.3.2 Prohibited Materials

| Material | Reason for Prohibition |
|----------|------------------------|
| **Carbon Steel** | Brittle failure at LH₂ temperatures |
| **Cast Iron** | Embrittlement and cracking |
| **PVC Plastics** | Becomes brittle and shatters |
| **Natural Rubber** | Loses elasticity, hardens |
| **Nylon** | Becomes brittle |
| **Most Elastomers** | Lose sealing properties (except PTFE) |

### 4.4 Thermal Management Standards

#### 4.4.1 Equipment Cooldown Procedures

**Gradual Cooldown Protocol:**

| Cooldown Phase | Temperature Range | Cooling Rate | Duration | Actions |
|----------------|-------------------|--------------|----------|---------|
| **Phase 1** | Ambient to 0°C | 50°C/hour max | 0.5-1 hour | Introduce cold GH₂ or GN₂ |
| **Phase 2** | 0°C to -100°C | 30°C/hour max | 3-4 hours | Monitor for ice, increase flow |
| **Phase 3** | -100°C to -200°C | 20°C/hour max | 5-6 hours | Slow introduction of LH₂ vapor |
| **Phase 4** | -200°C to -253°C | 10°C/hour max | 5-6 hours | Final cooldown with LH₂ |

**Total Cooldown Time**: 15-20 hours for initial system cooldown

**Rapid Cooldown Risks:**
- Thermal shock causing cracks or leaks
- Excessive thermal contraction causing joint failure
- Localized cold spots and stress concentrations
- Dangerous boil-off rates

**Cooldown Monitoring:**
- Temperature sensors at multiple locations (minimum 4)
- Pressure monitoring (watch for pressure spikes)
- Visual inspection for ice, frost patterns
- Acoustic monitoring for cracking sounds

#### 4.4.2 Boil-Off Management

**LH₂ Boil-Off Characteristics:**

| Scenario | Typical Boil-Off Rate | Acceptability |
|----------|----------------------|---------------|
| **Well-Insulated Storage** | 0.3-1.0% per day | Acceptable |
| **Transfer Operations** | 1-2% of transfer volume | Acceptable |
| **Poorly Insulated Equipment** | >3% per day | Unacceptable — repair required |
| **First Fill (warm tank)** | 5-10% initial | Expected, decreases with cooldown |

**Boil-Off Gas Management:**
- Vent system designed for safe dispersion
- Vent height minimum 7 meters above ground
- Vent directed away from personnel, equipment, and ignition sources
- Continuous monitoring of vent flow rate
- H₂ detectors positioned around vent outlets

#### 4.4.3 Ice and Frost Management

**Ice Formation Causes:**
- Atmospheric moisture condensing on cold surfaces
- Air leaks into vacuum-insulated spaces
- Poor or damaged insulation

**Ice Prevention:**
- Use of vapor barriers on insulation
- Regular inspection of insulation integrity
- Dehumidification of enclosed spaces
- Proper sealing of vacuum insulation

**Ice Removal:**
- Allow natural warming in well-ventilated area
- Never use heat sources (thermal shock risk)
- Never chip ice off cryogenic components (damage risk)
- For heavy ice buildup, defrost equipment before reuse

### 4.5 Operational Procedures

#### 4.5.1 Pre-Operation Checks

```markdown
CRYOGENIC EQUIPMENT PRE-OPERATION CHECKLIST

☐ All personnel wearing complete cryogenic PPE
☐ Equipment recently inspected (within 24 hours)
☐ No visible ice buildup or frost (except on expected cold surfaces)
☐ Insulation intact and in good condition
☐ Vacuum integrity verified (for vacuum-insulated equipment)
☐ All pressure relief valves functional (tested within 6 months)
☐ Temperature sensors operational
☐ Vent system clear and unobstructed
☐ No personnel within 15 meters (except essential operators)
☐ Emergency shower and eyewash accessible (<10 meters)
☐ Cryogenic spill kit available
☐ Oxygen level monitors functional (reading ~21% O₂)
☐ Communication system tested
☐ Emergency procedures reviewed
```

#### 4.5.2 Safe Handling Procedures

**General Rules:**
1. **Never rush** cryogenic operations — thermal equilibrium takes time
2. **Never seal** a system containing LH₂ (pressure buildup)
3. **Never look** directly into vents (unexpected venting can occur)
4. **Never touch** cryogenic equipment without proper PPE
5. **Always vent** slowly to avoid pressure surges
6. **Always verify** temperatures before connections
7. **Always maintain** visual contact with cryogenic surfaces being worked on

**Valve Operation:**
- Open/close valves slowly (quarter-turn every 5 seconds)
- Listen for unusual sounds (cracking, hissing)
- Watch for excessive venting or frost formation
- If valve sticks, do not force — allow warming or seek assistance

**Hose Handling:**
- Support hoses to avoid strain on connections
- Never kink or bend cryogenic hoses sharply
- Allow hoses to "relax" after use (thermal contraction)
- Inspect before and after each use

#### 4.5.3 Spill Response

**Small Spill (<10 liters):**
1. Evacuate immediate area (5-meter radius)
2. Allow natural evaporation (do not approach for 5 minutes)
3. Ventilate area thoroughly
4. Monitor H₂ levels with detectors
5. Inspect for ice or frosted surfaces after evaporation
6. Document spill and circumstances

**Large Spill (>10 liters):**
1. Activate emergency alarm
2. Evacuate to 50 meters minimum
3. Notify fire department immediately
4. Do not attempt to clean up
5. Allow fire department/HAZMAT to manage response
6. Full incident investigation required

### 4.6 Emergency Cryogenic Exposure Response

#### 4.6.1 Cold Burn / Frostbite Treatment

**Immediate Actions:**
1. Remove victim from cold source
2. Remove contaminated clothing (cut if necessary — don't pull)
3. Do NOT rub affected area (tissue damage)
4. Warm affected area gradually with lukewarm water (37-40°C)
5. Never use hot water or direct heat
6. Cover with dry, sterile dressing
7. Seek immediate medical attention (all cases)

**Severity Assessment:**

| Severity | Symptoms | First Aid | Medical Action |
|----------|----------|-----------|----------------|
| **First-Degree** | Redness, numbness | Lukewarm water, 20-30 min | Outpatient if small area |
| **Second-Degree** | Blisters, white/gray tissue | Lukewarm water, sterile dressing | Emergency care required |
| **Third-Degree** | Hard, white/mottled tissue, no pain | Cover, keep warm, no immersion | Immediate hospitalization |

#### 4.6.2 Cryogenic Liquid in Eyes

1. **Immediately** flush eyes with lukewarm water (15 minutes minimum)
2. Do not allow victim to rub eyes
3. Remove contact lenses if present and easy to remove
4. Continue flushing during transport to medical facility
5. Emergency medical care required (potential vision loss)

## 5. Performance Metrics

### 5.1 Cryogenic Safety KPIs

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| **Cryogenic Injury Rate** | 0 injuries | Monthly | Safety Manager |
| **PPE Compliance** | 100% | Per operation | Operations Supervisor |
| **Equipment Cooldown Time** | Within procedure limits | Per cooldown | Cryogenic Technician |
| **Boil-Off Rate** | <2% during operations | Per operation | Operations Manager |
| **Ice-Related Incidents** | 0 incidents | Monthly | Maintenance Manager |
| **Emergency Response Drills** | 4 per year minimum | Quarterly | Safety Manager |

## 6. Training and Competency

### 6.1 Cryogenic Training Requirements

| Training Module | Audience | Duration | Recurrency |
|----------------|----------|----------|------------|
| **Cryogenic Safety Fundamentals** | All LH₂ personnel | 8 hours | Annual |
| **Cryogenic PPE Use** | All operators | 2 hours | Annual |
| **Cryogenic Emergency Response** | All operators + safety team | 4 hours | Annual |
| **Advanced Cryogenic Operations** | Senior operators, supervisors | 16 hours | Bi-annual |

### 6.2 Practical Competency Demonstration

Personnel must demonstrate:
- Proper PPE donning and doffing
- Safe valve operation on cryogenic equipment
- Spill response procedures
- Cold burn first aid
- Emergency evacuation procedures

## 7. Cross-References

### 7.1 Related Documents

- **Parent Document**: [03-00-14_Ops_Std_Sustain](../)
- **LH2 Fueling**: [03-00-14-02-01A_LH2_Fueling_Ops_Standards.md](./03-00-14-02-01A_LH2_Fueling_Ops_Standards.md)
- **H2 Safety**: [03-00-14-02-03A_H2_Safety_Ops_Standards.md](./03-00-14-02-03A_H2_Safety_Ops_Standards.md)
- **Emergency Procedures**: [03-00-14-02-04A_H2_Emergency_Ops_Standards.md](./03-00-14-02-04A_H2_Emergency_Ops_Standards.md)

## 8. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-07 | AMPEL360 Cryogenic Operations Team | Initial release |

---

## Document Control

- **Document ID**: 03-00-14-02-02A
- **Version**: 1.0.0
- **Status**: DRAFT — Subject to human review and approval
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Human approver**: _[to be completed]_
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: 2025-12-07
- **Classification**: Internal Use — Safety Critical
- **Owner**: AMPEL360 Cryogenic Operations WG

---

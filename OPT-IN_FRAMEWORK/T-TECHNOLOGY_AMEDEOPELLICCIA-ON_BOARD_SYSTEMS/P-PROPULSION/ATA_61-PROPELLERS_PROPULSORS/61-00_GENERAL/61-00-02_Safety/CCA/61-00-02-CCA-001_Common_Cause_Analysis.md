# 61-00-02-CCA-001 — Common Cause Analysis

## Document Information

- **Document ID**: 61-00-02-CCA-001
- **Title**: Common Cause Analysis — Propulsor System
- **Version**: 1.0
- **Date**: 2025-12-03
- **Status**: Draft
- **Category**: Safety / CCA
- **ATA Chapter**: 61 — Propellers/Propulsors

---

## 1. Purpose

This document presents the **Common Cause Analysis (CCA)** for the ATA 61 Propellers/Propulsors domain within the AMPEL360 Q100 BWB H2/Hybrid-Electric aircraft.

The CCA encompasses:

- **Zonal Safety Analysis (ZSA)**: Assessment of zonal threats affecting multiple propulsors
- **Particular Risks Analysis (PRA)**: Evaluation of specific threats (fire, HIRF, lightning, bird strike)
- **Common Mode Analysis (CMA)**: Identification of common design, manufacturing, or operational errors

The analysis follows [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) methodology.

---

## 2. Scope

### 2.1 System Boundaries

The CCA covers the propulsor system as defined in [61-00-01-001 Domain Description](../../61-00-01_Overview/61-00-01-001_ATA_61_Domain_Description.md), including:

- Four Electric Ducted Fan (EDF) propulsor units
- Propulsor Control Units (PCUs)
- Associated wiring, cooling, and sensing systems
- Interfaces with power, control, and thermal systems

### 2.2 Independence Claims

The CCA validates the following independence claims from the PSSA:

| Claim ID | Independence Claim | Source |
|----------|-------------------|--------|
| IC-61-001 | Propulsor units are independent — single failure affects max one unit | PSSA SR-61-001 |
| IC-61-002 | Left/right propulsor groups are independent | PSSA SR-61-003 |
| IC-61-003 | PCU channels are independent | PSSA SR-61-010 |
| IC-61-004 | Overspeed protections (HW/SW) are independent | PSSA SR-61-005 |

---

## 3. Zonal Safety Analysis (ZSA)

### 3.1 Zone Definitions

The propulsor system is distributed across multiple aircraft zones:

| Zone ID | Zone Description | Propulsor(s) | Adjacent Systems |
|---------|------------------|--------------|------------------|
| Z-61-01 | Port outboard pylon | Propulsor 1 | Fuel (H₂), electrical, hydraulics |
| Z-61-02 | Port inboard pylon | Propulsor 2 | Fuel (H₂), electrical, thermal |
| Z-61-03 | Starboard inboard pylon | Propulsor 3 | Fuel (H₂), electrical, thermal |
| Z-61-04 | Starboard outboard pylon | Propulsor 4 | Fuel (H₂), electrical, hydraulics |
| Z-61-05 | Central power distribution | PCU power feeds | Fuel cells, batteries, avionics |
| Z-61-06 | Central control routing | Control buses | Flight control, avionics |

### 3.2 Zone Separation Matrix

Distance and barrier between propulsor zones:

| From \ To | Z-61-01 | Z-61-02 | Z-61-03 | Z-61-04 |
|-----------|---------|---------|---------|---------|
| Z-61-01 | — | 5 m | 15 m | 20 m |
| Z-61-02 | 5 m | — | 10 m | 15 m |
| Z-61-03 | 15 m | 10 m | — | 5 m |
| Z-61-04 | 20 m | 15 m | 5 m | — |

**Note**: Minimum separation exceeds containment damage radius for single propulsor failure.

### 3.3 Zonal Threats Assessment

#### 3.3.1 Fire Propagation

| Zone | Fire Source | Affected Equipment | Propagation Risk | Mitigation |
|------|-------------|-------------------|------------------|------------|
| Z-61-01 | Motor/inverter fire | Propulsor 1 only | Low — isolated nacelle | Fire detection, suppression |
| Z-61-02 | Motor/inverter fire | Propulsor 2 only | Low — isolated nacelle | Fire detection, suppression |
| Z-61-03 | Motor/inverter fire | Propulsor 3 only | Low — isolated nacelle | Fire detection, suppression |
| Z-61-04 | Motor/inverter fire | Propulsor 4 only | Low — isolated nacelle | Fire detection, suppression |
| Z-61-05 | Power distribution fire | Multiple feeds possible | Medium | Fire walls, redundant routing |
| Z-61-06 | Control center fire | Multiple control paths | Medium | Redundant routing, separation |

#### 3.3.2 Equipment Failure Cascading

| Failure Origin | Potential Cascade | Assessment | Mitigation |
|---------------|------------------|------------|------------|
| Blade release (any propulsor) | Damage to adjacent structure | Fragments contained by nacelle | Containment design per SR-61-007 |
| Motor fire | Pylon damage | Fire suppression limits damage | Fire detection/suppression |
| Cooling line rupture | Fluid spread | Contained within nacelle | Drainage, fire-resistant materials |
| Inverter explosion | Nacelle damage | Energy contained by housing | Robust inverter housing |

#### 3.3.3 Maintenance Error Effects

| Error Type | Zone Impact | Multi-Propulsor Risk | Mitigation |
|------------|-------------|---------------------|------------|
| Wrong fluid | Single propulsor | Low — independent systems | Maintenance procedures, labeling |
| Incorrect assembly | Single propulsor | Low — independent assemblies | QA inspection, torque verification |
| Cross-connection | Up to 2 propulsors (same side) | Medium if routing shared | Color coding, physical separation |

### 3.4 ZSA Conclusions

| Zone Pair | Independence Validated | Notes |
|-----------|----------------------|-------|
| Z-61-01 ↔ Z-61-02 | Partial | Adjacent — need confirmation of fragment containment |
| Z-61-01 ↔ Z-61-03 | Yes | Adequate separation (15 m) |
| Z-61-01 ↔ Z-61-04 | Yes | Maximum separation (20 m) |
| Z-61-02 ↔ Z-61-03 | Yes | Separation (10 m) |
| Z-61-02 ↔ Z-61-04 | Yes | Adequate separation (15 m) |
| Z-61-03 ↔ Z-61-04 | Partial | Adjacent — need confirmation of fragment containment |

---

## 4. Particular Risks Analysis (PRA)

### 4.1 Fire

#### 4.1.1 Fire Sources

| Component | Fire Risk | Detection | Suppression |
|-----------|-----------|-----------|-------------|
| Electric motor | Medium — electrical fault | Temp sensors, smoke detection | Motor shutdown, fire suppression |
| Inverter | Medium — thermal runaway | Overcurrent, temp sensing | Automatic shutdown |
| Cooling system | Low — fluid is non-flammable | N/A | N/A |
| Wiring | Low | Smoke detection | Circuit breakers |

#### 4.1.2 Fire Spread Prevention

- Nacelle designed as fire containment zone
- Fire walls between propulsor zones and aircraft structure
- Fire-resistant materials in nacelle construction
- Automatic shutdown on fire detection

#### 4.1.3 Fire Impact on Multiple Propulsors

| Scenario | Probability | Impact | Mitigation |
|----------|-------------|--------|------------|
| Fire in one nacelle spreads to adjacent | Very low | Loss of 2 propulsors (same side) | Fire walls, separation, suppression |
| Fire in central zone affects multiple feeds | Low | Loss of multiple propulsors | Redundant routing, fire walls |

**Conclusion**: Fire risk to multiple propulsors is adequately mitigated by design.

### 4.2 High-Intensity Radiated Fields (HIRF)

#### 4.2.1 HIRF Susceptibility

| Component | HIRF Sensitivity | Protection Level Required |
|-----------|------------------|--------------------------|
| PCU electronics | High | [DO-160G](https://www.rtca.org/content/standards-guidance-documents) Level 3 |
| Motor windings | Low | Shielding not required |
| Sensors | Medium | DO-160G Level 2 |
| Wiring | Medium | Shielded cables |

#### 4.2.2 HIRF Protection

- PCU housed in shielded enclosure
- Shielded cables for all control and power connections
- Fiber optic communication where practical
- Grounding and bonding per [DO-160G](https://www.rtca.org/content/standards-guidance-documents) Section 22

#### 4.2.3 HIRF Common Mode Effect

| Scenario | Assessment | Mitigation |
|----------|------------|------------|
| All PCUs affected by HIRF | Possible if inadequate shielding | Qualification to DO-160G Level 3 |
| All sensors affected | Possible for same sensor type | Different sensor technologies |

**Conclusion**: HIRF protection must be verified by test per DO-160G.

### 4.3 Lightning

#### 4.3.1 Lightning Zones

Per [SAE ARP5414](https://www.sae.org/standards/content/arp5414/):

| Zone | Location | Component Exposure |
|------|----------|-------------------|
| 1A | Nacelle leading edge | Fan blades, inlet |
| 1B | Nacelle edges | Nacelle structure |
| 2A | Nacelle sides | Motor housing, inverter |
| 2B | Pylon | Wiring, cooling lines |
| 3 | Internal | PCU electronics |

#### 4.3.2 Lightning Protection

- Lightning strike attachment points defined and protected
- Bonding network ensures current flow path away from electronics
- Surge protection on PCU inputs
- Cable shielding grounded at both ends

#### 4.3.3 Lightning Common Mode Effect

| Scenario | Assessment | Mitigation |
|----------|------------|------------|
| Direct strike to propulsor | Single propulsor affected | Attachment point design, bonding |
| Indirect effects to multiple PCUs | Possible — transient coupling | Surge protection, qualification |
| Cable damage from strike | Local damage | Redundant routing, protection |

**Conclusion**: Lightning protection design must ensure single-strike affects max one propulsor.

### 4.4 Bird Strike

#### 4.4.1 Bird Strike Exposure

| Component | Exposure | Impact |
|-----------|----------|--------|
| Fan inlet | High | Blade damage, possible release |
| Nacelle | Medium | Structural damage |
| Motor | Low (protected) | No direct exposure |

#### 4.4.2 Bird Strike Requirements

Per [CS-25.631](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):

- Fan must demonstrate continued safe operation after medium bird strike
- Large bird strike may cause engine shutdown but not hazardous effects
- Multiple bird (flocking) requirements apply

#### 4.4.3 Bird Strike Common Mode Effect

| Scenario | Assessment | Mitigation |
|----------|------------|------------|
| Single bird to one propulsor | Expected — continue on 3 | Blade containment, N-1 capability |
| Multiple birds to multiple propulsors | Possible — flocking event | N-2 capability, separation |
| Flock through multiple propulsors | Low probability | Physical separation, flock avoidance |

**Conclusion**: Multiple bird strike scenario requires quantification based on separation.

### 4.5 Foreign Object Damage (FOD)

| FOD Source | Exposure | Multi-Propulsor Risk | Mitigation |
|------------|----------|---------------------|------------|
| Runway debris | All propulsors during T/O | Low — sequential ingestion unlikely | Inlet design, FOD screens if needed |
| Ice shedding from aircraft | Downstream propulsors | Medium | De-icing, inlet heating |
| Maintenance debris | Any propulsor | Low | FOD prevention procedures |

---

## 5. Common Mode Analysis (CMA)

### 5.1 Design Common Modes

| Common Mode | Affected Items | Analysis | Mitigation |
|-------------|---------------|----------|------------|
| Same motor design | All 4 motors | Design error affects all | Design reviews, type test |
| Same PCU software | All 8 PCU channels | Software error affects all | DO-178C DAL B, diverse backup |
| Same blade design | All blades | Design flaw affects all | Safe-life analysis, inspection |
| Same sensor type | All sensors of type | Systematic failure | Multiple sensor types |

### 5.2 Manufacturing Common Modes

| Common Mode | Affected Items | Analysis | Mitigation |
|-------------|---------------|----------|------------|
| Same motor batch | Multiple motors | Manufacturing defect | Quality control, batch separation |
| Same PCU production line | Multiple PCUs | Process error | Lot testing, traceability |
| Same blade manufacturing | Multiple blades | Material/process defect | NDI, material certification |

### 5.3 Operational Common Modes

| Common Mode | Affected Items | Analysis | Mitigation |
|-------------|---------------|----------|------------|
| Common power source | All propulsors | Power loss affects all | Multiple power sources (FC1, FC2, battery) |
| Common control bus | All propulsors | Bus failure affects all | Redundant buses, dissimilar routing |
| Common coolant supply | All propulsors | Coolant loss affects all | Separate cooling circuits |
| Same maintenance action | Multiple propulsors | Error repeated | Staggered maintenance, independence |

### 5.4 Environmental Common Modes

| Common Mode | Affected Items | Analysis | Mitigation |
|-------------|---------------|----------|------------|
| Icing conditions | All propulsors exposed | Ice accumulation | Anti-icing systems |
| High altitude operation | All propulsors | Thermal/electrical stress | Environmental qualification |
| Extreme temperature | All propulsors | Performance degradation | Operating envelope limits |

### 5.5 CMA Beta Factors

For quantitative analysis of common cause failures:

| Item Type | Beta Factor | Basis | Notes |
|-----------|-------------|-------|-------|
| Identical propulsor units | 0.01 | Physical separation | Low beta due to location diversity |
| PCU channels (same unit) | 0.05 | Dissimilar software | Medium beta — shared environment |
| PCU channels (different units) | 0.01 | Physical separation | Low beta |
| Triplicated sensors (same propulsor) | 0.10 | Different technologies | Conservative estimate |
| Propulsor and power supply | 0.001 | Different systems | Very low coupling |

---

## 6. Independence Claim Validation

### 6.1 IC-61-001: Propulsor Unit Independence

| Threat | Independence Maintained | Evidence |
|--------|------------------------|----------|
| Internal failure | Yes | Separate units, no physical coupling |
| Fire | Yes | Fire walls, containment |
| HIRF | Requires verification | Shielding qualification needed |
| Lightning | Yes | Bonding design, attachment points |
| Bird strike (single) | Yes | Containment |
| Bird strike (flock) | Partial | Quantification needed |
| Design error | No — addressed by design assurance | DAL allocation |
| Manufacturing error | Partial — batch controls needed | Lot separation |

**Validation Status**: Partially validated — HIRF and flock bird strike require further analysis.

### 6.2 IC-61-002: Left/Right Group Independence

| Threat | Independence Maintained | Evidence |
|--------|------------------------|----------|
| Physical damage | Yes | 10+ m separation |
| Fire | Yes | Separate zones |
| Common power | Requires analysis | Power distribution design |
| Common control | Requires analysis | Control routing design |

**Validation Status**: Partially validated — power and control routing to be confirmed.

### 6.3 IC-61-003: PCU Channel Independence

| Threat | Independence Maintained | Evidence |
|--------|------------------------|----------|
| Hardware failure | Yes | Separate components |
| Software error | Partial | Dissimilar software mitigates |
| Power supply | Yes | Independent supplies |
| Environmental | Partial | Shared enclosure |

**Validation Status**: Partially validated — dissimilar software effectiveness to be confirmed.

### 6.4 IC-61-004: Overspeed Protection Independence

| Threat | Independence Maintained | Evidence |
|--------|------------------------|----------|
| Hardware failure | Yes | Separate circuits |
| Software error | N/A | One is hardware-only |
| Common trigger | Yes | Different sensing inputs |
| Environmental | Partial | Shared sensing environment |

**Validation Status**: Validated — HW and SW protections are independent.

---

## 7. Open Items

| ID | Description | Owner | Status | Target Date |
|----|-------------|-------|--------|-------------|
| CCA-OI-001 | Complete HIRF qualification test plan | EMC Lead | Open | TBD |
| CCA-OI-002 | Quantify flock bird strike probability | Safety | Open | TBD |
| CCA-OI-003 | Confirm power distribution routing | Electrical | Open | TBD |
| CCA-OI-004 | Confirm control bus routing | Avionics | Open | TBD |
| CCA-OI-005 | Define batch separation requirements | Quality | Open | TBD |
| CCA-OI-006 | Lightning indirect effects analysis | EMC Lead | Open | TBD |

---

## 8. Conclusions

1. **Zonal Safety**: Propulsor physical separation is adequate for most zonal threats. Adjacent propulsor pairs (1-2 and 3-4) require confirmed containment effectiveness.

2. **Fire**: Adequate mitigations exist through nacelle design and fire suppression.

3. **HIRF**: Requires qualification testing per DO-160G to confirm protection adequacy.

4. **Lightning**: Direct attachment design appears adequate; indirect effects analysis needed.

5. **Bird Strike**: Single bird is mitigated; flock scenario requires quantification.

6. **Common Modes**: Design and manufacturing common modes are the primary concern for multi-propulsor failure. Mitigation through design assurance (DAL) and quality controls.

---

## 9. References

### Internal References

- [61-00-02-SFHA-001 Propulsor System Hazards](../SFHA/61-00-02-SFHA-001_Propulsor_System_Hazards.md)
- [61-00-02-PSSA-001 Preliminary Safety Assessment](../PSSA/61-00-02-PSSA-001_Preliminary_Safety_Assessment.md)
- [61-00-02-FTA-001 Propulsor Failure Trees](../FTA/61-00-02-FTA-001_Propulsor_Failure_Trees.md)
- [61-00-01-001 Domain Description](../../61-00-01_Overview/61-00-01-001_ATA_61_Domain_Description.md)

### External Standards

- [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) — Guidelines and Methods for Conducting the Safety Assessment Process
- [RTCA DO-160G](https://www.rtca.org/content/standards-guidance-documents) — Environmental Conditions and Test Procedures
- [SAE ARP5414](https://www.sae.org/standards/content/arp5414/) — Aircraft Lightning Zoning
- [EASA CS-25.631](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) — Bird Strike Damage

---

## 10. Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-03_.

---

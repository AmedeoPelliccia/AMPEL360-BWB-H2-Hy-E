# 57-00-02-60 — Shared Resources Map

**ATA Chapter**: 57 — Wings  
**Folder**: 57-00-02_Safety / 57-00-02-60_COMMON_CAUSES  
**Status**: DRAFT  
**Owner**: Airframe & Structures Domain (ATA 57)

---

## 1. Purpose

This document maps **shared resources** that could affect wing safety, identifying potential common cause vulnerabilities.

---

## 2. Shared Resource Categories

### 2.1 Power Sources

| Resource | Systems Using | Single Point? | Mitigation |
| :-- | :-- | :-- | :-- |
| Hydraulic System 1 | Flaps, spoilers, slats (set A) | No - System 2 backup | Dual systems |
| Hydraulic System 2 | Flaps, spoilers, slats (set B) | No - System 1 backup | Dual systems |
| Electrical Bus 1 | Actuator control (set A) | No - Bus 2 backup | Dual buses |
| Electrical Bus 2 | Actuator control (set B) | No - Bus 1 backup | Dual buses |

### 2.2 Control Systems

| Resource | Systems Using | Single Point? | Mitigation |
| :-- | :-- | :-- | :-- |
| Flight Control Computer 1 | Primary control | No - FCC 2 backup | Triplex/dual |
| Flight Control Computer 2 | Primary control | No - FCC 1 backup | Triplex/dual |
| High Lift Control Unit | Flaps, slats | Potentially | Design review TBD |

### 2.3 Structural Resources

| Resource | Systems Dependent | Single Point? | Mitigation |
| :-- | :-- | :-- | :-- |
| Front spar | All wing load transfer | Yes | Damage tolerance, inspection |
| Rear spar | All wing load transfer | Yes | Damage tolerance, inspection |
| Wing root fittings | Wing attachment | Redundant | Multiple fittings |

### 2.4 Environmental Systems

| Resource | Systems Using | Single Point? | Mitigation |
| :-- | :-- | :-- | :-- |
| Bleed air | Wing ice protection | TBD | Alternative (electrical) TBD |
| Fuel vent | Tank pressure | TBD | Multiple vents |

---

## 3. Shared Resource Matrix

### 3.1 Control Surface Systems

| Resource | Aileron L | Aileron R | Flap In | Flap Out | Spoiler | Slat |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| HYD Sys 1 | ✓ | - | ✓ | - | ✓ | ✓ |
| HYD Sys 2 | - | ✓ | - | ✓ | ✓ | ✓ |
| Elec Bus 1 | ✓ | - | ✓ | - | ✓ | ✓ |
| Elec Bus 2 | - | ✓ | - | ✓ | ✓ | ✓ |
| FCC 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| FCC 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### 3.2 Structural Monitoring

| Resource | SHM Ch1 | SHM Ch2 | Manual Insp |
| :-- | :-- | :-- | :-- |
| Elec Bus 1 | ✓ | - | - |
| Elec Bus 2 | - | ✓ | - |
| SHM Processor | ✓ | ✓ | - |
| NDT Equipment | - | - | ✓ |

---

## 4. Key Shared Resource Concerns

### 4.1 Single Points Requiring Attention

| Resource | Concern | Status | Action |
| :-- | :-- | :-- | :-- |
| Front spar | Single structural element | Addressed | Damage tolerance design |
| Rear spar | Single structural element | Addressed | Damage tolerance design |
| SHM processor | Single data processing point | TBD | Review architecture |

### 4.2 Diverse Backup Assessment

| Primary | Backup | Diversity | Assessment |
| :-- | :-- | :-- | :-- |
| Hydraulic actuation | Electrical actuation | High | Acceptable |
| SHM monitoring | Manual inspection | High | Acceptable |
| Thermal ice protection | TBD | TBD | Under review |

---

## 5. Cross-ATA Shared Resources

| Resource | Wing Systems | Other ATA Systems | Concern |
| :-- | :-- | :-- | :-- |
| HYD System 1 | Control surfaces | ATA 27, ATA 32 | Multi-ATA failure |
| HYD System 2 | Control surfaces | ATA 27, ATA 32 | Multi-ATA failure |
| Electrical buses | All wing electronics | All aircraft systems | Loss of electrical |
| Bleed air | Ice protection | ATA 21 (ECS) | Bleed system failure |

---

## 6. Traceability

| From | To | Purpose |
| :-- | :-- | :-- |
| Shared Resources | CCA | Common cause assessment |
| Shared Resources | FTA | Failure combinations |
| Shared Resources | Design | Architecture decisions |

---

## TODO

- [ ] Complete shared resource identification  
- [ ] Verify backup diversity  
- [ ] Review single points with design team  
- [ ] Update after architecture freeze  

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.  
- Status: **DRAFT** — Subject to human review and approval.  
- Human approver: _[to be completed]_.  
- Repository: `AMPEL360-BWB-H2-Hy-E`  
- Last AI update: 2025-11-29

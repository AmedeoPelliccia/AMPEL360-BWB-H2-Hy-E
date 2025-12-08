# 03-60-03-02A - Vacuum Insulated Storage

## 1. Purpose
This document specifies the design, operation, and maintenance requirements for vacuum insulated cryogenic storage systems, focusing on vacuum system performance and management for optimal thermal efficiency.

## 2. Scope
This document covers:
- Vacuum insulation principles and technology
- Vacuum system components and design
- Vacuum maintenance and monitoring
- Performance troubleshooting and optimization
- Lifecycle management of vacuum systems

## 3. Applicable Documents
- ISO 21009 (Cryogenic Vessels - Static Vacuum Insulated Vessels)
- EN 13458-2 (Cryogenic Vessels - Operational Requirements)
- ASME BPVC Section VIII (Pressure Vessel Code)
- CGA P-12 (Safe Handling of Cryogenic Liquids)
- PNEUROP 6606 (Acceptance and Routine Tests for Vacuum Pumps)
- ISO 3529-1 (Vacuum Technology - Vocabulary)

## 4. Storage Description

### 4.1 Overview
Vacuum insulation is the primary thermal protection method for cryogenic storage systems, utilizing the near-absence of gas molecules in the annular space between inner and outer vessels to dramatically reduce conductive and convective heat transfer. Only radiative heat transfer remains significant, which is mitigated through low-emissivity surfaces and multi-layer insulation.

Key principles:
- Vacuum reduces gas-phase heat transfer
- Lower pressure = less heat transfer (below 10⁻² mbar)
- Getter materials maintain vacuum over time
- Monitoring critical for performance maintenance

### 4.2 Specifications

#### Vacuum Performance Levels
| Vacuum Quality | Pressure Range | Heat Transfer Reduction | Application |
|----------------|----------------|-------------------------|-------------|
| Rough Vacuum | 1000-1 mbar | Minimal | Initial pump-down only |
| Medium Vacuum | 1-10⁻³ mbar | 50-80% | Low-performance insulation |
| High Vacuum | 10⁻³-10⁻⁶ mbar | 90-98% | Standard cryogenic storage |
| Ultra-High Vacuum | <10⁻⁶ mbar | >98% | Long-duration missions, research |

#### Vacuum System Components
| Component | Specification | Function |
|-----------|---------------|----------|
| Primary Pump | Rotary vane or scroll | Initial evacuation to 10⁻² mbar |
| Secondary Pump | Turbomolecular or diffusion | High vacuum achievement |
| Getter Material | Activated charcoal or molecular sieve | Passive vacuum maintenance |
| Vacuum Gauge | Pirani + cold cathode | Full-range pressure measurement |
| Valve (Vacuum Port) | All-metal seal, bakeable | Access for evacuation/testing |
| Relief Device | Burst disk | Protect outer vessel from over-pressure |

### 4.3 Capacity and Requirements

#### Vacuum System Design
- **Evacuation Time**: < 48 hours to operating vacuum for new vessels
- **Leak Rate**: < 1×10⁻⁷ mbar·L/s (helium leak test)
- **Getter Capacity**: Sufficient for 10-year service life minimum
- **Pump-down Port**: Minimum DN 25 (1 inch) connection
- **Vacuum Monitoring**: Continuous for critical storage, periodic for smaller systems

#### Performance Monitoring
| Parameter | Normal Range | Action Level | Frequency |
|-----------|--------------|--------------|-----------|
| Vacuum Pressure | <10⁻³ mbar | >10⁻² mbar | Continuous or monthly |
| Boil-off Rate | 0.1-0.3%/day | >0.5%/day | Daily |
| Heat Ingress Rate | <2 W/m² | >5 W/m² | Calculated from boil-off |
| Outer Shell Temperature | Ambient ±10°C | Frost formation | Visual inspection |

## 5. Safety Requirements
| Requirement | Standard | Implementation |
|-------------|----------|----------------|
| Vacuum Integrity Testing | ISO 21009, Section 8 | Initial and after any breach |
| Overpressure Protection (Outer Vessel) | ASME Section VIII | Burst disk sized for worst-case |
| Insulation Space Monitoring | Manufacturer recommendation | Vacuum gauge with alarm |
| Re-evacuation Procedures | Site-specific procedure | After vacuum degradation |
| Personnel Training | Site safety training | Vacuum system maintenance certification |

## 6. Cross-References
- Related ATA Chapters:
  - ATA 03-60-03-01A (Cryogenic Tank Systems) - Overall tank design
  - ATA 03-60-03-03A (Boil-Off Management) - Performance impact
  - ATA 03-60-02 (H2/LH2 Storage Systems) - LH2 applications
- Parent Document: 03-60_Storages
- Standards: ISO 21009, ASME Section VIII

## 7. Revision History
| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-08 | AMPEL360 Documentation Team | Initial release |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-08_.

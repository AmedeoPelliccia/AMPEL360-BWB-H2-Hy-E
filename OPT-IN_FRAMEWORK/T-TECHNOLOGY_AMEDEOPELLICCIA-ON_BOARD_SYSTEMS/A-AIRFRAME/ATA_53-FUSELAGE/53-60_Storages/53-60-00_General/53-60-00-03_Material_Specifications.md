# 53-60-00-03 Material Specifications

## Document Information

- **Document ID**: 53-60-00-03
- **Title**: Material Specifications
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: General
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the material specifications and compatibility requirements for all storage systems within the AMPEL360 BWB fuselage structure.

## Scope

This specification covers:
- Primary structural materials
- Sealing and gasket materials
- Insulation materials
- Material compatibility matrix
- Certification requirements

## Material Categories

### Primary Structural Materials

| Material | Specification | Application | Notes |
|----------|---------------|-------------|-------|
| Aluminum 6061-T6 | AMS 4027 | Housing, frames | General structure |
| Aluminum 7050-T7451 | AMS 4050 | High-strength fittings | Corrosion resistant |
| Stainless 316L | AMS 5653 | Wetted surfaces | Food-grade certified |
| Titanium Ti-6Al-4V | AMS 4911 | High-temp fittings | Fire resistance |
| CFRP IM7/8552 | PS-53-001 | Composite housings | Weight optimization |

### Sealing Materials

| Material | Specification | Temperature Range | Application |
|----------|---------------|-------------------|-------------|
| PTFE | AMS 3651 | -200°C to +260°C | Universal seals |
| EPDM | AMS 3216 | -40°C to +120°C | General purpose |
| Viton (FKM) | AMS 7259 | -20°C to +200°C | High-temp seals |
| Silicone | AMS 3302 | -55°C to +200°C | Thermal interface |

### Insulation Materials

| Material | Thermal Conductivity | Max Temp | Application |
|----------|---------------------|----------|-------------|
| Aerogel blanket | 0.015 W/m·K | 650°C | High-performance |
| MLI (Multi-Layer Insulation) | 0.0001 W/m·K (vacuum) | 400°C | Cryogenic |
| Ceramic fiber | 0.05 W/m·K | 1260°C | Fire barrier |
| Closed-cell foam | 0.035 W/m·K | 80°C | General purpose |

## Material Compatibility Matrix

| Material | Battery (Coolant) | CO₂ | Water | PCM Fluid | Notes |
|----------|-------------------|-----|-------|-----------|-------|
| Aluminum 6061-T6 | ✓ | ✓ | ✓ | ✓ | Primary structure |
| Stainless 316L | ✓ | ✓ | ✓ | ✓ | Wetted surfaces |
| HDPE | — | — | ✓ | — | Water bladder only |
| PTFE | ✓ | ✓ | ✓ | ✓ | Universal seals |
| EPDM | ✓ | ✓ | ✓ | ✓ | Non-HV seals |
| Viton | ✓ | ✓ | ✓ | ✓ | High-temp seals |
| Silicone | ✓ | — | ✓ | ✓ | Not for CO₂ |
| Aerogel | ✓ | ✓ | — | ✓ | Not for water contact |

Legend: ✓ = Compatible, — = Not recommended

## Application-Specific Requirements

### Battery Storage Materials

| Component | Material | Requirement |
|-----------|----------|-------------|
| Housing | Aluminum 6061-T6 | Fire containment |
| Thermal jacket | Aerogel + ceramic fiber | Thermal runaway protection |
| Coolant wetted | Stainless 316L | Corrosion resistance |
| HV insulation | Silicone | Dielectric strength |
| Seals | EPDM | Coolant compatibility |

### CO₂ Storage Materials

| Component | Material | Requirement |
|-----------|----------|-------------|
| Cartridge shell | Aluminum 6061-T6 | Pressure containment |
| Valve body | Stainless 316L | Corrosion resistance |
| Seals | PTFE | CO₂ compatibility |
| Insulation | Ceramic fiber | Temperature stability |

### Water Storage Materials

| Component | Material | Requirement |
|-----------|----------|-------------|
| Tank | Stainless 316L | Food-grade |
| Bladder | HDPE (food-grade) | Potable water |
| Fittings | Stainless 316L | Corrosion resistance |
| Insulation | Closed-cell foam | Condensation prevention |

### Thermal Storage Materials

| Component | Material | Requirement |
|-----------|----------|-------------|
| Accumulator shell | Aluminum 6061-T6 | Thermal conductivity |
| PCM container | Stainless 316L | Chemical resistance |
| Insulation | MLI + aerogel | Heat retention |
| Heat exchanger | Aluminum + copper | Thermal transfer |

## Certification Requirements

All materials shall:
1. Have documented traceability per [ARP4754A](https://www.sae.org/standards/content/arp4754a/)
2. Meet flammability requirements per [CS 25.853](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)
3. Include material certifications (Certificates of Conformance)
4. Support DPP material tracking requirements

## References

### Standards
- AMS Aerospace Material Specifications (SAE International)
- [CS-25.853 Compartment Interiors](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27)

### Internal References
- [53-60-00-02 Design Rules](53-60-00-02_Design_Rules.md)
- [53-60-00-04 Safety Requirements](53-60-00-04_Safety_Requirements.md)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---

# NEUTRAL_FORMATS — CAD Neutral Format Exports

This directory contains CAD model exports in neutral (vendor-independent) formats for interoperability with external partners, suppliers, and analysis tools.

## Purpose

Neutral format exports enable:

- Cross-platform CAD system compatibility
- Data exchange with manufacturing partners
- Long-term archival independent of proprietary formats
- Regulatory submission requirements
- Supplier data packages

## Directory Structure

```
NEUTRAL_FORMATS/
├── README.md       # This file
├── STEP/           # STEP AP242 exports (preferred)
├── JT/             # JT format with PMI
├── IGES/           # Legacy IGES support
└── PARASOLID/      # Parasolid kernel exports
```

## Format Specifications

### STEP (STEP/)

**Preferred format for all neutral exports**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Standard             | ISO 10303-242 (AP242)                    |
| Edition              | Edition 2 preferred                      |
| Geometric Accuracy   | 0.001 mm                                 |
| PMI                  | Include where available                  |
| Validation           | Run AP242 conformance check              |
| Naming               | `Q100-61-EXP-[COMPONENT]-[VARIANT].step` |

**Use Cases:**

- Primary neutral format for all exchanges
- Certification submissions
- Long-term archival
- Manufacturing process planning

### JT (JT/)

**Visualization and lightweight CAD exchange**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Version              | JT 10.5 or later                         |
| Tessellation         | High quality (chord deviation ≤ 0.05 mm) |
| PMI                  | Include GD&T and annotations             |
| XT BRep              | Include for precise geometry             |
| Naming               | `Q100-61-EXP-[COMPONENT]-[VARIANT].jt`   |

**Use Cases:**

- Design review with external partners
- Lightweight visualization
- Digital mock-up (DMU)
- PLM system integration

### IGES (IGES/)

**Legacy format support only**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Version              | IGES 5.3                                 |
| Flavor               | Default (no flavoring)                   |
| Accuracy             | 0.001 mm                                 |
| Entity Types         | Surfaces and curves                      |
| Naming               | `Q100-61-EXP-[COMPONENT]-[VARIANT].igs`  |

> **Note:** IGES is deprecated. Use only when specifically requested by legacy systems or partners who cannot accept STEP.

**Use Cases:**

- Legacy system compatibility
- Specific supplier requirements
- Historical data migration

### Parasolid (PARASOLID/)

**Kernel-level geometry exchange**

| Setting              | Value                                    |
|----------------------|------------------------------------------|
| Version              | Latest stable (35.0+)                    |
| Format               | Binary (.x_b) or text (.x_t)             |
| Accuracy             | Match source model                       |
| Attributes           | Include where supported                  |
| Naming               | `Q100-61-EXP-[COMPONENT]-[VARIANT].x_b`  |

**Use Cases:**

- High-fidelity geometry transfer
- Siemens NX interoperability
- Analysis tool preprocessing

## Naming Convention

All neutral format exports follow:

```
Q100-61-EXP-[SYSTEM]-[COMPONENT]-[VARIANT].[ext]
```

### Examples

```
Q100-61-EXP-FPS-TOP-ASSY.step           → Full Propulsor STEP assembly
Q100-61-EXP-EMD-ROTOR-ASSY.step         → Motor rotor STEP
Q100-61-EXP-GBX-GEAR-SET.jt             → Gearbox gear set JT
Q100-61-EXP-FAN-BLADE-S01.x_b           → Fan blade stage 1 Parasolid
Q100-61-EXP-NAC-OUTER-SHELL.igs         → Nacelle shell IGES (legacy)
```

## Export Procedures

1. **Source Validation**: Verify source model is current and approved
2. **Configuration Selection**: Choose correct design configuration/variant
3. **Export Settings**: Use settings from Q100-61-EXPORT-SETTINGS.yaml
4. **Quality Check**: Run format-specific validation tools
5. **Metadata**: Record version, date, engineer, and checksum
6. **Manifest Update**: Update RELEASE_HISTORY manifest

## Quality Requirements

- All exports must pass validation without critical errors
- Geometry accuracy verified within tolerance
- Assembly structure preserved where applicable
- PMI (Product Manufacturing Information) included when available
- File size reasonable for intended use

## Related Documentation

- [Q100-61-EXPORT-SETTINGS.yaml](../Q100-61-EXPORT-SETTINGS.yaml) - Detailed export settings
- [AMPEL360_ASSETS_STANDARD.md](../../../../../../../../AMPEL360_ASSETS_STANDARD.md) - Asset management
- [../README.md](../README.md) - EXPORTS overview

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---

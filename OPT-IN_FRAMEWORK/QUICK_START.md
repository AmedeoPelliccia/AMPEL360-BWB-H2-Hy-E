# OPT-IN Framework — Quick Start Guide

**Version:** 1.0  
**Date:** 2025-11-13

## Overview

This guide helps you get started with the OPT-IN Framework, the mandatory documentation topology for AMPEL360.

## What is the OPT-IN Framework?

The **OPT-IN Framework** organizes all AMPEL360 documentation into:
- **5 main axes** (O, P, T, I, N)
- **79 ATA chapters** distributed across axes
- **14 lifecycle folders** in each chapter's GENERAL layer
- **9 cross-ATA buckets** for cross-cutting concerns

This ensures **certification-grade traceability** and **consistent navigation**.

## Quick Navigation

### 1. Find Your Axis

Depending on your work area, navigate to the appropriate axis:

```
OPT-IN_FRAMEWORK/
├── O-ORGANIZATION/          # Policies, airworthiness, maintenance
├── P-PROGRAM/               # Geometry, handling, servicing
├── T-TECHNOLOGY_.../        # On-board systems (15 subsystems)
├── I-INFRASTRUCTURES/       # Ground support, airports, H₂ chains
└── N-NEURAL_NETWORKS_.../   # AI, DPP, traceability
```

### 2. Find Your ATA Chapter

Each axis contains relevant ATA chapters. For example:

- **Safety Engineer** → O-ORGANIZATION/ATA_04-AIRWORTHINESS_LIMITATIONS/
- **Fuel System Engineer** → T-TECHNOLOGY_.../C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/
- **Operations Planner** → I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/

### 3. Navigate the Chapter Structure

Every ATA chapter has the same structure:

```
ATA_XX-DESCRIPTION/
├── XX-00_GENERAL/           # 14 lifecycle folders (start here!)
├── XX-10_Operations/        # Operational procedures
├── XX-20_Subsystems/        # Functional subsystems
├── XX-30_Circularity/       # Sustainability & LCA
├── XX-40_Software/          # Software & control logic
├── XX-50_Structures/        # Physical structures
├── XX-60_Storages/          # Tanks & storage
├── XX-70_Propulsion/        # Propulsion interfaces
├── XX-80_Energy/            # Energy management
└── XX-90_Tables_Schemas_Diagrams/  # Data & documentation
```

### 4. Use the Lifecycle Folders

The **XX-00_GENERAL** layer contains 14 mandatory folders:

1. **01_Overview** - Start here! System overview and architecture
2. **02_Safety** - Safety analysis and requirements
3. **03_Requirements** - Requirements and traceability
4. **04_Design** - Design specifications
5. **05_Interfaces** - Interface control documents
6. **06_Engineering** - Analysis, models, simulation
7. **07_V_AND_V** - Verification and validation
8. **08_Prototyping** - Prototype development
9. **09_Production_Planning** - Manufacturing planning
10. **10_Certification** - Certification evidence
11. **11_EIS_Versions_Tags** - Configuration management
12. **12_Services** - Maintenance and service
13. **13_Subsystems_Components** - Component breakdown
14. **14_Ops_Std_Sustain** - Operational standards

## Common Workflows

### As a Design Engineer

1. Navigate to your ATA chapter
2. Read **XX-00-01_Overview/** for context
3. Review **XX-00-03_Requirements/** for requirements
4. Add your design work to **XX-00-04_Design/**
5. Document interfaces in **XX-00-05_Interfaces/**
6. Add detailed designs to **XX-20_Subsystems/** (design-driven structure)

### As a Test Engineer

1. Navigate to your ATA chapter
2. Review **XX-00-03_Requirements/** for test requirements
3. Create test plans in **XX-00-07_V_AND_V/**
4. Link evidence to certification in **XX-00-10_Certification/**

### As a Program Manager

1. Check **XX-00-01_Overview/** for status across all chapters
2. Monitor progress through lifecycle folders (01-14)
3. Review **XX-00-10_Certification/** for compliance status
4. Track cross-system concerns in XX-10/20/30/40/50/60/70/80/90 buckets

### As a Certification Authority

1. Start with **XX-00-10_Certification/** in each chapter
2. Review **XX-00-03_Requirements/** for traceability
3. Check **XX-00-07_V_AND_V/** for test evidence
4. Verify **XX-00-02_Safety/** for safety case

## Validation & CI

### Check Your Structure

```bash
# Validate entire framework
python tools/ci/optin_structure_validator.py --check

# Validate specific chapter
python tools/ci/optin_structure_validator.py --check --chapter 95

# Generate SARIF report
python tools/ci/optin_structure_validator.py --check --sarif results.sarif
```

### Create Missing Structure

If a chapter is missing the required structure:

```bash
# Dry-run first (see what would be created)
python tools/ci/create_optin_structure.py --dry-run

# Create the structure
python tools/ci/create_optin_structure.py
```

## Tips & Best Practices

### 1. Always Start with Overview
Read the **XX-00-01_Overview/** folder first to understand the system.

### 2. Use README Files
Every folder has a README.md explaining its purpose. Read them!

### 3. Follow the Lifecycle
The 14 lifecycle folders (01-14) follow a logical progression. Work through them sequentially when developing a new system.

### 4. Design-Driven Buckets
Inside XX-20_Subsystems/ and other buckets, organize content based on how your system is designed and implemented. The structure is flexible here.

### 5. Link Documentation
Use markdown links to connect related documents across folders. For example:
```markdown
See [Requirements](../../XX-00-03_Requirements/REQ-001.md) for details.
```

### 6. Maintain Traceability
Always link your work to requirements, safety cases, and certification artifacts.

## Getting Help

### Documentation
- [OPT-IN_FRAMEWORK_STANDARD.md](../OPT-IN_FRAMEWORK_STANDARD.md) - Complete standard
- [README.md](README.md) - Framework overview
- [AMPEL360_DOCUMENTATION_STANDARD.md](../AMPEL360_DOCUMENTATION_STANDARD.md) - Documentation guidelines

### Tools
- `tools/ci/create_optin_structure.py` - Generate structure
- `tools/ci/optin_structure_validator.py` - Validate structure
- `.github/workflows/optin-structure-check.yml` - CI workflow

### ATA 95 as Template
ATA 95 (Digital Product Passport / Neural Networks) serves as the canonical template. When in doubt, look at:
```
N-NEURAL_NETWORKS_USERS_TRACEABILITY/
└── ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/
```

## Frequently Asked Questions

### Q: Why so many folders?
**A:** The structure ensures complete lifecycle coverage and certification compliance. Each folder has a specific purpose.

### Q: Can I skip folders that don't apply?
**A:** No. All folders are mandatory. If not applicable, include a README.md stating "Not Applicable" and why.

### Q: How do I add content to buckets?
**A:** Use the naming convention `XX-YY-ZZ_DESCRIPTION`:
- XX = ATA chapter (e.g., 95)
- YY = Bucket number (10, 20, 30, etc.)
- ZZ = Sequential number (00, 01, 02, etc.)

### Q: What if my system spans multiple ATA chapters?
**A:** Document the primary aspects in the most relevant chapter, then cross-reference from other chapters' XX-05_Interfaces/ folders.

### Q: How is this enforced?
**A:** The CI workflow (`.github/workflows/optin-structure-check.yml`) automatically validates structure on every commit.

## Summary

The OPT-IN Framework provides:
1. **Consistent structure** across all ATA chapters
2. **Complete lifecycle** coverage (14 folders)
3. **Cross-cutting concerns** (9 buckets)
4. **Certification-ready** documentation
5. **Automated validation** via CI

Start with your axis → Find your ATA chapter → Navigate the structure → Follow the lifecycle!

---

**Document Control:**
- **Version**: 1.0
- **Status**: Active
- **Owner**: AMPEL360 Documentation WG
- **Last Updated**: 2025-11-13

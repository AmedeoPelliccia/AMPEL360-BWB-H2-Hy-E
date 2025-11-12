# DMC Numbering Scheme
## Data Module Code Structure for AMPEL360

**Version:** 1.0  
**Date:** 2025-11-05

---

## 1. Overview

This document defines the Data Module Code (DMC) numbering scheme for AMPEL360 technical publications.

## 2. DMC Structure

### Format
```
DMC-AMP-A-{ATA}-{SUB}-{SEC}-{ASSY}-{INFO}-{VAR}
```

### Example: DMC-AMP-A-02-00-00-00A-941A-A

| Position | Value | Description |
|----------|-------|-------------|
| Model ID | AMP | AMPEL360 Model |
| Sys Diff | A | System Difference Code A |
| System | 02 | ATA Chapter 02 (Operations) |
| Subsystem | 00 | General (no subsystem) |
| Section | 00 | No specific section |
| Assembly | 00A | Assembly code |
| Info Code | 941A | System Description |
| Variant | A | Variant A |

## 3. Information Code Table

| Code | Type | Description | Usage |
|------|------|-------------|-------|
| 012A | Procedural | Servicing | Routine servicing tasks |
| 013A | Procedural | Safety Precautions | H₂ safety, PPE |
| 014A | Procedural | Consumables | Materials, fluids |
| 018A | Descriptive | Technical Data | Specs, limits |
| 720A | Fault | Access Requirements | Panel removal |
| 941A | Descriptive | System Description | Overview |

## 4. Naming Conventions

- Use ATA chapter numbering (00-99)
- Subsystem codes follow ATA iSpec 2200
- Assembly codes: 00A, 00B, 00C, etc.
- Info codes per S1000D standard
- Variants: A, B, C, etc. for revisions

## 5. Examples

### ATA 02-00-00 (GENERAL)
- DMC-AMP-A-02-00-00-00A-941A-A (System Description)
- DMC-AMP-A-02-00-00-00A-018A-A (Technical Data)
- DMC-AMP-A-02-00-00-00A-012A-A (Special Tools)
- DMC-AMP-A-02-00-00-00A-014A-A (Consumables)
- DMC-AMP-A-02-00-00-00A-720A-A (Access Requirements)
- DMC-AMP-A-02-00-00-00A-013A-A (Safety Precautions H₂)

---

**Document Owner:** Technical Publications

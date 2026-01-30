# APPLICABILITY Directory

## Purpose

Centralizes **ACT/PCT/CCT** (Applicability Cross-reference Tables) for filtering Data Modules (DMs) of the AMM for ATA 31-00-00 (Indicating/Recording - General). In S1000D, these modules enable content filtering by **product attributes** and **operational conditions**.

### How Used

Each DM under `CSDB/DM` must reference the **ACT** in its `dmStatus` section. The ACT serves as the "hub" of applicability, linking to the **PCT** (Product Cross-reference Table) and **CCT** (Conditions Cross-reference Table).

**Standard Pattern:** ACT ↔ (PCT, CCT)

All DMs → ACT → PCT (product instances) + CCT (conditions)

## File Structure

```text
APPLICABILITY/
├─ README.md                                                    # This file
├─ DMC-AMPEL360AT-31-00-00-00W-A-001_001_00_EN-US_001-00.XML  # ACT
├─ DMC-AMPEL360AT-31-00-00-00P-A-001_001_00_EN-US_001-00.XML  # PCT
├─ DMC-AMPEL360AT-31-00-00-00Q-A-001_001_00_EN-US_001-00.XML  # CCT
└─ DMC-AMPEL360AT-31-00-00-0A3-A-001_001_00_EN-US_001-00.XML  # ACT Catalog (optional)
```

## S1000D Info Codes

- **00W** = Applicability Cross-reference Table (**ACT**)
  - The central hub that declares attributes and links to PCT and CCT
  - All AMM DMs reference this ACT in their dmStatus

- **00P** = Product Cross-reference Table (**PCT**)
  - Defines product instances with real attribute values
  - Examples: MSN/Effectivity, installed options, configurations

- **00Q** = Conditions Cross-reference Table (**CCT**)
  - Defines conditions affecting applicability
  - Examples: ground/air, maintenance mode, temperature bands

- **0A3** = Applicability Cross-reference Table Catalog (optional)
  - Used for multi-set ACT/PCT/CCT scenarios
  - Relates which ACT applies to which program/variant/partner

## Module Descriptions

### A) ACT (00W) - Applicability Cross-reference Table

**What it is:** The "hub" of applicability management.

**Purpose:** Declares product attributes (e.g., variant, configuration) and links to PCT and CCT DMs. All DMs in the AMM reference this ACT.

**Expected Content:**
- Product attribute declarations (list of attributes and types)
- References to PCT dmRef and CCT dmRef
- Base rules (e.g., "ALL" when no filter applies)

### B) PCT (00P) - Product Cross-reference Table

**What it is:** Table of product instances with actual attribute values.

**Purpose:** Defines real-world product variations such as MSN/Effectivity, installed options, configuration variants, etc.

**Expected Content:**
- Product instances (e.g., MSN / Block / Config)
- Attribute values per instance
- Alias / equivalences of attributes (if applicable)

### C) CCT (00Q) - Conditions Cross-reference Table

**What it is:** Table of conditions affecting applicability.

**Purpose:** Defines technical, operational, or environmental conditions that filter content (e.g., "ground/air", temperature ranges, "maintenance mode").

**Expected Content:**
- Condition definitions (name, type, values)
- Incorporation status / technical conditions
- Boolean / enumerated conditions

### D) ACT Catalog (0A3) - Optional

**What it is:** Catalog for multi-set ACT/PCT/CCT management.

**Purpose:** Relates which ACT applies to which set/partner in multi-program or multi-partner scenarios. Some toolchains detect this explicitly.

**Expected Content:**
- List of ACT/PCT/CCT sets
- Relationship: set ↔ program/variant/partner
- Selection rules per publication

## Product Attributes (Placeholder Baseline)

For **AMPEL360AT**, the following attributes serve as initial placeholders:

### Product Attributes (ACT/PCT)

| Attribute | Type | Example Values | Description |
|-----------|------|----------------|-------------|
| `aircraftFamily` | String | Q100 | Aircraft family designation |
| `variant` | String | BASELINE, GEN2 | Variant designation |
| `configuration` | String | STANDARD, EXTENDED | Configuration options |
| `msn` | String | MSN001, MSN002 | Manufacturer Serial Number |
| `softwareLoad` | String | SW-V1.0, SW-V2.0 | Software load version (if procedures filter by load) |

### Conditions (CCT)

| Condition | Type | Values | Description |
|-----------|------|--------|-------------|
| `groundAir` | Enumerated | GROUND, AIR | Flight phase |
| `maintenanceMode` | Boolean | TRUE, FALSE | Maintenance mode active |
| `temperatureBand` | Enumerated | LOW, NOM, HIGH | Temperature range (if content filtering applies) |
| `dispatchDegraded` | Boolean | TRUE, FALSE | Degraded dispatch mode |

## Usage Guidelines

1. **For DM Authors:**
   - Reference the ACT in your DM's `<dmStatus>` section
   - Use `<applic>` elements to filter content by attributes/conditions
   - Ensure attribute values match those defined in the PCT

2. **For Configuration Managers:**
   - Update PCT when new product instances are introduced
   - Update CCT when new operational conditions are added
   - Maintain ACT links to ensure consistency

3. **For Publishing:**
   - Publishing tools will use these tables to filter content
   - Ensure all referenced DMCs are valid and accessible
   - Test applicability filtering before release

## References

- [S1000D Issue 5.0 Specification](http://www.s1000d.org/)
- [Adobe FrameMaker S1000D - Applicability](https://help.adobe.com/en_US/framemaker/s1000d/WS9ad62b8fb4f8a997-1d8392ca12e0a8ffdb9-7ff3.html)
- AMPEL360 BREX (Business Rules Exchange) documents in `../BREX/`

## Document Control

- **Directory**: APPLICABILITY
- **Subject**: ATA 31-00-00-general (Indicating/Recording - General)
- **Publication**: AMM (Aircraft Maintenance Manual)
- **Standard**: S1000D Issue 5.0
- **Status**: Active
- **Generated with**: AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
- **Last AI update**: 2026-01-10

# IPC — Illustrated Parts Catalog

## Overview

This directory contains the **Illustrated Parts Catalog (IPC)** for ATA Chapter 22 - Autoflight, organized as an S1000D Common Source Database (CSDB).

## Purpose

The IPC provides complete parts information to:
- Identify parts by illustration and nomenclature
- Determine correct part numbers for ordering
- Verify quantity requirements per assembly
- Check parts applicability to aircraft variants
- Support inventory and procurement planning

## Content Scope

### Parts Information

- **Illustrated Breakdowns**: Exploded view illustrations with item callouts
- **Parts Lists**: Complete part numbers with nomenclature
- **Quantities**: Units required per next higher assembly
- **Reference Designations**: Electrical and mechanical designators
- **Vendor Information**: Manufacturer codes (CAGE) and sources

### Applicability and Effectivity

- **Product Variants**: Which aircraft models use which parts
- **Configuration Options**: Optional equipment parts
- **Serial Number Effectivity**: When parts were introduced/changed
- **Modification Status**: Pre/post-modification part differences
- **Interchangeability**: Substitute and alternate parts

### Procurement Data

- **Part Numbers**: Full P/N including revision letters
- **Nomenclature**: Official part names and descriptions
- **CAGE Codes**: Commercial and Government Entity codes
- **NSN**: NATO Stock Numbers (when applicable)
- **Unit of Issue**: EA (each), SET, KIT, etc.

## CSDB Structure

```
IPC/
└── CSDB/
    ├── DM/              # Data Modules (parts lists)
    ├── PM/              # Publication Modules (catalog structure)
    ├── DML/             # Data Module Lists (parts groupings)
    ├── ICN/             # Illustrations (exploded views, identification)
    ├── BREX/            # Business Rules (validation)
    ├── COMMON/          # Common Information (standard part descriptions)
    └── APPLICABILITY/   # Applicability (product variants, effectivity)
```

Each CSDB subdirectory contains a comprehensive README explaining its purpose, structure, and usage.

## Typical IPC Organization

1. **Introduction**
   - How to use the IPC
   - Part number format explanation
   - Abbreviations and symbols
   - Effectivity explanation

2. **Numerical Index**
   - Parts listed by part number
   - Cross-reference to figure and item number
   - Supersession information

3. **Illustrated Parts Breakdown**
   - Organized by ATA chapter/section
   - Exploded view illustrations
   - Parts lists with item numbers
   - Quantity and applicability data

4. **Vendor Code Cross-Reference**
   - CAGE code directory
   - Manufacturer names and addresses
   - Contact information

## Parts Identification

### Item Numbering

Each part on an illustration is identified by:
- **Item Number**: Sequential (1, 2, 3, etc.)
- **Reference Designation**: System identifier (U1, J5, A10)
- **Find Number**: Larger assembly callout

### Part Number Format

AMPEL360 parts follow this pattern:
```
PN-AMPEL360-{ATA}-{SEQUENCE}-{REV}
```

Example: `PN-AMPEL360-22-1000-A`
- `PN`: Part number prefix
- `AMPEL360`: Project/aircraft
- `22`: ATA chapter (Autoflight)
- `1000`: Sequential number
- `A`: Revision letter

## Users

The IPC is used by:
- **Parts Specialists**: Identify and order correct parts
- **Procurement**: Source parts from vendors
- **Inventory Management**: Stock level planning
- **Maintenance Planning**: Spares provisioning
- **Maintenance Technicians**: Part identification during repairs
- **Quality Assurance**: Verify correct parts installed

## Integration with AMM

IPC works with AMM:
- **AMM References IPC**: Procedures cite figure and item numbers
- **Part Identification**: AMM uses IPC nomenclature
- **Installation Verification**: Confirm correct parts via IPC
- **Removal/Installation**: IPC shows assembly relationships

## Effectivity Management

### Serial Number Effectivity

Parts are tracked by when they apply:
- **001 AND UP**: All aircraft
- **100-200**: Specific serial number range
- **300 TO 999**: From S/N 300 onward

### Modification Effectivity

Parts change with modifications:
- **Before Mod XX-YYY**: Pre-modification part
- **After Mod XX-YYY**: Post-modification part
- **Mod XX-YYY Kit**: Parts in modification kit

### Configuration Management

- Standard configuration parts
- Optional equipment parts
- Customer-specific configurations
- Service Bulletin incorporation

## Supersession and Interchangeability

### Supersession

When parts are replaced by improved versions:
```
Old P/N: PN-AMPEL360-22-1000-A
Superseded by: PN-AMPEL360-22-1000-B
```

### Interchangeability

Alternative parts that are form/fit/function equivalent:
- **Direct Replacement**: No procedure differences
- **With Modification**: Requires installation procedure
- **Not Interchangeable**: Cannot substitute

## Electronic IPC (eIPC)

S1000D format enables:
- **Interactive Navigation**: Click illustrations to see parts
- **Dynamic Filtering**: Show only applicable parts
- **Integrated Search**: Find by P/N, nomenclature, or keywords
- **Hotspots**: Clickable areas on illustrations
- **Cross-References**: Link to related assemblies
- **ERP Integration**: Direct connection to ordering systems

## Regulatory Compliance

IPC supports:
- **Type Certificate requirements**: Parts list validation
- **Airworthiness Directives**: Affected part identification
- **Service Bulletins**: Parts for modifications
- **FAA/EASA Compliance**: Traceable parts records

## Related Publications

- **AMM** (`../AMM/`): Maintenance procedures referencing IPC
- **Component Maintenance Manuals (CMM)**: Detail repair information
- **Service Bulletins (SB)**: Modification parts kits
- **Tool and Equipment Manual**: Special tools and equipment

## Updates

IPC is updated for:
- **New Part Numbers**: Design changes
- **Supersessions**: Improved parts
- **Effectivity Changes**: New variants or modifications
- **Vendor Changes**: New suppliers
- **Error Corrections**: Data accuracy improvements

## S1000D Benefits

Using S1000D for the IPC enables:
- **Modular Updates**: Change only affected assemblies
- **Multiple Outputs**: PDF, HTML, Interactive from single source
- **Product Variants**: Filter by aircraft configuration automatically
- **Translation**: Efficient multilingual catalogs
- **Integration**: Connect to ERP, inventory, procurement systems
- **Accuracy**: Validated against BREX rules

## Navigation

Access CSDB content in `CSDB/` directory. Each subdirectory contains detailed documentation about its contents and usage.

## Document Control

- **Standard**: S1000D Issue 5.0
- **Publication Type**: Illustrated Parts Catalog (IPC)
- **Project**: AMPEL360-AIR-T
- **ATA Chapter**: 22 (Autoflight)
- **Status**: Active
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia

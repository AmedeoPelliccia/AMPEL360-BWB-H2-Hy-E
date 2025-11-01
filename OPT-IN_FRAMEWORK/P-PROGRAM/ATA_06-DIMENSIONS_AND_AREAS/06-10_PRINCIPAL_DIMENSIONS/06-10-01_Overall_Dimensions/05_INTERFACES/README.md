# Interfaces: 06-10-01 - Overall Dimensions

## Purpose
This folder documents all interface definitions and requirements between the overall dimensions component and other aircraft systems and external entities.

## Internal Interfaces (Other ATA Chapters)

### ATA 00-10: Aircraft General Information
- **Interface:** Summary dimensions for Type Certificate Data Sheet (TCDS)
- **Data Flow:** Overall dimensions → TCDS summary
- **Update Frequency:** Any dimensional change

### ATA 07: Lifting and Shoring
- **Interface:** Jack point locations derived from overall dimensions
- **Data Flow:** Reference coordinates → Jack point positions
- **Critical Data:** Main gear location (FS 23,800), nose gear location (FS 2,500)

### ATA 08: Leveling and Weighing
- **Interface:** Datum references and measurement stations
- **Data Flow:** BRS coordinate system → Weight and balance datum
- **Critical Data:** Nose apex datum (FS 0), MAC reference

### ATA 09: Towing and Taxiing
- **Interface:** Tow bar attachment point coordinates
- **Data Flow:** Nose gear dimensions → Tow bar interface
- **Critical Data:** Nose gear height (3.2m), tow bar clearance envelope

### ATA 28: Fuel System
- **Interface:** LH₂ tank location and clearance envelope
- **Data Flow:** Tank dimensions → Overall volume allocation
- **Critical Data:** Tank center (FS 18,500), safety zone boundaries

### ATA 51-57: Structures
- **Interface:** Detailed component dimensions
- **Data Flow:** Overall dimensions → Component breakout
- **Critical Data:** Wing attachment points, center body bulkhead locations

## External Interfaces

### Airport Infrastructure
- **Interface:** Gate compatibility, hangar requirements
- **Data Flow:** Overall dimensions → Airport planning database
- **Standards:** ICAO Annex 14, FAA AC 150/5300-13B
- **Critical Data:** Wingspan (65m), length (52.5m), height (11.2m)

### Ground Support Equipment (GSE)
- **Interface:** Clearance envelopes for GSE operation
- **Data Flow:** Safety zones → GSE operational limits
- **Standards:** SAE ARP6116
- **Critical Data:** Propulsor safety zone (50m aft), fueling zone (10m radius)

### Regulatory Authorities (EASA/FAA)
- **Interface:** Certification basis dimensional data
- **Data Flow:** Measured dimensions → Type design documentation
- **Standards:** CS-25, 14 CFR Part 25
- **Critical Data:** All principal dimensions with tolerances

## Interface Control Documents (ICDs)
- ICD-06-00: Overall Dimensions to Aircraft General Info
- ICD-06-07: Overall Dimensions to Lifting/Shoring
- ICD-06-08: Overall Dimensions to Leveling/Weighing
- ICD-06-09: Overall Dimensions to Towing/Taxiing
- ICD-06-28: Overall Dimensions to Fuel System
- ICD-06-EXT-01: Overall Dimensions to Airport Infrastructure

## Interface Requirements
| Interface | Requirement | Status |
|-----------|-------------|--------|
| Gate clearance | Wingspan ≤65m for Code E | Met |
| Hangar clearance | Height ≤13m standard doors | Met |
| Tow bar interface | Standard NATO tow bar compatible | TBD |
| GSE clearance | Propulsor 3.8m ground clearance | Met |

## Document Status
**Status:** In Development  
**Last Review:** 2025-11-01  
**Next Review:** 2026-05-01

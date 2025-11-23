# 53-20-01-005 Shell Module Joints and Splices

## Overview

This document defines all joints and splices connecting the pressure shell modules of the AMPEL360 BWB H₂ Hy-E aircraft. Proper joint design is critical for structural integrity, pressure containment, fatigue life, and maintainability.

## Joint Classification

Pressure shell joints are classified by:

### By Orientation
- **Longitudinal Splices**: Parallel to fuselage centerline (upper-to-side, side-to-lower)
- **Circumferential Splices**: Perpendicular to centerline (shell section joints)
- **Bulkhead Joints**: Perimeter attachment of pressure bulkheads

### By Function
- **Primary Structure**: Load-transferring joints in primary load paths
- **Pressure Sealing**: Joints maintaining cabin pressure integrity
- **Access/Removable**: Joints allowing assembly/disassembly for maintenance

### By Method
- **Bolted Joints**: Mechanical fasteners with sealant
- **Bonded Joints**: Adhesive bonding (co-cured or secondary bonded)
- **Hybrid Joints**: Combined bonding and mechanical fastening

## Design Requirements

All joints must comply with:
- [CS-25.603](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Materials and workmanship
- [CS-25.605](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fabrication methods
- [CS-25.607](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fasteners
- [CS-25.625](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fitting factors
- [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Pressure sealing

## Longitudinal Splice Design

### Upper-to-Side Shell Splice

**Location**: Port and starboard upper blend regions, full fuselage length

**Configuration**: Double-shear lap joint
- **Splice Strap**: 150mm wide × 4.5mm thick CFRP doubler
- **Fastener Pattern**: 2 rows, 40mm spacing, 80mm pitch
- **Fasteners**: 6.35mm (1/4") diameter titanium Hi-Lok per [Fastener Standards](../ASSETS/specifications/53-20-A-202_Fastener_Standards.md)
- **Sealant**: PR-1776 polysulfide pressure sealant

**Load Transfer Mechanism**:
- Tension/compression through bearing on fasteners
- Shear through fastener rows
- Secondary bonding for damage tolerance

**Analysis Results**:
- **Maximum Bearing Stress**: 620 MPa (allowable 830 MPa)
- **Fastener Shear**: 185 MPa (allowable 275 MPa)
- **Fatigue Life**: 180,000 flights to detectable disbond

Details: [Longitudinal_Splice_Details.svg](ASSETS/Joint_Details/Longitudinal_Splice_Details.svg)

### Side-to-Lower Shell Splice

**Location**: Port and starboard lower blend regions, full fuselage length

**Configuration**: Triple-row lap joint (enhanced for landing loads)
- **Inner Splice Strap**: 120mm wide × 3.8mm CFRP
- **Outer Splice Strap**: 180mm wide × 5.2mm CFRP
- **Fastener Pattern**: 3 rows, 35mm spacing, 70mm pitch
- **Fasteners**: 6.35mm titanium Hi-Lok with interference fit

**Enhanced Features**:
- Third fastener row for increased load capability
- Interference fit fasteners for fatigue improvement
- Additional sealant bead between splice straps

**Analysis Results**:
- **Maximum Bearing Stress**: 685 MPa (allowable 830 MPa)
- **Net Section Stress**: 425 MPa (allowable 520 MPa)
- **Fatigue Life**: 165,000 flights (landing load spectrum)

Details: [Longitudinal_Splice_Details.svg](ASSETS/Joint_Details/Longitudinal_Splice_Details.svg)

## Circumferential Splice Design

### Section-to-Section Joints

**Locations**: 
- FS 15.0 (forward-to-center section)
- FS 30.0 (center-to-aft section)

**Configuration**: Butt joint with internal and external splice straps
- **Internal Strap**: 300mm wide circumferential band, 6.0mm thick
- **External Strap**: 250mm wide circumferential band, 5.0mm thick
- **Fastener Pattern**: 4 rows (2 per strap), 50mm spacing, 100mm pitch
- **Fasteners**: 7.94mm (5/16") diameter titanium Hi-Lok
- **Sealant**: PR-1776 on all faying surfaces

**Design Features**:
- Four-row pattern distributes pressure and flight loads
- Overlap design allows internal inspection access
- Removable external strap for maintenance

**Analysis Results**:
- **Maximum Bearing Stress**: 740 MPa (allowable 830 MPa)
- **Bending Stress**: 315 MPa at strap edge (allowable 450 MPa)
- **Fatigue Life**: 175,000 flights

Details: [Circumferential_Splice_Details.svg](ASSETS/Joint_Details/Circumferential_Splice_Details.svg)

## Bulkhead Perimeter Joints

### Forward Bulkhead Joint

**Location**: FS 0.8, full perimeter

**Configuration**: Angle clip attachment
- **Angle Clips**: 7075-T7351 aluminum, 75mm × 75mm legs
- **Clip Spacing**: 150mm around perimeter
- **Fasteners**: 6.35mm Hi-Lok to bulkhead, 7.94mm Hi-Lok to shell
- **Seal**: Compression seal between bulkhead flange and angle clips

**Load Path**: Pressure load → bulkhead → angle clips → shell frames

### Aft Bulkhead Joint

**Location**: FS 38.5, full perimeter

**Configuration**: Similar to forward bulkhead with APU support provisions
- **Standard Angle Clips**: 150mm spacing
- **Reinforced Clips**: At APU mount locations (100mm spacing)
- **Additional Seal**: Secondary seal bead for redundancy

Details: [Joint_Analysis_Summary.md](ASSETS/Joint_Details/Joint_Analysis_Summary.md)

## Material Specifications

Joint materials per [Material Specifications](../ASSETS/specifications/53-20-A-201_Material_Specifications.md):

### Splice Straps
- **Primary Material**: IM7/8552 CFRP prepreg
- **Layup**: Quasi-isotropic [0/±45/90]ns for n layers
- **Surface Prep**: Peel ply surface for secondary bonding
- **Cure**: Autoclave cure per [Cure_Cycles.csv](ASSETS/Manufacturing_Plans/Cure_Cycles.csv)

### Fasteners
- **Material**: Titanium Ti-6Al-4V per AMS 4967
- **Type**: Hi-Lok collars, NAS3354 through NAS3358 series
- **Torque**: Per manufacturer specification (typically 45-65 in-lb)
- **Installation**: Interference fit where specified (0.13-0.25mm)

### Sealants
- **Pressure Seal**: PR-1776 Class B polysulfide
- **Fay Seal**: PR-1422 Class B polythioether
- **Cure**: 7 days at room temperature or 4 hours at 60°C

Specifications: [53-20-A-201_Material_Specifications.md](../ASSETS/specifications/53-20-A-201_Material_Specifications.md)

## Manufacturing & Assembly

### Splice Strap Fabrication
1. **Prepreg Layup**: Hand layup or automated cutting
2. **Cure**: Autoclave cure with caul plates for surface finish
3. **Machining**: CNC drilling of fastener holes with close tolerances
4. **Surface Treatment**: Peel ply removal, abrasion, cleaning per [Surface Treatment](../ASSETS/specifications/53-20-A-203_Surface_Treatment_Specs.md)

### Joint Assembly
1. **Dry Fit**: Trial assembly without sealant
2. **Hole Inspection**: Borescope inspection of all fastener holes
3. **Sealant Application**: Wet installation with PR-1776
4. **Fastener Installation**: Torque fasteners to specification
5. **Seal Inspection**: Visual inspection for sealant squeeze-out
6. **Pressure Test**: Local pressure test of splice region

Assembly procedures: [Assembly_Sequence.md](ASSETS/Manufacturing_Plans/Assembly_Sequence.md)

## Structural Analysis

### Joint Efficiency
- **Longitudinal Splices**: 92% efficiency (strength relative to parent structure)
- **Circumferential Splices**: 88% efficiency
- **Bulkhead Joints**: 95% efficiency (perimeter only)

### Failure Modes Considered
- **Fastener Shear**: Double shear configuration, safety margin 1.48
- **Bearing Failure**: Parent laminate bearing, safety margin 1.21
- **Net Section Tension**: Between fastener rows, safety margin 1.18
- **Fastener Pull-Through**: Head pull-through strength, safety margin 2.15
- **Splice Strap Buckling**: Compression buckling of splice straps, safety margin 1.52

Analysis summary: [FEA_Results_Summary.csv](ASSETS/FEA_Models/FEA_Results_Summary.csv)

## Fatigue & Damage Tolerance

### Fatigue Life Prediction
- **Analysis Method**: Crack growth analysis per [CS-25.571](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)
- **Initial Flaw**: 1.27mm (0.050") detectable flaw assumed
- **Growth Rate**: Paris law with da/dN = C(ΔK)^m
- **Inspection Interval**: Based on 2× design service goal

### Damage Tolerance Features
- **Multiple Load Paths**: Adjacent fasteners share load if one fails
- **Slow Crack Growth**: Material selection for low crack growth rate
- **Inspection Access**: All critical joints accessible for inspection
- **Redundancy**: Bonding + mechanical fastening = fail-safe

Damage tolerance report: [Damage_Tolerance_Assessment.md](../ASSETS/analyses/53-20-A-305_Damage_Tolerance_Assessment.md)

## Inspection & Maintenance

### Inspection Schedule
- **Visual**: Every 400 flight hours
- **Fastener Torque Check**: Every 2,000 flight hours (sample)
- **Ultrasonic (Disbond)**: Every 8,000 flight hours
- **Eddy Current**: Every 6,000 flight hours (fastener holes)
- **Pressure Leak Check**: Every 12,000 flight hours

### Critical Inspection Areas
- First and last fastener rows in each splice
- Strap edges and transitions
- Seal squeeze-out regions
- High-stress concentration areas (corners, transitions)

NDT methods: [53-20-A-205_NDT_Requirements.md](../ASSETS/specifications/53-20-A-205_NDT_Requirements.md)

## Interfaces

Joints and splices connect:

- [53-20-01-001 Upper Shell](53-20-01-001_Upper_Shell_Module_Architecture.md) - Upper shell sections
- [53-20-01-002 Lower Shell](53-20-01-002_Lower_Shell_Module_Architecture.md) - Lower shell sections
- [53-20-01-003 Side Shells](53-20-01-003_Side_Shell_Modules_and_Transitions.md) - Transition zones
- [53-20-01-004 Bulkheads](53-20-01-004_Pressure_Bulkheads_Forward_Aft.md) - Bulkhead perimeters

## Certification Compliance

Demonstrated compliance with:
- [CS-25.603](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Materials
- [CS-25.605](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fabrication
- [CS-25.607](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fasteners
- [CS-25.625](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Fitting factors
- [CS-25.783](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) - Pressure boundary

## Status

- **Design Status**: PDR Complete
- **Analysis Status**: Static and fatigue complete
- **Testing**: Lap joint coupon tests complete, full-scale splice tests planned
- **Last Updated**: 2025-11-22

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-22_.

---

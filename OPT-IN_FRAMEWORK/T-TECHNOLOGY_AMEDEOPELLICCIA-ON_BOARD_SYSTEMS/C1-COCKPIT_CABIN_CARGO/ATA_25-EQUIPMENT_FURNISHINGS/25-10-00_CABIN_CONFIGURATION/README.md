# ATA 25-10-00: Cabin Configuration

**Framework**: OPT-IN AMEDEOPELLICCIA  
**Axis**: T-TECHNOLOGY  
**Domain**: C1-COCKPIT_CABIN_CARGO  
**ATA Chapter**: 25-10-00  
**Aircraft Platform**: AMPEL360 BWB H₂ Hy-E Q100 INTEGRA

---

## Overview

This directory contains comprehensive documentation for the AMPEL360 Q100 120-passenger cabin configuration. The baseline design optimizes passenger comfort, operational efficiency, and safety within the unique constraints and advantages of the Blended Wing Body (BWB) architecture.

---

## Q100 Configuration Summary

| Parameter | Value |
|-----------|-------|
| **Passengers** | 120 |
| **Seat Configuration** | Mixed: 2-3-2 (Rows 1-12), 2-2-2 (Rows 13-18) |
| **Seat Pitch** | 780 mm (30.7") |
| **Seat Width** | 450 mm (17.7") |
| **Cabin Length** | ~19,240 mm |
| **Cabin Width** | 4,550 mm (midsection) |
| **Aisles** | 2 × 500 mm (dual aisle) |
| **Galleys** | Forward (4.5×2.2×2.0 m) + Aft (4.5×1.8×2.0 m) |
| **Lavatories** | 4 units (900×1,200 mm footprint) |
| **Emergency Exits** | 8 (4 port, 4 starboard) |
| **Overhead Bins** | ~7,200 L total (60 L per passenger) |

---

## Document Structure

### 01_OVERVIEW
Comprehensive specifications and design philosophy documents.

**Key Documents:**
- `Q100_120_Passenger_Cabin_Specifications.md` - Complete cabin specification with all parameters, layout diagrams, and design considerations

### 03_REQUIREMENTS
Detailed functional and performance requirements.

**Key Documents:**
- `RQ-25-10-001_120_Pax_Cabin_Requirements.md` - Complete requirements specification with verification matrix

### 04_DESIGN
Detailed design documentation and layout analysis.

**Key Documents:**
- `DESIGN-25-10-001_Q100_Cabin_Layout_Design.md` - Detailed design with dimensional analysis, cross-sections, and integration considerations

### 06_ENGINEERING
Engineering calculations and analysis.

**Key Documents:**
- `CALC-25-10-001_Cabin_Area_Volume_Calculations.md` - Comprehensive area, volume, and weight calculations

---

## Key Features

### BWB Advantages
1. **Wide Cabin:** 4,550 mm central width enables dual-aisle configuration
2. **Comfort:** 71% more width per passenger vs. conventional narrow-body
3. **Efficiency:** Optimized space utilization with mixed seating densities
4. **Safety:** Multiple emergency exits with 50%+ capacity margin

### Passenger Comfort
- Wide-body seat width (450 mm) in mid-size aircraft
- Generous seat pitch (780 mm)
- High cabin volume (2.67 m³ per passenger)
- Dual aisles reduce congestion
- Large overhead bins (60 L per passenger)

### Operational Efficiency
- Dual galleys support split-cabin service
- 4 lavatories (1 per 30 passengers)
- Fast turnaround (55-65 minutes estimated)
- Efficient boarding/deplaning

---

## Design Status

| Area | Status | Notes |
|------|--------|-------|
| **Overall Layout** | ✓ Complete | Baseline approved |
| **Seating Configuration** | ✓ Complete | 120-pax layout finalized |
| **Galley Design** | ✓ Complete | Dual galley configuration |
| **Lavatory Design** | ⚠ In Progress | Accessible lavatory pending |
| **Emergency Exits** | ✓ Complete | 8 exits with safety margin |
| **Overhead Bins** | ✓ Complete | 7,200 L capacity |
| **Weight Analysis** | ⚠ In Progress | Preliminary estimates complete |
| **3D CAD Model** | ⚠ Planned | Q1 2026 |
| **Physical Mockup** | ⚠ Planned | Q2 2026 |

---

## Compliance and Certification

### Regulatory Basis
- **CS-25 / FAR Part 25:** Primary certification basis
- **Special Conditions:** BWB-specific requirements (in coordination with EASA/FAA)

### Key Certification Requirements
- ✓ CS-25.787: Stowage compartments
- ⚠ CS-25.803: Emergency evacuation (testing scheduled)
- ✓ CS-25.807: Emergency exits (design complete)
- ✓ CS-25.815: Aisle width (compliant)
- ⚠ CS-25.853: Flammability (material selection in progress)
- ⚠ CS-25.562: Seat dynamic testing (pending seat selection)

---

## References

### Internal Documents
- TS-02-10-002: Passenger Capacity Trade Study (220-pax alternative)
- BWB Operations Engineering documentation
- Weight and Balance analysis
- CG envelope calculations

### External References
1. [GitHub - BWB Design Studies](https://github.com/Robbbo-T)
2. [BWB Cabin Design Research](https://escholarship.org/content/qt2nh551hr/qt2nh551hr.pdf)
3. [ICAS 2014 BWB Paper](https://www.icas.org/icas_archive/ICAS2014/data/papers/2014_0740_paper.pdf)
4. [AIAA BWB Technical Paper](https://arc.aiaa.org/doi/pdf/10.2514/1.C037582?download=true)
5. [NASA Cabin Design Study](https://ntrs.nasa.gov/api/citations/20240006450/downloads/SciTech%20Cabin%20MER%20Abstract%20v2.pdf)

---

## Next Steps

### Short Term (Q4 2025)
1. Complete accessible lavatory design
2. Finalize seat manufacturer selection
3. Complete material flammability testing
4. Develop detailed 3D CAD model
5. Initiate certification coordination

### Medium Term (2026 Q1-Q2)
1. Construct physical mockup
2. Conduct human factors evaluation
3. Perform emergency evacuation simulation
4. Complete weight and balance integration
5. Finalize equipment selection

### Long Term (2026 Q3+)
1. 16g seat dynamic testing
2. 90-second evacuation demonstration
3. Certification test program
4. Production documentation
5. Type Certificate Data Sheet preparation

---

## Contact Information

**Cabin Design Lead:** [TBD]  
**Requirements Engineer:** [TBD]  
**Certification Coordinator:** [TBD]  
**Project Manager:** [TBD]

---

## Document Control

**Created:** 2025-11-10  
**Status:** Active Development  
**Next Review:** 2026-Q1  
**Version:** 1.0

---

## Related ATA Chapters

- **ATA 02-10:** Aircraft General Data (performance, weight)
- **ATA 25-20:** Seats (detailed seat specifications)
- **ATA 25-30:** Galleys (equipment specifications)
- **ATA 25-40:** Lavatories (equipment specifications)
- **ATA 25-60:** Emergency Equipment
- **ATA 52:** Doors (emergency exit doors)

---

*For detailed specifications, see the documents in the subdirectories.*

---

**END OF README**

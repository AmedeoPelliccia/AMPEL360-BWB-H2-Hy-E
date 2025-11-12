# Dimension Measurement Fixtures
# Production Quality Control System

**System ID:** DMF-02-10-001  
**Date:** 2026-Q3 (Planned)  
**Status:** Design Phase  
**Purpose:** Production dimensional validation

---

## 1. Overview

### 1.1 Purpose

Establish precision measurement system for validating aircraft dimensions during production:
- Verify compliance with dimensional tolerances (±1 mm critical features)
- Ensure interchangeability of components
- Support quality assurance and certification requirements
- Provide traceability for production records

### 1.2 Measurement Approach

**Multi-Technology Strategy:**
1. **Laser Photogrammetry** - Overall airframe geometry (full 3D scan)
2. **Laser Tracker** - Critical reference points and interfaces
3. **Coordinate Measuring Machine (CMM)** - Small components and details
4. **Manual Gauges** - Quick checks and in-situ measurements

---

## 2. Laser Photogrammetry System

### 2.1 Equipment

**System:** ATOS Q 12M (GOM / Zeiss)
- Measurement volume: 12,000 mm × 9,000 mm × 7,500 mm
- Point spacing: 0.1 mm
- Accuracy: ±0.03 mm + 0.015 mm/m
- Scan time: 2-3 seconds per position
- Total points per scan: ~5 million

**Application:** Full airframe surface scanning
- Wing geometry validation
- Fuselage contour verification
- Control surface alignment
- Overall dimensions check

### 2.2 Procedure

1. Apply photogrammetry targets (coded + non-coded, 200-300 per aircraft)
2. Establish reference coordinate system (nose apex origin)
3. Perform multi-position scanning (15-20 positions for full coverage)
4. Post-process scan data (alignment, merge, noise filtering)
5. Compare to nominal CAD model (color-coded deviation map)
6. Generate inspection report

**Acceptance Criteria:**
- 95% of surface within ±2 mm of nominal
- 99% of critical features within ±1 mm
- Zero deviations > ±5 mm

**Frequency:** Every aircraft (100% inspection)

---

## 3. Laser Tracker System

### 3.1 Equipment

**System:** Leica AT960
- Range: 160 m (spherically mounted retroreflector)
- Accuracy: ±15 μm + 6 μm/m
- Measurement rate: 1000 points/sec
- Environmental compensation: Temperature, pressure, humidity

**Application:** Critical reference points
- Landing gear attachment points (6 locations)
- Engine mount interfaces (4 locations)
- Control surface hinge lines (12 locations)
- Fuel tank mounting (8 locations)
- Wing-to-fuselage interface (20 locations)

### 3.2 Measurement Procedure

**Reference Network:**
- Establish 8-10 reference nests around aircraft
- Verify network stability (daily checks)
- Coordinate system aligned to aircraft datum

**Measurement Protocol:**
1. Preheat tracker (30 min temperature stabilization)
2. Check reference nests (verify stability within ±0.1 mm)
3. Measure critical features using SMR (Spherically Mounted Retroreflector)
4. Record temperature, pressure, humidity for compensation
5. Analyze results vs. tolerance (real-time display)

**Frequency:** Critical assembly stages (wing attach, final assembly)

---

## 4. Coordinate Measuring Machine (CMM)

### 4.1 Equipment

**System:** Zeiss CONTURA G2
- Measuring range: 1000 × 1200 × 800 mm
- Accuracy: (1.5 + L/300) μm (L in mm)
- Probe: VAST XXT scanning probe head
- Environmental: Temperature-controlled room (20°C ± 1°C)

**Application:** Component-level inspection
- Machined fittings and brackets
- Composite panel thickness
- Hole pattern verification
- Thread inspection

### 4.2 Inspection Programs

**Automated Programs:** 
- 50+ part programs (critical components)
- Statistical process control (SPC) integration
- Automatic report generation

**Sampling Plan:** 
- First article: 100% features
- Production: 10% sample or per control plan

---

## 5. Manual Measurement Tools

### 5.1 Tool Set

| Tool | Specification | Application |
|------|--------------|-------------|
| **Digital Caliper** | Mitutoyo 500 series, ±0.01 mm | General dimensions |
| **Height Gauge** | Mitutoyo HDS-30C, ±0.015 mm | Vertical measurements |
| **Depth Gauge** | Starrett 449, ±0.02 mm | Hole depths, recesses |
| **Radius Gauge** | Set 1-25 mm, ±0.1 mm | Fillet radii |
| **Angle Gauge** | Digital protractor, ±0.1° | Angle verification |
| **Go/No-Go Gauges** | Custom, ±0.01 mm | Fastener holes |

### 5.2 Calibration

**Schedule:** All tools calibrated annually (NIST traceable)  
**Records:** Calibration certificates maintained in QMS

---

## 6. Measurement Traceability

### 6.1 Coordinate System

**Aircraft Reference:**
- Origin: Nose apex
- X-axis: Longitudinal (forward positive)
- Y-axis: Lateral (right positive)
- Z-axis: Vertical (up positive)

**Datum Features:**
- Fuselage Station 0 (FS 0): Nose apex
- Buttock Line 0 (BL 0): Centerline
- Water Line 0 (WL 0): Fuselage bottom at FS 0

### 6.2 Data Management

**Software:** Polyworks Inspector (scanning data), Spatial Analyzer (tracker data)
- Automatic report generation
- Integration with PLM system (Teamcenter)
- Deviation analysis and trending

**Records Retention:** 50 years (aircraft lifetime + 20 years)

---

## 7. Budget and Schedule

### 7.1 Equipment Costs

| Item | Quantity | Unit Cost (€) | Total (€) |
|------|----------|--------------|----------|
| ATOS Q 12M System | 1 | 180,000 | 180,000 |
| Leica AT960 Tracker | 2 | 85,000 | 170,000 |
| Zeiss CONTURA CMM | 1 | 150,000 | 150,000 |
| Manual Tools Set | 10 | 2,000 | 20,000 |
| Software Licenses | - | 25,000 | 25,000 |
| Calibration Lab Setup | - | 30,000 | 30,000 |
| **Total** | - | - | **575,000** |

### 7.2 Timeline

- Equipment procurement: Q1 2026
- Installation & training: Q2 2026
- System validation: Q3 2026
- Production ready: Q4 2026

---

## 8. Deliverables

1. **Measurement Procedures** - Standard work instructions for each system
2. **Inspection Programs** - Automated CMM and tracker programs
3. **Calibration Plan** - Schedule and procedures for all equipment
4. **Training Materials** - Operator certification program
5. **Quality Records Template** - Inspection report formats

---

**Document Owner:** Quality Assurance Manager  
**Approval:** [ ] Manufacturing Engineer | [ ] QA Manager | [ ] Chief Engineer  
**Status:** Design Phase / Equipment Procurement Q1 2026

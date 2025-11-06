# PNR-02-10-203 - CG Calculation Tools

**Part Number:** PNR-02-10-203  
**Type:** GSE / Software  
**Manufacturer:** AMPEL360  
**Status:** Active

## Description

Comprehensive center of gravity calculation and weight & balance management system for the AMPEL360 BWB H2 Hy-E aircraft. Includes software, hardware interfaces, and documentation for accurate CG determination.

## System Components

### 1. Software Suite

#### CG Calculation Software v3.2
- **Platform:** Windows 10/11, Linux, tablet app
- **Functions:**
  - Real-time weight and CG calculations
  - Multiple loading scenarios
  - Fuel loading optimization
  - Cargo/passenger distribution
  - Graphical CG envelope display
  - Historical data logging

- **Features:**
  - 3D aircraft model visualization
  - What-if scenario analysis
  - Regulatory compliance checking
  - PDF report generation
  - Integration with weighing equipment
  - Cloud backup capability

#### Database Module
- **Aircraft Data:**
  - Empty weight and CG
  - Equipment list with weights and arms
  - Fuel tank positions and capacities
  - Cargo bay positions and limits
  - Seat positions and passenger weights

- **Configuration Management:**
  - Track modifications
  - Update weight changes
  - Maintain historical records
  - Audit trail for all changes

### 2. Hardware Components

#### Tablet Computer (Ruggedized)
- **Specifications:**
  - 12-inch touchscreen display
  - IP65 rated (dust/water resistant)
  - 12-hour battery life
  - Wi-Fi and cellular connectivity
  - USB ports for weighing equipment interface

#### Wireless Scale Interface
- **Connectivity:** Bluetooth 5.0
- **Range:** 30m line-of-sight
- **Battery:** Rechargeable, 24-hour operation
- **Compatibility:** Standard load cell output (0-5V, 4-20mA)

#### Portable Printer
- **Type:** Thermal, battery-powered
- **Paper:** 80mm wide, roll feed
- **Output:** Weight & balance reports, CG charts

### 3. Reference Materials

#### BWB-Specific CG Calculation Guide
- **Contents:**
  - MAC (Mean Aerodynamic Chord) definition for BWB
  - Station-to-MAC conversion tables
  - Moment arm references
  - Sample calculations
  - Troubleshooting guide

#### Cargo Loading Planner
- **Format:** Laminated charts and digital templates
- **Information:**
  - Cargo bay dimensions and positions
  - Maximum floor loading
  - Tie-down point locations
  - Loading sequence recommendations

## CG Calculation Methodology

### Basic Formula
```
CG Position (% MAC) = (Total Moment / Total Weight - LEMAC Station) / MAC Length × 100

Where:
- Total Moment = Σ(Weight × Arm)
- LEMAC (Leading Edge MAC) = Station 450 for BWB
- MAC Length = 300 stations/units (Station 450 to 750)  <!-- If stations are unitless or not defined as mm -->
```

### Loading Stations Reference
```
Station    Description              Typical Use
FS 100     Forward cargo bay        Baggage, cargo
FS 250     Cabin forward            Passengers
FS 400     Cabin center             Passengers, galley
FS 550     Cabin aft                Passengers
FS 700     Aft cargo bay            Baggage, cargo
FS 850     Tail section             Equipment
```

### Fuel Moments
```
Tank Location    Capacity (kg)    Arm (Station)    Full Tank Moment
Forward Tank     5,000            FS 200           1,000,000
Center Tank L    15,000           FS 450           6,750,000
Center Tank R    15,000           FS 450           6,750,000
Aft Tank         8,000            FS 700           5,600,000
```

## Operating Procedures

### 1. Pre-Flight CG Calculation
1. Load current empty weight and CG into software
2. Enter passenger count and distribution
3. Input cargo weights and positions
4. Specify fuel load (departure and landing)
5. Review CG envelope plot
6. Generate and file load sheet

### 2. In-Flight CG Monitoring
- Software tracks fuel burn
- Updates CG position in real-time
- Alerts if approaching limits
- Suggests fuel transfer if needed

### 3. Post-Modification Updates
- Weigh aircraft after modifications
- Update software database
- Recalculate empty CG
- Document in aircraft log

## CG Limits (BWB Configuration)

### Normal Category
- **Forward Limit:** 15% MAC (Station 495)
- **Aft Limit:** 35% MAC (Station 555)
- **Lateral Limit:** ±5% span (±35mm from centerline)

### Maximum Weight Conditions
- **MTOW:** CG range 20-30% MAC
- **MLW:** CG range 18-32% MAC
- **MZFW:** CG range 17-33% MAC

## Compliance and Validation

- **Regulatory:** Complies with EASA CS-25, FAA FAR Part 25
- **Accuracy Requirements:** ±0.5% MAC
- **Verification:** Monthly ground check, annual recalibration
- **Documentation:** All calculations logged and archived

## Training Requirements

- Initial training: 8 hours classroom + 4 hours practical
- Annual recurrent: 2 hours
- Certification: Weight and Balance Specialist (WBS)

## Related Documents

- Weight and Balance Manual (WBM-AMPEL360-001)
- Aircraft Loading Manual (ALM-BWB-H2-E)
- AMM 02-10-12 CG Calculation Procedures
- PNR-02-10-103 CG Reference Markers
- PNR-02-10-201 Weighing Kit

---

**Document Control:**
- Version: 1.0
- Status: Active
- Last Updated: 2025-11-05
- Software Version: 3.2.0
- Database Schema: v2.1

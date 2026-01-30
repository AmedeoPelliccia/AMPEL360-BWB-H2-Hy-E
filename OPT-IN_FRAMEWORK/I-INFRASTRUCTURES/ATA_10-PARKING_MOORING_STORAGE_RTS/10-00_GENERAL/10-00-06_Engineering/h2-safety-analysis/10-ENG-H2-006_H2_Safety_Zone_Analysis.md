# 10-ENG-H2-006 - H2 Safety Zone Analysis

## 1. Analysis Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-ENG-H2-006 |
| Analysis Type | Safety Analysis - ATEX Classification |
| Software/Tools | Risk Assessment, ATEX Analysis |
| Status | Draft |
| Revision | A |
| Date | 2025-12-09 |

## 2. Purpose

Determine safety zones and ATEX (ATmosphères EXplosibles) classification around AMPEL360-BWB-H2 aircraft during ground operations. Define exclusion zones, establish access restrictions, specify equipment requirements, and ensure personnel safety in accordance with hydrogen safety standards.

## 3. Scope

- ATEX zone classification per IEC 60079-10-1
- Safety zone determination based on dispersion analysis
- Exclusion zone definition for personnel and equipment
- Ignition source control requirements
- Equipment classification and certification
- Operational procedures for zone management

## 4. Applicable Documents

- IEC 60079-10-1 - Explosive atmospheres classification (gases)
- NFPA 2 - Hydrogen Technologies Code
- SAE AS6968 - Hydrogen Aircraft Systems
- ISO 13984 - Liquid Hydrogen Systems
- 10-ENG-H2-001 - H2 Dispersion Analysis
- ATEX Directive 2014/34/EU

## 5. Input Data

| Parameter | Value | Unit | Source |
|-----------|-------|------|--------|
| LFL (Lower Flammability Limit) | 4 | % vol | H2 Properties |
| UFL (Upper Flammability Limit) | 75 | % vol | H2 Properties |
| Normal Vent Rate | 0.85 | kg/hr | 10-ENG-H2-005 |
| Emergency Vent Rate | 125 | kg/min | 10-ENG-H2-004 |
| Small Leak Rate | 0.05 | kg/s | 10-ENG-H2-002 |
| Large Leak Rate | 2.5 | kg/s | 10-ENG-H2-002 |
| LFL Distance (worst case) | 12 | m | 10-ENG-H2-001 |

## 6. Assumptions

1. **Worst-Case Scenario**: ATEX zones based on most severe credible conditions
2. **Wind Conditions**: Low wind (2 m/s) for zone extent
3. **Continuous Release Potential**: Zones assume release can persist
4. **Indoor Facility**: Classification for hangared operations
5. **Mechanical Ventilation**: Adequate ventilation available

## 7. Methodology

### 7.1 Release Characterization
- Identify all H2 release sources
- Classify release grade (continuous, primary, secondary)
- Determine release rate and duration

### 7.2 ATEX Zone Classification
- Zone 0: Explosive atmosphere present continuously or for long periods
- Zone 1: Explosive atmosphere likely during normal operations
- Zone 2: Explosive atmosphere unlikely or only for short periods

### 7.3 Zone Extent Calculation
- Based on dispersion analysis (10-ENG-H2-001)
- Considers ventilation effectiveness
- Applies safety margins

## 8. Analysis

### 8.1 Release Source Classification

| Source | Location | Release Grade | Zone Classification |
|--------|----------|---------------|---------------------|
| Vent Stack Outlet | 8.5m height | Continuous | Zone 0 (vent), Zone 2 (ground) |
| Tank Fittings | Center body | Secondary | Zone 2 |
| Transfer Connections | Lower fuselage | Secondary | Zone 2 |
| Pressure Relief Valve | Vent stack | Primary | Zone 1 (vent path) |
| Service Couplings | Service panel | Secondary | Zone 2 |

### 8.2 ATEX Zone Extents

**Zone 0: Continuous Explosive Atmosphere**
- **Location**: Vent stack outlet immediate vicinity
- **Extent**: 1m radius sphere around vent outlet
- **Height**: 7.5m to 9.5m above ground
- **Duration**: Continuous during LH2 storage
- **Access**: Prohibited

**Zone 1: Likely Explosive Atmosphere**
- **Location**: Vent stack path and emergency relief path
- **Extent**: 3m radius cylinder around vent stack (full height)
- **Height**: Ground to 10m
- **Duration**: During emergency venting
- **Access**: Restricted, authorized personnel only with hot work permit

**Zone 2: Unlikely Explosive Atmosphere**
- **Location**: Around aircraft fuel system components
- **Horizontal Extent**: 
  - 5m radius around vent stack base
  - 3m radius around tank fittings and connections
  - 2m radius around service points
- **Vertical Extent**: Ground to 3m height
- **Duration**: Transient during fueling, defueling, or leaks
- **Access**: Controlled, trained personnel, appropriate equipment

### 8.3 Detailed Zone Map

**Around Vent Stack:**
| Zone | Radius (m) | Height Range (m) | Equipment Category | Personnel Access |
|------|------------|------------------|---------------------|------------------|
| Zone 0 | 1 | 7.5-9.5 | Category 1 | Prohibited |
| Zone 1 | 3 | 0-10 | Category 2 | Restricted |
| Zone 2 | 5 | 0-3 | Category 3 | Controlled |

**Around Tank Fittings:**
| Zone | Radius (m) | Height Range (m) | Equipment Category | Personnel Access |
|------|------------|------------------|---------------------|------------------|
| Zone 2 | 3 | 0-2 | Category 3 | Controlled |

**Around Service Connections:**
| Zone | Radius (m) | Height Range (m) | Equipment Category | Personnel Access |
|------|------------|------------------|---------------------|------------------|
| Zone 2 | 2 | 0-1.5 | Category 3 | Controlled |

### 8.4 Equipment Requirements by Zone

**Zone 0 (if equipment required):**
- Equipment Category: 1G (Group IIC, Temperature Class T1)
- Protection: Ex ia, Ex ma
- No equipment recommended in this zone

**Zone 1:**
- Equipment Category: 2G (Group IIC, Temperature Class T1)
- Protection: Ex d, Ex p, Ex e
- Examples: Cameras, sensors, lighting (if required)

**Zone 2:**
- Equipment Category: 3G (Group IIC, Temperature Class T1)
- Protection: Ex n, Ex nA, standard industrial equipment
- Examples: Ground support equipment, tools, vehicles

**H2 Equipment Group: IIC (Most stringent)**
- H2 has smallest MESG (Maximum Experimental Safe Gap): 0.29mm
- H2 has lowest MIC (Minimum Ignition Current): 0.016 mA
- Requires most restrictive equipment design

**Temperature Class: T1**
- H2 autoignition temperature: 560°C
- T1 class: Surface temp <450°C
- Provides adequate safety margin

### 8.5 Exclusion Zones for Specific Operations

**During Fueling/Defueling:**
- Inner Zone: 10m radius - No ignition sources, trained personnel only
- Outer Zone: 20m radius - Restricted access, no hot work

**During Maintenance (Tank Open):**
- Inner Zone: 15m radius - Full H2 safety protocol
- Outer Zone: 30m radius - No ignition sources

**Normal Parked (Sealed System):**
- Safety Zone: 5m radius - Standard precautions
- No specific restrictions beyond ATEX compliance

### 8.6 Ignition Source Control

**Prohibited within Zone 2 and above:**
- Open flames (smoking, cutting, welding)
- Spark-producing tools
- Non-certified electrical equipment
- Vehicles without proper exhaust systems
- Hot surfaces >300°C
- Electrostatic discharge sources
- Portable heaters
- Cell phones (in Zone 1)

**Permitted with precautions:**
- Intrinsically safe (IS) equipment
- Certified ATEX equipment appropriate to zone
- Bonding and grounding procedures
- ESD-safe clothing and footwear

## 9. Results

| Zone | Total Volume (m³) | Equipment Category | Access Level | Approx. Area (m²) |
|------|-------------------|---------------------|--------------|-------------------|
| Zone 0 | 4.2 | 1G | Prohibited | 3.1 |
| Zone 1 | 283 | 2G | Restricted | 28.3 |
| Zone 2 | 863 | 3G | Controlled | 196 |

## 10. H2/BWB Considerations

### BWB Advantages
- High vent outlet on upper center body provides good separation from personnel zones
- Wide upper surface keeps vent away from edges
- Distributed fuel system minimizes concentrated hazard zones

### H2 Characteristics Impact on Zones
- **Buoyancy**: Rising H2 reduces ground-level zone extents
- **High Diffusivity**: Rapid dispersion reduces zone size vs. heavier gases
- **Wide Flammability**: 4-75% range requires conservative classification
- **Low Ignition Energy**: 0.02 mJ necessitates strict ignition source control

## 11. Conclusions

1. **Zone 0 Minimal**: Only 1m radius at vent outlet; easily avoided
2. **Zone 1 Limited**: 3m radius around vent; manageable restriction
3. **Zone 2 Reasonable**: 5m radius; normal operations possible with precautions
4. **Equipment Available**: ATEX-certified equipment readily available for all zones
5. **Operational Impact**: Safety zones do not preclude normal ground operations

## 12. Recommendations

1. **Signage and Marking:**
   - Clear ATEX zone boundary markings on ground
   - Warning signs at zone entrances
   - Vent outlet hazard indication

2. **Personnel Requirements:**
   - H2 safety training for all personnel
   - ATEX awareness for personnel working in classified zones
   - Emergency response training

3. **Equipment Management:**
   - Inventory and certify all equipment for appropriate zones
   - Regular inspection of ATEX equipment
   - Maintenance procedures for certified equipment

4. **Operational Procedures:**
   - Hot work permit system for Zone 2 and beyond
   - Access control for Zone 1
   - Continuous H2 monitoring in all zones
   - Emergency procedures for zone evacuation

5. **Monitoring:**
   - Install H2 detectors at zone boundaries
   - Alarm at 25% LFL (1% vol H2)
   - Continuous monitoring during fuel onboard

6. **Ventilation:**
   - Ensure adequate natural or mechanical ventilation
   - Ventilation rate: 6 air changes/hour minimum
   - Monitor ventilation system operation

7. **Documentation:**
   - Maintain ATEX classification documentation
   - Update zones if operations change
   - Annual review of zone classification

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | Engineering Team | Initial release - ATEX zone classification |

---

**Document Control**
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **DRAFT** – Subject to human review and approval
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-09

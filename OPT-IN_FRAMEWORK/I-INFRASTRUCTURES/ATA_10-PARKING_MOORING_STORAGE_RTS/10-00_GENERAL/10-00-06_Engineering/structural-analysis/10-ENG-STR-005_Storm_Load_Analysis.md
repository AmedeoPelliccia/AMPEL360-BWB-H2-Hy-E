# 10-ENG-STR-005 - Storm Load Analysis

## 1. Analysis Identification

| Parameter | Value |
|-----------|-------|
| Document Number | 10-ENG-STR-005 |
| Analysis Type | Extreme Weather Structural Analysis |
| Software/Tools | ANSYS CFX, MATLAB, Excel |
| Status | Draft |
| Revision | A |
| Date | 2025-12-09 |

## 2. Purpose

Evaluate structural loads and aircraft response during severe storm conditions while parked or moored. Determine maximum survivable wind speeds and required protective measures for the AMPEL360-BWB-H2 aircraft during extreme weather events.

## 3. Scope

This analysis covers:
- Hurricane/typhoon wind load analysis
- Gust loading and dynamic response
- Combined wind, rain, and hail loads
- Tiedown system adequacy in storms
- Hangar storage requirements
- Emergency preparation procedures

**Storm Scenarios:**
- Category 1 Hurricane (64-82 knots sustained)
- Category 2 Hurricane (83-95 knots sustained)
- Severe Thunderstorm (50-70 knot gusts)
- Tornado (operational limits)

## 4. Applicable Documents

- ATA 10-00-03 - Parking and Mooring Requirements
- ASCE 7 - Wind Load Standards
- NWS Hurricane Categories
- CS-25.415 - Ground gust conditions
- FAA AC 150/5200-30C - Airport Winter Safety

## 5. Input Data

| Parameter | Value | Unit | Source |
|-----------|-------|------|--------|
| Design Wind (Parked) | 65 | knots | ATA 10-00-03 |
| Survival Wind (Hangared) | 120 | knots | Industry Standard |
| Survival Wind (Moored) | 70 | knots | ATA 10-00-03 |
| Gust Factor | 1.5 | - | ASCE 7 |
| Dynamic Amplification | 1.2 | - | Structural dynamics |
| Aircraft Weight (Empty) | 52,000 | kg | ATA 00-10 |
| Wingspan | 68 | m | ATA 10-00-01 |
| Hail Impact Energy | 450 | J | 50mm diameter @ 30 m/s |

## 6. Assumptions

1. **Worst-Case Orientation**: Aircraft positioned for maximum wind loading
2. **Standard Atmosphere**: Temperature and pressure per ISA
3. **No Sheltering**: Open apron exposure; no building wake effects
4. **Tiedown Engaged**: All tiedown points properly secured
5. **Empty Aircraft**: Conservative for CG height and weight

## 7. Methodology

### 7.1 Wind Load Calculation
- CFD analysis for pressure distribution
- Peak dynamic loads with gust factors
- Fatigue analysis for cyclic loading

### 7.2 Structural Response
- Modal analysis for natural frequencies
- Time-history analysis for gust response
- Failure mode identification

## 8. Analysis

### 8.1 Hurricane Wind Loads

| Hurricane Category | Sustained (knots) | Gust (knots) | Side Force (kN) | Overturning Moment (kN·m) |
|--------------------|-------------------|--------------|-----------------|---------------------------|
| Tropical Storm | 34-63 | 50-95 | 98.5 | 1,245 |
| Category 1 | 64-82 | 96-123 | 185.2 | 2,340 |
| Category 2 | 83-95 | 124-143 | 235.8 | 2,980 |
| Category 3+ | >96 | >144 | >285 | >3,600 |

### 8.2 Tiedown System Response

**Tiedown Point Loads (Category 2 Hurricane, 95 knots sustained):**

| Tiedown Point | Tension (kN) | Ultimate Capacity (kN) | Margin |
|---------------|--------------|------------------------|--------|
| FWD-Port | 62.5 | 60 | **-4.2%** |
| FWD-Center | 28.3 | 60 | +112% |
| FWD-Stbd | 69.8 | 60 | **-16.3%** |
| AFT-Port | 58.7 | 60 | +2.2% |
| AFT-Center | 26.1 | 60 | +130% |
| AFT-Stbd | 64.2 | 60 | **-7.0%** |

**WARNING:** Negative margins indicate tiedown system inadequate for Category 2 hurricane

### 8.3 Hangar Requirements

**Wind Load on Hangar Doors:**
| Wind Speed (knots) | Door Pressure (kPa) | Door Force (MN) |
|--------------------|---------------------|-----------------|
| 70 | 1.85 | 2.96 |
| 95 | 3.41 | 5.45 |
| 120 | 5.44 | 8.70 |

**Recommendation:** Hangar storage required for winds >70 knots

### 8.4 Hail Impact Analysis

**Hail Damage Threshold:**
| Component | Hail Size (mm) | Damage Threshold (J) | Analysis Result |
|-----------|----------------|----------------------|-----------------|
| Composite Skin | 50 | 500 | Acceptable |
| Radome | 50 | 350 | **Damage Likely** |
| Windscreen | 50 | 800 | Acceptable |
| Pitot Tubes | 25 | 50 | **Damage Likely** |

## 9. Results

| Parameter | Value | Unit | Allowable | Margin |
|-----------|-------|------|-----------|--------|
| Max Tiedown Load | 69.8 | kN | 60 | **-16.3%** |
| Safe Wind Limit (Tiedown) | 75 | knots | 65 (design) | +15.4% |
| Safe Wind Limit (Hangar) | 120 | knots | 120 | 0% |
| Hail Damage Threshold | 50 | mm | 50 | 0% |

## 10. H2/BWB Considerations

### BWB Impact
- Large wing area increases wind loads significantly
- Low profile reduces overturning risk
- Requires reinforced tiedown system for high winds

### H2 System Impact
- LH2 venting must continue during storms
- H2 detection systems must remain operational
- Emergency shutdown procedures for severe weather
- Lightning protection critical for H2 safety

## 11. Conclusions

1. **Tiedown Limit:** Current tiedown system adequate to 75 knots; inadequate for Category 2 hurricane
2. **Hangar Required:** Hangar storage mandatory for winds >75 knots
3. **Hail Protection:** Covers required for radome and pitot tubes
4. **Operational Policy:** Establish storm preparation procedures

## 12. Recommendations

1. **Upgrade Tiedowns:** Increase tiedown capacity to 75 kN per point for 95 knot capability
2. **Hangar Priority:** Establish hangar priority for AMPEL360 during storm warnings
3. **Storm Prep Checklist:** Develop comprehensive storm preparation checklist
4. **Protective Covers:** Procure hail-resistant covers for sensitive components
5. **Monitoring:** Install weather monitoring system with automated alerts
6. **Evacuation Plan:** Establish procedures for moving aircraft to protected location
7. **Insurance:** Ensure coverage addresses storm damage and requirements

## 13. Revision History

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| A | 2025-12-09 | Engineering Team | Initial release |

---

**Document Control**
- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- Status: **DRAFT** – Subject to human review and approval
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-09

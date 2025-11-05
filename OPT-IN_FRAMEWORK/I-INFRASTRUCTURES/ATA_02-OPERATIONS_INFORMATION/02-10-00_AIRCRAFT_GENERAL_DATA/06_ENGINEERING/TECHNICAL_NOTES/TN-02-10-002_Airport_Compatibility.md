# TN-02-10-002: Airport Compatibility Analysis

**Document ID:** TN-02-10-002  
**Title:** AMPEL360 Airport Infrastructure Compatibility  
**Project:** AMPEL360 BWB H₂ Hy-E Q100 INTEGRA  
**Date:** 2025-11-05  
**Author:** AMPEL360 Engineering Team  
**Classification:** Technical Note

---

## Summary

This technical note addresses airport compatibility for the AMPEL360 BWB aircraft, focusing on physical infrastructure requirements, ground handling considerations, and hydrogen refueling capability.

---

## 1. ICAO Classification

### 1.1 Aircraft Code

**AMPEL360 Classification: Code E**

| Parameter | Value | Code E Range |
|-----------|-------|--------------|
| Wingspan | 70.0 m | 65-80 m ✓ |
| Outer Main Gear Span | 9.0 m | <9 m (Code D) ⚠ |
| Length | 42.0 m | <52 m ✓ |

**Note:** Wingspan drives Code E classification, even though gear span is Code D.

### 1.2 Implications

**Code E Requirements:**
- Taxiway width: 23 m (centerline to edge: 11.5 m)
- Runway width: 45 m minimum
- Taxiway/runway separation: 182.5 m
- Apron parking: 80 m × 80 m minimum
- **Global airport availability: ~3,000 airports**

---

## 2. Physical Dimensions

### 2.1 Critical Clearances

| Dimension | Value | ICAO Requirement | Margin |
|-----------|-------|------------------|--------|
| **Wingspan** | 70.0 m | 65-80 m (Code E) | 10.0 m |
| **Length** | 42.0 m | <52 m (Code E) | 10.0 m |
| **Height** | 12.5 m | <15 m typical | 2.5 m |
| **Wheelbase** | 19.0 m | N/A | - |
| **Wheel Track** | 9.0 m | <14 m (Code E) | 5.0 m ✓ |

### 2.2 Ground Clearances

**Minimum Clearances (Static):**
- Fuselage belly: 0.80 m
- Engine nacelles: 0.95 m
- Wingtips: 1.20 m
- Tail cone: 1.85 m

**All adequate for standard airport surfaces** ✓

---

## 3. Taxiway Operations

### 3.1 Turning Radius

**Nose Gear Steering:**
- Maximum steering angle: 70°
- Minimum turn radius (outer wingtip): 42 m
- Minimum turn radius (nose): 15 m

**Taxiway Requirements:**
- 90° turn minimum radius: 50 m (standard = 45 m for Code E) ✓
- 180° turn minimum width: 60 m

### 3.2 Taxiway Clearances

**At 23m Taxiway (Code E Standard):**
- Centerline to edge: 11.5 m
- Wingtip to edge: 11.5 - 35 = **-23.5 m ❌**
- **Requires careful centerline tracking**

**Safe Operation:**
- Pilot awareness critical
- Wing walkers may be required initially
- Taxiway center line lighting essential
- Consider wider 30m taxiways for primary routes

### 3.3 Wingspan Sensitivity

**Wingtip Awareness:**
- 70m span = 35m from centerline each side
- Code E taxiway = 11.5m clearance
- **Margin: Only 1.5m from wingtip to taxiway edge**
- Requires precise taxi technique

**Mitigation:**
- Enhanced pilot training
- Marshaller guidance
- Camera/sensor systems on wingtips
- Paint markings on taxiways

---

## 4. Runway Operations

### 4.1 Runway Requirements

**Takeoff:**
- Required distance (MTOW, sea level, ISA): 2,150 m
- Balanced field length: 2,280 m
- **Recommended runway: 2,500 m minimum** (safety margin)

**Landing:**
- Required distance (MLW, sea level, ISA): 1,650 m
- **Recommended runway: 2,000 m minimum**

**Runway Width:**
- ICAO minimum (Code E): 45 m
- AMPEL360 comfortable: 45 m ✓
- Ideal: 60 m (more margin for crosswinds)

### 4.2 Crosswind Limitations

**Maximum Demonstrated Crosswind:**
- 30 kts (15 m/s) - typical for Code E
- 40 kts with autoland
- BWB configuration may have good crosswind handling due to high inertia

---

## 5. Apron and Gate Operations

### 5.1 Parking Stand

**Required Space:**
- Minimum: 80 m × 80 m (Code E standard)
- Preferred: 85 m × 85 m (with safety margins)
- Wingtip clearance to adjacent stands: 7.5 m minimum

**Compatibility:**
- Most Code E gates: Compatible ✓
- Code D gates: Too small ❌
- Wide-body gates (A380): Oversized but usable ✓

### 5.2 Passenger Boarding

**Door Configuration:**
- Forward entry door (L1): 3.20 m sill height
- Aft emergency door (L3): 3.15 m sill height

**Jetway Compatibility:**
- Standard jetway: 2.8-3.5 m height range ✓
- 70m span may require:
  - Dual jetways (forward + over-wing)
  - Extended jetway reach
  - Noseapron parking (not parallel)

**Alternative:** Remote stands with bus boarding (acceptable for initial operations)

### 5.3 Ground Service Equipment

**Standard Equipment Compatible:**
- Baggage loaders ✓
- Catering trucks ✓
- Cargo loaders (LD3 containers) ✓
- Lavatory service ✓
- Potable water ✓
- GPU ✓

**Specialized Equipment Required:**
- **H₂ refueling unit** (see Section 6)
- Extended-reach tugs (for 70m span)

---

## 6. Hydrogen Refueling

### 6.1 Infrastructure Requirements

**H₂ Refueling Station:**
- Liquid H₂ storage: 20,000 kg minimum (2-3 aircraft turnarounds)
- Cryogenic transfer pump: 200 kg/min flow rate
- Refueling time: ~35 minutes (8,000 kg capacity)
- Safety zone: 50 m radius during refueling

**Airport Modifications:**
- Dedicated H₂ storage area (remote from terminal)
- Cryogenic transfer lines to apron
- Emergency response equipment
- Trained refueling personnel

### 6.2 Current H₂ Airport Status

**2025 Status:**
- **0 commercial airports** with large-scale LH₂ infrastructure
- Several R&D installations (NASA, DLR, etc.)
- Planning underway at major hubs

**Deployment Roadmap:**
- 2026-2027: First 5 airports (test locations)
- 2028-2030: 25 airports (major hubs)
- 2031-2035: 100 airports (network coverage)
- 2036+: Standard infrastructure

**Initial Target Airports (Proposed):**
1. Amsterdam Schiphol (AMS) - Strong H₂ commitment
2. Frankfurt (FRA) - Lufthansa hub
3. Paris CDG (CDG) - Air France hub
4. Copenhagen (CPH) - Leading sustainability
5. Munich (MUC) - Infrastructure investment

### 6.3 Interim Solutions

**Before Full H₂ Infrastructure:**
- Ferry flights to H₂-capable airports
- Mobile H₂ refueling units (trucked LH₂)
- Reduced route network initially
- Partner with airports for infrastructure investment

---

## 7. Compatible Airport List

### 7.1 Selection Criteria

**Must Have:**
- ICAO Code E certification
- Runway ≥2,500 m
- Available apron space
- Interest in sustainable aviation

**Preferred:**
- Existing wide-body operations
- Strong environmental commitment
- High traffic volume
- Slot availability

### 7.2 Top 50 Target Airports (Europe)

**Tier 1 (Initial Operations - H₂ Infrastructure by 2027):**
1. Amsterdam Schiphol (AMS) 🇳🇱
2. Frankfurt (FRA) 🇩🇪
3. Paris Charles de Gaulle (CDG) 🇫🇷
4. Copenhagen (CPH) 🇩🇰
5. Munich (MUC) 🇩🇪

**Tier 2 (Network Expansion - H₂ by 2029):**
6. London Heathrow (LHR) 🇬🇧
7. Madrid Barajas (MAD) 🇪🇸
8. Rome Fiumicino (FCO) 🇮🇹
9. Zurich (ZRH) 🇨🇭
10. Vienna (VIE) 🇦🇹

(Additional 40 airports documented separately)

### 7.3 North American Targets

**Major Hubs:**
- San Francisco (SFO) - Sustainability leader
- Los Angeles (LAX) - Large market
- Seattle (SEA) - Boeing proximity
- Denver (DEN) - Central location
- Boston (BOS) - Tech corridor

### 7.4 Asia-Pacific Considerations

**Long-Term (2035+):**
- Tokyo Narita (NRT) 🇯🇵
- Singapore (SIN) 🇸🇬
- Seoul Incheon (ICN) 🇰🇷
- Sydney (SYD) 🇦🇺

**Note:** Initial focus on shorter routes within Europe/North America given current H₂ infrastructure timeline.

---

## 8. Operational Constraints

### 8.1 Airport Limitations

**Cannot Operate At:**
- Code C airports (runway/taxiway too narrow)
- Code D airports (unless granted waiver)
- Airports without adequate apron space
- Airports without H₂ infrastructure (initially)

**Estimated Available:**
- Total Code E airports: ~3,000 globally
- With adequate apron: ~2,500
- **With planned H₂ infrastructure (2030): ~100**
- **Initial network (2027): 5-10 airports**

### 8.2 Operational Flexibility

**Route Planning:**
- Focus on point-to-point hub routes
- Target environmentally-conscious markets
- Coordinate with airport H₂ infrastructure development
- Plan for network expansion as infrastructure grows

**Fleet Deployment:**
- Initial: 5-10 aircraft, 5 H₂ airports
- 2030: 50 aircraft, 25 H₂ airports
- 2035: 200 aircraft, 100 H₂ airports
- 2040: 500+ aircraft, 250+ H₂ airports

---

## 9. Competitive Analysis

### 9.1 Airport Accessibility vs Competitors

| Aircraft | Code | Airports | H₂ Capability | Flexibility |
|----------|------|----------|---------------|-------------|
| A320neo | C | 5,000+ | No (Jet-A) | High |
| A321XLR | C | 5,000+ | No (Jet-A) | High |
| 737MAX | C | 5,000+ | No (Jet-A) | High |
| **AMPEL360** | **E** | **3,000** | **Yes (LH₂)** | **Medium** |
| A380 | F | 500 | No (Jet-A) | Low |

**Trade-off:** Less airport flexibility vs environmental/economic benefits

### 9.2 Market Positioning

**Strategy:**
- Focus on major hubs (300+ available Code E)
- Target environmentally-regulated routes
- Premium positioning (comfort + sustainability)
- Partner with forward-thinking airlines

---

## 10. Recommendations

### 10.1 Aircraft Design

**For Airport Compatibility:**
- ✅ 70m span is acceptable (Code E standard)
- ✅ Ground clearances adequate
- ⚠️ Wingtip awareness systems critical
- ⚠️ Enhanced pilot training required

### 10.2 Infrastructure Strategy

**Airport Partnerships:**
1. Engage early with Tier 1 airports
2. Co-invest in H₂ infrastructure
3. Secure gate/slot commitments
4. Coordinate certification process

**H₂ Infrastructure Development:**
- Target 5 airports by 2027 (EIS)
- Expand to 25 by 2030
- 100 by 2035 (full network)
- Standardize refueling procedures

### 10.3 Operational Planning

**Route Development:**
- Phase 1 (2027-2029): Hub-to-hub within Europe (5 airports)
- Phase 2 (2030-2032): European network expansion (25 airports)
- Phase 3 (2033-2035): Transatlantic routes (50 airports)
- Phase 4 (2036+): Global network (100+ airports)

---

## 11. Conclusions

The AMPEL360's Code E classification provides access to 3,000+ airports globally, which is adequate for a hub-focused network strategy. The primary constraint is hydrogen refueling infrastructure, not physical airport compatibility.

**Key Takeaways:**
- Physical compatibility: ✅ Adequate for Code E operations
- Infrastructure readiness: ⚠️ Requires H₂ development (in progress)
- Market access: ✅ Sufficient for viable network
- Growth potential: ✅ Expanding as H₂ infrastructure deploys

**Critical Path:** H₂ infrastructure deployment, not aircraft design

---

**References:**
1. ICAO Annex 14: Aerodrome Design
2. AR-02-10-001: BWB Configuration Analysis
3. CALC-02-10-203: Ground Clearances
4. TS-02-10-001: Wingspan Optimization

---

**Document Control:**
- **Version:** 1.0
- **Date:** 2025-11-05
- **Next Review:** 2026-02-05

*END OF TECHNICAL NOTE*

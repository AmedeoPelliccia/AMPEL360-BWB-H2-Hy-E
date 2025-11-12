# Airport Compatibility Mockup
# Gate Fit and Ground Operations Validation

**Mockup ID:** ACM-02-10-003  
**Date:** 2026-Q2 (Planned)  
**Status:** Planning Phase  
**Classification:** Operational Validation

---

## 1. Overview

### 1.1 Purpose

Validate AMPEL360 BWB compatibility with existing airport infrastructure:
- **Gate envelope compliance** - Does aircraft fit within standard parking positions?
- **Jet bridge compatibility** - Can passenger boarding bridges reach doors?
- **Taxiway clearances** - Adequate wingtip clearance during taxi?
- **Apron maneuvering** - Turning radius compatible with ramp space?
- **Ground service access** - Can standard GSE (Ground Service Equipment) service aircraft?

### 1.2 Unique BWB Considerations

**Challenge:** 64m wingspan exceeds many regional airport design standards
- Standard gate designed for narrowbody: 36m wingspan (A320/737)
- AMPEL360 is widebody-class wingspan but regional-class passengers (220 pax)
- Risk: May be restricted to widebody gates (limited availability, higher fees)

**Opportunity:** If compatible with more gates, operational flexibility increases

---

## 2. Mockup Approach

### 2.1 Physical Mockup (Option A - Full-Scale)

**Concept:** Construct full-scale plan-view template of aircraft
- Material: Painted plywood on wheels (2D plan view, no vertical dimension)
- Scale: 1:1 (64m × 52m footprint)
- Mobility: Towable by tug (simulates taxiing)
- Cost: €15,000

**Pros:**
✅ Actual gate fit test at real airports  
✅ Visual demonstration for airport operators  
✅ Ground crew training tool  
✅ Marketing/sales tool (airline presentations)

**Cons:**
⚠️ Transport logistics (64m wide, must be assembled on-site)  
⚠️ Weather-dependent (outdoor testing)  
⚠️ Airport access approvals (may take months)

### 2.2 Virtual Mockup (Option B - Digital Twin)

**Concept:** CAD-based gate fit analysis
- Software: CATIA V6 + Airport Design module
- Gate databases: ICAO Annex 14 compliant airports (500+)
- Analysis: Automated clearance checking

**Pros:**
✅ Fast (days vs. months)  
✅ Inexpensive (€5,000 software + engineering time)  
✅ Scalable (test 500 airports in same time as 1 physical test)  
✅ "What-if" scenarios (different gate layouts)

**Cons:**
⚠️ No physical validation  
⚠️ Limited stakeholder demonstration value  
⚠️ Doesn't capture operational nuances (tug angles, etc.)

### 2.3 Hybrid Approach (Selected)

**Strategy:** Virtual analysis first, physical validation at key airports
1. **Phase 1 - Virtual (Q1 2026):**
   - Analyze 50 target airports (European focus)
   - Identify gates compatible with AMPEL360
   - Rank airports by accessibility

2. **Phase 2 - Physical (Q2 2026):**
   - Build full-scale mockup template
   - Test at 3-5 key hub airports (FRA, AMS, CDG, LHR, MAD)
   - Demonstrate to airport authorities and airlines

**Budget:** €35,000 (virtual analysis + mockup fabrication + travel)

---

## 3. Target Airports

### 3.1 Primary Markets (Europe)

| Airport | IATA | Annual PAX | AMPEL360 Target Gate | Compatible? |
|---------|------|-----------|---------------------|-------------|
| Frankfurt | FRA | 70M | Pier A (A380 gates) | ✅ Likely |
| Amsterdam Schiphol | AMS | 72M | Pier D/E/F | ✅ Likely |
| Paris CDG | CDG | 67M | Terminal 2E (widebody) | ✅ Likely |
| London Heathrow | LHR | 80M | Terminal 2/5 remote | ✅ Likely |
| Madrid Barajas | MAD | 61M | Terminal 4S | ✅ Likely |
| Munich | MUC | 48M | Terminal 2 satellite | ✅ Likely |
| Zurich | ZRH | 32M | Dock E (widebody) | ⚠️ TBD |
| Copenhagen | CPH | 30M | Pier C | ⚠️ TBD |
| Vienna | VIE | 31M | Pier D/G | ⚠️ TBD |
| Barcelona | BCN | 50M | Terminal 1 satellite | ✅ Likely |

### 3.2 Gate Class Requirements

**ICAO Aerodrome Code:** Code E (52m < wingspan ≤ 65m)
- AMPEL360: 64m wingspan → Code E
- Requires: Taxiway width ≥ 23m, separation ≥ 182.5m

**Compatibility:**
- Code E gates available at major hubs (✅)
- Limited at regional airports (⚠️)
- Regional operations may require Code F gates (more expensive)

---

## 4. Test Scenarios

### 4.1 Gate Fit Validation

**Objective:** Confirm aircraft fits within gate parking position

**Test Procedure:**
1. Position mockup at gate centerline (CAT III ILS precision)
2. Measure clearances to:
   - Adjacent gates (wing tip to wing tip)
   - Terminal building (forward fuselage to building)
   - Ground service equipment zones
   - Taxilanes (aft fuselage to taxilane edge)

**Target Clearances (ICAO Annex 14):**
| Feature | Minimum Clearance | AMPEL360 Target |
|---------|------------------|-----------------|
| Wing tip to adjacent aircraft | 7.5 m (Code E) | ≥ 10 m |
| Nose to terminal building | 3.0 m | ≥ 5 m |
| Tail to taxilane edge | 10 m | ≥ 12 m |
| Wing tip to fixed object | 4.5 m | ≥ 6 m |

**Instrumentation:**
- Laser rangefinders (Leica Disto D810, ±1 mm accuracy)
- Total station survey (Trimble S7, ±1" angular accuracy)
- Photographic documentation (aerial drone + ground-level)

### 4.2 Jet Bridge Compatibility

**Objective:** Verify passenger boarding bridges can reach doors

**AMPEL360 Door Locations:**
- Door L1 (forward entry): FS 8,500 mm, Floor height 5.2 m
- Door L2 (mid entry): FS 23,000 mm, Floor height 5.2 m

**Standard Jet Bridge Reach:**
- Type A bridge (narrowbody): Reach 8-12 m, height 2-5 m
- Type B bridge (widebody): Reach 10-18 m, height 3-7 m

**Test:**
1. Position mockup at gate
2. Extend actual jet bridge to door location
3. Verify:
   - Bridge can reach door threshold (±0.5 m tolerance)
   - Bridge slope within limits (5-12% preferred, 15% max)
   - No interference with fuselage contour
   - Emergency retraction clearance adequate

**Acceptance:** Bridge reaches door within ±0.5 m horizontal, ±0.3 m vertical

### 4.3 Ground Service Equipment Access

**Scenarios:**

1. **Catering Trucks (2× required)**
   - Forward galley: Door at FS 10,000 mm, height 5.0 m
   - Aft galley: Door at FS 42,000 mm, height 5.0 m
   - Test: Position trucks, verify no interference with wings/gear

2. **Fuel Truck (H₂ Refueling)**
   - Refueling port: Aft fuselage, FS 48,000 mm, height 3.5 m
   - Requires specialized H₂ truck (development in parallel)
   - Test: Verify clearance for truck approach, hose routing

3. **Baggage Loaders (2×)**
   - Forward cargo: Door at FS 6,000 mm
   - Aft cargo: Door at FS 46,000 mm
   - Test: Belt loader positioning, clearance under wing

4. **GPU (Ground Power Unit)**
   - Electrical connection: Forward fuselage, FS 3,000 mm, height 2.5 m
   - Test: Cable routing, clearance with nose gear

5. **Lavatory Service**
   - Service panel: Aft fuselage, FS 38,000 mm
   - Test: Truck positioning

6. **Potable Water**
   - Service panel: Forward fuselage, FS 12,000 mm
   - Test: Truck positioning

**Documentation:** Clearance diagram for each GSE type, photo documentation

### 4.4 Taxiway Clearances

**Objective:** Confirm wing tip clearances during taxi

**Test Procedure:**
1. Simulate taxi along taxiway (mockup towed by tug)
2. Measure clearances to:
   - Taxiway edge lights
   - Taxiway edge stripe
   - Adjacent taxiway (parallel operations)

**ICAO Standards (Code E):**
- Taxiway width: 23 m (edge to edge)
- Wing tip clearance to edge: ≥ 4.5 m (total 32 m required)
- AMPEL360 wingspan: 64 m → Requires 73 m separation for parallel taxi

**Concern:** May limit parallel taxiway operations at some airports

### 4.5 Apron Maneuvering

**Objective:** Verify turning radius compatible with apron space

**Test:**
1. Perform 180° turn on apron (pushback + power-out turn)
2. Measure swept path (wing tip trace)
3. Compare to available apron space

**Metrics:**
- Turning radius: ~40 m (based on nose gear steering angle ±75°)
- Swept path width: ~80 m (wing tip to wing tip during turn)

**Acceptance:** Fits within standard widebody apron space (100 m × 100 m)

---

## 5. Virtual Analysis (Phase 1)

### 5.1 Methodology

**Software:** CATIA Airport Design Module + custom scripts
- Import AMPEL360 CAD model (plan view)
- Import airport gate layouts (50 airports, ICAO Annex 14 data)
- Automated clearance checking (wing tips, nose, tail)
- Report generation (compatible gates, clearance margins)

**Acceptance Criteria:**
- Clearance ≥ 4.5 m (wing tip to object)
- Nose clearance ≥ 3.0 m
- Tail clearance ≥ 10 m (to taxilane)

### 5.2 Expected Outcomes

**Hypothesis:**
- Major hubs (>50M PAX/year): 80% gate compatibility
- Medium hubs (20-50M PAX/year): 60% gate compatibility
- Regional airports (<20M PAX/year): 40% gate compatibility

**Risk Mitigation:**
- If compatibility < 50% at target airports, consider:
  - Wing tip fold mechanism (reduces wingspan to 52m on ground)
  - Remote parking (no jet bridge, bus to terminal)
  - Dedicated AMPEL360 gates (future infrastructure)

### 5.3 Deliverable

**Airport Compatibility Database (ACD-02-10-001)**
- Excel spreadsheet: 50 airports × gate compatibility analysis
- Summary report: Compatible gates, restrictions, recommendations
- Maps: Geographic distribution of compatible airports

---

## 6. Physical Mockup (Phase 2)

### 6.1 Mockup Design

**Construction:**
- Base: 5 sections of plywood (12 mm), each 15m × 10m
- Assembly: Bolted connections, on-site assembly in 2 hours
- Paint: White with black outline (aircraft plan view)
- Graphics: Door locations, service points labeled
- Mobility: 8× caster wheels (4× swivel, 4× fixed), towbar connection

**Dimensions (Plan View):**
- Wingspan: 64.0 m (actual)
- Length: 52.0 m (actual)
- Wing tips: Marked with reflective tape (high visibility)

**Weight:** ~500 kg (towable by standard aircraft tug)

### 6.2 Test Program

**Airports (Planned):**
1. **Frankfurt (FRA)** - Hub, Lufthansa base
2. **Amsterdam (AMS)** - Hub, KLM base
3. **Paris CDG** - Hub, Air France base

**Test Duration:** 2 days per airport
- Day 1: Gate fit at 3-5 gates, jet bridge test
- Day 2: Taxiway/apron maneuvering, GSE access

**Participants:**
- AMPEL360 engineering team (3 persons)
- Airport authority representative
- Airline ground operations (if available)
- Ground service provider

**Coordination:**
- Airport access approvals (3 months lead time)
- Test windows: Early morning (05:00-07:00) or late night (23:00-01:00)
- Safety briefing, airport escort required

---

## 7. Budget and Schedule

### 7.1 Cost Breakdown

| Item | Cost (€) |
|------|---------|
| **Phase 1 - Virtual Analysis** | |
| Software licenses | 2,000 |
| Engineering time (2 weeks) | 8,000 |
| Airport data procurement | 1,000 |
| **Subtotal Phase 1** | **11,000** |
| **Phase 2 - Physical Mockup** | |
| Mockup fabrication | 10,000 |
| Transport to airports (3×) | 4,000 |
| Airport access fees | 3,000 |
| Travel & accommodation (3 persons × 6 days) | 5,000 |
| Contingency (15%) | 3,000 |
| **Subtotal Phase 2** | **25,000** |
| **Total** | **36,000** |

### 7.2 Timeline

| Phase | Duration | Dates | Status |
|-------|----------|-------|--------|
| Virtual Analysis | 3 weeks | Jan 2026 | 📋 |
| Airport Coordination | 3 months | Jan-Mar 2026 | 📋 |
| Mockup Fabrication | 3 weeks | Apr 2026 | 📋 |
| Physical Testing | 6 days | May-Jun 2026 | 📋 |
| Data Analysis & Report | 2 weeks | Jun 2026 | 📋 |

---

## 8. Deliverables

1. **Airport Compatibility Database (ACD-02-10-001)**
   - 50 airports analyzed, gate compatibility matrix
   - Clearance margins, restrictions documented

2. **Physical Test Report (PTR-02-10-001)**
   - Results from 3 airport tests
   - Photographic evidence, measurement data
   - Lessons learned, recommendations

3. **Airline Operations Guide (AOG-02-10-001)**
   - Gate compatibility quick reference
   - GSE positioning procedures
   - Taxiway restrictions by airport

---

## 9. Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Airport denies access | Coordinate early (6 months advance), offer incentives |
| Mockup damage during transport | Design for disassembly, robust packaging |
| Gate compatibility worse than predicted | Early virtual analysis identifies issues, design changes if needed |
| Weather delays (outdoor testing) | Schedule backup dates, indoor gate test if available |

---

## 10. Success Criteria

**Compatibility Acceptable If:**
- ✅ ≥60% of analyzed gates compatible (major hubs)
- ✅ All 3 physical test airports confirm virtual analysis
- ✅ No showstopper issues discovered (e.g., cannot fit any standard gate)
- ✅ Clearance margins adequate for safe operations

**Decision Gate:** Proceed to airline route planning (Q3 2026)

---

## 11. References

1. ICAO Annex 14: Aerodromes (Volume I - Aerodrome Design and Operations)
2. IATA Airport Handling Manual (AHM)
3. Eurocontrol Airport Capacity Study
4. AMPEL360 Ground Operations Design (GOD-02-32-001)

---

**Document Owner:** Airport Compatibility Engineer  
**Approval:**
- [ ] Chief Engineer - Aircraft General Data
- [ ] Operations Design Lead
- [ ] Airline Liaison Manager

**Status:** Planning Phase / Virtual Analysis Starting Jan 2026  
**Next Review:** 2026-01-15 (Phase 1 Kickoff)

# ATA 52: Doors

**TECHNOLOGY CHAPTER STATUS:** ATA 52 establishes the design, operation, and maintenance requirements for all doors, hatches, and access panels on the AMPEL360 aircraft. The BWB configuration requires innovative door placement and evacuation strategies, monitored and optimized through CAOS predictive systems.

## Scope and Structure
This chapter documents all aircraft doors and access provisions, including:
- **Passenger Entry Doors:** Main cabin doors (Type A, Type I)
- **Emergency Exits:** Overwing exits, ventral exits (BWB-specific)
- **Cargo Doors:** Main cargo doors, bulk cargo door
- **Service Doors:** Avionics access, equipment bays, refueling panels
- **Flight Deck Doors:** Reinforced cockpit door (security requirements)
- **Door Mechanisms:** Latching, sealing, actuation systems
- **Evacuation Systems:** Escape slides, rafts, deployment mechanisms
- **Warning Systems:** Door position sensors, unlock alerts
- **CAOS Integration:** Predictive maintenance, smart evacuation management
- **Structural Integration:** Composite door frames, pressure sealing

## The 14-Folder Skeleton
Every 6-digit component within this chapter represents a door system, mechanism, or operational procedure. Each component is managed through the full lifecycle skeleton to ensure requirements traceability, regulatory compliance, operational safety, and continuous improvement through CAOS analytics.

## Regulatory Framework

### Certification Requirements
- **CS-25.783:** Doors (general requirements)
- **CS-25.807:** Emergency Exits
- **CS-25.809:** Emergency Exit Arrangement
- **CS-25.810:** Emergency Egress Assist Means and Escape Routes
- **CS-25.811:** Emergency Exit Marking
- **CS-25.812:** Emergency Lighting
- **CS-25.813:** Emergency Exit Access
- **CS-25.831:** Ventilation
- **CS-25.853:** Compartment Interiors (material flammability)
- **CS-25 Appendix J:** Emergency Evacuation

### Security Requirements
- **CS-25.795:** Security Considerations (flight deck door)
- **FAA AC 25.795-1:** Flight Deck Security Procedures
- **TSA/EASA Security Directives:** Cockpit door intrusion resistance
- **ICAO Annex 17:** Security - Protection of International Civil Aviation

### Industry Standards
- **ATA iSpec 2200 Chapter 52:** Doors
- **SAE AS8043:** Escape Slide Systems
- **SAE ARP5359:** Commercial Aircraft Door Seal Design
- **ISO 23509:** Aerospace - Escape Rope Devices
- **RTCA DO-160:** Environmental Conditions and Test Procedures (door sensors)

### CAOS-Related Standards
- **ISO 13374:** Condition Monitoring (door mechanism wear prediction)
- **IEEE 1451:** Smart Transducer Interface (door sensors)
- **ISO 23247:** Digital Twin Framework (evacuation simulation)

## AMPEL360 Unique Characteristics

### 1. **BWB Door Configuration Challenge**

The AMPEL360's Blended Wing Body creates unique challenges for door placement and evacuation:

**Conventional Aircraft (Tube-and-Wing):**
- **Fuselage Doors:** Evenly spaced along cylindrical fuselage sides
- **Overwing Exits:** Above wing, easy access to wing surface
- **Evacuation:** Passengers slide down to ground or walk on wing
- **Door Count:** Typically 8 doors for 300-passenger aircraft (4 per side)

**AMPEL360 BWB Configuration:**
- **Wide Center Body:** 22.5m wide cabin (vs. 5.6m Airbus A350 fuselage)
- **Door Challenge:** Passengers in center seats far from side doors (11m distance)
- **Evacuation Strategy:** Combination of side doors + ventral exits (underfloor egress)
- **Door Count:** 10 doors total (4 side + 2 ventral + 4 overwing)

**BWB Door Placement Philosophy:**
```
AMPEL360 CENTER BODY - TOP VIEW (Door Locations)

           ┌────────────────────────────────────────┐
           │                NOSE                    │
           │         ┌──────────────┐               │
           │         │   COCKPIT    │               │
           │         └──────────────┘               │
           │                                        │
  ┌────────┼────────────────────────────────────────┼────────┐
  │  L-1   │                                        │  R-1   │
  │  (A)   │         FORWARD CABIN                  │  (A)   │
  │        │         Rows 1-10                      │        │
  ├────────┤                                        ├────────┤
  │  L-2   │                                        │  R-2   │
  │  (A)   │         CENTER CABIN                   │  (A)   │
  │        │         Rows 11-20                     │        │
  │        │    [LH₂ TANK Below]                    │        │
  ├────OW──┤                                        ├──OW────┤
  │  L-3   │         AFT CABIN                      │  R-3   │
  │ (I+OW) │         Rows 21-30                     │ (I+OW) │
  └────────┼────────────────────────────────────────┼────────┘
           │                                        │
           │         MAIN CARGO HOLD                │
           │      V-1              V-2               │
           │    (Ventral)      (Ventral)            │
           └────────────────────────────────────────┘
           
Legend:
L/R = Left/Right Side
A = Type A door (large passenger door, 107cm × 183cm)
I = Type I door (smaller passenger door, 61cm × 183cm)
OW = Overwing emergency exit (Type III, 51cm × 91cm)
V = Ventral emergency exit (Type II, 51cm × 107cm, underfloor)
```

**Regulatory Compliance (CS-25.807):**
- **Minimum Exits Required:** For 300 passengers, minimum 8 Type A or Type I exits
- **AMPEL360 Provision:** 4× Type A (sides) + 2× Type I (overwing) + 4× Type III (overwing) = 10 exits
- **Exit Area:** Type A (1,963 cm²) × 4 + Type I (1,117 cm²) × 2 + Type III (465 cm²) × 4 = 12,452 cm² total
- **Required:** Minimum 3,728 cm² for 300 PAX (CS-25.807) → AMPEL360 exceeds by 334%

### 2. **Door Inventory and Specifications**

**Passenger Entry Doors (Main Boarding):**

**Doors L-1 / R-1 (Forward, Type A):**
- **Location:** FS 12,000 / BL ±11,000 / WL 5,500 (forward cabin, left/right)
- **Type:** Type A passenger door (per CS-25.807)
- **Dimensions:** 107cm (width) × 183cm (height) = 19,581 cm² opening
- **Sill Height:** 3.8m above ground (requires airstairs or jetway)
- **Primary Use:** Normal passenger boarding/deplaning
- **Evacuation:** Dual-lane escape slide (Type A slide, 70 passengers/90 sec)
- **Opening Direction:** Inward-pivoting plug door (pressure-sealing design)

**Doors L-2 / R-2 (Center, Type A):**
- **Location:** FS 22,000 / BL ±11,000 / WL 5,500 (center cabin, left/right)
- **Type:** Type A passenger door
- **Dimensions:** 107cm × 183cm = 19,581 cm²
- **Sill Height:** 3.8m above ground
- **Primary Use:** Additional boarding (dual jetway operations), emergency egress
- **Evacuation:** Dual-lane escape slide (Type A slide)
- **Opening Direction:** Inward-pivoting plug door

**Doors L-3 / R-3 (Aft, Type I + Overwing):**
- **Location:** FS 32,000 / BL ±11,000 / WL 5,500 (aft cabin, left/right)
- **Type:** Type I passenger door + Type III overwing exit
- **Type I Dimensions:** 61cm × 183cm = 11,163 cm²
- **Type III Dimensions:** 51cm × 91cm = 4,641 cm² (overwing hatch)
- **Sill Height:** 3.5m above ground (door), 3.2m (overwing to wing surface)
- **Primary Use:** Emergency egress (door not used for normal boarding)
- **Evacuation:** Single-lane slide (Type I) + overwing slide (Type III)
- **Opening Direction:** Type I plug door, Type III outward-opening hatch

**Emergency Exits (Ventral - Underfloor):**

**Ventral Exits V-1 / V-2 (Type II Equivalent):**
- **Location:** FS 28,000 / BL ±5,000 / WL 4,200 (underfloor, left/right)
- **Type:** Ventral emergency exit (BWB-specific design)
- **Dimensions:** 51cm × 107cm = 5,457 cm²
- **Drop Height:** 2.5m to ground (lower than side doors due to BWB flat bottom)
- **Primary Use:** Emergency evacuation only (crew-operated)
- **Evacuation:** Single-lane escape slide (Type II slide, deploys downward from floor)
- **Opening Direction:** Hinged door (opens downward, slides deploy automatically)
- **Unique Feature:** Accessed via floor hatches in cabin aisle (passengers descend ladder to exit)

**Cargo Doors:**

**Main Cargo Doors (Left/Right):**
- **Location:** FS 40,500 / BL ±10,000 / WL 4,800 (aft center body)
- **Type:** Class C cargo door
- **Dimensions:** 3.2m × 2.0m = 6.4 m²
- **Opening Direction:** Outward-opening plug door (swings up to horizontal)
- **Actuation:** Electric motor (16-second opening cycle)
- **Primary Use:** ULD loading/unloading
- **Detailed in:** ATA 50-40 (cross-reference)

**Bulk Cargo Door:**
- **Location:** FS 41,500 / BL -6,000 / WL 4,800 (left side, aft)
- **Type:** Service door
- **Dimensions:** 1.2m × 1.0m = 1.2 m²
- **Opening Direction:** Hinged (manual operation)
- **Primary Use:** Loose baggage access

**Service and Access Doors:**

**Flight Deck Door (Cockpit Security Door):**
- **Location:** FS 7,500 / BL 0 / WL 5,300 (between cockpit and cabin)
- **Type:** Reinforced security door (per CS-25.795)
- **Dimensions:** 81cm × 203cm
- **Material:** Composite panel + Kevlar armor (ballistic protection)
- **Locking:** Electronic lock (keypad + RFID card) + manual deadbolt
- **Viewing:** Peephole + video camera (interior cabin view)
- **Intrusion Resistance:** 5 minutes minimum (blunt force, ballistic, fire)
- **Emergency Access:** Flight crew unlock from cockpit, cabin crew emergency code (15-second delay)

**Avionics Access Doors (AEB-1, AEB-2):**
- **Locations:** FS 10,000 / FS 13,000 / BL 0 / WL 4,500 (underfloor, cabin access)
- **Type:** Removable floor panels (internal access)
- **Dimensions:** 80cm × 100cm each
- **Fasteners:** Quarter-turn Dzus fasteners (tool-free removal)
- **Primary Use:** Maintenance access to avionics equipment bays
- **Safety:** Red-tagged when removed (prevent FOD/fall hazard)

**Fuel Cell Access Panels (FCEB-1, FCEB-2):**
- **Locations:** FS 19,000 / FS 21,000 / BL 0 / WL 6,200 (top of center body, external)
- **Type:** External composite panels
- **Dimensions:** 1.5m × 2.0m = 3.0 m² each
- **Fasteners:** Captive bolts (Allen key, 32 bolts per panel)
- **Primary Use:** Fuel cell stack removal/installation
- **Safety:** H₂ detection required before opening (verify <10 ppm)

**LH₂ Fuel Fill Door:**
- **Location:** FS 22,000 / BL 0 / WL 6,200 (top center body)
- **Type:** Flush-mounted fueling panel
- **Dimensions:** 40cm × 40cm
- **Actuation:** Electric motor (cockpit or ground control)
- **Locking:** Mechanical lock + safety interlock (cannot open if tank pressurized)
- **Detailed in:** ATA 28-31 (LH₂ Fuel System)

### 3. **Passenger Door Design (Type A - Main Entry)**

**Door L-1/R-1 and L-2/R-2 Detailed Design:**

**Structural Design:**
- **Door Panel:** Carbon fiber sandwich (face sheets + Nomex honeycomb core)
  - Face sheets: 4 plies CFRP (2mm total)
  - Core: 40mm Nomex honeycomb (48 kg/m³)
  - Total thickness: 44mm
  - Weight: 95 kg (door panel only, excluding mechanisms)
- **Door Frame:** Aluminum 7075-T6 extrusion
  - Bonded to composite fuselage structure
  - 8 mounting lugs (titanium inserts, 50 kN ultimate each)

**Plug Door Mechanism:**
- **Principle:** Door moves inward 10cm, then rotates parallel to fuselage → opens inward
- **Advantage:** Cannot open if cabin pressurized (pressure holds door against frame)
- **Actuation Sequence:**
  1. Unlatch (8 latches disengage) - 2 seconds
  2. Move inward (10cm travel, clears door stop) - 1 second  
  3. Rotate 90° (door parallel to cabin wall) - 3 seconds
  4. **Total:** 6 seconds (powered assist), 20 seconds (manual backup)

**Latching System:**
- **Primary Latches:** 8× rotating hook latches (mechanical)
- **Material:** Steel 4340 (high strength, 1,900 MPa tensile)
- **Load Capacity:** 30 kN per latch (240 kN total, factor of safety 2.5×)
- **Actuation:** Electric motor + gearbox (primary), manual handle (backup)
- **Latch Position Sensors:** Proximity sensors (3 per latch, 2oo3 voting)
- **Indication:** Cockpit EICAS + door-specific annunciator light

**Sealing System:**
- **Primary Seal:** Inflatable rubber seal (circumferential)
  - Material: Silicone rubber (high/low temperature capability -55°C to +120°C)
  - Inflation: 2.0 bar pneumatic pressure (aircraft pneumatic system)
  - Width: 50mm (compressed state)
- **Secondary Seal:** Compression seal (backup, passive)
- **Leak Rate:** <0.05 CFM at 8.5 psi cabin differential (CS-25.783)
- **Inspection:** Visual inspection every 300 FH, leak test every C-Check

**Escape Slide System (Type A):**
- **Type:** Dual-lane slide/raft (SAE AS8043)
- **Deployment:** Automatic (when door opened in armed mode) or manual (pull handle)
- **Deployment Time:** <6 seconds (inflate fully)
- **Capacity:** 70 passengers / 90 seconds (per CS-25 Appendix J)
- **Inflation:** Compressed nitrogen (2 bottles per slide, 150 bar)
- **Slide Angle:** 45° (optimal evacuation speed vs. safety)
- **Raft Mode:** Detachable (converts to life raft, 44-person capacity)
- **Service Life:** 12 years (requires repack every 2 years)

**Door Warning Systems:**
- **Position Sensors:** 3× proximity sensors per latch (2oo3 voting logic)
- **Seal Pressure Sensor:** Monitors seal inflation pressure
- **Slide Arming Sensor:** Detects slide arming lever position
- **Cockpit Indications:**
  - "DOOR L-1 UNLOCKED" (amber) - if any latch not fully engaged
  - "DOOR L-1 OPEN" (red) - if door not closed
  - "SLIDE L-1 DISARMED" (amber) - if slide not armed for takeoff/landing
- **Aural Warning:** "DOOR OPEN" chime (if door open during taxi)

### 4. **Ventral Emergency Exit Design (BWB-Specific Innovation)**

**Rationale for Ventral Exits:**
The AMPEL360's wide cabin (22.5m) means passengers in center seats are up to 11m from side doors - too far to evacuate within 90 seconds. Ventral exits provide egress for center-seated passengers.

**Ventral Exit V-1/V-2 Design:**

**Location:**
- FS 28,000 / BL ±5,000 / WL 4,200 (underfloor, left/right sides)
- Access: Via floor hatches in cabin aisle (between seat rows 18-19)

**Exit Sequence (Emergency Evacuation):**
1. **Cabin Floor Hatch Opens:**
   - Crew member pulls T-handle (located in aisle floor)
   - Floor panel hinges up (80cm × 100cm opening)
   - Reveals ladder (4 rungs, aluminum, 1.5m descent)

2. **Passenger Descends Ladder:**
   - Passenger climbs down ladder to lower level (cargo bay height)
   - Lower level is 1.3m high passageway (crawl space)

3. **Ventral Door Opens:**
   - Crew member (or first passenger) pulls red handle
   - Door hinges downward (becomes ramp/slide combination)
   - Escape slide deploys automatically (Type II slide, 51cm × 107cm)

4. **Evacuation:**
   - Passengers slide down to ground (2.5m drop)
   - Slide capacity: 40 passengers / 90 seconds
   - Total capacity: 80 passengers (2 ventral exits)

**Design Challenges:**
- **Structural:** Cargo floor must support cutouts (reinforced frames around openings)
- **Pressurization:** Ventral doors are below pressure floor (no pressure differential)
- **Safety:** Ladder must be sturdy (support 130 kg passenger + dynamic load)
- **Certification:** Novel exit type required full-scale evacuation demonstration (EASA witnessed)

**Certification Testing:**
- **Full-Scale Evacuation Demo:** 300 volunteers evacuated in 78 seconds (target: <90 sec)
- **Ventral Exit Performance:** 72 passengers used ventral exits (average time: 18 seconds per passenger)
- **Result:** Certified per CS-25.807, ventral exits count as Type II equivalent

### 5. **Flight Deck Security Door**

**Post-9/11 Security Requirements:**
The flight deck door must prevent unauthorized access while allowing emergency egress.

**Door Specification:**
- **Structure:** Composite sandwich + Kevlar armor layers
  - Outer: 3mm carbon fiber face sheet
  - Armor: 6mm Kevlar (ballistic protection, NIJ Level IIIA)
  - Core: 15mm aluminum honeycomb
  - Inner: 3mm carbon fiber face sheet
  - Total thickness: 27mm
  - Weight: 42 kg

**Locking Mechanism:**
- **Primary Lock:** Electronic deadbolt (12mm diameter steel bolt)
  - Activated by keypad (flight crew side) or RFID card
  - Code: 6-digit PIN (changed after every crew rotation)
  - Power: 28 VDC aircraft power + 9V battery backup
- **Manual Lock:** Mechanical deadbolt (backup, flight crew only)
  - Engages if electronic system fails
  - Cannot be overridden from cabin side

**Access Control Logic:**
1. **Normal Access (Cabin Crew):**
   - Cabin crew enters emergency code on cabin-side keypad
   - 15-second delay (flight crew can deny access if suspicious)
   - If flight crew does not deny: door unlocks (remains locked if denied)

2. **Emergency Access (Forced Entry):**
   - If flight crew incapacitated: cabin crew can use emergency override
   - Override requires simultaneous action: emergency code + physical key
   - Door unlocks after 30-second delay

3. **Intrusion Attempt:**
   - Door designed to resist forced entry for 5 minutes minimum
   - Ballistic protection: Small arms fire (<9mm handgun)
   - Fire resistance: 30 minutes at 1,000°C

**Viewing System:**
- **Peephole:** Wide-angle optical viewer (180° field of view)
- **Video Camera:** HD camera (cabin side), display in cockpit (7-inch LCD)
- **Intercom:** Two-way audio (flight crew ↔ cabin crew communication)

**Decompression Protection:**
- **Pressure Equalization:** 4 small vents (10mm diameter) allow pressure equalization if rapid decompression
- **Function:** Prevents door from jamming due to pressure differential (allows emergency egress)

### 6. **Door Actuation and Control Systems**

**Powered Door Actuation (Passenger Doors):**

**Electric Motor System:**
- **Motor Type:** Brushless DC motor (400W)
- **Gearbox:** Planetary gearbox (100:1 reduction)
- **Torque Output:** 150 Nm (sufficient to overcome seal friction)
- **Speed:** 6-second opening cycle (powered assist)
- **Power:** 28 VDC aircraft electrical system
- **Backup:** Manual handle (mechanical override, 20-second opening)

**Control Logic:**
- **Door Handle Position:** 3 positions (Closed, Neutral, Open)
- **Interlock:** Cannot open door if cabin pressurized (>0.2 psi differential)
  - Pressure sensor monitors cabin differential
  - If pressurized: electric motor disabled, handle mechanically locked
- **Override:** Emergency handle (red, protected by cover) bypasses interlock
  - Used if cabin must be depressurized in emergency (e.g., fire/smoke)

**Cargo Door Actuation:**
- **Opening Sequence:**
  1. Unlatch (8 latches) - 3 seconds
  2. Swing outward 15° - 3 seconds
  3. Swing upward 90° (horizontal position) - 10 seconds
  4. Total: 16 seconds
- **Motor:** 1.5 kW electric motor (28 VDC)
- **Manual Backup:** Hand crank (90-second opening)
- **Safety:** Cannot open if cargo net not secured (prevents cargo shift)

### 7. **Door Structural Integration with BWB Composite Airframe**

**Door Frame Design:**

**Composite-to-Metal Transition:**
- **Fuselage Structure:** Carbon fiber composite center body
- **Door Frame:** Aluminum 7075-T6 extrusion (easier to attach hinges, latches)
- **Interface:** Co-bonded during fuselage manufacture
  - Frame adhesively bonded to composite (Cytec FM 300 film adhesive)
  - Mechanical fastening: Titanium Hi-Lok fasteners (100mm spacing)
  - Glass fiber isolation layer (prevents galvanic corrosion)

**Load Transfer:**
- **Pressure Loads:** 8.5 psi cabin pressure → 15 kN per meter of door perimeter
- **Frame Stiffness:** 8 mounting lugs transfer load to fuselage frames
- **Factor of Safety:** 2.0× ultimate load (per CS-25.783)

**Pressure Seal Interface:**
- **Seal Groove:** Machined into aluminum door frame
- **Seal Retention:** Spring-loaded retainer (keeps seal in place during door operation)
- **Tolerances:** ±0.5mm door-to-frame gap (ensures seal compression)

**Damage Tolerance:**
- **Crack Growth:** Aluminum frame inspected for cracks (eddy current, every C-Check)
- **Composite Skin:** Delamination inspection (ultrasonic, every 2C-Checks)
- **Acceptance:** No cracks >6mm, no delamination >25mm diameter

### 8. **Emergency Evacuation System (Slides and Rafts)**

**Slide/Raft System Overview:**

**Type A Slide/Raft (Doors L-1, L-2, R-1, R-2):**
- **Type:** Dual-lane slide, detachable raft
- **Capacity:** 70 passengers evacuate / 90 seconds, 44 persons life raft
- **Inflation:** Nitrogen (2× cylinders, 150 bar, 40 L each)
- **Deployment:** Automatic (if door opened when armed) or manual
- **Slide Length:** 7.5m (sill to ground)
- **Slide Angle:** 45° (optimized for evacuation speed)
- **Raft Mode:** Detaches from door, inflatable floor + canopy + survival kit
- **Survival Kit Contents:**
  - Emergency locator transmitter (ELT) - 406 MHz COSPAS-SARSAT
  - Flares (12× handheld, 6× parachute)
  - Drinking water (20 L, vacuum-sealed pouches)
  - Emergency rations (10,000 kcal)
  - First aid kit (40-person capacity)
  - Survival manual (waterproof)

**Type I Slide (Doors L-3, R-3):**
- **Type:** Single-lane slide
- **Capacity:** 40 passengers / 90 seconds
- **Inflation:** Single cylinder (150 bar, 40 L)
- **Raft Capability:** Not designed for flotation (no detachable raft)

**Type III Overwing Slide (Overwing Exits):**
- **Type:** Ramp-style slide (deploys onto wing surface)
- **Capacity:** 35 passengers / 90 seconds
- **Deployment:** Automatic (when exit opened)
- **Wing Evacuation:** Passengers walk on wing, then slide off trailing edge (2m drop)

**Ventral Slide (Exits V-1, V-2):**
- **Type:** Single-lane slide
- **Capacity:** 40 passengers / 90 seconds
- **Inflation:** Single cylinder (150 bar, 30 L)
- **Deployment:** Downward from cargo bay opening (2.5m to ground)

**Slide Arming System:**
- **Arming Lever:** Located at each door, 3 positions:
  - **ARMED:** Slide deploys automatically when door opened (takeoff/landing)
  - **DISARMED:** Door opens normally, slide does not deploy (ground operations)
  - **TEST:** Allows slide pack removal without deploying (maintenance)
- **Indication:** Cockpit EICAS shows arming status for all doors
- **Warning:** Aural alert "SLIDES DISARMED" if door not armed before takeoff

**Slide Maintenance:**
- **Repack Interval:** 24 months (or after deployment)
- **Inflation Test:** Functional test every repack (full inflation, pressure hold test)
- **Cylinder Hydrostatic Test:** Every 60 months (test to 250 bar, 1.67× service pressure)
- **Replacement:** Slide fabric replaced at 12 years (UV degradation, material fatigue)

### 9. **CAOS Integration - Smart Door Systems**

**Digital Twin - Door Module:**

**Real-Time Door Monitoring:**
```
DOOR STATUS DASHBOARD - Aircraft G-AMPL-450

PASSENGER DOORS                    CARGO DOORS
├─ L-1: CLOSED & LOCKED ✓         ├─ Cargo L: CLOSED & LOCKED ✓
│  └─ Latches: 8/8 engaged         │  └─ Latches: 8/8 engaged
│  └─ Seal: 2.0 bar (nominal)      │  └─ Opening cycles: 8,547 (total)
│  └─ Slide: ARMED ✓               │
├─ L-2: CLOSED & LOCKED ✓         └─ Cargo R: CLOSED & LOCKED ✓
│  └─ Latches: 8/8 engaged             └─ Latches: 8/8 engaged
│  └─ Seal: 2.1 bar (nominal)          └─ Opening cycles: 8,502 (total)
│  └─ Slide: ARMED ✓
├─ L-3: CLOSED & LOCKED ✓
│  └─ Latches: 8/8 engaged
│  └─ Seal: 2.0 bar (nominal)
│  └─ Slide: ARMED ✓

Right side doors: Similar status (all green)

FLIGHT DECK DOOR
└─ LOCKED (flight mode) ✓
   └─ Electronic lock engaged
   └─ Last access: 12:34 UTC (Capt. Johnson)

PREDICTIVE MAINTENANCE ALERTS
├─ L-1 Door Seal: Pressure drop trend detected
│  └─ Current: 2.0 bar (nominal)
│  └─ Trend: -0.02 bar/month (slow leak developing)
│  └─ Prediction: Replace seal in 1,200 FH (95% confidence)
│  └─ Action: Pre-order seal kit P/N AMPEL-52-SEAL-L1
│
└─ Cargo L Door Motor: Current draw increase
    └─ Current: 24 A (nominal 18-22 A)
    └─ Likely cause: Gearbox lubrication degradation
    └─ Recommendation: Inspect and re-lubricate at next overnight maintenance
    └─ If not addressed: Motor failure predicted in 800 FH
```

**Service Twin - Predictive Door Maintenance:**

**Example 1: Door Seal Degradation Prediction**
```
PREDICTIVE ANALYSIS: Door L-1 Seal

Historical Data (10,000 flight hours):
├─ Seal inflation pressure: 2.0 bar ±0.1 (nominal range)
├─ Leak rate: <0.05 CFM at 8.5 psi cabin pressure (specification)
├─ Inspection findings: No visible damage, normal compression set

Recent Trend (last 500 FH):
├─ Seal pressure: 2.1 → 2.0 → 1.9 bar (declining trend)
├─ Rate of decline: -0.02 bar/month
├─ Leak rate: 0.04 CFM (increasing, approaching 0.05 CFM limit)

Service Twin Simulation:
├─ Physics model: Seal material degradation (silicone rubber hardening)
├─ Monte Carlo: 10,000 scenarios (varying environmental factors)
├─ Result: Seal will exceed 0.05 CFM leak rate in 1,200 FH (95% confidence)

Recommended Action:
├─ Replace seal at 1,000 FH (proactive, before limit exceeded)
├─ Schedule: Next C-Check (1,050 FH from now) - alignment opportunity
├─ Spare parts: Auto-order seal kit P/N AMPEL-52-SEAL-L1 (lead time 2 weeks)
├─ Cost savings: Prevent unscheduled maintenance (AOG avoided)
```

**Example 2: Cargo Door Actuator Wear**
```
PREDICTIVE ANALYSIS: Cargo Door L Motor

Current Condition:
├─ Opening cycles: 8,547 (since new)
├─ Motor current draw: 24 A (nominal 18-22 A, +9% high)
├─ Opening time: 17 seconds (specification 16 seconds, +6% slow)
├─ Gearbox noise: Increased (maintenance report: audible grinding)

Root Cause Analysis:
├─ Likely cause: Gearbox lubrication breakdown (normal wear)
├─ Contributing factors: High cycle count (8,547 vs. 6,000 typical at this FH)
│   └─ Aircraft operates short-haul routes (3 cycles/day vs. 1.5 typical)
├─ Secondary factor: Environmental (high dust environment at hub airport)

Failure Prediction:
├─ If not addressed: Gearbox seizure predicted in 800 FH (80% confidence)
├─ Failure mode: Motor overload → thermal shutdown → door inoperative
├─ Operational impact: Aircraft AOG (cargo door cannot open/close)

Service Twin Recommendation:
├─ Inspect gearbox at next overnight maintenance (tonight)
├─ Clean and re-lubricate (estimated repair time: 2 hours)
├─ If damage found: Replace gearbox assembly P/N AMPEL-52-GB-CDL
├─ Prevention: Increase lubrication interval for this aircraft (high-cycle ops)
├─ Cost savings: $45,000 (avoided AOG + passenger compensation)
```

**Autodetermination - Autonomous Door Management:**

**Decision 1: Evacuation Route Optimization**
- **Scenario:** Engine fire detected on left side during taxi
- **CAOS Analysis:** Fire location FS 30,000 / BL -12,000 (left aft, near door L-3)
- **Digital Twin Simulation:** Wind direction 270° (west wind) → smoke will blow toward door L-3
- **Decision:** Automatically recommend evacuation via right-side doors only (R-1, R-2, R-3) + ventral exits
- **Crew Alert:** Tablet display shows optimal evacuation plan (visual diagram)
- **Approval:** Flight crew executes (human-in-the-loop), CAOS provides decision support

**Decision 2: Automatic Slide Arming Alert**
- **Observation:** Aircraft taxiing for takeoff, door L-2 slide shows "DISARMED"
- **CAOS Action:** Automatic alert to cabin crew (tablet notification + aural chime)
  - "SLIDE L-2 DISARMED - ARM BEFORE TAKEOFF"
- **Verification:** Cabin crew arms slide, confirms via tablet
- **Safety:** Prevents takeoff with disarmed slide (regulatory requirement)
- **Approval:** Automatic alert (safety-critical, no approval needed)

**Decision 3: Door Maintenance Scheduling Optimization**
- **Observation:** 4 aircraft in fleet need door seal replacement (due within next 200 FH)
- **Service Twin Analysis:** Coordinate maintenance to minimize fleet impact
  - Aircraft S/N 025: Replace during scheduled C-Check (1,050 FH from now)
  - Aircraft S/N 042: Replace during overnight maintenance (100 FH from now)
  - Aircraft S/N 077: Defer to next A-Check (150 FH, seal still within limits)
  - Aircraft S/N 088: Emergency replacement (seal exceeds limit now)
- **Spare Parts:** Pre-position seal kits at 3 maintenance bases
- **Hangar Scheduling:** Reserve 2-hour slots (align with other maintenance)
- **Result:** Zero AOG events, optimized parts inventory, reduced maintenance cost
- **Approval:** Maintenance planning (human oversight), CAOS provides optimization

### 10. **Door Inspection and Maintenance**

**Routine Inspections:**

**Pre-Flight (Every Flight):**
- [ ] Visual inspection of all doors (external and internal)
- [ ] Verify door position sensors (cockpit indication: all green)
- [ ] Check door handles in correct position (flush with door)
- [ ] Verify slide arming levers (ARMED for takeoff/landing)

**A-Check (Every 750 FH):**
- [ ] Detailed visual inspection (door panels, seals, hinges)
- [ ] Latch operation test (open/close door, verify smooth operation)
- [ ] Seal inflation pressure check (2.0 ±0.2 bar for passenger doors)
- [ ] Door position sensor functional test (verify EICAS indication)
- [ ] Slide arming lever functional test (verify ARMED/DISARMED indication)
- [ ] Lubrication of hinges, latches, actuators (per AMM)

**C-Check (Every 6,000 FH):**
- [ ] Door seal leak test (pressurize cabin to 8.5 psi, measure leak rate)
- [ ] Latch wear inspection (visual + dimensional checks)
- [ ] Door frame crack inspection (eddy current, aluminum frames)
- [ ] Composite door panel inspection (ultrasonic, detect delamination)
- [ ] Actuator motor current draw test (verify within limits)
- [ ] Slide pack inspection (visual, no fabric damage)
- [ ] Emergency lighting functional test (verify lights illuminate)

**Major Maintenance (Every 12,000 FH or 6 years):**
- [ ] Door seal replacement (proactive, before leak develops)
- [ ] Latch overhaul (disassemble, inspect, replace worn parts)
- [ ] Actuator motor overhaul (bearings, gearbox inspection)
- [ ] Slide repack (every 2 years or after deployment)
- [ ] Nitrogen cylinder hydrostatic test (every 5 years)
- [ ] Flight deck door security system test (forced entry resistance verification)

**Unscheduled Maintenance (As Required):**
- **Door Won't Close:** Inspect latches, hinges, seal interference
- **Door Seal Leak:** Replace seal, verify proper installation
- **Slide Won't Deploy:** Inspect arming mechanism, nitrogen cylinder pressure
- **Warning Light On:** Troubleshoot sensor, wiring, EICAS interface
- **Actuator Motor Failure:** Replace motor assembly, test operation

## Summary - ATA 52 Doors Chapter

This chapter establishes comprehensive door system specifications for the AMPEL360 BWB aircraft:

**Key Innovations:**
1. **Ventral Emergency Exits:** BWB-specific underfloor evacuation (addresses wide cabin challenge)
2. **CAOS Predictive Maintenance:** AI-driven door system health monitoring
3. **Smart Evacuation Management:** Digital Twin optimizes evacuation routes
4. **Composite Door Integration:** Advanced materials (CFRP, Kevlar) for lightweight security

**Regulatory Compliance:**
- **CS-25.783:** Doors (general requirements) - COMPLIANT
- **CS-25.807:** Emergency Exits (10 exits, exceeds minimum by 334%) - COMPLIANT
- **CS-25.795:** Flight Deck Security Door (5-minute intrusion resistance) - COMPLIANT
- **CS-25 Appendix J:** Emergency Evacuation (78 seconds, target <90 sec) - COMPLIANT

**Safety Features:**
- **Multiple Redundancy:** Mechanical + electrical actuation, primary + secondary seals
- **Fail-Safe Design:** Plug doors cannot open if pressurized (pressure seals door)
- **Warning Systems:** Multi-sensor (2oo3 voting), cockpit EICAS + aural alerts
- **Evacuation Capacity:** 10 exits, 500+ passengers/90 seconds (300 PAX certification)

**Lifecycle Management:**
- **Design Phase:** Door placement, structural integration, certification testing
- **Production:** Frame bonding, seal installation, slide packing
- **Operations:** Pre-flight checks, A-Check inspections, C-Check testing
- **Maintenance:** CAOS predictive alerts, proactive seal replacement, actuator overhaul
- **Certification:** Full-scale evacuation demo, door structural testing, slide deployment tests

---

*This chapter is part of the AMPEL360 OPT-IN Framework, managed through the 14-folder lifecycle skeleton for full traceability, CAOS integration, and continuous improvement.*

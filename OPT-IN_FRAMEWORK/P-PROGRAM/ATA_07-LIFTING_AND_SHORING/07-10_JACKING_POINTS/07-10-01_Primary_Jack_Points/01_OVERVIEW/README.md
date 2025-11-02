# Overview: 07-10-01 - Primary Jack Points

## 1.0 Purpose
This component defines the three primary jack points used for routine lifting of the AMPEL360 aircraft during maintenance operations. These jack points are certified for unlimited use and are the only approved locations for normal jacking operations.

## 2.0 Jack Point Summary

### 2.1 Three-Point Jacking Configuration
The AMPEL360 uses a conventional three-point jacking system:
- **1× Nose Jack Point:** Forward support
- **2× Main Jack Points:** Aft support (left and right)

This configuration provides stable, triangulated support with the aircraft's center of gravity located within the support triangle.

### 2.2 Jack Point Specifications Table

| Jack Point | Location (BRS) | Structural Frame | Capacity | Load Direction |
|------------|----------------|------------------|----------|----------------|
| **NJP-1 (Nose)** | FS 6,500 / BL 0 / WL 2,800 | Nose gear attachment frame | 200 kN | Vertical (axial) |
| **MJP-L (Main Left)** | FS 23,800 / BL -7,800 / WL 3,200 | Main gear attachment frame | 550 kN | Vertical (axial) |
| **MJP-R (Main Right)** | FS 23,800 / BL +7,800 / WL 3,200 | Main gear attachment frame | 550 kN | Vertical (axial) |

**Total System Capacity:** 1,300 kN (133 metric tons)  
**Aircraft MTOW:** 120,000 kg (1,177 kN at 1g)  
**Safety Factor:** 1.10 (adequate for static jacking with proper load distribution)

## 3.0 Design Rationale

### 3.1 Jack Point Location Selection
**Nose Jack Point (NJP-1):**
- Located at nose landing gear attachment frame (strongest forward structure)
- Position: 6.5m aft of nose apex (25% of total aircraft length)
- Benefits: 
  - Utilizes existing structural hard point (no new structure required)
  - Accessible from below aircraft with standard hangar floor clearance
  - Allows nose gear servicing when jacked

**Main Jack Points (MJP-L, MJP-R):**
- Located at main landing gear attachment frames (strongest aft structure)
- Position: 23.8m aft of nose apex (45% of total aircraft length)
- Lateral spacing: 15.6m (main gear track width)
- Benefits:
  - Utilizes existing structural hard points (main gear side brace attachment)
  - Wide lateral spacing provides excellent roll stability
  - Positioned near aircraft center of gravity (minimizes jack reactions)

### 3.2 Center of Gravity Considerations
**Aircraft CG Range:** 25% - 65% MAC (Mean Aerodynamic Chord)  
**MAC Location:** FS 18,000 to FS 35,000 (17m chord length)

**CG Position Analysis:**
- **Empty Aircraft:** CG at ~38% MAC (FS 24,500) - slightly aft of main jack points
- **MTOW (Full Fuel):** CG at ~35% MAC (FS 21,500) - slightly forward of main jack points
- **Jacking Stability:** CG always within support triangle (nose jack to main jacks)

**Jack Load Distribution (Typical - Empty Aircraft):**
- Nose Jack: 18% of aircraft weight (~21,600 kg)
- Main Jack Left: 41% of aircraft weight (~49,200 kg)
- Main Jack Right: 41% of aircraft weight (~49,200 kg)

**Verification:** Sum of jack loads = 100% aircraft weight ✓

### 3.3 Structural Interface Design
**Jack Point Structural Reinforcement:**
- Jack point frames are primary structure (not added for jacking)
- Landing gear attachment fittings sized for 3g ultimate landing loads
- Jacking loads are static (no dynamic load factor required)
- Stress analysis confirms adequate margin for jacking operations

**Composite Structure Considerations:**
- Jack points located at composite-to-metal interface (landing gear fittings)
- Metal fittings distribute load into composite structure via bonded/bolted joints
- No direct jack loading of composite laminates (prevents delamination risk)

## 4.0 Jack Point Identification

### 4.1 Physical Markings
**Nose Jack Point (NJP-1):**
- Yellow circle (300mm diameter) painted on lower surface
- Text: "JACK POINT NJP-1 / 200 kN MAX"
- Stencil includes jack adapter part number: P/N AMPEL-07-JP-001

**Main Jack Points (MJP-L, MJP-R):**
- Yellow circles (300mm diameter) painted on lower surface
- Text: "JACK POINT MJP-L/R / 550 kN MAX"
- Stencil includes jack adapter part number: P/N AMPEL-07-JP-002

**Marking Standard:** ATA Spec 100 Chapter 11 (Placards and Markings)

### 4.2 Tactile Identification
**Jack Pad Receptacles:**
- 4× M12 threaded inserts (recessed 2mm below surface)
- 200mm diameter circular boss (raised 5mm) for tactile location
- Inserts protected by rubber caps when not in use

**Access:**
- Jack points accessible without panel removal
- Clear area ±500mm around each jack point (no obstructions)

### 4.3 Documentation References
**Drawings:**
- Aircraft General Arrangement: AMPEL-06-001 (shows jack point locations)
- Jack Point Detail Drawing: AMPEL-07-001 (shows structural interface)
- Jack Pad Adapter Drawing: AMPEL-07-JP-001/002 (shows adapter design)

**Maintenance Manual:**
- AMM 07-10-00: Jack Point Identification and Preparation
- AMM 07-20-00: Jacking Procedures

## 5.0 Jack Pad Adapters

### 5.1 Adapter Design
**Nose Jack Adapter (P/N AMPEL-07-JP-001):**
- Material: Aluminum 7075-T6 (high-strength)
- Dimensions: 200mm diameter × 50mm thick
- Weight: 2.8 kg
- Interface: 4× M12 bolts attach to aircraft (torque: 150 Nm)
- Jack interface: 100mm diameter spherical socket (accepts ball-end jack head)
- Neoprene rubber face: 10mm thick (Shore A 60 durometer)

**Main Jack Adapter (P/N AMPEL-07-JP-002):**
- Material: Aluminum 7075-T6
- Dimensions: 250mm diameter × 60mm thick (larger due to higher load)
- Weight: 4.5 kg
- Interface: 4× M12 bolts attach to aircraft (torque: 150 Nm)
- Jack interface: 120mm diameter spherical socket
- Neoprene rubber face: 12mm thick (Shore A 60 durometer)

### 5.2 Load Distribution Analysis
**Contact Pressure Analysis:**

**Nose Jack Point:**
- Load: 200 kN (max)
- Contact area: 314 cm² (200mm diameter)
- Contact pressure: 6.4 MPa (930 psi)
- Composite allowable: 20 MPa (limit load)
- Safety margin: 3.1× (adequate)

**Main Jack Point:**
- Load: 550 kN (max)
- Contact area: 491 cm² (250mm diameter)
- Contact pressure: 11.2 MPa (1,625 psi)
- Composite allowable: 20 MPa (limit load)
- Safety margin: 1.8× (adequate)

**Conclusion:** Jack pad design provides adequate load distribution to prevent composite damage.

### 5.3 Inspection Requirements
**Pre-Use Inspection (Every Jacking Event):**
- Visual inspection: No cracks in adapter body
- Rubber face condition: No tears, cuts, or excessive wear
- Bolt threads: Clean and undamaged
- Spherical socket: No deformation or damage
- Identification marking: Legible part number

**Periodic NDT Inspection (Every 500 Jacking Cycles):**
- Ultrasonic inspection of adapter body (detect internal cracks)
- Eddy current inspection of bolt holes (detect fatigue cracks)
- Dimensional check: Verify adapter thickness (measure wear)

**Replacement Criteria:**
- Cracks detected (any size): Replace immediately
- Rubber face wear >3mm: Replace
- Deformation of spherical socket >0.5mm: Replace
- Bolt hole elongation >0.2mm: Replace

## 6.0 Operational Procedures

### 6.1 Jack Pad Installation
1. Clean jack point area (remove dirt, grease, debris)
2. Remove protective caps from threaded inserts
3. Inspect threaded inserts (clean with tap if necessary)
4. Position jack pad adapter on jack point (align bolt holes)
5. Install 4× M12 bolts finger-tight
6. Torque bolts in star pattern to 150 Nm ±10 Nm
7. Verify jack pad seated flush against aircraft surface

**Critical:** Do not over-torque bolts (risk of damaging composite structure)

### 6.2 Jack Pad Removal
1. Remove jack load (aircraft on wheels or safety stands)
2. Loosen M12 bolts in reverse star pattern
3. Remove bolts and jack pad adapter
4. Inspect jack point area for damage
5. Clean threaded inserts
6. Install protective caps on threaded inserts

### 6.3 Jack Point Inspection After Jacking
**Visual Inspection:**
- Check for cracks in composite structure around jack point
- Check for delamination (tap test - listen for hollow sound)
- Check for paint damage or scratches
- Check threaded inserts for pull-out or damage

**Documentation:**
- Record inspection results in aircraft logbook
- Note any discrepancies found
- Initiate corrective action if damage detected

## 7.0 Safety Considerations

### 7.1 Load Limits
**Never Exceed Limits:**
- Nose Jack Point: 200 kN (44,960 lbf)
- Main Jack Points: 550 kN (123,640 lbf) each

**Consequences of Overload:**
- Composite structure damage (delamination, cracking)
- Jack pad adapter failure
- Loss of structural integrity at jack point
- Potential aircraft collapse

### 7.2 Hydrogen Safety
**LH₂ System Proximity:**
- Nose jack point is 2.5m from forward hydrogen tank
- Main jack points are 1.8m from main hydrogen tank

**Mandatory Precautions:**
- LH₂ system must be depressurized before jacking
- Hydrogen detector monitoring required (<10 ppm)
- No hot work within 15m of jack points during jacking
- Fire extinguishers staged at each jack point

### 7.3 Composite Structure Protection
**Prevent Damage:**
- Always use approved jack pad adapters (do not jack directly on composite)
- Ensure jack pad properly seated before applying load
- Monitor for unusual sounds during jacking (cracking, popping)
- Stop immediately if structural distress observed

## 8.0 Related Documentation

### 8.1 Design Documents
- Structural Analysis Report: AMPEL-07-SAR-001
- Jack Point Stress Analysis: AMPEL-51-CALC-007
- Composite Interface Design: AMPEL-51-DES-012
- Load Distribution Study: AMPEL-07-LDS-001

### 8.2 Maintenance Documents
- AMM 07-10-00: Jack Point Identification
- AMM 07-20-00: Jacking Procedures
- AMM 51-00-00: Structural Inspection
- SRM 51-10-00: Composite Repair (if damage occurs)

### 8.3 Certification Documents
- Type Certificate Data Sheet (TCDS): Section 7 - Jacking
- Continued Airworthiness Instructions: CAI-07-001
- Service Bulletin (if issued): SB-AMPEL-07-XXX

## 9.0 Training Requirements

### 9.1 Personnel Qualifications
**Jack Point Inspection:**
- Basic aircraft maintenance training
- Composite structure familiarization (8-hour course)
- ATA 07 procedures training (4 hours)

**Jacking Operations:**
- Type-specific jacking certification (40-hour course)
- Hydrogen safety training (16 hours)
- Emergency procedures training (8 hours)

### 9.2 Recurrent Training
- Annual refresher: 4 hours
- Post-incident training: As required
- Procedure update training: When AMM revised

## 10.0 Revision History

| Revision | Date | Author | Description |
|----------|------|--------|-------------|
| 1.0 | 2025-11-02 | AMEDEOPELLICCIA | Initial release |

## 11.0 Approvals

**Technical Review:**  
Name: ________________  Date: ________

**Safety Review:**  
Name: ________________  Date: ________

**Certification Liaison:**  
Name: ________________  Date: ________

---

**Document Control:**  
- Document Number: AMPEL-07-10-01-OVR-001
- Classification: Internal Use
- Distribution: Engineering, Maintenance, Operations
- Next Review: 2026-11-02

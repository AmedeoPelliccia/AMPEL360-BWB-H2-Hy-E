# Build Specification
## PROTO-001 Engineering Development Unit

**Document:** PROTO-001-BUILD-SPEC  
**Status:** Conceptual  
**Date:** 2025-11-03

### 1. PURPOSE

Engineering development unit for:
- Structural validation (17 psi ultimate)
- **Modal testing and damping measurement (CRITICAL)**
- Manufacturing process development
- Correlation with FEA predictions

### 2. CONFIGURATION

#### 2.1 Door Panel
- **Size:** 1120mm × 1880mm (full scale)
- **Construction:** Composite sandwich
- **Face sheets:** 8-ply CFRP [0/+45/90/-45]s
- **Core:** Nomex HRH10-1/8-3.0, 38mm thick
- **Adhesive:** EA9396 film adhesive
- **Total thickness:** 48mm
- **Target weight:** <22 kg (panel only)

#### 2.2 Frame Structure
- **Type:** Simplified frame (non-flight)
- **Material:** Aluminum 6061-T6 angles
- **Purpose:** Support for testing only
- **Interfaces:** Hinge points, latch points

#### 2.3 Mechanisms
- **Latches:** Manual operation (6 locations)
- **Hinges:** Simplified bearing hinges
- **Handle:** Representative only
- **NO slide system (not required for EDU)**

#### 2.4 NOT INCLUDED
- Interior trim panels
- Insulation
- Wiring harness
- Pneumatic system
- Slide/raft system
- Production finish

### 3. MATERIAL SPECIFICATIONS

| Component | Material | Specification | Supplier |
|-----------|----------|---------------|----------|
| Prepreg | CFRP M21E | AMS 3863 | Hexcel |
| Core | Nomex HRH10 | AMS 3711 | DuPont |
| Adhesive | EA9396 | MMM-A-132 | Henkel |
| Inserts | Ti-6Al-4V | AMS 4928 | TBD |
| Frame | Al 6061-T6 | AMS-QQ-A-200 | Local |

### 4. MANUFACTURING PROCESS

#### 4.1 Face Sheet Layup
- **Method:** Hand layup
- **Environment:** Clean room (Class 100,000)
- **Temperature:** 23±2°C
- **Humidity:** 40-60% RH
- **Layup rate:** ~2 plies/hour
- **Debulking:** Every 2 plies, 5 minutes vacuum

#### 4.2 Core Preparation
- **Cutting:** Water jet or bandsaw
- **Adhesive:** Film adhesive application
- **Edge bands:** 25mm width, same prepreg

#### 4.3 Cure Cycle
```
Stage 1: Heat-up
- Ramp: 2°C/min to 120°C
- Vacuum: Full vacuum throughout

Stage 2: Adhesive cure
- Hold: 60 minutes at 120°C
- Pressure: Vacuum only

Stage 3: Prepreg cure
- Ramp: 2°C/min to 180°C
- Pressure: Apply 7 bar at 150°C
- Hold: 120 minutes at 180°C

Stage 4: Cooldown
- Rate: 2°C/min maximum
- Release pressure: At 80°C
- Remove from autoclave: <60°C
```

#### 4.4 Post-Cure Operations
- Trim to net dimensions
- Drill holes for inserts
- Install titanium inserts (adhesively bonded)
- NDT inspection (ultrasonic C-scan)
- Dimensional inspection (CMM)

### 5. QUALITY REQUIREMENTS

| Parameter | Requirement | Inspection Method |
|-----------|-------------|-------------------|
| Void content | <5% | Ultrasonic C-scan |
| Ply orientation | ±1° | Witness marks |
| Thickness | 48±1mm | Micrometer, 10 points |
| Flatness | <2mm over span | Straightedge |
| Weight | 22±2kg | Scale |
| Insert bond | >25 MPa | Pull test (witness) |

### 6. ACCEPTANCE CRITERIA

**ACCEPT if:**
- [ ] All dimensions within tolerance
- [ ] No defects >25mm diameter
- [ ] Void content <5% by area
- [ ] Weight 20-24 kg
- [ ] Visual quality: A-surface standard

**CONDITIONAL ACCEPT if:**
- Minor defects <25mm, not in high-stress areas
- Weight 24-26 kg (document for FEA update)
- Void content 5-7% (not in critical areas)

**REJECT if:**
- Any dimension out by >5mm
- Void content >7%
- Delaminations present
- Weight >26 kg
- Structural defects in high-stress zones

### 7. INSTRUMENTATION PROVISIONS

For testing, provide:
- **Accelerometer mount points:** 20 locations (bonded studs)
- **Strain gauge locations:** 30 locations (marked)
- **Pressure tap locations:** 10 locations (drilled)
- **Lifting/handling points:** 4 locations

### 8. BUILD SCHEDULE

| Activity | Duration | Dependencies |
|----------|----------|--------------|
| Tool preparation | 1 week | Mold available |
| Material kitting | 1 week | Materials received |
| Face sheet 1 layup | 2 days | Ready to start |
| Core bonding | 1 day | Face 1 cured |
| Face sheet 2 layup | 2 days | Core bonded |
| Autoclave cure | 1 day | Layup complete |
| Post-cure ops | 1 week | Cure complete |
| NDT & inspection | 3 days | Machining done |
| **Total** | **4 weeks** | **Critical path** |

### 9. COST ESTIMATE

| Item | Cost |
|------|------|
| Materials | $15,000 |
| Tooling time | $5,000 |
| Labor (320 hrs @ $100/hr) | $32,000 |
| Autoclave | $4,000 |
| NDT | $3,000 |
| Inspection | $2,000 |
| **Subtotal** | **$61,000** |
| Contingency (20%) | $12,200 |
| **Total** | **$73,200** |

### 10. LESSONS LEARNED CAPTURE

Document during build:
- Layup challenges
- Tool pulling issues
- Cure cycle adequacy
- Defect causes
- Process improvements
- Time actuals vs. estimates

---

**Document Control:** PROTO-001-BUILD-SPEC-001  
**Revision:** A  
**Date:** 2025-11-03

**Approvals:**
- Manufacturing Engineer: [ ]
- Quality Engineer: [ ]
- Program Manager: [ ]

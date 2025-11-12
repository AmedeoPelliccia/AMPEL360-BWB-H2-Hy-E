# Production Flow Diagram - Door L1 Forward

**Document:** AMPEL360-52-10-01-FLOW  
**Date:** 2025-11-03  
**Status:** DRAFT

---

## Manufacturing Flow Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DOOR L1 FORWARD PRODUCTION FLOW                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌───────────────┐
│   RECEIVING   │  Day 0: Material arrival, inspection, quarantine
│   Materials   │  - Prepreg rolls (frozen storage)
└───────┬───────┘  - Honeycomb core
        │          - Hardware, adhesives
        │
        ▼
┌───────────────┐
│    KITTING    │  Day 1: Material preparation and staging
│   & CUTTING   │  - Thaw prepreg (4 hours)
└───────┬───────┘  - Cut plies per templates
        │          - Kit hardware
        │          - Prepare adhesives
        ▼
┌───────────────┐
│     LAYUP     │  Day 2-3: Composite fabrication
│  (Clean Room) │  - Outer face sheet (8 plies)
└───────┬───────┘  - Core placement with adhesive
        │          - Inner face sheet (8 plies)
        │          - Debulking between stages
        │
        ▼
┌───────────────┐
│  VACUUM BAG   │  Day 3: Preparation for cure
│   & INSPECT   │  - Apply breather, release film
└───────┬───────┘  - Vacuum bag installation
        │          - Leak check (<10 mbar/min)
        │          - QC inspection hold point
        │
        ▼
┌───────────────┐
│   AUTOCLAVE   │  Day 4: Cure cycle
│     CURE      │  - Transport to autoclave facility
└───────┬───────┘  - 8-hour cure cycle (180°C, 7 bar)
        │          - Cooldown and removal
        │          - Return to factory
        │
        ▼
┌───────────────┐
│  INSPECTION   │  Day 5: Post-cure validation
│   & NDT       │  - Visual inspection
└───────┬───────┘  - Dimensional check
        │          - C-scan ultrasonic NDT (100%)
        │          - Document results
        │
        ▼
┌───────────────┐
│   TRIMMING    │  Day 5-6: Edge finishing
│   & DRILLING  │  - CNC trim to final dimensions
└───────┬───────┘  - Drill fastener holes
        │          - Install threaded inserts
        │          - Edge sealing
        │
        ▼
┌───────────────┐
│   ASSEMBLY    │  Day 7-9: Integration
│  (Mechanism)  │  - Install hinge mechanisms
└───────┬───────┘  - Mount latches and locks
        │          - Install seals and gaskets
        │          - Electrical connections (ECF, sensors)
        │          - Surface preparation
        │
        ▼
┌───────────────┐
│   PAINTING    │  Day 10: Finishing
│  & MARKING    │  - Prime and paint
└───────┬───────┘  - Apply markings
        │          - Cure paint
        │
        ▼
┌───────────────┐
│  FINAL TEST   │  Day 11: Functional validation
│ & INSPECTION  │  - Dimensional verification
└───────┬───────┘  - Function tests (open/close cycles)
        │          - Leak test (pressure decay)
        │          - Electrical continuity
        │          - Weight check
        │          - Final QC sign-off
        │
        ▼
┌───────────────┐
│   PACKAGE &   │  Day 12: Preparation for delivery
│   DELIVERY    │  - Protective packaging
└───────────────┘  - Documentation package
                   - Ship to customer/integration facility
```

---

## Detailed Process Steps

### 1. RECEIVING (Day 0)
**Duration:** 4 hours  
**Location:** Receiving dock  
**Inputs:** Raw materials from suppliers  
**Outputs:** Accepted materials in storage

**Activities:**
- Inspect packaging for damage
- Verify packing lists vs. purchase orders
- Check certificates of conformance
- Record material lot numbers
- Quarantine for inspection approval
- Store prepreg in freezer (-18°C)
- Store core in climate-controlled area

**Quality Control:**
- 100% visual inspection
- Certificate review
- Temperature verification for prepreg

---

### 2. KITTING & CUTTING (Day 1)
**Duration:** 8 hours  
**Location:** Prep area  
**Inputs:** Released materials  
**Outputs:** Cut plies, kitted hardware

**Activities:**
- Remove prepreg from freezer (4-hour thaw)
- Cut plies using templates
- Mark ply orientation and sequence
- Cut honeycomb core to size
- Kit fasteners, inserts, adhesives
- Verify kit completeness

**Quality Control:**
- Prepreg out-time tracking
- Ply dimension verification
- Kit completeness check

---

### 3. LAYUP (Days 2-3)
**Duration:** 16 hours  
**Location:** Clean room (Class 100,000)  
**Inputs:** Cut plies, core, adhesive  
**Outputs:** Assembled laminate ready for cure

**Activities:**
- Prepare and clean tool
- Apply release agent
- Lay up outer face sheet (8 plies)
- Debulk (5 min vacuum)
- Apply adhesive film
- Position honeycomb core
- Apply adhesive film
- Lay up inner face sheet (8 plies)
- Final debulk
- Install ECF (outer surface only)

**Quality Control:**
- Ply orientation verification (laser guide)
- Photo documentation each ply
- Witness corners marked
- Electrical continuity check for ECF
- No wrinkles, gaps, or bridging

---

### 4. VACUUM BAGGING (Day 3)
**Duration:** 4 hours  
**Location:** Clean room  
**Inputs:** Laid-up laminate  
**Outputs:** Bagged assembly ready for cure

**Activities:**
- Apply breather material
- Install perforated release film
- Position vacuum bag
- Seal edges with tape
- Install vacuum fittings
- Pull vacuum and leak check
- Achieve <10 mbar/min leak rate

**Quality Control:**
- Vacuum bag integrity
- Leak rate test
- Inspector sign-off required

---

### 5. AUTOCLAVE CURE (Day 4)
**Duration:** 8 hours (cycle) + transport  
**Location:** External autoclave facility  
**Inputs:** Bagged assembly  
**Outputs:** Cured composite panel

**Activities:**
- Transport to autoclave (in vacuum)
- Load into autoclave
- Connect thermocouples (6 locations)
- Run validated cure cycle:
  - Ramp: 2°C/min to 180°C
  - Hold: 120 minutes at 180±5°C
  - Pressure: 7.0±0.3 bar
  - Cooldown: <3°C/min
- Remove from autoclave
- Transport back to facility

**Quality Control:**
- Continuous monitoring of T, P, time
- Chart recording reviewed
- Out-of-spec conditions → scrap or engineering review

---

### 6. INSPECTION & NDT (Day 5)
**Duration:** 6 hours  
**Location:** Quality lab  
**Inputs:** Cured panel  
**Outputs:** Inspected, documented panel

**Activities:**
- Remove vacuum bag materials
- Visual inspection for defects
- Dimensional measurement (CMM)
- Ultrasonic C-scan (100% area)
- Analyze void content and delaminations
- Document all findings

**Quality Control:**
- No delaminations >25mm
- Void content <2%
- Dimensions within tolerance (±2mm)
- Accept/reject decision

---

### 7. TRIMMING & DRILLING (Days 5-6)
**Duration:** 8 hours  
**Location:** Machine shop  
**Inputs:** Inspected panel  
**Outputs:** Trimmed panel with holes

**Activities:**
- Mount in trim fixture
- CNC trim edges to final dimensions
- Drill fastener holes (CNC or manual)
- Ream holes to final size
- Install threaded inserts (bonded)
- Seal edges
- Clean and degrease

**Quality Control:**
- Edge distance verification
- Hole position check (CMM sample)
- Insert pull-out test (sample)
- No delamination at edges

---

### 8. ASSEMBLY (Days 7-9)
**Duration:** 12 hours  
**Location:** Assembly area  
**Inputs:** Trimmed panels, mechanisms, hardware  
**Outputs:** Complete door assembly

**Activities:**
- Assemble hinge mechanisms
- Install latches and locks
- Mount door handles
- Install seals and gaskets
- Route and connect electrical wiring
- Install sensors
- Torque all fasteners to specification
- Final cleaning

**Quality Control:**
- Torque verification (100% fasteners)
- Electrical continuity checks
- Mechanism function tests
- Gap and flush checks

---

### 9. PAINTING & MARKING (Day 10)
**Duration:** 8 hours (including cure)  
**Location:** Paint booth  
**Inputs:** Assembled door  
**Outputs:** Painted door

**Activities:**
- Mask off areas (seals, mechanisms)
- Apply primer
- Apply topcoat (per specification)
- Cure paint
- Apply placards and markings
- Remove masking
- Final cleaning

**Quality Control:**
- Paint thickness check
- Visual inspection for defects
- Marking placement verification

---

### 10. FINAL TEST & INSPECTION (Day 11)
**Duration:** 6 hours  
**Location:** Test area  
**Inputs:** Painted door  
**Outputs:** Tested, certified door

**Activities:**
- Final dimensional check
- Weight measurement
- Function test (50 cycles open/close)
- Leak test (pressure decay method)
- Electrical system check
- Final visual inspection
- Generate inspection report
- Apply conformity label

**Quality Control:**
- All dimensions within tolerance
- Weight: 72±7 kg
- Leak rate: <0.05 CFM
- 50 cycles without failure
- All electrical functions operational

---

### 11. PACKAGE & DELIVERY (Day 12)
**Duration:** 4 hours  
**Location:** Shipping area  
**Inputs:** Certified door  
**Outputs:** Packaged door ready for shipment

**Activities:**
- Install protective covers
- Pack in custom shipping container
- Include documentation package:
  - Certificate of conformance
  - Inspection reports
  - Material certifications
  - Installation instructions
  - IPC (Illustrated Parts Catalog) data
- Arrange shipment

**Quality Control:**
- Package integrity check
- Documentation completeness
- Shipping damage protection

---

## Work-in-Process (WIP) Tracking

| Stage | Typical WIP | Max WIP | Buffer Reason |
|-------|-------------|---------|---------------|
| Kitting | 1-2 units | 3 | Material availability |
| Layup | 1-2 units | 2 | Clean room capacity |
| Cure queue | 2-4 units | 6 | Autoclave schedule |
| Post-cure | 1-2 units | 3 | NDT capacity |
| Trim/drill | 1 unit | 2 | Quick operation |
| Assembly | 2-3 units | 4 | Complex operations |
| Painting | 1-2 units | 2 | Cure time |
| Final test | 1 unit | 2 | Testing time |
| **Total WIP** | **10-15 units** | **24** | Safety margin |

---

## Cycle Time Analysis

**Total Touch Time:** 52 hours  
**Total Calendar Time:** 12 working days  
**Efficiency:** ~33% (touch time / calendar time)

**Non-value-added time:**
- Waiting for autoclave: 1-2 days
- Paint cure: 0.5 day
- Queue time between operations: 2-3 days
- Transportation: 0.5 day

**Improvement Opportunities:**
- Reduce autoclave wait with better scheduling
- Overlapping operations where possible
- Better WIP management
- Expedited transport to/from autoclave

---

**Document Control:**
- **Revision:** Draft 1.0
- **Date:** 2025-11-03
- **Next Review:** Upon process changes

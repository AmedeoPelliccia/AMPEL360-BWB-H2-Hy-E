# Dimensional Build Standard Control

**Component Code:** 02-11-00  
**Folder:** 09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT  
**Document:** Dimensional_Build_Standard_Control.md

## Purpose

This document defines how dimensional design versions are controlled and tracked against each build standard, ensuring that the correct geometric configuration is applied to each Manufacturer Serial Number (MSN) for the AMPEL360 BWB H₂ Hy-E aircraft.

## Overview

Build standard control for dimensions ensures that:
- Each aircraft is built to the correct dimensional design version
- Design changes affecting dimensions are properly incorporated at the right MSN
- As-built geometry is traceable to the approved build standard
- Dimensional deviations from build standard are identified and dispositioned
- Configuration management maintains dimensional integrity across the fleet

## Build Standard Definition

### Build Standard Hierarchy

**Level 1: Aircraft Model**
- AMPEL360 BWB H₂ Hy-E Q100
- Top-level aircraft configuration defining overall architecture

**Level 2: Build Standard (BS)**
- Specific design configuration applicable to a range of MSNs
- Example: BS-001 (Prototype), BS-002 (Pre-Production), BS-003 (Production Standard)
- Includes all design documentation: CAD models, drawings, specifications

**Level 3: Dimensional Configuration**
- Subset of build standard specific to ATA 02-11-00 dimensions and geometry
- Defined by: baseline_dimensions.json version, CAD model version, tolerance specifications
- Example: BS-001 uses baseline_dimensions.json v1.0, CAD model release R1.0

**Level 4: MSN-Specific Configuration**
- Individual aircraft as-built geometry
- Starts with build standard nominal dimensions
- Includes approved deviations and as-built measurements
- Example: MSN-P001 built to BS-001, with approved deviations per ECR-2024-0015

## Build Standard Development Process

### Prototype Build Standard (BS-001)

**Purpose:** Initial aircraft design for type certification

**Dimensional Configuration:**
- **baseline_dimensions.json:** v1.0 (initial design)
- **CAD model:** Release R1.0 (frozen for prototype manufacturing)
- **Tolerance specifications:** Initial design tolerances per `03_REQUIREMENTS/RQ-TOLERANCES-*`
- **Special considerations:**
  - Prototype may include test instrumentation affecting dimensions
  - Some dimensions may be TBD (To Be Determined) pending analysis
  - Dimensional deviations more liberal for prototype learning

**Applicability:** MSN-P001 (single prototype aircraft)

**Approval:** Chief Engineer, Certification Lead

### Pre-Production Build Standard (BS-002)

**Purpose:** Refined design incorporating prototype lessons learned, suitable for early customer deliveries

**Dimensional Configuration:**
- **baseline_dimensions.json:** v2.0 (updated based on prototype as-built and flight test)
- **CAD model:** Release R2.0 (dimensional changes from R1.0 incorporated)
- **Tolerance specifications:** Refined tolerances based on manufacturing capability
- **Key changes from BS-001:**
  - Dimensional corrections based on prototype deviations
  - Tightened tolerances in areas where manufacturing demonstrated capability
  - Removal of test instrumentation provisions affecting dimensions
  - TBD dimensions resolved

**Applicability:** MSN-PP001 through MSN-PP010 (10 pre-production aircraft)

**Approval:** Chief Engineer, Certification Lead, Customer Approval (for delivery aircraft)

### Production Build Standard (BS-003)

**Purpose:** Final production configuration after type certification

**Dimensional Configuration:**
- **baseline_dimensions.json:** v3.0 (certified configuration)
- **CAD model:** Release R3.0 (type certified design)
- **Tolerance specifications:** Production tolerances optimized for manufacturing
- **Key changes from BS-002:**
  - All dimensions validated through flight test and certification
  - Production tolerances established based on process capability
  - Design optimizations for manufacturability (if any)
  - Customer options defined (if dimensional variants exist)

**Applicability:** MSN-001 onwards (serial production aircraft)

**Approval:** Type Certificate Data Sheet (TCDS) issued by certification authority, Chief Engineer

### Subsequent Build Standards (BS-004, BS-005, ...)

**Triggers for new build standard:**
- Significant dimensional design change (e.g., wing extension, fuselage stretch)
- Product improvement program affecting dimensions
- Customer variant with different dimensions
- Regulatory-mandated change affecting geometry

**Process:**
1. Engineering Change Request (ECR) proposes dimensional change
2. Impact analysis: effect on aerodynamics, structures, systems, certification
3. ECR approved by Change Board
4. New build standard defined with updated baseline_dimensions.json and CAD model
5. Effectivity defined: MSN at which new build standard applies
6. Certification authority concurrence (if affecting type certificate)

## Dimensional Configuration Tracking

### Build Standard to MSN Mapping

**Master Configuration Table:**
- Maintained in production database and CAOS system
- Columns: MSN, Build Standard, Baseline Dimensions Version, CAD Model Release, Manufacturing Start Date, Delivery Date, Customer

**Example:**

| MSN | Build Standard | Baseline Dimensions | CAD Model | Start Date | Status |
|---|---|---|---|---|---|
| MSN-P001 | BS-001 | v1.0 | R1.0 | 2027-01-15 | Completed |
| MSN-PP001 | BS-002 | v2.0 | R2.0 | 2027-09-01 | In Progress |
| MSN-PP002 | BS-002 | v2.0 | R2.0 | 2027-10-01 | Planned |
| ... | ... | ... | ... | ... | ... |
| MSN-001 | BS-003 | v3.0 | R3.0 | 2029-03-01 | Planned |

### Dimensional Effectivity Management

**Effectivity Definition:**
- **From MSN:** First aircraft to which dimensional change applies
- **To MSN:** Last aircraft with previous dimension (if not open-ended)
- **Effectivity options:**
  - **Immediate:** Applies to next aircraft in sequence
  - **Optional:** Customer choice to incorporate or not
  - **Mandatory:** All aircraft from effectivity point forward

**Example Effectivity:**
- ECR-2025-0042: Wing span increase by 2 m
- Effectivity: MSN-050 and subsequent (open-ended)
- Build Standard: BS-004 (new) applicable from MSN-050
- Baseline Dimensions: v4.0 (wingspan updated from 65.0 m to 67.0 m)

### Engineering Change Control

**Engineering Change Request (ECR) for Dimensions:**
1. **Initiation:** Engineer identifies need for dimensional change (performance, manufacturing, certification)
2. **Proposal:** ECR drafted with:
   - Description of dimensional change
   - Reason for change
   - Affected dimensions (from baseline_dimensions.json)
   - Impact assessment (aerodynamics, weight, systems, certification)
   - Proposed effectivity
   - Updated CAD model and drawings
3. **Review:** Change Board reviews ECR (Engineering, Certification, Production, Quality, Customer Support)
4. **Approval:** Change Board approves ECR, assigns build standard effectivity
5. **Implementation:** CAD model updated, baseline_dimensions.json revised, drawings released
6. **Verification:** First aircraft to new build standard inspected to verify dimensional change

**ECR Classification for Dimensions:**
- **Class I:** Significant dimensional change affecting type certificate (e.g., wing extension)
  - Requires certification authority approval
  - May require amended type certificate or supplemental type certificate
- **Class II:** Dimensional change within type certificate limits (e.g., minor ground clearance adjustment)
  - Engineering approval, certification authority informed
- **Class III:** Manufacturing tolerance or process change, no design dimension change
  - Engineering and production approval

## Dimensional Deviation Management

### Deviation from Build Standard

**Types of Dimensional Deviations:**
1. **Manufacturing Deviation:** As-built dimension differs from build standard nominal
   - Example: Overall length 48.52 m vs. nominal 48.50 m (within tolerance, no action)
2. **Engineering Disposition:** Out-of-tolerance dimension accepted by engineering
   - Example: Belly clearance 0.79 m vs. minimum 0.80 m (accepted with concession)
3. **Temporary Deviation:** Short-term deviation on specific MSNs, not permanent change
   - Example: Prototype has test instrumentation affecting height (+0.2 m)

**Deviation Control Process:**
1. **Identification:** Dimensional deviation identified during inspection (see `QUALITY_CONTROL/As_Built_Geometry_Inspection.md`)
2. **Documentation:** Non-Conformance Report (NCR) generated
3. **Engineering review:** Responsible engineer evaluates deviation
4. **Disposition:**
   - **Accept as-is:** Deviation within acceptance limits, no rework
   - **Rework:** Correct dimension to bring within tolerance
   - **Repair:** Implement approved repair to achieve acceptable dimension
   - **Use-as-is (concession):** Out-of-tolerance but acceptable for operation (requires authority approval if affecting certification)
5. **Traceability:** Deviation recorded in MSN configuration record
6. **Build standard update:** If deviation recurs, consider updating build standard (tolerance or nominal dimension)

### Concession Process

**When required:** Dimensional deviation outside design tolerance but acceptable for safety and function

**Process:**
1. Engineering prepares concession request:
   - Deviation description and magnitude
   - Engineering justification (why it is acceptable)
   - Impact on performance, safety, certification
   - Affected MSNs
   - Whether one-time or recurring
2. Internal approval: Chief Engineer, Certification Lead
3. External approval (if required):
   - Certification authority (if affecting type certificate)
   - Customer (if affecting operational performance or aesthetics)
4. Concession documented and linked to MSN(s)
5. Concession review: Periodic review to determine if design change needed

## Quality Control of Build Standard Application

### Build Standard Verification

**At Start of MSN Manufacturing:**
- [ ] Verify MSN is assigned to correct build standard
- [ ] Verify CAD model release matches build standard
- [ ] Verify baseline_dimensions.json version matches build standard
- [ ] Verify all ECRs effective for this MSN have been incorporated
- [ ] Verify tooling and fixtures are correct for build standard

**During Manufacturing:**
- [ ] Monitor dimensional compliance to build standard (inspection per `QUALITY_CONTROL/As_Built_Geometry_Inspection.md`)
- [ ] Track deviations and dispositions
- [ ] Verify no unapproved dimensional changes

**At MSN Completion:**
- [ ] Final verification that as-built geometry conforms to build standard (within tolerances or approved deviations)
- [ ] As-built configuration record complete and accurate
- [ ] MSN configuration linked to build standard in database

### Build Standard Audit

**Frequency:** Quarterly for production aircraft, per aircraft for prototype/pre-production

**Audit Activities:**
1. Sample MSNs: Select 2-3 aircraft currently in production
2. Verify build standard assignment: Correct BS assigned to each MSN per effectivity
3. Verify dimensional data: As-built dimensions traceable to build standard baseline
4. Verify deviation management: All deviations properly documented and dispositioned
5. Verify change control: All ECRs effective for sample MSNs incorporated
6. Findings and corrective actions: Document any discrepancies, implement corrections

**Responsible Party:** Quality Engineering, Configuration Management

## Integration with CAOS Digital Twin

### Build Standard in Digital Twin

**CAOS Digital Twin Model:**
- Each MSN digital twin instantiated from build standard configuration
- Build standard defines nominal geometry loaded into digital twin
- As-built measurements update digital twin with actual geometry
- Deviations visualized in digital twin (color-coded: green = conforming, yellow = accepted deviation, red = out-of-tolerance)

**CAOS Configuration Management:**
- CAOS database stores build standard hierarchy and MSN assignments
- Automated checks ensure MSN manufactured to correct build standard
- Alerts if CAD model or baseline_dimensions.json version mismatch for MSN
- Change control workflow integrated: ECR approval triggers build standard update in CAOS

### Lifecycle Traceability

**From Design to Operations:**
1. **Design:** Build standard defined with baseline_dimensions.json and CAD model
2. **Manufacturing:** MSN manufactured to build standard, as-built geometry captured
3. **Certification:** Build standard geometry certified via TCDS
4. **Operations:** AFM and WBM reference build standard dimensions
5. **Maintenance:** As-built geometry used for maintenance planning, spare parts compatibility
6. **Modification:** Design changes create new build standard, effectivity tracked
7. **End of life:** Build standard history archived for fleet analysis

## Related Documents

- `01_OVERVIEW/baseline_dimensions.json` – Dimensional baseline for each build standard
- `04_DESIGN/` – CAD models and drawings for each build standard release
- `09_PRODUCTION_PLANNING/DATA_GENERATION/As_Built_Geometry_Configuration.md` – As-built data management
- `09_PRODUCTION_PLANNING/QUALITY_CONTROL/As_Built_Geometry_Inspection.md` – Inspection procedures
- `09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT/Dimensional_Configuration_Tracking.csv` – MSN configuration tracking
- `09_PRODUCTION_PLANNING/SERIAL_NUMBER_MANAGEMENT/MSN_Geometry_Data_Linkage.md` – MSN data linkage
- `14_META_GOVERNANCE/` – Configuration management procedures, change control processes
- Company Configuration Management Plan
- Engineering Change Control Procedures

---

**Document Control:**
- Version: 1.0
- Status: Template
- Last Updated: 2025-11-11
- Classification: Configuration Critical

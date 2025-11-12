# ATA 02 - Operations Information
## Numbering System Guide

**Document ID:** AMPEL360-02-00-00-OVR-NS  
**Version:** 1.0.0  
**Date:** 2025-11-04  
**Classification:** Operations Critical

---

## 1. PURPOSE

This guide explains the ATA numbering system used throughout AMPEL360 operational documentation, ensuring consistent identification and organization of all operational information.

---

## 2. ATA CHAPTER SYSTEM

### 2.1 ATA 100 Specification

**Origin:** Air Transport Association (ATA) Specification 100  
**Purpose:** Standardized chapter numbering for aerospace technical documentation  
**Adoption:** Worldwide standard across aviation industry

**ATA Chapters Relevant to Operations:**

| Chapter | Title | Operations Relevance |
|---------|-------|---------------------|
| **02** | **Operations Information** | **Primary - All operational data** |
| 05 | Time Limits/Maintenance Checks | MEL, dispatch requirements |
| 06 | Dimensions and Areas | Loading, parking |
| 07 | Lifting and Shoring | Ground handling |
| 12 | Servicing | Refueling procedures |
| 28 | Fuel (H2) | Fuel system data |
| 71-73 | Power Plant (Fuel Cells) | Propulsion system data |
| 95 | Neural Networks (CAOS) | AI operations support |

---

## 3. ATA 02 NUMBERING STRUCTURE

### 3.1 Primary Level: Systems (02-XX-00)

**Format:** `02-XX-00` where XX = 10-99

**Structure:**

```
02-00-00  GENERAL
02-10-00  AIRCRAFT GENERAL DATA
02-20-00  WEIGHT AND BALANCE
02-30-00  HYDROGEN FUEL DATA
02-40-00  PERFORMANCE DATA
02-50-00  OPERATING LIMITATIONS
02-60-00  FLIGHT PLANNING DATA
02-70-00  EMERGENCY PROCEDURES DATA
02-80-00  OPERATIONAL PROCEDURES
02-90-00  CAOS OPERATIONS INTEGRATION
```

**Numbering Logic:**
- **00-09**: General, overview, introductory
- **10-19**: Aircraft physical data
- **20-29**: Weight, balance, loading
- **30-39**: Fuel system (H2-specific for AMPEL360)
- **40-49**: Performance data
- **50-59**: Limitations
- **60-69**: Flight planning
- **70-79**: Emergency procedures
- **80-89**: Normal operations
- **90-99**: Advanced systems (CAOS, neural networks)

### 3.2 Secondary Level: Subsystems (02-XX-YY-00)

**Format:** `02-XX-YY-00` where YY = 00-99

**Example: 02-30-00 HYDROGEN FUEL DATA**

```
02-30-00  HYDROGEN FUEL DATA (System Level)
    ├── 02-31-00  H2 Fuel Capacity Data
    ├── 02-32-00  H2 Refueling Procedures
    ├── 02-33-00  H2 Weight and CG Effects
    ├── 02-34-00  H2 System Limitations
    ├── 02-35-00  H2 Fuel Planning Data
    ├── 02-36-00  H2 Temperature Effects
    ├── 02-37-00  H2 Quantity Indication
    ├── 02-38-00  H2 Emergency Procedures
    └── 02-39-00  H2 Ground Operations
```

**Subsystem Numbering Logic:**
- **X0**: General/overview for that system
- **X1**: Primary data (capacity, specifications)
- **X2**: Procedures (normal operations)
- **X3**: Effects and interactions
- **X4**: Limitations and constraints
- **X5**: Planning data
- **X6**: Environmental factors
- **X7**: Indications and monitoring
- **X8**: Emergency procedures
- **X9**: Ground/special operations

### 3.3 Tertiary Level: Procedure Groups (02-XX-YY-ZZ)

**Format:** `02-XX-YY-ZZ` where ZZ = 00-99

**Example: 02-32-03 H2 Refueling Operation**

```
02-32-00  H2 REFUELING PROCEDURES (Subsystem Level)
    ├── 02-32-01  Refueling Equipment
    ├── 02-32-02  Pre-Refueling Checks
    ├── 02-32-03  Refueling Operation
    ├── 02-32-04  Post-Refueling Checks
    ├── 02-32-05  Emergency Defueling
    ├── 02-32-06  Troubleshooting
    └── 02-32-07  Documentation
```

### 3.4 Quaternary Level: Specific Procedures (02-XX-YY-ZZ-AA)

**Format:** `02-XX-YY-ZZ-AA` where AA = 01-99

**Example: 02-32-03-05 Pressure Monitoring**

```
02-32-03  REFUELING OPERATION (Procedure Group)
    ├── 02-32-03-01  Connection Procedure
    ├── 02-32-03-02  Flow Rate Control
    ├── 02-32-03-03  Temperature Monitoring
    ├── 02-32-03-04  Leak Detection
    ├── 02-32-03-05  Pressure Monitoring
    ├── 02-32-03-06  Quantity Verification
    └── 02-32-03-07  Disconnection Procedure
```

---

## 4. DOCUMENT IDENTIFICATION

### 4.1 Document Number Format

**Complete Format:** `AMPEL360-02-XX-YY-ZZ-AAA`

**Components:**
- **AMPEL360**: Platform identifier
- **02**: ATA Chapter
- **XX**: System code
- **YY**: Subsystem code
- **ZZ**: Document type code
- **AAA**: Sequential number within type

**Document Type Codes:**

| Code | Type | Description |
|------|------|-------------|
| **OVR** | Overview | General descriptions, introductions |
| **LIM** | Limitations | Operating limits and constraints |
| **PER** | Performance | Performance data and charts |
| **PRO** | Procedures | Step-by-step operational procedures |
| **DAT** | Data | Data tables and specifications |
| **CHK** | Checklists | Action checklists |
| **REF** | Reference | Quick reference materials |
| **TRN** | Training | Training documentation |
| **EMG** | Emergency | Emergency procedures |
| **CAO** | CAOS | AI-enhanced operations data |

### 4.2 Document Number Examples

```
AMPEL360-02-00-00-OVR-001
   ↓      ↓  ↓  ↓  ↓   ↓
Platform Ch Sy Ss Type Seq
AMPEL360  02 00 00 OVR 001

Translation: AMPEL360 platform, ATA 02 (Operations), 
             General (00-00), Overview type, Document #1
```

```
AMPEL360-02-32-03-PRO-005
   ↓      ↓  ↓  ↓  ↓   ↓
Platform Ch Sy Ss Type Seq
AMPEL360  02 32 03 PRO 005

Translation: AMPEL360 platform, ATA 02 (Operations),
             H2 Refueling (32), Refueling Operation (03),
             Procedure type, Document #5
```

---

## 5. FOLDER AND FILE NAMING

### 5.1 Folder Naming Convention

**Format:** `XX-YY-ZZ_DESCRIPTIVE_NAME`

**Rules:**
- Always use 2-digit codes with leading zeros
- Use underscores for spaces
- ALL CAPS for descriptive names
- Avoid special characters except hyphen and underscore

**Examples:**
```
02-00_OPS-GENERAL-INFO
02-30-00_HYDROGEN_FUEL_DATA
02-32-00_H2_REFUELING_PROCEDURES
02-32-03_REFUELING_OPERATION
```

### 5.2 File Naming Convention

**Markdown Files:** `Descriptive_Name.md`
- Use Title Case
- Underscores for spaces
- Descriptive and meaningful

**Examples:**
```
ATA_02_Purpose_Scope.md
AMPEL360_Operations_Overview.md
H2_Refueling_Quick_Reference.md
```

**PDF Files:** `Document_Type_Description.pdf`

**Examples:**
```
Quick_Reference_Card.pdf
H2_Emergency_Procedures.pdf
Performance_Charts_Takeoff.pdf
```

**Asset Files:** `Category_Description.extension`

**Examples:**
```
ATA_02_Structure_Diagram.svg
BWB_Configuration_Overview.pdf
H2_System_Schematic.png
```

---

## 6. CROSS-REFERENCING

### 6.1 Internal References

**Format:** `See Section XX-YY-ZZ`

**Examples:**
```
"For H2 refueling procedures, see Section 02-32-00."
"Refer to Section 02-40-01 for takeoff performance data."
"Emergency defueling procedures are in Section 02-38-05."
```

**With Document ID:**
```
"See AMPEL360-02-32-03-PRO-001 for detailed refueling procedure."
```

### 6.2 External References

**To Other ATA Chapters:**
```
"For fuel system description, see ATA 28-00-00."
"Fuel cell technical data is in ATA 71-00-00."
"CAOS neural network architecture is in ATA 95-00-00."
```

**To Regulatory Documents:**
```
"As required by EASA CS-25.1583."
"Per FAA 14 CFR 25.1585."
"In accordance with ICAO Annex 6, Part I."
```

---

## 7. SPECIAL AMPEL360 NUMBERING

### 7.1 Hydrogen Fuel System (02-30-XX)

**Dedicated series for H2 operations:**

```
02-30-00  HYDROGEN FUEL DATA (Main)
02-31-00  H2 Fuel Capacity Data
02-32-00  H2 Refueling Procedures
02-33-00  H2 Weight and CG Effects
02-34-00  H2 System Limitations
02-35-00  H2 Fuel Planning Data
02-36-00  H2 Temperature Effects
02-37-00  H2 Quantity Indication
02-38-00  H2 Emergency Procedures
02-39-00  H2 Ground Operations
```

**Rationale:** Hydrogen fuel system is unique to AMPEL360 and requires dedicated numbering series for comprehensive coverage.

### 7.2 CAOS Operations (02-90-XX)

**Dedicated series for AI-enhanced operations:**

```
02-90-00  CAOS OPERATIONS INTEGRATION (Main)
02-91-00  Digital Twin Operations Interface
02-92-00  Predictive Operations Analytics
02-93-00  Real-Time Performance Monitoring
02-94-00  Fleet Operations Data Sharing
02-95-00  Neural Network Operations Support
02-96-00  Automated Flight Planning
02-97-00  Operations Data Recording
02-98-00  Crew Decision Support Systems
02-99-00  Operations Optimization AI
```

**Rationale:** CAOS integration is fundamental to AMPEL360 operations and requires comprehensive operational documentation.

### 7.3 BWB-Specific Numbering

**Enhanced weight and balance coverage:**

```
02-20-00  WEIGHT AND BALANCE (Main)
02-21-00  Empty Weight Data
02-22-00  Loading Procedures
02-23-00  Center of Gravity Limits
02-24-00  Weight Limitations
02-25-00  Load Distribution Requirements
02-26-00  Weighing Procedures
02-27-00  Ballast Requirements
02-28-00  Cargo Loading Procedures
02-29-00  CAOS Weight Monitoring
```

**Rationale:** BWB configuration has unique weight and balance characteristics requiring detailed procedures.

---

## 8. REVISION AND VERSION NUMBERING

### 8.1 Document Versions

**Format:** `Major.Minor.Patch` (e.g., 1.0.0)

**Major Version (X.0.0):**
- Significant operational changes
- New systems or procedures
- Regulatory requirement changes
- Requires training

**Minor Version (X.Y.0):**
- Improvements and enhancements
- Clarifications
- Additional data
- May require briefing

**Patch Version (X.Y.Z):**
- Corrections and typos
- Formatting changes
- Minor clarifications
- No training required

**Examples:**
```
1.0.0 → Initial release
1.0.1 → Typo correction
1.1.0 → Additional data added
2.0.0 → Major procedure change
```

### 8.2 Revision Tracking

**Revision Header:**
```
Document ID: AMPEL360-02-32-03-PRO-001
Version: 1.2.1
Date: 2025-11-04
Supersedes: 1.2.0 (2025-10-15)
Status: Released
```

**Revision History Table:**
```
| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0.0 | 2025-01-01 | Initial release | J. Smith |
| 1.0.1 | 2025-02-15 | Typo corrections | J. Smith |
| 1.1.0 | 2025-06-01 | Added winter ops | M. Jones |
| 1.2.0 | 2025-10-15 | Updated H2 data | K. Brown |
| 1.2.1 | 2025-11-04 | Formatting fixes | K. Brown |
```

---

## 9. DIGITAL SYSTEM INTEGRATION

### 9.1 EFB (Electronic Flight Bag) Navigation

**Folder Structure in EFB:**
```
AMPEL360 Operations
├── 02-00-00 GENERAL
├── 02-10-00 AIRCRAFT DATA
├── 02-20-00 WEIGHT & BALANCE
├── 02-30-00 H2 FUEL
├── 02-40-00 PERFORMANCE
├── 02-50-00 LIMITATIONS
├── 02-60-00 FLIGHT PLANNING
├── 02-70-00 EMERGENCY
├── 02-80-00 PROCEDURES
└── 02-90-00 CAOS
```

**Quick Access Codes:**
- Users can type "02-32" to jump directly to H2 refueling
- Search by keyword also available
- Recent documents tracked
- Bookmarks supported

### 9.2 CAOS System References

**CAOS Database IDs:**
- Format: `CAOS-02-XXXXX`
- Examples:
  - `CAOS-02-32001`: H2 refueling procedure in CAOS
  - `CAOS-02-40015`: Takeoff performance calculator
  - `CAOS-02-90005`: Real-time optimization module

**Integration:**
- Paper/EFB documents reference CAOS IDs
- CAOS displays reference ATA numbers
- Bidirectional linking
- Automatic updates

---

## 10. INTERNATIONAL STANDARDS ALIGNMENT

### 10.1 EASA/FAA Alignment

**CS-25 / FAR 25 Sections:**
```
ATA 02-50-00 (Operating Limitations)
    → Maps to CS-25.1583 / FAR 25.1583

ATA 02-40-00 (Performance Data)
    → Maps to CS-25.1587 / FAR 25.1587

ATA 02-80-00 (Operational Procedures)
    → Maps to CS-25.1585 / FAR 25.1585
```

### 10.2 ICAO Alignment

**ICAO Annex 6 Cross-Reference:**
```
ATA 02-60-00 (Flight Planning)
    → Aligns with Annex 6, Part I, Chapter 4

ATA 02-70-00 (Emergency Procedures)
    → Aligns with Annex 6, Part I, Chapter 6

ATA 02-20-00 (Weight and Balance)
    → Aligns with Annex 6, Part I, Chapter 7
```

---

## 11. QUICK REFERENCE

### 11.1 Common ATA 02 Numbers

| Number | Description | Use Case |
|--------|-------------|----------|
| 02-00-00 | General | Overview, conventions |
| 02-20-00 | W&B | Loading, CG calculations |
| 02-30-00 | H2 Fuel | Refueling, planning |
| 02-32-03 | H2 Refuel Op | Detailed refueling steps |
| 02-40-01 | Takeoff Perf | Takeoff calculations |
| 02-43-00 | Cruise Perf | Cruise planning |
| 02-45-00 | Landing Perf | Landing calculations |
| 02-50-00 | Limitations | All operational limits |
| 02-70-00 | Emergency | Emergency procedures |
| 02-90-00 | CAOS | AI-enhanced operations |

### 11.2 Finding Information

**By Topic:**
1. Identify general category (10, 20, 30, etc.)
2. Find specific subsystem (XX-YY-00)
3. Locate procedure or data (XX-YY-ZZ)

**By Keyword:**
- Use EFB search function
- Web portal search
- CAOS voice query
- Document index

**By Need:**
- **Pre-flight:** 02-80-01 (Normal procedures)
- **Refueling:** 02-32-03 (Refueling operation)
- **Flight planning:** 02-60-00 (Flight planning data)
- **Emergency:** 02-70-00 (Emergency procedures)
- **Performance:** 02-40-XX (Performance data)

---

## 12. NUMBERING SYSTEM MAINTENANCE

### 12.1 Adding New Numbers

**Process:**
1. Identify appropriate XX-YY level
2. Check for available numbers in series
3. Assign next sequential number
4. Update master index
5. Document in revision notes

**Reservation:**
- Numbers can be reserved for future use
- Reserved numbers documented
- Prevents duplicate assignment

### 12.2 Deprecating Numbers

**When to Deprecate:**
- Procedure no longer used
- Data superseded
- System removed

**Process:**
1. Mark as "DEPRECATED" in index
2. Cross-reference to replacement
3. Archive original content
4. Update all cross-references

---

## 13. TRAINING ON NUMBERING SYSTEM

### 13.1 Initial Training

**Content:**
- ATA 100 overview (1 hour)
- ATA 02 structure (1 hour)
- AMPEL360-specific numbering (1 hour)
- Finding information (1 hour)
- Hands-on practice (2 hours)

**Assessment:**
- Find 10 specific procedures
- Identify correct ATA numbers
- Navigate EFB efficiently

### 13.2 Quick Reference Card

**Pocket guide includes:**
- Common ATA 02 numbers
- Document ID format
- Revision number meaning
- Quick search tips
- Emergency procedure numbers

---

## 14. CONTACT INFORMATION

**Numbering System Questions:**
- Email: ata-numbering@ampel360.aero
- Phone: +34 91 XXX XXXX

**Technical Publications:**
- Email: tech-pubs@ampel360.aero
- Phone: +34 91 XXX XXXX (24/7)

**Document Access Support:**
- Email: docs-support@ampel360.aero
- Phone: +34 91 XXX XXXX (24/7)

---

**Document Status:** ✅ RELEASED  
**Effective Date:** 2029-01-01 (Entry Into Service)  
**Next Review:** 2026-11-04 (Annual)  
**Configuration Control:** Git SHA-256: [hash]

---
document_id: 95-00-01-010-LOOPS-README
title: Loop Packet System Documentation
subtitle: Per-ID CCert/CVal Circuit Control Infrastructure
version: 1.0
date: 2025-12-13
status: ACTIVE
owner: AMPEL360 / ATA 95 Governance
classification: INTERNAL
primary_ata: "95"
related_ata: ["ALL"]
---

# Loop Packet System Documentation

## 1. Purpose

This document describes the **Loop Packet** infrastructure for managing the **CCert/CVal circuit** on a per-artifact basis.

**Key Concept**: The BB Identity Register (95-00-01-010_BB_Identity_Register.md) is the *index*. The **Loop Packet** is the *per-ID lifecycle dossier* that contains all circuit artifacts for deterministic evidence management.

**Epistemological Foundation**: This infrastructure implements **PR-O-RO™ (Protorobotics)** — a certification-grade epistemology for hybrid cyber-physical artifacts. See:
- [PRORO_FOUNDING_MANIFESTO.md](PRORO_FOUNDING_MANIFESTO.md) — Complete PR-O-RO™ framework
- [PROTO_ROBOT_PARADIGM.md](PROTO_ROBOT_PARADIGM.md) — Biological lifecycle analogies

**Proto-Robot Paradigm**: Each BB artifact is a **proto-robot híbrido** (cyber-physical entity) with a biological lifecycle, governed by PR-O-RO principles.

---

## 2. Architecture Overview

### 2.1 Proto-Robot as Living Entity

Each **BB-xxx** is a proto-robot with:
- **Cuerpo** (Body) — Physical instantiation
- **Cerebro** (Brain) — Embedded intelligence  
- **ADN** (DNA) — AM baseline (immutable after DV)
- **Pasaporte** (Passport) — DPP with predictive claims
- **Experiencia** (Experience) — OM operational events
- **Validación médica** (Medical checkup) — OAV empirical gate
- **Sabiduría** (Wisdom) — DT accumulated truth
- **Evolución** (Evolution) — AM → AM′ under governance

### 2.2 Two-Layer Structure

1. **Register Layer** (Index)
   - Location: `95-00-01-010_BB_Identity_Register.md` + CSV
   - Purpose: Master index of all Body+Brain artifacts
   - Content: One-line summary per artifact with loop status

2. **Loop Packet Layer** (Detailed Dossier)
   - Location: `LOOPS/<bb_id>/`
   - Purpose: Complete lifecycle evidence for one artifact
   - Content: 7 minimum artifacts per BB ID

---

## 3. Loop Packet Structure

### 3.1 Folder Organization

```
95-00-01_Registers/
└── 95-00-01-010_BB_Identity_Register/
    ├── LOOPS/
    │   ├── TEMPLATES/           # Reusable templates
    │   │   ├── LOOP_TEMPLATE.md
    │   │   ├── AM_TEMPLATE.md
    │   │   ├── DV_TEMPLATE.md
    │   │   ├── DPP_TEMPLATE.md
    │   │   ├── OM_TEMPLATE.md
    │   │   ├── OAV_TEMPLATE.md
    │   │   └── DT_TEMPLATE.md
    │   │
    │   └── <bb_id>/             # One folder per artifact
    │       ├── LOOP_<bb_id>.md  # Circuit control record
    │       ├── AM_<bb_id>.md    # At-Rest Model
    │       ├── DV_<bb_id>.md    # Design Validation
    │       ├── DPP_<bb_id>.md   # Digital Product Passport
    │       ├── OM_<bb_id>.md    # Operational Mission
    │       ├── OAV_<bb_id>.md   # On-Asset Validation
    │       └── DT_<bb_id>.md    # Digital Twin
    │
    └── ASSETS/
        └── 95-00-01-010-A-001_BodyBrain_Identity_Register.csv
```

### 3.2 Minimum Artifacts per BB ID

Every `<bb_id>` SHALL eventually have these 7 artifacts:

1. **LOOP_<bb_id>.md** — Circuit control record (state machine)
2. **AM_<bb_id>.md** — At-Rest Model (baseline definition)
3. **DV_<bb_id>.md** — Design Validation (pre-operational proof)
4. **DPP_<bb_id>.md** — Digital Product Passport (authoritative identity)
5. **OM_<bb_id>.md** — Operational Mission (predicted behavior)
6. **OAV_<bb_id>.md** — On-Asset Validation (operational truth)
7. **DT_<bb_id>.md** — Digital Twin (accumulated evidence)

---

## 4. The CCert/CVal Circuit

### 4.1 Circuit Flow

```
AM → DV → DPP → OM → OAV → DT → AM′
│    │    │     │    │     │     │
│    │    │     │    │     │     └─ Updated AM under change control
│    │    │     │    │     └─ Accumulated operational truth
│    │    │     │    └─ Operational context validation
│    │    │     └─ Predicted operational manifestation
│    │    └─ Authoritative identity record
│    └─ Design validation gate
└─ Baseline definition
```

### 4.2 Gate Rules

**DV Gate**: "DPP issuance allowed?"
- **Condition**: DV must PASS before DPP can be issued
- **Evidence**: Test reports, coverage, simulation, safety validation
- **Authority**: Engineering + Certification

**OAV Gate**: "OM validated in asset context?"
- **Condition**: OAV must PASS to confirm OM predictions
- **Evidence**: Flight test, telemetry, operational campaigns
- **Authority**: Flight test + Certification

---

## 5. CSV Register Columns

### 5.1 Core Identity Columns (existing)

- `bb_id` — Unique identifier (ATAxx-BB-###)
- `artifact_name` — Human-readable name
- `body_summary` — Physical components
- `brain_summary` — Embedded logic
- `body_ata` — Functional ATA (physical ownership)
- `brain_ata` — Functional ATA (logic ownership)
- `dal` — Design Assurance Level
- `brain_type` — Classification (ML-INF, RT-CTRL, NAV, etc.)

### 5.2 Evidence Pointer Columns (existing)

- `dpp_id` — Digital Product Passport ID
- `image_id` — Software loadable package
- `sbom_ref` — Software Bill of Materials
- `bom_ref` — (Physical) Bill of Materials
- `am_ref` — At-Rest Model reference
- `dv_ref` — Design Validation reference
- `om_class` — Operational Mission classification
- `oav_ref` — On-Asset Validation reference
- `dt_ref` — Digital Twin reference

### 5.3 NEW: Loop Status Columns

- **`loop_packet_path`** — Relative path to Loop Packet folder
  - Example: `LOOPS/27-BB-008`

- **Circuit State Columns**:
  - `am_status` — `[NOT_STARTED | IN_PROGRESS | COMPLETED | APPROVED]`
  - `dv_status` — `[NOT_STARTED | IN_PROGRESS | PASSED | FAILED | APPROVED]`
  - `dpp_status` — `[NOT_ISSUED | ISSUED | UPDATED | FROZEN]`
  - `om_status` — `[NOT_DEFINED | DEFINED | VALIDATED]`
  - `oav_status` — `[NOT_STARTED | PLANNED | IN_PROGRESS | PASSED | FAILED]`
  - `dt_status` — `<snapshot_count>` (integer)

- **Control Columns**:
  - `next_gate` — `[DV | OAV | COMPLETE]` (deterministic next action)
  - `last_truth_snapshot_id` — Most recent DT snapshot ID

- **notes** — Free-form notes

---

## 6. Deterministic Next Step Rule

For any `bb_id`, the system can compute the next required action:

```
IF am_status = NOT_STARTED THEN
  next_gate = "DV"
  next_action = "Write AM (At-Rest Model) first"

ELSE IF dv_status ≠ PASSED THEN
  next_gate = "DV"
  next_action = "Write/Complete DV and mark DV gate"

ELSE IF dpp_status = NOT_ISSUED AND dv_status = PASSED THEN
  next_gate = "OAV"
  next_action = "Issue DPP (locked identity + claims)"

ELSE IF om_status ≠ DEFINED THEN
  next_gate = "OAV"
  next_action = "Author OM (what DPP predicts operationally)"

ELSE IF oav_status ≠ PASSED THEN
  next_gate = "OAV"
  next_action = "Define/Execute OAV (asset context truth validation)"

ELSE
  next_gate = "COMPLETE"
  next_action = "Append DT snapshot and propose AM′ (change-controlled update)"
```

---

## 7. Using the Loop Packet System

### 7.1 Creating a New Loop Packet

**Step 1**: Add entry to CSV register
```csv
bb_id,artifact_name,...,loop_packet_path,am_status,dv_status,...
XX-BB-YYY,My Artifact,...,LOOPS/XX-BB-YYY,NOT_STARTED,NOT_STARTED,...
```

**Step 2**: Create Loop Packet folder
```bash
mkdir LOOPS/XX-BB-YYY
```

**Step 3**: Generate skeleton from templates
```bash
for template in LOOP AM DV DPP OM OAV DT; do
  sed 's/<bb_id>/XX-BB-YYY/g; ...' \
    LOOPS/TEMPLATES/${template}_TEMPLATE.md > \
    LOOPS/XX-BB-YYY/${template}_XX-BB-YYY.md
done
```

**Step 4**: Populate according to deterministic next step

### 7.2 Updating Loop State

When an artifact completes a lifecycle stage:

1. Update the relevant artifact file (e.g., complete `AM_XX-BB-YYY.md`)
2. Update `LOOP_XX-BB-YYY.md` with new status
3. Update CSV register with new status columns
4. Compute and update `next_gate` based on rules

### 7.3 Gate Passage

**DV Gate Passage**:
1. Complete all DV validation activities
2. Update `DV_XX-BB-YYY.md` with gate decision = PASS
3. Update CSV: `dv_status = PASSED`
4. Update CSV: `next_gate = OAV` (now DPP can be issued)
5. Update `LOOP_XX-BB-YYY.md` DV gate section

**OAV Gate Passage**:
1. Complete all OAV validation campaigns
2. Update `OAV_XX-BB-YYY.md` with gate decision = PASS
3. Update CSV: `oav_status = PASSED`
4. Update CSV: `next_gate = COMPLETE`
5. Update `LOOP_XX-BB-YYY.md` OAV gate section

---

## 8. Automation and Tooling

### 8.1 Suggested Automation

**Loop Packet Generator** (Python script):
- Input: BB ID, artifact details
- Output: Complete Loop Packet skeleton with placeholders filled
- Location: `tools/generate_loop_packet.py`

**Loop Status Checker** (Python script):
- Input: BB ID or CSV register
- Output: Current status, next gate, missing artifacts
- Location: `tools/check_loop_status.py`

**Loop Dashboard** (Web UI):
- Visual representation of all Loop Packets
- Status indicators (red/yellow/green)
- Filterable by ATA, DAL, status
- Location: TBD

### 8.2 CI/CD Integration

**Validation Checks** (GitHub Actions):
- Verify Loop Packet completeness
- Validate CSV register consistency
- Check that `next_gate` matches computed value
- Ensure file references are valid

---

## 9. Example: 27-BB-008 Loop Packet

### 9.1 Artifact Details

| Field | Value |
|---|---|
| BB ID | 27-BB-008 |
| Artifact Name | Active Gust Alleviation System |
| Body ATA | 27 (Flight Controls) |
| Brain ATA | 95 (Neural Networks & AI) |
| DAL | A (most critical) |
| Brain Type | ML-INF (Machine Learning Inference) |

### 9.2 Loop Packet Location

```
LOOPS/27-BB-008/
├── LOOP_27-BB-008.md    # Control record
├── AM_27-BB-008.md      # At-Rest Model
├── DV_27-BB-008.md      # Design Validation
├── DPP_27-BB-008.md     # Digital Product Passport
├── OM_27-BB-008.md      # Operational Mission
├── OAV_27-BB-008.md     # On-Asset Validation
└── DT_27-BB-008.md      # Digital Twin
```

### 9.3 Current Status (Example)

```csv
bb_id,am_status,dv_status,dpp_status,om_status,oav_status,dt_status,next_gate
27-BB-008,NOT_STARTED,NOT_STARTED,NOT_ISSUED,NOT_DEFINED,NOT_STARTED,0,DV
```

**Interpretation**: AM needs to be written first. Next action is to populate `AM_27-BB-008.md`.

---

## 10. ATA Sovereignty in Loop Packets

### 10.1 Sovereignty Rules

- **Body ATA** owns physical definition (BOM, drawings, installation)
- **Brain ATA** owns logic definition (SBOM, algorithms, models)
- **ATA 95** governs DPP and circuit coordination
- **Interface Contract** defines how Body and Brain interact

### 10.2 Multi-ATA Coordination

For artifacts like 27-BB-008:
- **Body**: ATA 27 owns control surfaces, sensors, actuators
- **Brain**: ATA 95 owns ML model, training data, inference runtime
- **DPP**: ATA 95 governs the passport
- **Certification**: Both ATAs contribute evidence under unified safety case

---

## 11. Change Control and AM → AM′

### 11.1 When to Update AM

Triggers for AM → AM′:
- DT truth reveals performance deviation
- New operational requirements
- Safety-relevant findings
- Regulatory changes

### 11.2 Change Control Process

1. **Propose AM′**: Document rationale in DT
2. **CCB Review**: Configuration Control Board evaluates impact
3. **Impact Assessment**: Safety, certification, fleet implications
4. **Approval**: CCB approves or rejects
5. **Update**: Create AM′ version (new DPP version may be required)
6. **Traceability**: Update LOOP control record with change history

### 11.3 Immutability Rules

Elements that **cannot change** without creating new BB ID:
- Core functional purpose
- Safety classification (DAL)
- Certification basis
- Physical/logical interface specifications (breaking changes)

Elements that **can be updated** via AM′:
- Performance targets (improvements)
- Maintainability procedures
- Non-breaking interface extensions
- Brain updates (within certified envelope)

---

## 12. Relationship to Other ATA 95 Documents

### 12.1 Upstream Documents

- **95-00-01-009**: CCert/CVal Body+Brain Circuit Model
  - Defines the conceptual circuit
  - Loop Packets are the *implementation* of that circuit

- **95-00-01-003**: DPP Key Concepts
  - Defines what a DPP is
  - Loop Packets contain the actual DPP artifacts

### 12.2 Downstream Documents

- **ATA-specific documentation**: Each artifact links to its functional ATA
  - Example: 27-BB-008 links to ATA 27 flight control specs

- **95-90 Schemas**: Loop Packet data maps to database schemas
  - Common Entity Schemas
  - TimeSeries and Telemetry Schemas
  - CCert/CVal Database Schema

---

## 13. Document Control

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2025-12-13 | AMPEL360/ATA 95 Governance | Initial Loop Packet system documentation |

---

**End of Loop Packet System Documentation**

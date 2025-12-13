# Loop Packet Quick Start Guide

## Overview

The **Loop Packet** system provides per-artifact lifecycle dossiers for managing the CCert/CVal circuit.

**Key Concept**: 
- **Register** (CSV + MD) = Index (one-line per artifact)
- **Loop Packet** = Complete lifecycle evidence (7 files per artifact)

---

## Creating a New Loop Packet

### Method 1: Using the Generator Script (Recommended)

```bash
cd /path/to/AMPEL360-BWB-H2-Hy-E

python3 tools/generate_loop_packet.py \
  --bb-id 32-BB-001 \
  --name "Brake System Control Unit" \
  --body-ata 32 \
  --brain-ata 32 \
  --dal A \
  --brain-type RT-CTRL \
  --body-summary "Brake assemblies and valves" \
  --brain-summary "Antiskid and autobrake software" \
  --om-class "Landing Gear - Braking Control"
```

**Output**:
- Creates `LOOPS/32-BB-001/` with all 7 files
- Generates CSV entry for register
- All placeholders filled with your values

### Method 2: Manual Creation

1. **Copy templates**:
   ```bash
   mkdir LOOPS/<bb_id>
   cp LOOPS/TEMPLATES/*_TEMPLATE.md LOOPS/<bb_id>/
   ```

2. **Rename files**:
   ```bash
   cd LOOPS/<bb_id>
   for f in *_TEMPLATE.md; do mv "$f" "${f/_TEMPLATE/_<bb_id>}"; done
   ```

3. **Fill placeholders**:
   - Replace `<bb_id>`, `<Artifact_Name>`, etc. in each file
   - Use search-and-replace in your editor

---

## Checking Loop Status

### Check specific artifact:

```bash
python3 tools/check_loop_status.py --bb-id 27-BB-008
```

**Output**:
```
BB ID: 27-BB-008
Name:  Active Gust Alleviation System
✅ Loop Packet directory exists
✅ All 7 files present
Next Gate: DV
Next Action: Write AM (At-Rest Model) first
```

### Check all artifacts (summary):

```bash
python3 tools/check_loop_status.py --summary
```

**Output**:
```
Total Artifacts: 150
With Loop Packets: 45 (30.0%)
Complete (7 files): 38 (25.3%)
With Issues: 7

Next Gates:
  DV: 120
  OAV: 25
  COMPLETE: 5
```

### Validate consistency:

```bash
python3 tools/check_loop_status.py --validate --verbose
```

---

## Working with Loop Packets

### 1. Start New Artifact

**Add to CSV register**:
```csv
32-BB-001,Brake System Control Unit,Brake assemblies...,Antiskid software...,32,32,A,RT-CTRL,TBD,TBD,TBD,TBD,LOOPS/32-BB-001/AM_32-BB-001.md,TBD,Landing Gear - Braking Control,TBD,LOOPS/32-BB-001/DT_32-BB-001.md,LOOPS/32-BB-001,NOT_STARTED,NOT_STARTED,NOT_ISSUED,NOT_DEFINED,NOT_STARTED,0,DV,NONE,New artifact
```

**Generate Loop Packet** (using script above)

**Next action**: Populate `AM_32-BB-001.md`

### 2. Progress Through Circuit

**After completing AM**:
1. Update `AM_32-BB-001.md` with actual content
2. Update `LOOP_32-BB-001.md`: `am_status = COMPLETED`
3. Update CSV: `am_status = COMPLETED`, `next_gate = DV`
4. **Next action**: Write `DV_32-BB-001.md`

**After DV passes**:
1. Complete `DV_32-BB-001.md` with validation evidence
2. Mark DV gate as `PASSED` in both LOOP and CSV
3. Update CSV: `dv_status = PASSED`, `next_gate = OAV`
4. **Next action**: Issue `DPP_32-BB-001.md`

**Continue pattern** through OM → OAV → DT → AM′

### 3. Gate Decisions

**DV Gate** (Design Validation):
- **Question**: "Can we issue a DPP?"
- **Criteria**: All design validation complete
- **Evidence**: Test reports, coverage, safety validation
- **Authority**: Engineering + Certification

**OAV Gate** (On-Asset Validation):
- **Question**: "Does OM match operational reality?"
- **Criteria**: Flight test or operational validation complete
- **Evidence**: Telemetry, campaign results, crew feedback
- **Authority**: Flight test + Certification

---

## Deterministic Next Step

The system always knows what to do next:

```
IF am_status = NOT_STARTED
  → Write AM first

ELSE IF dv_status ≠ PASSED
  → Complete DV

ELSE IF dpp_status = NOT_ISSUED
  → Issue DPP

ELSE IF om_status ≠ DEFINED
  → Write OM

ELSE IF oav_status ≠ PASSED
  → Execute OAV

ELSE
  → Append DT + propose AM′
```

**Check your next step**:
```bash
python3 tools/check_loop_status.py --bb-id <your_id>
# Look at "Next Action" field
```

---

## The 7 Files Explained

1. **LOOP_<bb_id>.md**: Control record
   - Current state of all artifacts
   - Gate decisions
   - Next action
   - Change history

2. **AM_<bb_id>.md**: At-Rest Model
   - Body definition (physical)
   - Brain definition (logic)
   - Requirements
   - Maintainability

3. **DV_<bb_id>.md**: Design Validation
   - Test campaigns
   - Requirements coverage
   - Performance validation
   - Gate decision

4. **DPP_<bb_id>.md**: Digital Product Passport
   - Locked identity
   - Configuration baseline
   - Predictive claims
   - Certification evidence
   - JSON payload

5. **OM_<bb_id>.md**: Operational Mission
   - Predicted behavior
   - Operational envelope
   - Performance targets
   - Crew procedures

6. **OAV_<bb_id>.md**: On-Asset Validation
   - Validation campaigns
   - Telemetry analysis
   - Performance vs prediction
   - Gate decision

7. **DT_<bb_id>.md**: Digital Twin
   - Snapshot registry
   - Operational data
   - Anomalies/events
   - Truth ledger
   - Lessons learned

---

## Common Workflows

### Adding Multiple Artifacts

**Bulk creation script** (example):
```bash
#!/bin/bash
# add_multiple_artifacts.sh

artifacts=(
  "32-BB-001:Brake System Control Unit:32:32:A:RT-CTRL"
  "32-BB-002:Landing Gear Control Unit:32:42:A:RT-CTRL"
  "32-BB-003:Nose Wheel Steering:32:32:B:RT-CTRL"
)

for artifact in "${artifacts[@]}"; do
  IFS=':' read -r bb_id name body_ata brain_ata dal brain_type <<< "$artifact"
  
  python3 tools/generate_loop_packet.py \
    --bb-id "$bb_id" \
    --name "$name" \
    --body-ata "$body_ata" \
    --brain-ata "$brain_ata" \
    --dal "$dal" \
    --brain-type "$brain_type" \
    --body-summary "TBD" \
    --brain-summary "TBD" \
    --om-class "TBD"
    
  # Add CSV entry to register
  tail -1 "LOOPS/$bb_id/${bb_id}_register_entry.csv" >> \
    ASSETS/95-00-01-010-A-001_BodyBrain_Identity_Register.csv
done
```

### Validating Before Release

```bash
# Check all artifacts
python3 tools/check_loop_status.py --validate

# Fix any issues
# Re-check
python3 tools/check_loop_status.py --summary

# If clean, proceed with release
```

---

## File Locations

```
OPT-IN_FRAMEWORK/
└── N-NEURAL_NETWORKS_USERS_TRACEABILITY/
    └── ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/
        └── 95-00_GENERAL/
            └── 95-00-01_Registers/
                └── 95-00-01-010_BB_Identity_Register/
                    ├── README.md           # Full documentation
                    ├── LOOPS/
                    │   ├── TEMPLATES/      # 7 template files
                    │   ├── 27-BB-008/      # Example Loop Packet
                    │   └── <other_ids>/    # Your artifacts
                    └── ASSETS/
                        └── 95-00-01-010-A-001_BodyBrain_Identity_Register.csv

tools/
├── generate_loop_packet.py    # Generator script
└── check_loop_status.py        # Status checker
```

---

## Tips & Best Practices

1. **Use the generator**: Don't copy templates manually
2. **Update LOOP file frequently**: It's the state machine
3. **Keep CSV in sync**: Run status checker regularly
4. **One gate at a time**: Don't skip steps
5. **Document decisions**: Gate rationale is crucial
6. **Evidence pointers**: Always link to actual evidence
7. **Use TBD wisely**: Mark unknowns clearly, resolve later

---

## Getting Help

- **Full documentation**: `95-00-01_Registers/95-00-01-010_BB_Identity_Register/README.md`
- **Main register**: `95-00-01-010_BB_Identity_Register.md` (section 4.4)
- **Example**: `LOOPS/27-BB-008/` (Active Gust Alleviation System)
- **Templates**: `LOOPS/TEMPLATES/` (reference structures)

---

**End of Quick Start Guide**

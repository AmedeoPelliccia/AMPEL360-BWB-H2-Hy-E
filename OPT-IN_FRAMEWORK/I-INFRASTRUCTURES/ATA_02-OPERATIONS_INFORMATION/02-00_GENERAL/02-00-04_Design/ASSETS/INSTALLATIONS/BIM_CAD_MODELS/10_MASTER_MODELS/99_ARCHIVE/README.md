# 10_MASTER_MODELS / 99_ARCHIVE

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 10_MASTER_MODELS / 99_ARCHIVE  
**Purpose:** Date-segregated archive for superseded master models with location preservation

---

## Archive Organization

This archive uses **date-segregated folders** that preserve the location structure (OPSCTR, DATACENTER, H2ROOM, GSE_AREA). This allows you to see what the complete coordinated design looked like at any point in time.

---

## Structure Pattern

```
99_ARCHIVE/
├── 02-00-04-MSTR-ARCHIVE_YYYY-MM-DD_<Milestone>/
│   ├── OPSCTR/
│   │   ├── <archived master model files>
│   │   └── EXPORTS/
│   ├── DATACENTER/
│   │   └── <archived master model files>
│   ├── H2ROOM/
│   │   └── <archived master model files>
│   ├── GSE_AREA/
│   │   └── <archived master model files>
│   └── INDEX_Archive_YYYY-MM-DD.csv
├── 02-00-04-MSTR-ARCHIVE_YYYY-MM-DD_<Milestone>/
│   └── ...
└── README.md (this file)
```

### Folder Naming Convention

```
02-00-04-MSTR-ARCHIVE_YYYY-MM-DD_<Milestone>
```

Where:
- `YYYY-MM-DD` = Archive date (when models were superseded)
- `<Milestone>` = Brief description (e.g., PreCoordination, PostReview_V1, DesignFreeze)

### Examples

- `02-00-04-MSTR-ARCHIVE_2025-01-15_PreCoordination/`
- `02-00-04-MSTR-ARCHIVE_2025-03-30_PostReview_V1/`
- `02-00-04-MSTR-ARCHIVE_2025-06-20_DesignFreeze/`

---

## Why Preserve Location Structure

**Location folders** (OPSCTR, DATACENTER, etc.) are preserved in archives because:
1. **Context** - Shows complete design snapshot at milestone
2. **Comparison** - Easy to compare OPSCTR design across time periods
3. **Retrieval** - Find specific location's archived model quickly
4. **Coordination** - See how different locations related at a point in time

This is different from templates archive (05_TEMPLATES/99_ARCHIVE), which doesn't need location structure because templates aren't location-specific.

---

## When to Archive Master Models

Archive master models at:
1. **Major milestones** - End of design phase, design freeze, pre-construction
2. **Coordination cycles** - After major coordination review and clash resolution
3. **Client deliverables** - When submitting to client for approval
4. **Before major changes** - Before significant design changes
5. **Phase transitions** - Transition from LOD300 to LOD350, etc.

**Typical archive frequency:** Every 2-4 weeks during active design, at each major milestone

---

## Archiving Process

### 1. Create Archive Folder

```bash
mkdir "02-00-04-MSTR-ARCHIVE_2025-MM-DD_<Milestone>"
cd "02-00-04-MSTR-ARCHIVE_2025-MM-DD_<Milestone>"
mkdir OPSCTR DATACENTER H2ROOM GSE_AREA
```

### 2. Copy Master Models by Location

Copy current master models from active folders to archive folders:

```bash
# Copy OPSCTR models
cp ../OPSCTR/02-00-04-MSTR-OPSCTR-Design-LOD300-R02.rvt \
   02-00-04-MSTR-ARCHIVE_2025-MM-DD_<Milestone>/OPSCTR/

# Copy DATACENTER models
cp ../DATACENTER/02-00-04-MSTR-DATACENTER-Design-LOD300-R01.rvt \
   02-00-04-MSTR-ARCHIVE_2025-MM-DD_<Milestone>/DATACENTER/

# Repeat for H2ROOM and GSE_AREA
```

### 3. Include Key Exports (Optional)

Optionally copy key IFC or VIEW_ONLY exports:

```bash
cp ../OPSCTR/EXPORTS/IFC/02-00-04-MSTR-OPSCTR-Design-LOD300-R02.ifc \
   02-00-04-MSTR-ARCHIVE_2025-MM-DD_<Milestone>/OPSCTR/
```

### 4. Create Archive Index

Create `INDEX_Archive_YYYY-MM-DD.csv` documenting:
- Model file name
- Location
- LOD level
- Revision number
- Milestone/reason for archive
- Key changes from previous archive

### 5. Update Active CHANGELOG

Document the archiving action in the parent `10_MASTER_MODELS/README.md` or CHANGELOG.

---

## Archive Index Format

**File:** `INDEX_Archive_YYYY-MM-DD.csv`

```csv
Model_File,Location,LOD,Revision,Milestone,Key_Changes,Archive_Date
02-00-04-MSTR-OPSCTR-Design-LOD300-R02.rvt,OPSCTR,LOD300,R02,PreCoordination,Console layout finalized,2025-01-15
02-00-04-MSTR-DATACENTER-Design-LOD300-R01.rvt,DATACENTER,LOD300,R01,PreCoordination,Initial rack layout,2025-01-15
02-00-04-MSTR-H2ROOM-Design-LOD300-R01.rvt,H2ROOM,LOD300,R01,PreCoordination,Safety systems defined,2025-01-15
02-00-04-MSTR-GSE_AREA-Design-LOD300-R01.rvt,GSE_AREA,LOD300,R01,PreCoordination,Kiosk locations set,2025-01-15
```

---

## Retention Policy

### Archive Retention

- **Active project**: Keep all archives for project duration + 1 year
- **Post-project**: Retain archives for 7 years (standard project records retention)
- **Milestone archives**: Retain permanently (design freeze, as-built, etc.)

### Storage Considerations

- Master models can be large (100MB - 1GB+ per file)
- Consider compression for long-term storage
- Use external storage or cloud archive for completed projects
- Ensure backups of critical milestone archives

---

## Retrieving Archived Master Models

### When to Retrieve

- Compare current design to previous milestone
- Investigate design changes or evolution
- Client requests previous design version
- Coordination issue requiring historical review
- Litigation or dispute resolution
- Lessons learned or post-project review

### Retrieval Process

1. **Locate archive folder** by date and milestone
2. **Navigate to location folder** (OPSCTR, DATACENTER, etc.)
3. **Review INDEX file** to confirm model details
4. **Copy (don't move)** model from archive
5. **Open as read-only** to prevent accidental modification
6. **Document purpose** of retrieval

### Comparison Workflow

To compare archived model to current:
1. Open archived model (read-only)
2. Open current model
3. Use comparison tools (if available)
4. Document differences
5. Close without saving changes to archived model

---

## Archive Quality Standards

### Before Archiving

✅ Models open without errors  
✅ All links resolved  
✅ Coordinate system correct  
✅ Key views saved  
✅ IFC export successful (if including)  
✅ Archive index created  
✅ Milestone clearly documented  
✅ CHANGELOG updated  

### Archive Integrity

- **Read-only** - Set archived files to read-only after creating archive
- **Checksums** - Calculate checksums for large archives to verify integrity
- **Documentation** - Include comprehensive INDEX file with each archive
- **Testing** - Spot-check archived models periodically to ensure they open correctly

---

## Best Practices

### Archive Organization

✅ **DO:**
- Archive at consistent milestones
- Include all locations in each archive (complete snapshot)
- Create comprehensive INDEX files
- Document reason for archive clearly
- Maintain location structure

❌ **DON'T:**
- Don't archive individual locations separately (breaks snapshot)
- Don't modify archived files (read-only)
- Don't delete archives without approval
- Don't skip INDEX file creation

### Milestone Selection

Good milestones for archiving:
- Design phase completion (SD, DD, CD)
- Coordination cycle completion
- Client approval milestones
- Design freeze before construction
- As-built model completion

Avoid:
- Too frequent archiving (creates clutter)
- Arbitrary dates without meaningful milestone

---

## Archive Naming Examples

### Typical Archive Folders

```
02-00-04-MSTR-ARCHIVE_2025-01-15_PreCoordination/
├── OPSCTR/
│   └── 02-00-04-MSTR-OPSCTR-Design-LOD300-R01.rvt
├── DATACENTER/
│   └── 02-00-04-MSTR-DATACENTER-Design-LOD300-R01.rvt
├── H2ROOM/
│   └── 02-00-04-MSTR-H2ROOM-Design-LOD300-R01.rvt
└── INDEX_Archive_2025-01-15.csv

02-00-04-MSTR-ARCHIVE_2025-03-30_PostReview_V1/
├── OPSCTR/
│   └── 02-00-04-MSTR-OPSCTR-Design-LOD300-R02.rvt
├── DATACENTER/
│   └── 02-00-04-MSTR-DATACENTER-Design-LOD300-R02.rvt
└── INDEX_Archive_2025-03-30.csv

02-00-04-MSTR-ARCHIVE_2025-06-20_DesignFreeze/
├── OPSCTR/
│   ├── 02-00-04-MSTR-OPSCTR-Design-LOD350-R02.rvt
│   └── EXPORTS/
│       └── IFC/
│           └── 02-00-04-MSTR-OPSCTR-Design-LOD350-R02.ifc
├── DATACENTER/
│   └── 02-00-04-MSTR-DATACENTER-Design-LOD350-R02.rvt
└── INDEX_Archive_2025-06-20.csv
```

---

## Related Documentation

- [10_MASTER_MODELS README](../README.md)
- [BIM_CAD_MODELS 00_ADMIN README](../../00_ADMIN/README.md)
- [20_DISCIPLINE_MODELS README](../../20_DISCIPLINE_MODELS/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Coordination Team

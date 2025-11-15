# 05_TEMPLATES / 99_ARCHIVE

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / BIM_CAD_MODELS / 05_TEMPLATES / 99_ARCHIVE  
**Purpose:** Date-segregated archive for superseded BIM/CAD templates

---

## Archive Organization

This archive uses **date-segregated folders** with milestone descriptions. This keeps the archive simple and avoids duplicating the room/module/component organization that exists in active folders.

---

## Structure Pattern

```
99_ARCHIVE/
├── 02-00-04-BIM-TPL-ARCHIVE_YYYY-MM-DD_<Milestone>/
│   ├── <archived template files>
│   └── INDEX_Archive_YYYY-MM-DD.csv
├── 02-00-04-BIM-TPL-ARCHIVE_YYYY-MM-DD_<Milestone>/
│   └── ...
└── README.md (this file)
```

### Folder Naming Convention

```
02-00-04-BIM-TPL-ARCHIVE_YYYY-MM-DD_<Milestone>
```

Where:
- `YYYY-MM-DD` = Archive date (when templates were superseded)
- `<Milestone>` = Brief description (e.g., PreCoordination, V1_TemplateRefresh, PostReview)

### Examples

- `02-00-04-BIM-TPL-ARCHIVE_2025-01-15_PreCoordination/`
- `02-00-04-BIM-TPL-ARCHIVE_2025-03-30_V1_TemplateRefresh/`
- `02-00-04-BIM-TPL-ARCHIVE_2025-06-20_PostDesignReview/`

---

## When to Archive Templates

Archive templates when:
1. **Major revision** - Template updated with significant changes
2. **Standard update** - BIM standards or shared parameters change
3. **Project milestone** - End of design phase, pre-construction, etc.
4. **Obsolete** - Template no longer needed or replaced by new approach

---

## Archiving Process

### 1. Create Archive Folder

```bash
mkdir "02-00-04-BIM-TPL-ARCHIVE_2025-MM-DD_<Milestone>"
```

### 2. Move Superseded Templates

Move old template files from active folders (ROOM_TEMPLATES, MODULE_TEMPLATES, etc.) to the archive folder:

```bash
mv ../ROOM_TEMPLATES/02-00-04-TPL-BIM-GenericRoom-LOD200-R01.rvt \
   02-00-04-BIM-TPL-ARCHIVE_2025-MM-DD_<Milestone>/
```

### 3. Create Archive Index

Create `INDEX_Archive_YYYY-MM-DD.csv` documenting:
- Template file name
- Original location (ROOM_TEMPLATES, MODULE_TEMPLATES, etc.)
- Reason for archiving
- Replacement template (if any)

### 4. Update Active CHANGELOG

Document the archiving action in the parent `05_TEMPLATES/README.md` changelog or separate CHANGELOG.md.

---

## Archive Index Format

**File:** `INDEX_Archive_YYYY-MM-DD.csv`

```csv
Template_File,Original_Location,Archive_Date,Reason,Replacement
02-00-04-TPL-BIM-GenericRoom-LOD200-R01.rvt,ROOM_TEMPLATES,2025-01-15,Superseded by R02,02-00-04-TPL-BIM-GenericRoom-LOD200-R02.rvt
02-00-04-TPL-BIM-OPSCTR-ConsoleModule-LOD300-R01.rvt,MODULE_TEMPLATES/OPSCTR_CONSOLES,2025-01-15,Standard update,02-00-04-TPL-BIM-OPSCTR-ConsoleModule-LOD300-R02.rvt
```

---

## Retention Policy

### Archive Retention

- **Current project**: Keep all archives for project duration
- **Post-project**: Retain archives for 7 years (standard project records retention)
- **Critical templates**: Mark for permanent retention if needed for future reference

### Cleanup Guidelines

Only delete archives:
1. After project completion + retention period
2. With approval from BIM manager
3. After verifying no dependencies or references exist

---

## Retrieving Archived Templates

### When to Retrieve

- Need to reference old design
- Compare template versions
- Restore accidentally deleted/modified template
- Audit or compliance review

### Retrieval Process

1. Locate appropriate archive folder by date
2. Review INDEX_Archive file to find template
3. Copy (don't move) template from archive
4. If reactivating, rename and update revision number
5. Place in appropriate active folder

---

## Best Practices

### Archive Organization

✅ **DO:**
- Use clear, descriptive milestone names
- Create archive index for each archive folder
- Document reason for archiving
- Archive entire sets of related templates together

❌ **DON'T:**
- Don't recreate ROOM/MODULE/COMPONENT structure in archive
- Don't archive templates individually without context
- Don't delete archives without approval
- Don't modify archived files (read-only)

### Milestone Naming

Good milestone names:
- `PreCoordination` - Before coordination phase
- `V1_TemplateRefresh` - Version 1 template update
- `PostDesignReview` - After design review milestone
- `StandardUpdate_2025Q1` - Quarterly standard update

Avoid:
- Generic names like `Old` or `Backup`
- Vague names like `Archive1`, `Archive2`
- Names without dates

---

## Related Documentation

- [05_TEMPLATES README](../README.md)
- [BIM_CAD_MODELS 00_ADMIN README](../../00_ADMIN/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)

---

**Last Updated:** 2025-11-15  
**Owner:** AMPEL360 BIM Standards Team

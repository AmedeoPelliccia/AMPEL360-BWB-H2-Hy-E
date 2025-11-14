# DIAGRAMS — Administration

**Folder:** 02-00-04_Design / ASSETS / INSTALLATIONS / DIAGRAMS / 00_ADMIN  
**Purpose:** Administrative files, metadata, and change tracking for installation diagrams

---

## Contents

This folder contains:

- **README.md** - This file, describing the DIAGRAMS structure
- **CHANGELOG.md** - Revision history of all diagrams in this folder tree
- **02-00-04-DGM_Index.csv** - Master index of all diagrams with metadata

---

## DIAGRAMS Structure

```
DIAGRAMS/
├── 00_ADMIN/                      # Administrative files (this folder)
├── 05_TEMPLATES/                  # Reusable diagram templates
├── 10_INSTALLATION_LAYOUTS/       # Physical installation layouts
├── 20_ELECTRICAL_SINGLE_LINE/     # Electrical single-line diagrams (SLD)
├── 30_P_AND_ID/                   # Piping & Instrumentation Diagrams
├── 40_DATA_NETWORK/               # Data network topology diagrams
├── 50_SIGNAL_FLOW/                # Signal/information flow diagrams
├── 60_SAFETY_EMERGENCY/           # Safety and emergency diagrams
├── 70_EXPORTS/                    # Exported/rendered diagrams
│   └── VIEW_ONLY/                 # View-only formats (PNG, PDF)
└── 99_ARCHIVE/                    # Archived/superseded diagrams
```

---

## Diagram Categories

### 10_INSTALLATION_LAYOUTS
Physical installation layouts showing:
- Equipment placement
- Room/facility layouts
- Mounting details
- Cable routing paths
- Conduit runs

**Formats:** `.dwg`, `.dxf`, `.pdf`

### 20_ELECTRICAL_SINGLE_LINE
Electrical power distribution:
- Single-line diagrams (SLD)
- Power distribution layouts
- Load calculations
- Circuit protection
- Grounding schemes

**Formats:** `.dwg`, `.pdf`

### 30_P_AND_ID
Process flow diagrams for specialized systems:
- H2 fuel systems (if applicable)
- HVAC systems
- Fire suppression
- Cooling systems

**Formats:** `.dwg`, `.pdf`

### 40_DATA_NETWORK
Data network architecture:
- Network topology (L1, L2, L3)
- Switch/router configurations
- VLAN diagrams
- Firewall architectures
- Redundancy schemes

**Formats:** `.vsdx`, `.drawio`, `.pdf`

### 50_SIGNAL_FLOW
Information and signal flow:
- Information flow between systems
- Data flow diagrams
- Integration diagrams
- Communication protocols
- System interfaces

**Formats:** `.svg`, `.drawio`, `.mmd`, `.pdf`

### 60_SAFETY_EMERGENCY
Safety and emergency systems:
- Evacuation plans
- Fire alarm systems
- Emergency shutdown diagrams
- Safety interlocks
- Emergency lighting

**Formats:** `.pdf`, `.dwg`, `.svg`

### 70_EXPORTS
Rendered/exported diagrams for documentation:
- PNG exports for web viewing
- PDF exports for printing
- SVG exports for scalability
- Package files for client delivery

---

## File Naming Convention

All diagrams follow the pattern:

```
02-00-04-DGM-<FACILITY>-<TYPE>-<DETAIL>-R<nn>.<ext>
```

Where:
- `02-00-04` = ATA chapter and design folder
- `DGM` = Diagram category code
- `FACILITY` = OPSCTR (Operations Center), DATACENTER, H2ROOM, etc.
- `TYPE` = FloorLayout, Power, Network, InfoFlow, etc.
- `DETAIL` = Specific detail or sub-system (L1, SLD, L3Topology, etc.)
- `R<nn>` = Revision number (R01, R02, etc.)
- `ext` = File extension (.dwg, .pdf, .vsdx, .svg, etc.)

### Examples

- `02-00-04-DGM-OPSCTR-FloorLayout-L1-R01.dwg`
- `02-00-04-DGM-OPSCTR-Power-SLD-R01.dwg`
- `02-00-04-DGM-H2ROOM-PID-Process-R01.dwg`
- `02-00-04-DGM-OPSCTR-Network-L3Topology-R01.vsdx`
- `02-00-04-DGM-OPSCTR-InformationFlow-R01.svg`
- `02-00-04-DGM-OPSCTR-EvacuationPlan-L1-R01.pdf`

---

## Usage Guidelines

### Creating a New Diagram

1. **Select appropriate category** folder (10-60)
2. **Use template** from `05_TEMPLATES/` if available
3. **Follow naming convention** strictly
4. **Save source file** in native format (`.dwg`, `.vsdx`, etc.)
5. **Update CHANGELOG.md** with revision entry
6. **Export to VIEW_ONLY** formats (PDF, PNG) in `70_EXPORTS/VIEW_ONLY/`
7. **Update index** in `00_ADMIN/02-00-04-DGM_Index.csv`

### Diagram Standards

- **Line weights:** Follow standard CAD layer conventions
- **Fonts:** Use standard engineering fonts (Arial, ISO)
- **Colors:** Use color coding consistently across diagrams
- **Symbols:** Use standard symbols from templates
- **Legends:** Include legend on each diagram
- **Title blocks:** Use standard title block template
- **Scale:** Clearly indicate scale or "NTS" (Not To Scale)

### Revision Control

- Increment revision number for each significant change
- Document changes in CHANGELOG.md
- Keep previous revision in `99_ARCHIVE/` if needed
- Use revision clouds to highlight changes in CAD files

### Coordination

Diagrams must coordinate with:
- **BIM_CAD_MODELS/** - 3D models
- **LAYOUTS/** - Space planning layouts
- **Requirements/** - `02-00-03_Requirements`
- **Interfaces/** - `02-00-05_Interfaces`

---

## Export Guidelines

### View-Only Exports

Export all diagrams to view-only formats for:
- Documentation embedding
- Client reviews
- Web viewing
- Presentations

**Standard exports:**
- PDF (high resolution, searchable text)
- PNG (web resolution, 1920px wide max)
- SVG (for vector diagrams)

Place all exports in `70_EXPORTS/VIEW_ONLY/`

---

## Related Documentation

- [INSTALLATIONS README](../README.md)
- [BIM_CAD_MODELS README](../BIM_CAD_MODELS/00_ADMIN/README.md)
- [AMPEL360_ASSETS_STANDARD.md](/AMPEL360_ASSETS_STANDARD.md)
- CAD Standards Manual - see project documentation
- Electrical Design Standards - see project documentation

---

**Last Updated:** 2025-11-14  
**Owner:** AMPEL360 Engineering Documentation Team

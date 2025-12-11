# Architecture Diagram Template - Instructions

## Purpose

This template provides guidance for creating system and subsystem architecture diagrams for ATA 10 - Parking, Mooring, Storage & RTS documentation.

Architecture diagrams should be created as **SVG (Scalable Vector Graphics)** files and placed in appropriate ASSETS folders within the subsystem directories.

## Diagram Types

### 1. System Architecture Diagrams

**Purpose:** Show high-level system decomposition and major subsystem groupings

**File Naming:** `10-00-13-NNA_[System_Name]_Architecture.svg`

**Content Should Include:**
- Major subsystem blocks
- Primary interfaces between subsystems
- External system interfaces (ATA 28, ATA 21, etc.)
- Data flows (if applicable)
- Power distribution (if applicable)
- Safety-critical pathways highlighted

**Example:**
```
10-00-13-05A_H2_Safety_System_Architecture.svg
```

### 2. Subsystem Block Diagrams

**Purpose:** Show detailed subsystem components and internal architecture

**File Naming:** `10-00-13-NNA_[Subsystem_Name]_Block_Diagram.svg`

**Content Should Include:**
- All major components within the subsystem
- Component interconnections
- Signal types (analog, digital, mechanical, H2 flow, etc.)
- Interface points with other subsystems
- Redundancy paths (if applicable)
- Control logic flow (if applicable)

**Example:**
```
10-00-13-40A_H2_Detection_Block_Diagram.svg
```

### 3. Interface Diagrams

**Purpose:** Show detailed interface specifications between subsystems

**File Naming:** `10-00-13-NNA_[Subsystem_Name]_Interfaces.svg`

**Content Should Include:**
- All input interfaces (with interface IDs)
- All output interfaces (with interface IDs)
- Signal specifications (voltage, current, protocol, etc.)
- Physical connection types (connector P/N if available)
- Interface ownership (which subsystem is responsible)

**Example:**
```
10-00-13-43A_ESD_Interfaces.svg
```

### 4. Physical Layout Diagrams

**Purpose:** Show physical placement of components on/around aircraft

**File Naming:** `10-00-13-NNA_[Subsystem_Name]_Layout.svg`

**Content Should Include:**
- Aircraft outline (top, side, or isometric view)
- Component locations with IDs
- Routing of lines/cables
- Clearance zones
- Access points for maintenance
- BWB-specific geometry considerations

**Example:**
```
10-00-13-10A_Tiedown_Physical_Layout.svg
```

### 5. Zone Diagrams

**Purpose:** Show hazardous area zones or detection zones

**File Naming:** `10-00-13-NNA_[Subsystem_Name]_Zones.svg`

**Content Should Include:**
- Zone boundaries (Zone 0, 1, 2 for ATEX; or detection zones)
- Zone classifications and extents
- Sensor/equipment placement relative to zones
- Safety distances and clearances
- Ventilation paths (if applicable)

**Example:**
```
10-00-13-40A_H2_Detection_Zones.svg
```

## Visual Style Guidelines

### Color Coding

Use consistent color coding across all diagrams:

| Element Type | Color | Usage |
|-------------|-------|-------|
| Safety-Critical | Red (#CC0000) | Highlight safety-critical components/paths |
| H2/LH2 Lines | Yellow (#FFCC00) | Hydrogen gas or liquid lines |
| Electrical | Blue (#0066CC) | Electrical connections |
| Data/Communication | Green (#00AA00) | Data/network connections |
| Mechanical | Gray (#666666) | Mechanical connections |
| Pneumatic | Orange (#FF6600) | Pneumatic/air lines |
| Redundant Paths | Dashed lines | Show backup/redundant paths |
| Normal Components | Black (#000000) | Standard components |
| BWB-Specific | Purple (#6600CC) | BWB configuration-specific items |

### Symbol Library

Use standard symbols:

- **Sensor:** Circle with "S" or sensor type
- **Valve:** Valve symbol (ball, butterfly, check) with actuation type
- **Controller/PLC:** Rectangle with "PLC" or controller name
- **Junction/Connection:** Small filled circle
- **Interface Point:** Open circle with interface ID
- **Tank/Vessel:** Cylinder or rounded rectangle
- **Pump:** Pump symbol with flow direction arrow
- **Filter:** Hourglass shape
- **Flow Direction:** Arrow on line
- **Manual Operation:** Hand symbol
- **Automatic Operation:** "A" or automation symbol

### Text and Labels

- **Font:** Use clear, sans-serif fonts (Arial, Helvetica, or similar)
- **Size:** 
  - Title: 16-18 pt
  - Subsystem/Component Names: 12-14 pt
  - Labels and IDs: 10-12 pt
  - Notes: 8-10 pt
- **Component IDs:** Always include component IDs next to components
- **Interface IDs:** Label all interfaces with unique IDs (IF-XXX-NNN)

### Layout and Organization

- **Title Block:** Include in lower right corner:
  - Document ID
  - Title
  - Revision
  - Date
  - Author
  - Scale (if applicable)
- **Legend:** Include legend for colors, symbols, abbreviations
- **Grid/Alignment:** Use invisible grid to align components neatly
- **White Space:** Provide adequate spacing between components (avoid clutter)
- **Flow Direction:** Generally left-to-right for signal flow, top-to-bottom for hierarchy

## SVG Best Practices

### File Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     width="[width]" height="[height]" viewBox="0 0 [width] [height]">
  
  <!-- Title and metadata -->
  <title>[Document ID] - [Diagram Title]</title>
  <desc>System architecture diagram for [Subsystem Name]</desc>
  
  <!-- Define reusable elements -->
  <defs>
    <!-- Symbols, gradients, patterns -->
  </defs>
  
  <!-- Background -->
  <rect width="100%" height="100%" fill="white"/>
  
  <!-- Diagram content -->
  <g id="main-diagram">
    <!-- Components, lines, text -->
  </g>
  
  <!-- Title block -->
  <g id="title-block">
    <!-- Title, revision, date, etc. -->
  </g>
  
  <!-- Legend -->
  <g id="legend">
    <!-- Color/symbol legend -->
  </g>
  
</svg>
```

### Layering

Use logical grouping with `<g>` elements:

1. **Background layer** - Grid, background colors
2. **Connection layer** - All lines and connections
3. **Component layer** - All components and symbols
4. **Text layer** - All labels and text
5. **Annotation layer** - Notes, callouts, highlights
6. **Frame layer** - Border, title block, legend

### Accessibility

- Use `<title>` and `<desc>` tags for each significant element
- Provide `aria-label` attributes for screen readers
- Ensure sufficient contrast between colors
- Use patterns in addition to colors for color-blind accessibility

## Example: Creating an H2 Detection Zone Diagram

**Filename:** `10-00-13-40A_H2_Detection_Zones.svg`

**Steps:**

1. **Create aircraft outline** (top view, simplified BWB shape)
2. **Define zones:**
   - Zone 1: Fueling interface area (yellow fill, 25% opacity)
   - Zone 2: Aft LH2 tank access (yellow fill, 25% opacity)
   - Zone 3: Forward LH2 tank access (yellow fill, 25% opacity)
   - Zone 4: Vent outlet (yellow fill, 25% opacity)
   - Zone 5: GSE staging (yellow fill, 25% opacity)
3. **Place sensors:**
   - Use circle symbols with "H2" label
   - Color-code: Red for critical zones, orange for standard
   - Label each with sensor ID (e.g., H2-DETECT-CBS-01)
4. **Add legend:**
   - Zone color = Detection zone
   - Red circle = Critical H2 sensor
   - Orange circle = Standard H2 sensor
   - Numbers = Zone numbers
5. **Add title block:**
   - Document ID: 10-00-13-40A
   - Title: H2 Detection Zones
   - Revision: A
   - Date: 2025-12-11
6. **Add notes:**
   - Detection threshold: 25% LEL
   - Sensor type: CBS (Catalytic Bead Sensor)
   - 2-of-3 voting in critical zones

## Diagram Storage Locations

Place diagrams in the following locations:

| Diagram Type | Storage Location |
|-------------|------------------|
| System Architecture | `system-architecture/ASSETS/` |
| Subsystem Diagrams | `[subsystem-category]/ASSETS/` |
| Zone Diagrams | `h2-safety-subsystems/ASSETS/` or relevant subsystem folder |
| Layout Diagrams | `bwb-subsystems/ASSETS/` or relevant subsystem folder |
| Interface Diagrams | `10-00-05_Interfaces/ASSETS/` (general interfaces directory) |

## Tools for Creating SVG Diagrams

Recommended tools:

1. **Inkscape** (Free, open-source)
   - Excellent SVG support
   - Wide symbol library
   - Precise alignment tools

2. **Draw.io / diagrams.net** (Free, web-based or desktop)
   - Easy to use
   - Templates for technical diagrams
   - Exports clean SVG

3. **Adobe Illustrator** (Commercial)
   - Professional vector graphics
   - Precise control
   - Industry standard

4. **Microsoft Visio** (Commercial)
   - Technical diagram focus
   - Can export to SVG (with some limitations)

5. **LibreOffice Draw** (Free)
   - Basic SVG creation
   - Suitable for simple diagrams

## Referencing Diagrams in Documentation

In Markdown documents, reference diagrams using:

```markdown
![Diagram Title](ASSETS/10-00-13-NNA_Diagram_Name.svg)

*Figure N: [Figure caption]*
```

Or as a link:

```markdown
See [H2 Detection Zone Diagram](ASSETS/10-00-13-40A_H2_Detection_Zones.svg) for sensor placement.
```

## Review Checklist

Before finalizing a diagram:

- [ ] All components labeled with IDs
- [ ] All interfaces labeled with interface IDs
- [ ] Legend included and complete
- [ ] Title block includes: ID, title, rev, date, author
- [ ] Color coding consistent with standard
- [ ] Sufficient contrast and readability
- [ ] SVG file properly structured and clean
- [ ] File named according to convention
- [ ] Referenced in relevant subsystem document
- [ ] Reviewed for technical accuracy
- [ ] Approved by subsystem owner

## Revision Control

When updating a diagram:

1. Increment revision letter in title block
2. Add revision note in diagram (what changed)
3. Update date in title block
4. Save as new revision (can keep old revision for history)
5. Update references in all documents that link to this diagram
6. Document change in subsystem document revision history

---

**AI Generation Note:**

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-11

---

*End of Architecture Diagram Template*

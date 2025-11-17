# 95-50-00-004 Structural Taxonomy

**Document ID:** 95-50-00-004  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active

---

## 1. Purpose

Define a standardized classification system for all structural elements in the 95-50 Structures chapter, enabling consistent identification, documentation, and maintenance procedures.

---

## 2. Taxonomy Hierarchy

### Level 1: ATA Chapter
- **95-50-XX** where XX is the parent ATA chapter (21, 24, 28, 31, 42, 46, 49, 53, 57, 70)

### Level 2: Structure Type
- **A** = Assembly
- **I** = Installation
- **D** = Drawing
- **M** = Mount/Bracket
- **R** = Rack/Cabinet
- **T** = Tray/Conduit
- **F** = Fairing/Panel

### Level 3: Sequential Number
- **001-999** unique within each ATA chapter

---

## 3. Structure Categories

### 3.1 Racks and Enclosures (Type: R)
**Definition:** Enclosed structures housing LRUs and electronic equipment

**Examples:**
- IMA racks
- Server racks
- Electrical cabinets
- Recorder racks

**Naming Convention:** `95-50-XX-R-nnn`

### 3.2 Mounts and Brackets (Type: M)
**Definition:** Mechanical supports for individual components

**Examples:**
- Sensor mounts
- Antenna brackets
- Tank supports
- Equipment brackets

**Naming Convention:** `95-50-XX-M-nnn`

### 3.3 Cable Management (Type: T)
**Definition:** Structures for routing and protecting wiring

**Examples:**
- Cable trays
- Conduits
- Clamp assemblies
- Grommets

**Naming Convention:** `95-50-XX-T-nnn`

### 3.4 Fairings and Panels (Type: F)
**Definition:** Aerodynamic or protective covers

**Examples:**
- Antenna fairings
- Access panels
- Service doors
- Inspection covers

**Naming Convention:** `95-50-XX-F-nnn`

### 3.5 Assemblies (Type: A)
**Definition:** Complete installation units combining multiple structure types

**Examples:**
- Complete equipment bay
- Sensor cluster assembly
- Distribution manifold assembly

**Naming Convention:** `95-50-XX-A-nnn`

---

## 4. Attribute Classification

### 4.1 Material Class
- **M-AL** = Aluminum alloy
- **M-TI** = Titanium alloy
- **M-ST** = Stainless steel
- **M-CF** = Carbon fiber composite
- **M-GF** = Glass fiber composite

### 4.2 Environment Class
- **E-AMB** = Ambient (cabin temperature, dry)
- **E-HOT** = Hot zone (>100°C)
- **E-COLD** = Cold zone (<-50°C)
- **E-WET** = Wet zone (water/fluid exposure)
- **E-VIB** = High vibration (>2g RMS)

### 4.3 Access Class
- **AC-QA** = Quick access (tool-less or quarter-turn)
- **AC-STD** = Standard access (hand tools)
- **AC-SVC** = Service access (special tools/procedures)
- **AC-MX** = Major maintenance access (requires jacking/towing)

### 4.4 Criticality Class
- **CR-1** = Flight critical (failure affects flight safety)
- **CR-2** = Mission critical (failure prevents mission completion)
- **CR-3** = Non-critical (failure causes convenience loss)

---

## 5. Example Classifications

| Structure ID | Name | Type | Material | Environment | Access | Criticality |
|--------------|------|------|----------|-------------|--------|-------------|
| 95-50-42-R-001 | IMA Rack | R | M-AL | E-AMB | AC-SVC | CR-1 |
| 95-50-57-M-001 | Wing Sensor Mount | M | M-TI | E-COLD | AC-QA | CR-1 |
| 95-50-24-T-001 | Cable Tray Main | T | M-AL | E-AMB | AC-STD | CR-2 |
| 95-50-28-M-001 | H2 Tank Support | M | M-TI | E-COLD | AC-SVC | CR-1 |
| 95-50-53-A-001 | Avionics Bay Assy | A | M-AL | E-AMB | AC-MX | CR-1 |

---

## 6. Document Control

| Version | Date       | Author                     | Changes                |
|---------|------------|----------------------------|------------------------|
| 1.0     | 2025-11-17 | AMPEL360 Documentation Team | Initial creation       |

---

**Maintained by:** AMPEL360 Structures Team

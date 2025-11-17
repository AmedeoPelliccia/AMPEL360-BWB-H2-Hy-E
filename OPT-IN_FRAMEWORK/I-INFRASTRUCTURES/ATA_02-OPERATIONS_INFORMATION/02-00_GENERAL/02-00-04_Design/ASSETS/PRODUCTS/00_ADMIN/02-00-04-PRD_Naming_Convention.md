# PRODUCTS Naming Convention

## Product Folder Naming

All product folders follow this pattern:

```text
[ATA]-PRD-[Family]-[Code]_[ShortName]/
```

### Components

* **[ATA]** = ATA chapter code: `02-00-04`
* **PRD** = Product-level artifact identifier
* **[Family]** = Product family code:
  * `INH` — In-house designed product
  * `COTS` — Commercial Off-The-Shelf equipment
  * `KIT` — System kit or bundle
  * `SVC` — Service or software product
* **[Code]** = Four-digit numeric product code:
  * `0001-0499`, `0600-0999` — In-house products
  * `0500-0599` — System kits and bundles
  * `1000-1999` — COTS equipment
  * `2000-2999` — Service and software products
  * _Note: The `0500-0599` range is reserved exclusively for System kits and bundles, and is excluded from the In-house products range._
* **[ShortName]** = Human-readable product identifier (no spaces, use underscores)

### Examples

**In-house Products:**
```text
02-00-04-PRD-INH-0010_OPSCTR_ConsoleSystem/
02-00-04-PRD-INH-0011_OPSCTR_OperatorWorkstation/
02-00-04-PRD-INH-0020_GSE_PowerCart/
02-00-04-PRD-INH-0030_DC_Pod_StandardModule/
```

**COTS Equipment:**
```text
02-00-04-PRD-COTS-1000_19in_ServerRack_42U/
02-00-04-PRD-COTS-1001_UPS_10kVA_Online/
02-00-04-PRD-COTS-1010_DisplayMonitor_32in_4K/
```

**System Kits:**
```text
02-00-04-PRD-KIT-0500_OPSCTR_StarterKit/
02-00-04-PRD-KIT-0501_OPSCTR_FullRoom_6Operators/
02-00-04-PRD-KIT-0510_DC_Pod_BaseConfig/
```

**Service Products:**
```text
02-00-04-PRD-SVC-2000_RemoteMonitoringService/
02-00-04-PRD-SVC-2001_DigitalTwinPackage/
02-00-04-PRD-SVC-2010_MaintenanceSubscription_Annual/
```

---

## Internal File Naming

Files within product folders follow consistent patterns:

### Bill of Materials (BOM)
```text
[ATA]-PRD-[Family]-[Code]_BOM-R[nn].[ext]
```
Example: `02-00-04-PRD-INH-0010_BOM-R01.xlsx`

### Configuration Matrix
```text
[ATA]-PRD-[Family]-[Code]_ConfigMatrix-R[nn].[ext]
```
Example: `02-00-04-PRD-INH-0010_ConfigMatrix-R01.xlsx`

### Product Models
```text
[ATA]-MDL-PRD-[Family]-[Code]_[ModelType]_[Description]-R[nn].[ext]
```
Examples:
- `02-00-04-MDL-PRD-INH-0010_BIM_RefModel-R01.rvt`
- `02-00-04-MDL-PRD-INH-0010_FunctionalModel-R01.md`

### Product Drawings
```text
[ATA]-DWG-EQP-PRD-[Family]-[Code]-[Description]-SHT[nn]-R[nn].[ext]
```
Example: `02-00-04-DWG-EQP-PRD-INH-0010-ConsoleSystem-SHT01-R01.dwg`

### Manuals and Documentation
```text
[ATA]-PRD-[Family]-[Code]_[DocumentType]-R[nn].[ext]
```
Examples:
- `02-00-04-PRD-INH-0010_InstallationManual-R01.pdf`
- `02-00-04-PRD-INH-0010_ProductSheet-R01.pdf`
- `02-00-04-PRD-INH-0010_UserGuide-R01.pdf`
- `02-00-04-PRD-COTS-1000_Datasheet-R01.pdf`

### Options and Configuration Files
```text
[ATA]-PRD-[Family]-[Code]_Options-R[nn].[ext]
```
Example: `02-00-04-PRD-INH-0010_Options-R01.md`

---

## Revision Numbering

* **R01** — First official release
* **R02, R03, ...** — Subsequent revisions
* Increment revision number for significant changes
* Document all changes in `02-00-04-PRD_Change_Log.csv`

---

## Reserved Codes

### In-house Products (0001-0999)
* 0001-0099: Operations center equipment
* 0100-0199: Ground support equipment (GSE)
* 0200-0299: Data center equipment
* 0300-0399: Special infrastructure

### COTS Equipment (1000-1999)
* 1000-1099: Racks and enclosures
* 1100-1199: Power systems (UPS, PDU)
* 1200-1299: Computing equipment
* 1300-1399: Display and visualization
* 1400-1499: Communications equipment
* 1500-1599: Environmental control

### System Kits (0500-0599)
* 0500-0529: Operations center kits
* 0530-0549: Data center kits
* 0550-0569: GSE kits
* 0570-0599: Special purpose kits

### Service Products (2000-2999)
* 2000-2099: Monitoring and diagnostic services
* 2100-2199: Software products
* 2200-2299: Training and support services
* 2300-2399: Maintenance subscriptions

---

## Notes

* All codes must be unique across the entire PRODUCTS directory
* Register all new products in `02-00-04-PRD_Global_Index.csv`
* Use consistent [ShortName] values that are descriptive and memorable
* Avoid special characters in file names (use alphanumerics, underscores, hyphens only)
* Keep [ShortName] under 40 characters for readability

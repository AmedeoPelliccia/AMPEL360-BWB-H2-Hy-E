# PRODUCTS — Product-Level Assets (ATA 02-00-04)

## 1. Purpose

This directory contains **product-level assets** for
**ATA 02-00-04_Design** (Operations Information infrastructures), i.e.
items that can be **offered, configured and delivered** as units, such as:

- In-house designed products (e.g. OPSCTR console systems, GSE units)
- Catalogued COTS equipment (e.g. 19" racks, UPS units)
- System kits / bundles (e.g. starter kits, pre-defined room packages)
- Service or software products (e.g. monitoring services, digital twin packages)

Each product aggregates:

- **Parts** from [`ASSETS/PARTS/`](../../PARTS/)
- **Models** from [`ASSETS/MODELS/`](../../MODELS/)
- **BIM / CAD** from [`ASSETS/INSTALLATIONS/BIM_CAD_MODELS/`](../../INSTALLATIONS/BIM_CAD_MODELS/)
- **Drawings** from [`ASSETS/DRAWINGS/`](../../DRAWINGS/)
- **Manuals / datasheets** under its own product folder

---

## 2. Structure

```text
PRODUCTS/
├── 00_ADMIN/                 # Governance, global index, naming, change log
├── 05_TEMPLATES/             # Templates for product folders, BOMs, configs
├── 10_INHOUSE_PRODUCTS/      # Products fully designed by the project
├── 20_COTS_EQUIPMENT/        # External catalogued products (normalized)
├── 30_SYSTEM_KITS_AND_BUNDLES/ # Bundles of products / parts into kits
├── 40_SERVICE_OR_SOFTWARE_PRODUCTS/ # Service / software style products
└── 99_ARCHIVE/               # Archived / retired products
```

Each product has its own folder:

```text
10_INHOUSE_PRODUCTS/
└── 02-00-04-PRD-INH-0010_OPSCTR_ConsoleSystem/
    ├── README.md
    ├── CONFIG/
    ├── BOM/
    ├── MODELS/
    ├── DRAWINGS/
    └── MANUALS/
```

---

## 3. Naming Convention

Product folders use:

```text
[ATA]-PRD-[Family]-[Code]_[ShortName]/
```

Where:

* **[ATA]** = `02-00-04`
* **[Family]** = product family:

  * `INH`  – in-house product
  * `COTS` – catalogued external product
  * `KIT`  – system kit / bundle
  * `SVC`  – service or software product
* **[Code]** = numeric code (e.g. `0010`, `1000`, `0500`, `2000`)
* **[ShortName]** = concise, readable slug (`OPSCTR_ConsoleSystem`, etc.)

**Examples**

* `02-00-04-PRD-INH-0010_OPSCTR_ConsoleSystem/`
* `02-00-04-PRD-COTS-1000_19in_ServerRack_42U/`
* `02-00-04-PRD-KIT-0500_OPSCTR_StarterKit/`
* `02-00-04-PRD-SVC-2000_RemoteMonitoringService/`

Internal files follow consistent patterns, e.g.:

* BOM: `02-00-04-PRD-INH-0010_BOM-R01.xlsx`
* Config matrix: `02-00-04-PRD-INH-0010_ConfigMatrix-R01.xlsx`
* Product sheet: `02-00-04-PRD-INH-0010_ProductSheet-R01.pdf`

---

## 4. Global Index & Traceability

`02-00-04-PRD_Global_Index.csv` should track at least:

* `Product_ID` (e.g. `PRD-INH-0010`)
* `Folder_Name`
* `Family` (INH, COTS, KIT, SVC)
* `ShortName`
* `Lifecycle_Status` (`CONCEPT`, `ACTIVE`, `LEGACY`, `RETIRED`)
* `Configuration_Types` (fixed, configurable, kit, service)
* `BOM_Path`
* `ConfigMatrix_Path`
* `Main_Models` (references into `ASSETS/MODELS` / BIM)
* `Main_Drawings` (references into `ASSETS/DRAWINGS`)
* `Related_Parts` (link to `ASSETS/PARTS`)
* `Related_Requirements`
* `Related_ATA_Chapters`
* `Notes`

---

## 5. Lifecycle & Usage

1. When defining a new product:

   * Assign a `Product_ID` (`PRD-INH-00xx`, etc.).
   * Create the folder under the appropriate family (`10_INHOUSE_PRODUCTS`, `20_COTS_EQUIPMENT`, etc.).
2. Populate:

   * `README.md` with product description and configuration rules.
   * `BOM/` with a structured BoM referencing `ASSETS/PARTS/`.
   * `CONFIG/` with configuration matrices, options and variants.
   * `MODELS/` and `DRAWINGS/` links/copies as needed.
3. Register the product in `02-00-04-PRD_Global_Index.csv`.
4. When a product is retired or superseded:

   * Move its folder under `99_ARCHIVE/` using an archive event folder:
     `02-00-04-PRD-ARCHIVE_YYYY-MM-DD_<tag>/`.
   * Update the global index.

---

## 6. Related Documentation

### 6.1 Internal Standards & Guidelines

* [AMPEL360 Assets Standard](../../../../../../../AMPEL360_ASSETS_STANDARD.md) - Asset naming and organization conventions
* [AMPEL360 Documentation Standard](../../../../../../../AMPEL360_DOCUMENTATION_STANDARD.md) - Documentation guidelines
* [ATA Numbering Guide](../../../../../../../ATA_03_NUMBERING_GUIDE.md) - ATA chapter structure reference

### 6.2 Related Asset Directories

* [PARTS](../../PARTS/) - Component-level parts library
* [ASSEMBLIES](../../ASSEMBLIES/) - Sub-assembly definitions
* [MODELS](../../MODELS/) - Logical and system models
* [DRAWINGS](../../DRAWINGS/) - Engineering drawings
* [INSTALLATIONS](../../INSTALLATIONS/) - Installation layouts and procedures

### 6.3 Related ATA Chapters

* [02-00-03_Requirements](../../../02-00-03_Requirements/) - Requirements specifications
* [02-00-02_Safety](../../../02-00-02_Safety/) - Safety requirements and analysis

---

## 7. Document Control

* **Originator:** *[Name / Role]*
* **Checker:** *[Name / Role]*
* **Approver:** *[Name / Role]*
* **Status:** `WORKING` / `FOR_REVIEW` / `APPROVED` / `RETIRED`
* **Notes:**

  * This structure and README were **generated by AI prompted by Amedeo Pelliccia**.
  * Content must be **reviewed and approved by a designated human checker/approver**
    before being used as an official design baseline.

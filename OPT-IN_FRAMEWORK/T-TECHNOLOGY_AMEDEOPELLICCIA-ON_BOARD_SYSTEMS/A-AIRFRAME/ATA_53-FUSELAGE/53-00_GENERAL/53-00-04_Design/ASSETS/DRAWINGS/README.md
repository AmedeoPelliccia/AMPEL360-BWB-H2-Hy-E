# 53-00-04_Design / ASSETS / DRAWINGS

## Purpose

The `DRAWINGS` directory contains the **2D design authority** for the AMPEL360 BWB fuselage (ATA 53), structured by **zones**, **joint types**, and **installation views**.

These drawings are:

- The graphical reference for **Configuration Items (CIs)** in `53-00-04_Design/02_Configuration_Items/`. <!-- TODO: Create target directory and update this link -->
- The basis for **assemblies** in [53-00-04_Design/ASSETS/ASSEMBLIES/](../ASSEMBLIES/).
- Inputs and evidence for **53-50_Structures** analysis and [53-00-03_Requirements](../../../53-00-03_Requirements/) verification.

All drawings are stored as **SVG** for version control and traceability.

---

## Directory Structure

```text
53-00-04_Design/ASSETS/DRAWINGS/
├── README.md
│
├── ZONE_100_NOSE_SECTION/
│   ├── 53-10-0000_Zone_100_General_Arrangement.svg
│   ├── 53-10-1000_Forward_Bulkhead_Assembly.svg
│   ├── 53-10-1001_Forward_Bulkhead_Details.svg
│   ├── 53-10-2000_NLG_Bay_Structure.svg
│   ├── 53-10-2001_NLG_Bay_Details.svg
│   ├── 53-10-3000_Cockpit_Structure_Assembly.svg
│   ├── 53-10-3001_Windshield_Frame_Details.svg
│   ├── 53-10-4000_Avionics_Bay_Structure.svg
│   └── Drawing_Register_Zone_100.csv
│
├── ZONE_200_FORWARD_CABIN/
│   ├── 53-20-0000_Zone_200_General_Arrangement.svg
│   ├── 53-20-1000_Frame_200_Assembly.svg
│   ├── 53-20-1001_Frame_200_Details.svg
│   ├── 53-20-2000_Upper_Shell_Panel_U01.svg
│   ├── 53-20-2001_Upper_Shell_Panel_U02.svg
│   ├── 53-20-2100_Lower_Shell_Panel_L01.svg
│   ├── 53-20-2101_Lower_Shell_Panel_L02.svg
│   ├── 53-20-3000_Side_Shell_Left.svg
│   ├── 53-20-3100_Side_Shell_Right.svg
│   ├── 53-20-4000_Passenger_Door_1L_Frame.svg
│   ├── 53-20-4001_Door_1L_Frame_Details.svg
│   ├── 53-20-4002_Door_1L_Corner_Fittings.svg
│   ├── 53-20-4010_Passenger_Door_1R_Frame.svg
│   ├── 53-20-4020_Passenger_Door_2L_Frame.svg
│   ├── 53-20-4030_Passenger_Door_2R_Frame.svg
│   ├── 53-20-5000_Floor_Beam_Grid_Assembly.svg
│   ├── 53-20-5001_Primary_Floor_Beam_Details.svg
│   ├── 53-20-5100_Floor_Panel_Assembly.svg
│   ├── 53-20-5200_Seat_Track_Installation.svg
│   └── Drawing_Register_Zone_200.csv
│
├── ZONE_300_MID_CABIN/
│   ├── 53-30-0000_Zone_300_General_Arrangement.svg
│   ├── 53-30-1000_Frame_300_Assembly.svg
│   ├── 53-30-2000_Upper_Shell_Panels.svg
│   ├── 53-30-3000_Side_Shell_Panels.svg
│   ├── 53-30-4000_Passenger_Door_3L_Frame.svg
│   ├── 53-30-4010_Passenger_Door_3R_Frame.svg
│   ├── 53-30-4020_Passenger_Door_4L_Frame.svg
│   ├── 53-30-4030_Passenger_Door_4R_Frame.svg
│   ├── 53-30-4100_Overwing_Exit_Left_1.svg
│   ├── 53-30-4110_Overwing_Exit_Right_1.svg
│   ├── 53-30-5000_Wing_Body_Blend_Transition.svg
│   └── Drawing_Register_Zone_300.csv
│
├── ZONE_400_CENTER_WING_BOX/
│   ├── 53-40-0000_Zone_400_General_Arrangement.svg
│   ├── 53-40-1000_Forward_Wing_Spar_Assembly.svg
│   ├── 53-40-1001_Forward_Spar_Web_Details.svg
│   ├── 53-40-1002_Forward_Spar_Upper_Cap_Details.svg
│   ├── 53-40-1003_Forward_Spar_Lower_Cap_Details.svg
│   ├── 53-40-1004_Wing_Attachment_Fitting_01.svg
│   ├── 53-40-1005_Wing_Attachment_Fitting_02.svg
│   ├── 53-40-1100_Rear_Wing_Spar_Assembly.svg
│   ├── 53-40-2000_Wing_Rib_01_Assembly.svg
│   ├── 53-40-3000_MLG_Bay_Left_Assembly.svg
│   ├── 53-40-3001_MLG_Beam_Left_Details.svg
│   ├── 53-40-3002_MLG_Bay_Left_Bulkhead_Forward.svg
│   ├── 53-40-3003_MLG_Bay_Left_Bulkhead_Aft.svg
│   ├── 53-40-3004_MLG_Attachment_Fitting_L1.svg
│   ├── 53-40-3100_MLG_Bay_Right_Assembly.svg
│   ├── 53-40-4000_Cargo_Door_Forward_Left_Frame.svg
│   ├── 53-40-4010_Cargo_Door_Forward_Right_Frame.svg
│   ├── 53-40-4020_Cargo_Door_Aft_Left_Frame.svg
│   ├── 53-40-4030_Cargo_Door_Aft_Right_Frame.svg
│   ├── 53-40-5000_Wing_Box_Splice_Forward.svg
│   ├── 53-40-5100_Wing_Box_Splice_Aft.svg
│   └── Drawing_Register_Zone_400.csv
│
├── ZONE_500_AFT_CABIN/
│   ├── 53-50-0000_Zone_500_General_Arrangement.svg
│   ├── 53-50-1000_Frame_500_Assembly.svg
│   ├── 53-50-2000_Upper_Shell_Panels.svg
│   ├── 53-50-3000_Empennage_Attachment_Structure.svg
│   ├── 53-50-3001_Vertical_Stabilizer_Fitting_Forward.svg
│   ├── 53-50-3002_Vertical_Stabilizer_Fitting_Mid.svg
│   ├── 53-50-3003_Vertical_Stabilizer_Fitting_Aft.svg
│   ├── 53-50-3100_Horizontal_Stabilizer_Fitting_Left.svg
│   ├── 53-50-3200_Horizontal_Stabilizer_Fitting_Right.svg
│   └── Drawing_Register_Zone_500.csv
│
├── ZONE_600_TAIL_SECTION/
│   ├── 53-60-0000_Zone_600_General_Arrangement.svg
│   ├── 53-60-1000_Aft_Pressure_Bulkhead_Assembly.svg
│   ├── 53-60-1001_Aft_Bulkhead_Details.svg
│   ├── 53-60-2000_Tail_Cone_Structure.svg
│   ├── 53-60-3000_APU_Bay_Structure.svg
│   └── Drawing_Register_Zone_600.csv
│
├── JOINTS_AND_SPLICES/
│   ├── 53-JS-1000_Longitudinal_Splice_Upper_Lower.svg
│   ├── 53-JS-1001_Longitudinal_Splice_Fastener_Pattern.svg
│   ├── 53-JS-2000_Circumferential_Splice_Zone_100_200.svg
│   ├── 53-JS-2001_Circumferential_Splice_Zone_200_300.svg
│   ├── 53-JS-2002_Circumferential_Splice_Zone_300_400.svg
│   ├── 53-JS-2003_Circumferential_Splice_Zone_400_500.svg
│   ├── 53-JS-2004_Circumferential_Splice_Zone_500_600.svg
│   ├── 53-JS-3000_Door_Frame_to_Shell_Interface.svg
│   ├── 53-JS-4000_Floor_Beam_to_Shell_Attachment.svg
│   └── Joint_Details_Index.csv
│
├── INSTALLATION_DRAWINGS/
│   ├── 53-IN-1000_Systems_Routing_Upper_Shell.svg
│   ├── 53-IN-2000_Systems_Routing_Lower_Shell.svg
│   ├── 53-IN-3000_Liner_Attachment_Points.svg
│   ├── 53-IN-4000_Monument_Attach_Provisions.svg
│   ├── 53-IN-5000_Overhead_Bin_Support_Layout.svg
│   └── Installation_Drawing_Index.csv
│
└── ASSETS/
    ├── Drawing_Standards.md
    ├── Title_Block_Template.svg
    ├── Symbol_Library.svg
    ├── Line_Type_Standards.md
    ├── Dimensioning_Standards.md
    ├── Material_Call_Out_Standards.md
    ├── Drawing_Revision_Process.md
    ├── CAD_Layer_Standards.csv
    ├── Drawing_Sizes_ISO_5457.csv
    └── Master_Drawing_Register.csv
```

---

## Numbering Convention

### Zone Drawings (53-zz-nnnn)

```text
Format: 53-[zone]-[sequence]_[Short_Title].svg

where:
  zone     = 10, 20, 30, 40, 50, 60  (100 → 600 mapped to 10–60)
  sequence = 4-digit drawing number within zone
```

Examples:

* `53-10-0000_Zone_100_General_Arrangement.svg`
* `53-20-4000_Passenger_Door_1L_Frame.svg`
* `53-40-1000_Forward_Wing_Spar_Assembly.svg`
* `53-60-1000_Aft_Pressure_Bulkhead_Assembly.svg`

General rules:

* `...0000` → zone-level General Arrangement (GA).
* `...1000`–`1999` → primary frames / spars / bulkheads.
* `...2000`–`2999` → shell panels and major skin segments.
* `...3000`–`3999` → special structures (bays, blend, attachments).
* `...4000`–`4999` → doors, large openings, special interfaces.
* `...5000`–`5999` → splices, transition structures, etc.

### Joints and Splices (53-JS-nnnn)

```text
Format: 53-JS-[sequence]_[Short_Title].svg
```

* `53-JS-1000`–`1999` → longitudinal joints.
* `53-JS-2000`–`2999` → circumferential joints / zone splices.
* `53-JS-3000`–`3999` → shell-to-door / local interfaces.
* `53-JS-4000`–`4999` → floor-to-shell / primary attachments.

### Installation Drawings (53-IN-nnnn)

```text
Format: 53-IN-[sequence]_[Short_Title].svg
```

* `53-IN-1000`–`1999` → systems routing on upper shell.
* `53-IN-2000`–`2999` → systems routing on lower shell.
* `53-IN-3000`–`3999` → cabin liners, interior attachment points.
* `53-IN-4000`–`4999` → monuments and interior structures.
* `53-IN-5000`–`5999` → overhead bins and support layouts.

---

## Drawing Registers

Each zone folder contains a local register:

* `Drawing_Register_Zone_100.csv`
* `Drawing_Register_Zone_200.csv`
* ...
* `Drawing_Register_Zone_600.csv`

And the root `ASSETS` contains a global:

* `Master_Drawing_Register.csv`

### Zone Drawing Register Template

Recommended header for each `Drawing_Register_Zone_XXX.csv`:

```csv
Drawing_Number,Title,Zone,Type,CI_Reference,Assembly_ID,Revision,Status,CAD_File,Owner,Checker,Approver,Last_Updated,Comments
53-10-0000,Zone 100 General Arrangement,100,GA,CI-53-100,,A,Released,53-10-0000_Zone_100_General_Arrangement.svg,J.Smith,A.Brown,C.Chief,2025-11-22,"Primary layout reference"
53-10-1000,Forward Bulkhead Assembly,100,Assembly,CI-53-100-BHD-FWD,ASM-53-100-001,A,Released,53-10-1000_Forward_Bulkhead_Assembly.svg,J.Smith,A.Brown,C.Chief,2025-11-22,"Stress-critical CI"
```

### Master Drawing Register

`Master_Drawing_Register.csv` aggregates all zone registers:

```csv
Drawing_Number,Title,Zone,Folder,Type,CI_Reference,Assembly_ID,Revision,Status,CAD_File
53-10-0000,Zone 100 General Arrangement,100,ZONE_100_NOSE_SECTION,GA,CI-53-100,,A,Released,53-10-0000_Zone_100_General_Arrangement.svg
53-40-1000,Forward Wing Spar Assembly,400,ZONE_400_CENTER_WING_BOX,Assembly,CI-53-400-SPAR-FWD,ASM-53-400-001,A,Released,53-40-1000_Forward_Wing_Spar_Assembly.svg
53-JS-2000,Circumferential Splice Zone 100–200,ALL,JOINTS_AND_SPLICES,Joint,,,"A",Released,53-JS-2000_Circumferential_Splice_Zone_100_200.svg
```

This file is the **single source of truth** for:

* Global drawing list.
* Links to CIs and assemblies.
* Status and revision tracking.

---

## Integration with Other Structures

* **CIs (53-00-04 / 02_Configuration_Items)**
  Each CI's `CI_Definition.yaml` and `Design_Description.md` should reference its primary and secondary drawings by `Drawing_Number`.
  <!-- TODO: Create 02_Configuration_Items directory and update this link -->

* **Assemblies ([53-00-04 / ASSETS/ASSEMBLIES](../ASSEMBLIES/))**
  Assembly YAMLs (e.g. `ASM-53-400-001_Forward_Wing_Spar_Assembly.yaml`) should point to their main assembly drawings in this folder.

* **Structures ([53-50_Structures](../../../../53-50_Structures/))**
  Structural analysis reports reference drawing IDs (e.g. `53-40-1000`) as geometry authority.

* **Requirements ([53-00-03_Requirements](../../../53-00-03_Requirements/))**
  Verification evidence for geometry- or interface-related requirements should cite drawing numbers and registers as part of the trace.

---

## Standards and Templates

The `ASSETS` subfolder contains the standards that govern all drawings:

* `Drawing_Standards.md` – general rules, symbology, and conventions.
* `Title_Block_Template.svg` – standard title block for all drawings.
* `Symbol_Library.svg` – reusable graphical library.
* `Line_Type_Standards.md` – line types and meanings.
* `Dimensioning_Standards.md` – dimensioning rules (tolerances, datums).
* `Material_Call_Out_Standards.md` – standard material annotations.
* `Drawing_Revision_Process.md` – how revisions are controlled and recorded.
* `CAD_Layer_Standards.csv` – mandatory layer structure for CAD/authoring tools.
* `Drawing_Sizes_ISO_5457.csv` – allowed drawing sizes and formats (see [ISO 5457](https://www.iso.org/standard/46590.html)).
* `Master_Drawing_Register.csv` – global register as described above.

All new drawings MUST:

1. Follow the naming convention described above.
2. Use the standard title block and layers.
3. Be added to the relevant `Drawing_Register_Zone_XXX.csv`.
4. Be propagated to `Master_Drawing_Register.csv` (manually or via CI tooling).

---

## Document Control

* **Folder**: `53-00-04_Design/ASSETS/DRAWINGS`
* **Status**: OPERATIONAL – Structure and conventions defined
* **Version**: 1.0
* **Date**: 2025-11-22
* **Owner**: ATA 53 Drawing & CAD Authority
* **Repository**: `AMPEL360-BWB-H2-Hy-E`
* **Generated with the assistance of AI (GitHub Copilot)**, prompted by **Amedeo Pelliccia**.
* **Human approver**: _[to be completed]_.
* **Last AI update**: 2025-11-22

---

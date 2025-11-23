---
description: "OPT-IN / ATA documentation conventions"
applyTo: "OPT-IN_FRAMEWORK/**/*.md"
---

## Documentation Rules

- Preserve any existing **Document ID**, **Version**, **Status**, and **Owner** blocks.
- When creating a new document:
  - Derive the ID and filename pattern from neighboring files.
  - Use the correct lifecycle subfolder (e.g. `01_OVERVIEW`, `03_REQUIREMENTS`, `04_DESIGN`, `07_V_AND_V`, `11_EIS_Versions_Tags`, etc.).
- Use **Markdown only** for textual content and **CSV** for tabular data (placed in appropriate `ASSETS/` folders and linked from the Markdown).
- Prefer **SVG** for diagrams and drawings; reference them under `ASSETS/DRAWINGS/`, `ASSETS/DIAGRAMS/`, or equivalent.
- If you reference a path that does not yet exist:
  - Create a minimal stub document with:
    - Title.
    - Document Control block.
    - `## TODO` section with a short note.
- Do not flatten or rename ATA/OPT-IN path segments (e.g. keep `53-00-04_Design`, `85-40_Software`, etc.).
- Maintain cross-references:
  - Update or add links to `CI_Database.csv`, drawing registers, or dashboards if new items are introduced.

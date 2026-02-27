# ICN Directory — ATA 31-00-00 Indicating & Recording

## Purpose

Contains **Illustration Control Number (ICN)** assets — SVG graphics and diagrams — providing
visual support for Data Modules within the ATA 31-00-00 AMM publication.

See [`ICN_SCAFFOLD.md`](./ICN_SCAFFOLD.md) for the full scaffold specification, BREX rules,
DM ↔ ICN mapping table, and SVG template guidelines.

## Naming Convention

```
ICN-AMPEL360AT-31-00-NNNN-A_NNN.SVG
│              │   │   │    │   └─ Variant number (001 = default)
│              │   │   │    └───── Issue letter (A = initial)
│              │   │   └────────── Sequential ICN number
│              │   └────────────── ATA section (00)
│              └────────────────── ATA chapter (31)
└───────────────────────────────── Project code
```

## Folder Structure

```
ICN/
├─ SYSTEM_OVERVIEW/             # 0001–0099 – Architecture & context
│  ├─ ICN-AMPEL360AT-31-00-0001-A_001.SVG   (Global architecture)
│  └─ ICN-AMPEL360AT-31-00-0002-A_001.SVG   (Avionics context / ATA interfaces)
│
├─ SIGNAL_FLOW/                 # 0100–0199 – Data & signal paths
│  ├─ ICN-AMPEL360AT-31-00-0101-A_001.SVG   (Sensor → DAU → Processing → Display)
│  └─ ICN-AMPEL360AT-31-00-0102-A_001.SVG   (Recording vs real-time paths)
│
├─ DISPLAY_LAYOUTS/             # 0200–0299 – HMI & cockpit layouts
│  ├─ ICN-AMPEL360AT-31-00-0201-A_001.SVG   (Generic cockpit display zones)
│  └─ ICN-AMPEL360AT-31-00-0202-A_001.SVG   (Indication symbology grouping)
│
├─ MAINTENANCE_SUPPORT/         # 0300–0399 – LRU locations & connectors
│  ├─ ICN-AMPEL360AT-31-00-0301-A_001.SVG   (LRU location overview)
│  └─ ICN-AMPEL360AT-31-00-0302-A_001.SVG   (Connector identification schematic)
│
└─ FAULT_ISOLATION/             # 0400–0499 – Troubleshooting aids
   ├─ ICN-AMPEL360AT-31-00-0401-A_001.SVG   (Fault isolation decision tree)
   └─ ICN-AMPEL360AT-31-00-0402-A_001.SVG   (Data validity / failure propagation)
```

## Key Rules

- All ICNs are **illustrative only** — they do not establish design authority.
- Every ICN must be referenced by at least one Data Module via `<graphicRef>`.
- File format: **SVG** (S1000D BREX 022E compliant).
- Each SVG must carry SPDX licence header and document-control comment block.

## Document Control

- **Directory**: ICN
- **Subject**: 31-00-00-general
- **Publication**: AMM
- **Standard**: S1000D Issue 5.0
- **Status**: Draft
- **Last updated**: 2026-02-27
- **AI assistance**: GitHub Copilot, prompted by **Amedeo Pelliccia**

# 02-20-11-003 — Document Management System (EFB)

**Subsystem ID:** 02-20-11
**Group:** [02-20_Subsystems](../README.md)
**ATA Chapter:** [ATA_02-OPERATIONS_INFORMATION](../../README.md)
**Axis:** I — Infrastructures
**Status:** OPERATIONAL
**Version:** 1.0

---

# 1. Purpose

This document defines the **Document Management System (DMS)** used by the
AMPEL360 **Electronic Flight Bag (EFB)** for:

* Storing
* Updating
* Indexing
* Searching
* Displaying
* Verifying

all operational documentation required for safe, efficient, hydrogen-based
AMPEL360 aircraft operations.

The EFB Document Viewer is one of the most-used tools by flight crew and must
achieve **high availability**, **low latency**, and **full offline capability**.

---

# 2. Scope

## Included

* Document categories & formats
* Lifecycle, updates, delta syncs
* Search, annotations, bookmarks, revision management
* Digital signature & integrity verification
* Storage structure and indexing
* DPP anchoring & compliance
* Integration with:

  * 02-20-01 Digital Ops Platform
  * AOC/Dispatch systems
  * ATA 95 (for traceability of NN-generated docs, if applicable)

## Excluded

* Airline MDM configuration
* Internal CAOS documentation workflows
* Detailed authoring toolchain (third-party DTP tools)

---

# 3. Document Library Overview

```yaml
document_library:
  total_documents: 12847
  formats:
    - pdf
    - svg
    - html5
    - markdown
  categories:
    AFM: 2450
    OM: 4200
    QRH: 850
    MEL: 320
    AMM: 3200
    Training: 1827
  features:
    full_text_search_ms: 500
    offline_mode: true
    annotation_sync: true
    multi_user_collab: true
```

The EFB provides a unified UI for all documents with:

* Fast rendering
* Smooth zoom/pan
* Persistent bookmarks
* Cross-reference linking across ATA chapters

---

# 4. Document Categories (ATA-Aligned)

| Category          | Description                 | Contains                                    |
| ----------------- | --------------------------- | ------------------------------------------- |
| **AFM**           | Approved Flight Manual      | Limitations, performance, procedures        |
| **OM (A/B)**      | Operations Manual           | Policies, SOPs, communications, crew duties |
| **QRH**           | Quick Reference Handbook    | Non-normal, emergency procedures            |
| **MEL**           | Minimum Equipment List      | Dispatchability rules                       |
| **AMM**           | Aircraft Maintenance Manual | Troubleshooting, tasks                      |
| **Training**      | CBT/phases content          | Training coursework, briefing packs         |
| **CAOS Profiles** | Operational analytics       | CAOS-generated operational advisories       |

---

# 5. Storage Model & Indexing

## 5.1 On-Device Storage

* Local SQLite + filesystem store
* Pre-compressed document packs
* Offline availability 100%
* Fail-safe snapshot rollback mechanism

### Folder Structure (Local EFB)

```
/Documents/
 ├── AFM/
 ├── OM/
 ├── QRH/
 ├── MEL/
 ├── AMM/
 ├── TRAINING/
 └── META/
     ├── index.sqlite
     ├── signatures/
     └── bookmarks.json
```

---

## 5.2 Indexing Engine

Capabilities:

* Full-text search (indexed)
* ATA-aware hierarchical tagging
* Tolerant fuzzy search
* Bookmarks + annotations stored as structured JSON

Search performance target: **≤ 500 ms** median.

---

# 6. Update & Synchronization Mechanism

All document updates flow from:

```
Document Server → 02-20-01 Digital Ops Platform → EFB
```

### 6.1 Update Triggers

* Daily cycle (~0400Z recommended)
* On-demand by crew
* Mandatory revision push for AFM/OM/QRH/MEL updates
* Zero-downtime patching

### 6.2 Incremental Update Format

```yaml
update_pack:
  type: delta
  compression: LZMA
  includes:
    - modified_files
    - index_diff
    - signature_block
    - dpp_anchor_hash
```

### 6.3 Integrity Verification

* Digital signatures (RSA-4096)
* Blockchain hash anchor (SHA-256 chain)
* Metadata validation (checksums, lineage)

If verification fails → **rollback** + alert.

---

# 7. User Features

## 7.1 Document Viewer

* Fast rendering engine
* Split-view (QRH + checklist)
* Page thumbnails
* Cross-document hyperlinks

## 7.2 Bookmarks

* Synced across devices (per crew ID)
* Stored as JSON
* Exportable for incident review

## 7.3 Annotations

* Stylus / finger input
* Colour-coded
* Collaborative (Cockpit → AOC)

Stored in:
`/Documents/META/annotations/`

## 7.4 Revision Tracking

* Version history visible to crew
* “What changed?” diff view
* Mandatory acknowledgement for OM/QRH revisions

---

# 8. CAOS & Predictive Integration

Certain CAOS outputs (e.g. operational advisories, weather risk profiles, turnaround bottlenecks) are stored as “virtual documents”.

Located under:

```
/Documents/CAOS/
   ├── CAOS_Profiles/
   ├── Predictive_Weather/
   └── Turnaround/
```

These are:

* Read-only
* Auto-updated
* Traceable via ATA 95 DPP mechanism

---

# 9. Digital Product Passport (DPP) Anchoring

Each document pack includes:

```json
{
  "document_pack_hash": "sha256:d9f1e4b2c8a3f6e5...",
  "generation_timestamp": "2025-11-15T04:32Z",
  "document_categories": ["AFM","OM","QRH","MEL","AMM","TRAINING"],
  "linked_models": [
    "NN-PERF-CALC-v1.0",
    "NN-WEATHER-PRED-v1.0"
  ],
  "signed_by": "AMPEL360 Digital Ops Platform",
  "blockchain_anchor": "0x3f8a2c9e7d1b5f4a..."
}
```

Allows:

* End-to-end documentation lineage
* Tamper-evident change history
* Certification audit support

---

# 10. Interface Dependencies

| Subsystem                         | Interaction                                     |
| --------------------------------- | ----------------------------------------------- |
| **02-20-01 Digital Ops Platform** | Document pack delivery, signatures, delta diffs |
| **02-20-13 Performance Computer** | Performance tables & documentation              |
| **02-20-17 Weather System**       | Weather briefing documents                      |
| **02-20-23 Predictive Ops NN**    | Predictive reports and CAOS profiles            |
| **ATA 31 Recording**              | Document use → operational event logs           |

---

# 11. Safety, HF & Certification

## 11.1 Safety Boundaries

* EFB documents are **advisory**
* Document viewer must remain accessible even in degraded power modes
* No multi-tasking during critical phases unless operator allows

## 11.2 HF Considerations

* Minimum font sizes
* High-contrast themes
* Restricted use of colour
* Quick accessibility to QRH

## 11.3 Certification

* FAA AC 120-76D
* EASA AMC 20-25
* DO-178C DAL D software components
* DO-326A cybersecurity framework

---

# 12. Performance KPIs

```yaml
KPIs:
  document_open_time_s: 2
  search_latency_ms: 500
  update_failure_rate: 0.0005
  annotation_sync_delay_s: <10
  offline_availability: 100%
```

---

# 13. Traceability

## Requirements

* RQ-02-11-A: Full-text search
* RQ-02-11-B: Document integrity verification
* RQ-02-11-C: Offline usage
* RQ-02-11-D: Revision notification

## Design Artefacts

* 02-20-11-A-001 System Architecture
* Local DB schema (in `META/index.sqlite`)
* Update pack specification

## Interfaces

* Digital Ops Platform
* AOC / Dispatch
* Predictive Ops feeds

---

# 14. Document Control

> **Originator:** AI prompted by Amedeo Pelliccia
> **Subsystem:** 02-20-11 Electronic Flight Bag
> **Toolchain:** MCP Doc Control + AMPEL360 OPT-IN Guidelines

| Version | Date       | Author               | Changes                                 |
| ------- | ---------- | -------------------- | --------------------------------------- |
| 1.0     | 2025-11-19 | AMPEL360 Digital Ops | Initial Document Management System spec |

---



Solo pide — te los dejo con la misma calidad.
**

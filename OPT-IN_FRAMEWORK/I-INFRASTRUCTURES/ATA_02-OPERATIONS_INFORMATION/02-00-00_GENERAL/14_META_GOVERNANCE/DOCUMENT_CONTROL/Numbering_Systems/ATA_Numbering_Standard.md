# ATA Numbering Standard

**Document ID:** AMPEL360-02-00-00-META-ATA  
**Version:** 1.0.0  
**Effective Date:** 2025-09-01

## Purpose

This document defines the ATA iSpec 2200 numbering standard as applied to AMPEL360 BWB H₂ Hy-E documentation.

## ATA Chapter Structure

### Format

**ATA-CHAPTER-SECTION-SUBSECTION**

Example: `02-00-00`, `02-32-00`, `28-10-00`

### Components

- **ATA Chapter (2 digits)**: Top-level system (e.g., 02 = Operations)
- **Section (2 digits)**: Major subdivision (e.g., 00 = General, 32 = H₂ Refueling)
- **Subsection (2 digits)**: Detailed subdivision (e.g., 00 = General, 01 = Tank 1)

## ATA 02 - Operations Information Structure

### 02-00-00 GENERAL
- Folder-level organization (01-14)
- Cross-cutting operations documentation

### 02-10-00 through 02-90-00
- Specific operational areas
- 02-32-00: H₂ Refueling Procedures (AMPEL360-specific)
- 02-66-00: ETOPS Extended Range Operations
- 02-95-00: Neural Network Operations Support

## Document Type Suffixes

Documents within ATA sections use type suffixes:
- **README**: Overview and index
- **OVERVIEW**: Conceptual and philosophical content
- **SAFETY**: Safety-related content
- **REQUIREMENTS**: Requirements specifications
- **DESIGN**: Design documentation
- **INTERFACES**: Interface control documents

## Full Document ID Format

**ATA-CHAPTER-SECTION-SUBSECTION-TYPE-SEQUENCE**

Examples:
- `02-00-00-README`: ATA 02-00-00 overview document
- `02-00-01-OVERVIEW`: Operations philosophy
- `02-32-00-PROC-001`: H₂ refueling procedure #1

## Compliance

This numbering standard complies with:
- ATA iSpec 2200 Chapter 1
- S1000D Data Module Coding scheme compatibility
- AMPEL360 internal document management

---

**Document Control:**
- Document ID: AMPEL360-02-00-00-META-ATA
- Version: 1.0.0
- Status: Released
- Owner: Documentation Manager

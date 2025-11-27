# 53-60-80-01 Thermal Insulation Specification

## Document Information

- **Document ID**: 53-60-80-01
- **Title**: Thermal Insulation Specification
- **Version**: 1.0
- **Date**: 2025-11-27
- **Status**: Draft
- **Category**: Insulation
- **ATA Chapter**: 53-60 - Fuselage Storages

## Purpose

This document defines the general thermal insulation specifications for storage system applications.

## Scope

This specification covers:
- Insulation material requirements
- Application-specific specifications
- Installation requirements
- Qualification testing

## Insulation Requirements Summary

### Application Requirements

| Application | R-Value | Max Surface | Material | Reference |
|-------------|---------|-------------|----------|-----------|
| Battery thermal jacket | 0.5 m²K/W | ≤ 60°C | Aerogel + ceramic | REQ-INS-001 |
| CO₂ cartridge bay | 0.3 m²K/W | ≤ 80°C | Ceramic fiber | REQ-INS-002 |
| Water tank | 0.4 m²K/W | ≤ 45°C | Closed-cell foam | REQ-INS-003 |
| Thermal accumulator | 0.8 m²K/W | ≤ 45°C | MLI + aerogel | REQ-INS-004 |
| Hot surfaces (>60°C) | Per CS 25.1359 | ≤ 45°C | Personnel protection | REQ-INS-005 |

## Material Specifications

### Aerogel Blanket

| Property | Value | Unit | Test Method |
|----------|-------|------|-------------|
| Thermal conductivity | 0.015 | W/m·K | ASTM C518 |
| Density | 150 | kg/m³ | ASTM C303 |
| Temperature range | -200 to +650 | °C | — |
| Hydrophobic | Yes | — | — |
| Flammability | Non-combustible | — | ASTM E84 |

### Ceramic Fiber Blanket

| Property | Value | Unit | Test Method |
|----------|-------|------|-------------|
| Thermal conductivity | 0.05 | W/m·K | ASTM C518 |
| Density | 100 | kg/m³ | ASTM C303 |
| Temperature range | -40 to +1260 | °C | — |
| Fiber diameter | 2-4 | μm | — |
| Flammability | Non-combustible | — | ASTM E84 |

### Closed-Cell Foam

| Property | Value | Unit | Test Method |
|----------|-------|------|-------------|
| Thermal conductivity | 0.035 | W/m·K | ASTM C518 |
| Density | 50 | kg/m³ | ASTM D1622 |
| Temperature range | -40 to +80 | °C | — |
| Water absorption | ≤ 2% | by volume | ASTM D2842 |
| Flammability | Self-extinguishing | — | FAR 25.853 |

## Installation Requirements

### General Requirements

| Requirement | Description | Reference |
|-------------|-------------|-----------|
| Vapor barrier | As required for application | REQ-INS-020 |
| Jacketing | Protective outer layer | REQ-INS-021 |
| Attachment | Mechanical or adhesive | REQ-INS-022 |
| Sealing | All joints sealed | REQ-INS-023 |
| Thickness | Per thermal calculation | REQ-INS-024 |

### Attachment Methods

| Material | Method | Notes |
|----------|--------|-------|
| Aerogel | Wire tie or tape | Avoid compression |
| Ceramic fiber | Wire mesh | Handle with care |
| Foam | Adhesive or mechanical | Compatible adhesive |

## Personnel Protection

Per [CS 25.1359](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27):

| Requirement | Description |
|-------------|-------------|
| Surface temperature | ≤ 45°C accessible surfaces |
| Duration | Sustained contact (>10 sec) |
| Warning labels | Required where >45°C possible |
| Guards | Physical barrier where practical |

## References

### Internal Documents
- [53-60-80-02 Aerogel Application Guide](53-60-80-02_Aerogel_Guide.md)
- [53-60-80-03 MLI Installation Procedures](53-60-80-03_MLI_Installation.md)

### External Standards
- [CS-25.1359](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Hot Surfaces
- [CS-25.853](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-amendment-27) - Compartment Interiors

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-11-27

---

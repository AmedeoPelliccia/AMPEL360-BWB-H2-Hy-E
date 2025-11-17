# 05_Data_and_Metadata — Data and Metadata Requirements

## Purpose

This folder contains **data and metadata requirements** — requirements governing data quality, lineage, provenance, and metadata management.

## Scope

### ID Range: RQ-95-00-03-400 to RQ-95-00-03-499

Data and metadata requirements address:
- **Training data lineage**: Dataset provenance and transformations
- **Environmental metrics**: CO₂e tracking for sustainability
- **Data provenance**: Origin and chain of custody
- **Hyperparameters**: Training configuration history
- **Performance metrics**: Model validation and testing data
- **Bias assessment**: Fairness and equity evaluation

## Requirements Summary

| ID | Title | Status |
|----|-------|--------|
| RQ-95-00-03-401 | DPP SHALL Store Training Data Lineage | APPROVED |
| RQ-95-00-03-402 | DPP SHALL Record CO₂e Metrics | APPROVED |
| RQ-95-00-03-403 | DPP SHALL Track Data Provenance | DRAFT |
| ... | (Additional requirements as defined) | ... |

---

## What Belongs Here

**Data and metadata requirements** govern information quality and tracking. Examples:
- "The DPP SHALL store complete training data lineage"
- "The DPP SHALL record CO₂e emissions for model training"
- "The DPP SHALL track data provenance with cryptographic hashes"

## What Doesn't Belong Here

- **Functional data operations** → 01_Functional
- **Performance of data operations** → 02_NonFunctional
- **Safety assessment data** → 03_Safety_and_AAI

---

## Document Control

- **Folder**: 05_Data_and_Metadata
- **ID Range**: 400-499
- **Owner**: Data WG / ML Engineering
- **Last Updated**: 2025-11-17

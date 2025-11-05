# S1000D Business Rules
## AMPEL360-Specific Validation Rules

**Version:** 1.0  
**Date:** 2025-11-05

---

## 1. Overview

This document defines business rules for S1000D data modules beyond standard schema validation.

## 2. Content Rules

### 2.1 Mandatory Elements
- Every DM must have: title, issueInfo, status, applicability
- Procedural DMs must include safety warnings for H₂-related tasks
- All references must resolve within CSDB

### 2.2 Language and Style
- Use American English (en-US)
- Use simplified technical English principles
- Maximum sentence length: 20 words
- Active voice preferred

### 2.3 H₂ System Rules
- All H₂ procedures must include:
  - Pressure system warnings
  - Ventilation requirements
  - Grounding procedures
  - Emergency response info

## 3. Structure Rules

### 3.1 Data Module Limits
- Maximum size: 50 pages equivalent
- Minimum granularity: Single task or topic
- Cross-reference depth: Max 3 levels

### 3.2 Illustration Rules
- Format: SVG (preferred), CGM, or X3D
- Resolution: 300 DPI minimum
- File size: <5 MB per illustration
- Alt text required for accessibility

## 4. Metadata Rules

### 4.1 Required Metadata
- Issue date in ISO 8601 format
- Applicability (all, specific tail numbers, or date range)
- Security classification (default: UNCLASSIFIED)
- Quality assurance approval

### 4.2 Change Tracking
- Reason for update (RFC number)
- Changed elements marked with change markers
- Revision history maintained

## 5. Validation Process

### 5.1 Automated Checks
- Schema validation (S1000D 6.0 XSD)
- Business rule validation (Schematron)
- Link validation
- Spelling and grammar check

### 5.2 Manual Review
- Technical accuracy review
- Editorial review
- Safety review (for procedures)
- Illustration quality review

## 6. Compliance

Non-compliance with business rules will result in:
- Warning notifications to author
- Rejection at QA gate
- Required corrections before publication

---

**Document Owner:** Quality Assurance

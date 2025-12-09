# DWG-10-000-005 — Approval Matrix

**Document ID:** DWG-10-000-005  
**Title:** Drawing Approval Matrix  
**ATA Chapter:** 10 – Parking, Mooring, Storage, RTS  
**Status:** DRAFT  
**Version:** A  
**Date:** 2025-12-09

---

## 1. Purpose

This document defines the approval requirements and authorization matrix for ATA 10 drawings in the Q100 (AMPEL360) aircraft project.

---

## 2. Approval Levels

### 2.1 Level 1: Technical Review

Required for all drawings:
- Drawing creator performs self-check
- Peer review by colleague in same discipline
- Check for compliance with drawing standards

### 2.2 Level 2: Engineering Approval

Required for released drawings:
- Discipline engineer review and approval
- Verification of technical accuracy
- Confirmation of interface compatibility

### 2.3 Level 3: Safety Review

Required for safety-critical drawings:
- Safety engineer review
- Risk assessment confirmation
- Hazard mitigation verification

### 2.4 Level 4: Configuration Management

Required for released drawings:
- CM specialist verification
- Drawing number assignment confirmation
- Version control compliance check

### 2.5 Level 5: Certification Authority

Required for type-certified components:
- Review by certification engineer
- Compliance with applicable regulations
- Documentation package completeness

---

## 3. Drawing Series Approval Requirements

| Series | Title | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Notes |
|--------|-------|---------|---------|---------|---------|---------|-------|
| DWG-10-000 | Index | ✓ | ✓ | – | ✓ | – | Standards only |
| DWG-10-100 | General Arrangement | ✓ | ✓ | ✓ | ✓ | ✓ | H₂/HV zones |
| DWG-10-200 | Mooring | ✓ | ✓ | ✓ | ✓ | ✓ | Load-bearing |
| DWG-10-300 | Towing | ✓ | ✓ | ✓ | ✓ | ✓ | Load-bearing |
| DWG-10-400 | Jacking | ✓ | ✓ | ✓ | ✓ | ✓ | Critical loads |
| DWG-10-500 | Tie-Down | ✓ | ✓ | ✓ | ✓ | – | Operational |
| DWG-10-600 | Ground Locks | ✓ | ✓ | ✓ | ✓ | – | Safety devices |
| DWG-10-700 | Protective Covers | ✓ | ✓ | – | ✓ | – | Non-structural |
| DWG-10-800 | H₂ System | ✓ | ✓ | ✓ | ✓ | ✓ | H₂ safety critical |
| DWG-10-900 | HV System | ✓ | ✓ | ✓ | ✓ | ✓ | HV safety critical |
| DWG-10-1000 | Ground Power | ✓ | ✓ | ✓ | ✓ | – | Electrical system |
| DWG-10-1100 | Environmental Protection | ✓ | ✓ | – | ✓ | – | Non-structural |
| DWG-10-1200 | Monitoring | ✓ | ✓ | ✓ | ✓ | – | Safety monitoring |
| DWG-10-1300 | RTS | ✓ | ✓ | ✓ | ✓ | ✓ | Operational safety |
| DWG-10-1400 | Safety Signage | ✓ | ✓ | ✓ | ✓ | – | Safety markings |

---

## 4. Approver Roles and Responsibilities

### 4.1 Drawing Creator

- Responsible for technical accuracy
- Follows drawing standards
- Performs self-check
- Incorporates review comments

### 4.2 Peer Reviewer

- Independent technical review
- Standards compliance check
- Constructive feedback
- No approval authority

### 4.3 Discipline Engineer

- Technical approval authority
- Ensures design intent met
- Verifies calculations and analysis
- Approves for release

### 4.4 Safety Engineer

- Safety-critical review authority
- Risk assessment verification
- Hazard analysis review
- Safety standards compliance

### 4.5 Configuration Manager

- Document control authority
- Drawing number management
- Version control oversight
- Archive and retrieval

### 4.6 Certification Engineer

- Regulatory compliance authority
- Type certificate coordination
- Documentation package review
- Authority liaison

---

## 5. Special Approval Requirements

### 5.1 H₂ System Drawings (DWG-10-800)

Additional approvals required:
- Cryogenic systems engineer
- H₂ safety specialist
- Fire protection engineer
- Certification authority

Review criteria:
- Compliance with H₂ safety standards
- Leak detection provisions
- Emergency shutoff systems
- Exclusion zone definitions

### 5.2 HV System Drawings (DWG-10-900)

Additional approvals required:
- Electrical systems engineer
- HV safety specialist
- Arc flash analyst
- Certification authority

Review criteria:
- Electrical isolation provisions
- Arc flash hazard analysis
- Lockout/tagout (LOTO) provisions
- Warning label placement

### 5.3 Jacking Drawings (DWG-10-400)

Additional approvals required:
- Structural engineer
- Loads and dynamics engineer
- Safety engineer
- Certification authority

Review criteria:
- Load distribution analysis
- Structural capacity verification
- Safety factor compliance
- Jacking sequence validation

---

## 6. Approval Process Flow

```
1. CREATE
   ↓
2. SELF-CHECK (Creator)
   ↓
3. PEER REVIEW
   ↓
4. REVISE as needed
   ↓
5. TECHNICAL APPROVAL (Level 2)
   ↓
6. SAFETY REVIEW (Level 3, if applicable)
   ↓
7. CM CHECK (Level 4)
   ↓
8. CERTIFICATION REVIEW (Level 5, if applicable)
   ↓
9. FINAL APPROVAL & RELEASE
   ↓
10. DISTRIBUTION
```

---

## 7. Approval Documentation

### 7.1 Approval Record

Each drawing shall have an approval record documenting:
- Approver name and role
- Approval date
- Signature (electronic or handwritten)
- Comments or conditions

### 7.2 Approval Tracking

- Maintained in configuration management database
- Linked to drawing metadata JSON files
- Auditable approval history
- Non-repudiable electronic signatures

---

## 8. Emergency Approval Process

For urgent changes in operational context:

1. Temporary approval by on-call engineer
2. Full approval within 48 hours
3. Retroactive documentation
4. Special notation in revision history

Conditions for emergency approval:
- Safety-critical operational need
- No increase in risk level
- Full approval cannot wait for normal process
- Documented justification required

---

## 9. Approval Matrix Updates

This approval matrix shall be reviewed:
- Annually as minimum
- When organizational changes occur
- When regulations change
- When new drawing types added
- After any approval-related audit findings

---

## 10. Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---

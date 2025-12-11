# DWG-10-099-E — Effectivity Matrix

**Document ID:** DWG-10-099-E  
**Title:** Drawing Effectivity Matrix  
**ATA Chapter:** 10 – Parking, Mooring, Storage, RTS  
**Status:** DRAFT  
**Version:** A  
**Date:** 2025-12-09

---

## 1. Purpose

This document defines the effectivity of ATA 10 drawings across different aircraft configurations, serial numbers, and operational scenarios.

---

## 2. Aircraft Variants

### 2.1 Q100 Variant Definitions

| Variant Code | Description | Configuration |
|--------------|-------------|---------------|
| Q100-P | Passenger variant | Standard config |
| Q100-C | Cargo variant | Cargo config |
| Q100-H | Hybrid (passenger/cargo) | Convertible config |
| Q100-E | Extended range | Additional H₂ capacity |
| Q100-R | Regional | Reduced capacity |

---

## 3. Drawing Effectivity by Series

### 3.1 Universal Drawings

These drawings apply to **all** Q100 variants:

#### DWG-10-100: General Arrangement
- All drawings in this series are universal
- Specific zones may vary by variant (see variant-specific notes)

#### DWG-10-000: Index and Standards
- All drawings in this series are universal
- Standard applies to all variants

#### DWG-10-1400: Safety Signage
- All drawings in this series are universal
- Safety markings required on all variants

---

## 4. Variant-Specific Effectivity

### 4.1 DWG-10-200: Mooring Drawings

| Drawing | Q100-P | Q100-C | Q100-H | Q100-E | Q100-R | Notes |
|---------|--------|--------|--------|--------|--------|-------|
| 200-001 to 200-005 | ✓ | ✓ | ✓ | ✓ | ✓ | Universal |
| 200-010, 200-011 | ✓ | ✓ | ✓ | ✓ | ✓ | Universal |
| 200-020, 200-030 | ✓ | ✓ | ✓ | ✓ | ✓ | Universal |

### 4.2 DWG-10-300: Towing Drawings

| Drawing | Q100-P | Q100-C | Q100-H | Q100-E | Q100-R | Notes |
|---------|--------|--------|--------|--------|--------|-------|
| All | ✓ | ✓ | ✓ | ✓ | ✓ | Universal |

### 4.3 DWG-10-400: Jacking Drawings

| Drawing | Q100-P | Q100-C | Q100-H | Q100-E | Q100-R | Notes |
|---------|--------|--------|--------|--------|--------|-------|
| 400-001 to 400-005 | ✓ | ✓ | ✓ | ✓ | ✓ | Universal points |
| 400-040 | ✓ | ✓* | ✓* | ✓* | ✓* | *Load values vary |

**Note:** Load distribution varies by variant due to different weight distributions.

### 4.4 DWG-10-800: H₂ System Drawings

| Drawing | Q100-P | Q100-C | Q100-H | Q100-E | Q100-R | Notes |
|---------|--------|--------|--------|--------|--------|-------|
| 800-001 to 800-006 | ✓ | ✓ | ✓ | ✓ | ✓ | Universal |
| 800-010 | ✓ | ✓ | ✓ | ✓* | ✓ | *E has additional tanks |
| 800-030, 800-031 | ✓ | ✓ | ✓ | ✓* | ✓ | *E has modified flow |
| 800-040 | ✓ | ✓ | ✓ | ✓* | ✓ | *E has larger zones |
| 800-050 | ✓ | ✓ | ✓ | ✓ | ✓ | Universal |

### 4.5 DWG-10-900: HV System Drawings

| Drawing | Q100-P | Q100-C | Q100-H | Q100-E | Q100-R | Notes |
|---------|--------|--------|--------|--------|--------|-------|
| All | ✓ | ✓ | ✓ | ✓ | ✓ | Universal (800V system) |

### 4.6 DWG-10-1000: Ground Power Drawings

| Drawing | Q100-P | Q100-C | Q100-H | Q100-E | Q100-R | Notes |
|---------|--------|--------|--------|--------|--------|-------|
| 1000-001 to 1000-005 | ✓ | ✓ | ✓ | ✓ | ✓ | Universal |
| 1000-040 | ✓ | ✓ | ✓ | ✓* | ✓ | *E has longer charge time |

---

## 5. Serial Number Effectivity

### 5.1 Production Blocks

| Block | Serial Numbers | Effectivity Date | Notes |
|-------|----------------|------------------|-------|
| Block 1 | S/N 001-010 | 2026-Q1 | Prototype/test aircraft |
| Block 2 | S/N 011-050 | 2026-Q3 | Initial production |
| Block 3 | S/N 051-100 | 2027-Q1 | Production standard |
| Block 4 | S/N 101+ | 2027-Q3 | Enhanced features |

### 5.2 Block-Specific Modifications

#### Block 1 (Prototype)
- May have interim drawing versions
- Test-specific equipment
- Not all drawings applicable

#### Block 2-4 (Production)
- All drawings applicable as specified
- Minor revisions between blocks
- See revision history for details

---

## 6. Operational Scenario Effectivity

### 6.1 Parking Operations

| Scenario | Required Drawings | Optional Drawings |
|----------|------------------|-------------------|
| Short-term parking (< 24h) | DWG-10-100, DWG-10-800, DWG-10-900 | DWG-10-700 |
| Long-term parking (> 24h) | DWG-10-100, DWG-10-500, DWG-10-800, DWG-10-900, DWG-10-700 | DWG-10-1100 |
| Maintenance parking | All relevant series | DWG-10-1200 |

### 6.2 Storage Operations

| Scenario | Required Drawings | Optional Drawings |
|----------|------------------|-------------------|
| Indoor storage | DWG-10-100, DWG-10-500, DWG-10-800, DWG-10-900 | DWG-10-1200 |
| Outdoor storage | DWG-10-100, DWG-10-500, DWG-10-700, DWG-10-800, DWG-10-900, DWG-10-1100, DWG-10-1200 | - |
| Long-term preservation | All series | - |

### 6.3 Maintenance Operations

| Scenario | Required Drawings | Optional Drawings |
|----------|------------------|-------------------|
| Line maintenance | DWG-10-100, DWG-10-600 | DWG-10-1300 |
| Base maintenance | DWG-10-400, DWG-10-600, DWG-10-1300 | DWG-10-200 |
| Heavy maintenance | All series | - |
| Return to service | DWG-10-1300 | All series |

---

## 7. Geographic/Environmental Effectivity

### 7.1 Climate Zones

| Zone | Description | Specific Requirements | Affected Drawings |
|------|-------------|----------------------|-------------------|
| Tropical | High temp, high humidity | Enhanced corrosion protection | DWG-10-1100 |
| Arctic | Low temp, ice/snow | Cold weather provisions | DWG-10-1100 |
| Desert | High temp, sand/dust | Enhanced sealing | DWG-10-1100 |
| Maritime | Salt spray, corrosion | Maritime protection | DWG-10-1100 |
| Standard | Temperate climate | Standard provisions | All |

### 7.2 Operational Environment

| Environment | Specific Drawings | Notes |
|-------------|------------------|-------|
| Commercial airport | All standard | Full suite applicable |
| Remote location | DWG-10-800, DWG-10-900, DWG-10-1200 | Monitoring critical |
| Military base | May require additional security provisions | Consult security annex |
| Test facility | May include test-specific provisions | Consult test plans |

---

## 8. Regulatory Effectivity

### 8.1 Certification Basis

| Authority | Regulation | Applicable Drawings | Notes |
|-----------|-----------|-------------------|-------|
| EASA | CS-25 | All | Primary certification |
| FAA | Part 25 | All | Secondary certification |
| TCCA | CAR 525 | All | Mutual recognition |
| CAAC | CCAR-25 | All | Mutual recognition |

### 8.2 Special Conditions

| Special Condition | Affected Drawings | Effectivity |
|------------------|------------------|-------------|
| H₂ Propulsion | DWG-10-800 series | All Q100 variants |
| HV Systems (>270V DC) | DWG-10-900 series | All Q100 variants |
| BWB Configuration | DWG-10-200, DWG-10-400 | All Q100 variants |

---

## 9. Customer-Specific Effectivity

### 9.1 Optional Equipment

| Option Code | Description | Affected Drawings |
|-------------|-------------|-------------------|
| OPT-10-001 | Enhanced monitoring system | DWG-10-1200 series |
| OPT-10-002 | Arctic operations kit | DWG-10-1100 series |
| OPT-10-003 | Extended storage kit | DWG-10-1100, DWG-10-1200 |
| OPT-10-004 | Quick turnaround kit | DWG-10-100-009 |

---

## 10. Maintenance and Updates

This effectivity matrix shall be:
- Reviewed quarterly
- Updated when new variants introduced
- Updated when drawing revisions affect effectivity
- Updated when operational scenarios change
- Maintained by Configuration Management

---

## 11. Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia.**
- **Status:** DRAFT – Subject to human review and approval.
- **Human approver:** _[to be completed]_
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-12-09

---

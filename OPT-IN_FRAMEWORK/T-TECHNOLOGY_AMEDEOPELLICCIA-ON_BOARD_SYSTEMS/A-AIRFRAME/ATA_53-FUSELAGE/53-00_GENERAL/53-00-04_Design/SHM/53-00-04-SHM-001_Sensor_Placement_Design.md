# 53-00-04-SHM-001: Sensor Placement Design

## Document ID
**53-00-04-SHM-001**

## Title
SHM Sensor Placement Design

## Purpose
Define the sensor placement design for the SHM system, including sensor locations, coverage optimization, and structural integration requirements.

## Design Philosophy

### Placement Criteria
| Priority | Criteria | Weight |
|----------|----------|--------|
| 1 | Damage-critical area coverage | 40% |
| 2 | Signal propagation efficiency | 25% |
| 3 | Accessibility for maintenance | 20% |
| 4 | Structural integration impact | 15% |

### Sensor Spacing Guidelines
| Material Type | Optimal Spacing | Maximum Spacing |
|---------------|-----------------|-----------------|
| Aluminum skin | 400-500 mm | 750 mm |
| CFRP laminate | 300-400 mm | 600 mm |
| Titanium fitting | 200-300 mm | 500 mm |
| Sandwich panel | 250-350 mm | 500 mm |

## Zone 1: Forward Fuselage

### Sensor Layout
| Area | PZT Sensors | FBG Channels | Priority |
|------|-------------|--------------|----------|
| Pressure bulkhead | 24 | 12 | Critical |
| Nose gear bay | 16 | 8 | Critical |
| Cockpit window frames | 12 | 4 | High |
| Forward door surrounds | 16 | 4 | High |
| General skin | 12 | 2 | Medium |

### Coverage Map Reference
- Drawing: 53-00-04-SHM-DWG-001

## Zone 2: Center Fuselage

### Sensor Layout
| Area | PZT Sensors | FBG Channels | Priority |
|------|-------------|--------------|----------|
| Wing-body junction (upper) | 32 | 16 | Critical |
| Wing-body junction (lower) | 32 | 16 | Critical |
| Passenger door frames | 24 | 8 | High |
| Window frames | 16 | 4 | Medium |
| Floor beams | 8 | 12 | High |
| General skin | 8 | 4 | Medium |

### Coverage Map Reference
- Drawing: 53-00-04-SHM-DWG-002

## Zone 3: Aft Fuselage

### Sensor Layout
| Area | PZT Sensors | FBG Channels | Priority |
|------|-------------|--------------|----------|
| Empennage attachment | 24 | 16 | Critical |
| Aft pressure bulkhead | 20 | 8 | Critical |
| APU mount structure | 12 | 4 | High |
| Tail cone | 12 | 8 | Medium |
| General skin | 12 | 4 | Medium |

### Coverage Map Reference
- Drawing: 53-00-04-SHM-DWG-003

## Structural Integration

### Mounting Requirements
| Parameter | Requirement |
|-----------|-------------|
| Surface flatness | ≤0.5 mm deviation |
| Edge distance | ≥25 mm from fasteners |
| Clearance | 100 mm minimum around sensor |
| Access | Removable panel or designed opening |

### Installation Details
| Feature | Specification |
|---------|---------------|
| Bond type | Structural adhesive (FM300-2 or equiv) |
| Surface prep | Per sensor OEM specification |
| Wire routing | Dedicated conduit/brackets |
| Strain relief | Per IPC-620 Class 3 |

### Structural Impact
| Parameter | Limit |
|-----------|-------|
| Stress concentration | ≤5% increase |
| Stiffness reduction | ≤2% local |
| Added mass | ≤50 kg total |
| Fatigue knockdown | None (per analysis) |

## Design Verification

### Analysis
| Analysis Type | Tool | Objective |
|---------------|------|-----------|
| Coverage optimization | MATLAB | Maximize coverage, minimize sensors |
| Wave propagation | Abaqus | Verify signal paths |
| Stress analysis | NASTRAN | Verify structural impact |

### Test Validation
- Phase 1: Element panels
- Phase 2: Component barrels
- Phase 3: Full-scale test article

## Traceability
- Parent Requirement: [53-00-03-01-005](../53-00-03_Requirements/01_Structural_Integrity/53-00-03-01-005_Compatibility_with_SHM_Assumptions.md)
- V&V Reference: V&V-53-012

---

## Document Control

| Field | Value |
|-------|-------|
| Generated with | AI assistance (GitHub Copilot) |
| Prompted by | **Amedeo Pelliccia** |
| Status | **DRAFT** |
| Repository | `AMPEL360-BWB-H2-Hy-E` |
| Last AI Update | 2025-11-27 |

---

# ICD: ATA 31-50-10 to ATA 22 (Autoflight)

## Interface Control Document

**Document ID**: ICD-31-50-ATA22-001  
**Version**: 1.0  
**Status**: Draft  
**Date**: 2026-01-09

## Overview

This Interface Control Document defines the interface between ATA 31-50-10 (Central Warning System - Message Model) and ATA 22 (Autoflight) for alert inhibit coordination.

## Interface Description

### Purpose

The autoflight system provides flight phase and mode information to the Central Warning System to enable appropriate alert inhibition during critical phases of flight (e.g., takeoff, landing, go-around).

### Interface Type

- **Physical Layer**: ARINC 429 or AFDX (depending on architecture)
- **Data Rate**: 100 kbps (ARINC 429) or 100 Mbps (AFDX)
- **Direction**: ATA 22 → ATA 31-50-10 (one-way)
- **Update Rate**: 10 Hz minimum

## Data Elements

### Flight Phase Signals

| Signal Name | Label | Data Type | Range | Units | Description |
|------------|-------|-----------|-------|-------|-------------|
| FLIGHT_PHASE | 270 (example) | Discrete | 0-15 | - | Current flight phase enumeration |
| AUTOFLIGHT_MODE | 271 (example) | Discrete | 0-31 | - | Active autoflight mode |
| TAKEOFF_INHIBIT_ACTIVE | 272 (example) | Boolean | 0-1 | - | Takeoff phase alert inhibit flag |
| LANDING_INHIBIT_ACTIVE | 273 (example) | Boolean | 0-1 | - | Landing phase alert inhibit flag |
| GO_AROUND_MODE_ACTIVE | 274 (example) | Boolean | 0-1 | - | Go-around mode active flag |

### Flight Phase Enumeration

| Value | Phase | Description |
|-------|-------|-------------|
| 0 | PREFLIGHT | Aircraft on ground, not moving |
| 1 | TAXI | Ground taxi operations |
| 2 | TAKEOFF | From thrust application to 1500' AGL |
| 3 | CLIMB | Climb to cruise altitude |
| 4 | CRUISE | Level cruise flight |
| 5 | DESCENT | Descent from cruise |
| 6 | APPROACH | Final approach to landing |
| 7 | LANDING | Below 200' AGL to touchdown |
| 8 | ROLLOUT | Touchdown to taxi speed |
| 9-15 | RESERVED | For future use |

## Inhibit Logic

### Takeoff Phase (Phase 2)

**Inhibited Alerts:**
- Non-essential cautions and advisories
- Configuration warnings already addressed

**Active Alerts:**
- Engine fire warnings
- Flight control failures
- Critical system failures

### Landing Phase (Phase 7)

**Inhibited Alerts:**
- Similar to takeoff inhibits
- Landing gear advisories (if gear down and locked)

**Active Alerts:**
- Same critical alerts as takeoff

### Go-Around Mode

**Inhibited Alerts:**
- All non-essential alerts during initial climb-out

**Active Alerts:**
- Critical warnings only

## Timing Requirements

- Signal latency: < 50 ms from source to CWS
- Update rate: Minimum 10 Hz for flight phase
- Alert inhibit activation: < 100 ms from signal reception

## Fault Handling

- Loss of autoflight signals: Default to no inhibits (conservative approach)
- Invalid data: Ignore and use last valid data for up to 1 second
- Signal restoration: Resume normal inhibit logic within 100 ms

## Testing and Verification

- Verify correct inhibit behavior in all flight phases
- Verify timing requirements through system integration tests
- Verify fault handling and degraded mode operation

## References

- ATA 22 System Description
- ATA 31-50-10 Alert Inhibit Logic Specification
- CS-25.1309 - Equipment, Systems and Installations
- ARINC 429 / AFDX Protocol Standards

## Document Control

- **Owner**: AMPEL360 Avionics Integration Team
- **Approver**: TBD
- **Generated with AI assistance**: GitHub Copilot, prompted by **Amedeo Pelliccia**
- **Last Updated**: 2026-01-09

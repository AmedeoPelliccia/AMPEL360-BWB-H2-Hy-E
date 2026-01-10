# ATA 31-50-10 — CAS/ECAM/EICAS Message Model and Priorities

## Overview

This subsection defines the message model, taxonomy, and prioritization logic for Central Crew Alerting Systems (CAS), Engine Indication and Crew Alerting System (EICAS), and Electronic Centralized Aircraft Monitor (ECAM).

## Purpose

To establish:

- Unified message taxonomy and data model
- Alert priority levels and hierarchies
- Message formatting and presentation rules
- Alert triggering conditions and logic
- Crew interaction and acknowledgment patterns

## Structure

This leaf node contains:

- **[SSOT/](./SSOT/)**: Single Source of Truth with complete lifecycle documentation (LC01-LC14)
- **[PUB/](./PUB/)**: S1000D-compliant publications (CSDB, EXPORT, IETP)

## Key Topics

### Message Taxonomy

Alert messages are categorized by:

- **Type**: Warning, Caution, Advisory, Status, Memo
- **System**: Engine, Hydraulic, Electrical, Flight Controls, etc.
- **Priority**: Level 1 (highest) through Level 5 (lowest)
- **Phase of Flight**: Applicable phases and inhibit conditions

### Alert Priority Levels

**Level 1 - Warning (RED)**
- Requires immediate crew action
- Potentially catastrophic condition
- Aural warning (continuous tone or voice)
- Master warning light illuminated

**Level 2 - Caution (AMBER)**
- Requires timely crew awareness and action
- Abnormal condition that could become hazardous
- Aural alert (single chime or intermittent tone)
- Master caution light illuminated

**Level 3 - Advisory (WHITE/CYAN)**
- Crew awareness required
- System operating in non-normal configuration
- No immediate action required
- No aural alert (generally)

**Level 4 - Status (WHITE/GREEN)**
- Informational messages
- Normal system status indication
- No crew action required

**Level 5 - Memo (WHITE)**
- Procedural reminders
- Configuration information
- No aural alert

### Message Model

Each alert message contains:

- Message ID (unique identifier)
- Message text (crew-facing description)
- Priority level and color
- Associated aural alert
- System source
- Triggering condition(s)
- Inhibit logic
- Crew actions (optional)
- Related checklist references
- BITE data and fault codes

### Prioritization Rules

When multiple alerts are active:

1. Highest priority alert is displayed prominently
2. Lower priority alerts may be suppressed or collapsed
3. Alert lists are dynamically reordered
4. Master warning/caution logic is maintained
5. Aural alerts follow priority hierarchy

## References

- ARINC 661 - Cockpit Display System Interfaces
- DO-257 - Minimum Aviation System Performance Standards for Flight Deck Displays
- CS-25.1309 - Equipment, Systems and Installations
- DO-178C - Software Considerations in Airborne Systems
- SAE ARP4761 - Guidelines and Methods for Conducting the Safety Assessment Process

## Document Control

- **Subsection**: 31-50-10
- **Status**: Active Development
- **Owner**: AMPEL360 Avionics Systems Engineering
- **Generated with AI assistance**: GitHub Copilot, prompted by **Amedeo Pelliccia**
- **Last Updated**: 2026-01-09

---

[⬆ Back to 31-50 Index](../00_INDEX.md) | [⬆ Back to ATA 31 Index](../../../00_INDEX.md)

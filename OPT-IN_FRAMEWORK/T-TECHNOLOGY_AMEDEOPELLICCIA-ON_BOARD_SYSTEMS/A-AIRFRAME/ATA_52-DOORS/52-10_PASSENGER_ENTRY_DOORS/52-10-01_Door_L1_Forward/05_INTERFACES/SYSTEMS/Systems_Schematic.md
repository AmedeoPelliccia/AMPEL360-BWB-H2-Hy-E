# Systems Schematic Overview
## Door L1 Forward Systems Integration

**Document:** Systems_Schematic.md  
**Date:** 2025-11-03  
**Status:** Reference Document

---

## System Architecture

The Door L1 Forward integrates with multiple aircraft systems:

```
┌─────────────────────────────────────────────────────────────┐
│                    AIRCRAFT SYSTEMS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐      ┌──────────────┐                   │
│  │  ATA 24      │─────▶│ Door Power   │                   │
│  │  Electrical  │ 28VDC│ Controller   │                   │
│  └──────────────┘      └──────┬───────┘                   │
│                                │                            │
│  ┌──────────────┐             │                            │
│  │  ATA 36      │─────────────┼──────┐                    │
│  │  Pneumatic   │ 15 psi      │      │                    │
│  └──────────────┘             │      │                    │
│                                ▼      ▼                    │
│  ┌──────────────┐      ┌──────────────────┐              │
│  │  ATA 42      │◀────▶│   DOOR L1 FWD    │              │
│  │  IMA         │ Data │                  │              │
│  └──────────────┘      │  - Motor Drive   │              │
│                        │  - Latch Ctrl    │              │
│  ┌──────────────┐      │  - Seal Inflate  │              │
│  │  ATA 31      │◀─────│  - Position Sens │              │
│  │  Indication  │Status│  - Lock Monitor  │              │
│  └──────────────┘      └──────────────────┘              │
│                                │                            │
│  ┌──────────────┐             │                            │
│  │  ATA 33      │◀────────────┘                           │
│  │  Emergency   │ Control                                 │
│  │  Lighting    │                                         │
│  └──────────────┘                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Power Distribution

```
28 VDC Main Bus
    │
    ├──[CB 35A]─────▶ Door Motor (30A max)
    │
    ├──[CB 5A]──────▶ Controller (0.5A)
    │
    └──[CB 5A]──────▶ Emergency Lighting (0.3A)

28 VDC Emergency Bus (backup)
    │
    └──[CB 10A]─────▶ Position Indication (0.7A)
```

---

## Signal Flow

```
Flight Deck Controls
    │
    ▼
┌─────────────┐
│ EICAS/ECAM  │
└──────┬──────┘
       │ ARINC 429
       ▼
┌─────────────┐
│     IMA     │
└──────┬──────┘
       │ ARINC 429 / Ethernet
       ▼
┌─────────────┐
│ Door        │
│ Controller  │───▶ Position sensors
│             │───▶ Lock switches
│             │───▶ Motor drive
│             │───▶ Seal valve
└─────────────┘
```

---

## Pneumatic System

```
Bleed Air System (50 psi)
    │
    ▼
[Pressure Regulator]
    │ 15 psi
    ▼
[Solenoid Valve]──28VDC Control
    │
    ▼
[Inflatable Seal]
```

---

## Data Interface

```
Door Controller
    │
    ├──▶ ARINC 429 TX (Label 250) @ 2 Hz
    │    └─ Door status, position, faults
    │
    ├──▶ ARINC 429 RX (Label 251) @ 1 Hz
    │    └─ Commands, configuration
    │
    └──▶ CMC (Maintenance Data) @ 1 Hz
         └─ Cycle counts, fault logs, trends
```

---

## Related Documents

- ICD-52-24-001: Electrical Power Interface
- ICD-52-36-001: Pneumatic Supply Interface
- ICD-52-31-001: Indication and Recording Interface
- ICD-52-33-001: Emergency Lighting Interface
- ICD-52-42-001: IMA Integration
- ICD-52-23-001: ARINC 429 Bus Interface

---

*This schematic is part of the AMPEL360 OPT-IN Framework interface documentation.*

# Human-Machine Interface Design

**Document ID:** AMPEL360-02-00-00-DES-HMI  
**Version:** 1.0.0

## Design Philosophy

**Human-Centered Design (HCD):**
- Interfaces designed around crew capabilities
- Minimize cognitive load
- Support situational awareness
- Enable error detection and recovery

## Display Hierarchy

### Primary Flight Display (PFD)
**Critical flight information:**
- Attitude, altitude, airspeed
- BWB-specific: CG position indicator
- Fuel cell power output
- H2 system status

### Navigation Display (ND)
**Route and position:**
- Standard nav display
- CAOS route optimization overlay (advisory)
- Weather radar
- Terrain awareness

### Engine/System Display (EICAS Style)
**System monitoring:**
- Fuel cell status (4 stacks)
- H2 system synoptic
- Electrical system
- CAOS advisories window

### Multi-Function Display (MFD)
**Configurable:**
- Checklists (digital)
- Performance data
- Weather
- Airport info
- CAOS detailed explanations

## H₂ System Synoptic Design

```
┌────────────────────────────────────────┐
│ H2 FUEL SYSTEM                         │
├────────────────────────────────────────┤
│                                        │
│     [CTR-1]        [CTR-2]            │
│     2,500kg        2,000kg            │
│     -253°C         -253°C             │
│     3.0 bar        3.0 bar            │
│        │              │                │
│        └──────┬───────┘                │
│            [MAIN]                      │
│               │                        │
│      ┌────────┴────────┐              │
│   [L-OUT]          [R-OUT]            │
│   1,750kg          1,750kg            │
│   -253°C           -253°C             │
│   3.0 bar          3.0 bar            │
│                                        │
│ TOTAL: 8,000 kg  FLOW: 65 kg/hr      │
└────────────────────────────────────────┘
```

## Color Coding Standards

**Operational States:**
- 🟢 Green: Normal operation
- 🟡 Amber: Caution (attention required)
- 🔴 Red: Warning (immediate action required)
- ⚪ White: Advisory/information
- 🔵 Blue: System status/mode

**H₂ System Specific:**
- 🟢 Green: No leaks detected, parameters normal
- 🟡 Amber: Minor leak detected OR parameter caution
- 🔴 Red: Major leak OR emergency condition

## Alerting Philosophy

**Priority Levels:**

**Level 3 - WARNING (Red):**
- Immediate crew action required
- Master WARNING lights
- Aural tone (continuous)
- **Example:** H2 LEAK - MAJOR

**Level 2 - CAUTION (Amber):**
- Crew awareness required
- Master CAUTION lights
- Aural tone (single chime)
- **Example:** H2 TEMP HIGH

**Level 1 - ADVISORY (White):**
- Crew information
- No lights
- No aural
- **Example:** H2 REFUEL COMPLETE

## CAOS Interface Design

**Advisory Intrusiveness:**
- Normal: Bottom window, no alert
- Time-sensitive: Amber border, single chime
- Critical safety: Integrated with normal alerting system

**Explanation Depth:**
- Level 1: One-line reason
- Level 2: Detailed explanation (button press)
- Level 3: Full analysis (CAOS page on MFD)

## Control Interface Standards

**Critical Controls:**
- Guarded switches (H2 master, fuel cell master)
- Two-action confirmation (emergency shutdowns)
- Tactile feedback

**Override Controls:**
- CAOS override: Single button, immediate effect
- Color: Red with "OVERRIDE" label
- Location: Easily reachable by both pilots

## Workload Management

**High Workload Phases (Takeoff/Landing):**
- Minimal CAOS advisories
- Only critical information displayed
- Declutter mode available

**Low Workload Phases (Cruise):**
- Full CAOS advisory capability
- Detailed performance data available
- Optimization recommendations active

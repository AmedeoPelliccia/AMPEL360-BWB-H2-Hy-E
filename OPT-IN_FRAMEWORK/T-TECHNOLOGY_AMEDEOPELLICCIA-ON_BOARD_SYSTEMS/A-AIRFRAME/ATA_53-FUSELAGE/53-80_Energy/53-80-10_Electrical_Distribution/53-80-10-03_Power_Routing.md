# 53-80-10-03 — Power Routing Logic

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-10-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | ENERGY / ELECTRICAL |

---

## 1. Purpose

This document defines the power routing logic for the ANCHORS electrical distribution system. It establishes the algorithms and decision trees used to route power from multiple sources to loads while optimizing efficiency and maintaining safety margins.

## 2. Power Source Hierarchy

### 2.1 Source Priority

| Priority | Source | Capacity | Availability | Notes |
|----------|--------|----------|--------------|-------|
| 1 | Fuel Cells | 1000 kW | In-flight | Primary source |
| 2 | Turbo-Generators | 1500 kW | In-flight | High-power phases |
| 3 | Battery Packs | 200 kWh | Always | Buffer/emergency |
| 4 | Regeneration | 800 kW | Descent | Variable |
| 5 | Ground Power | 200 kW | Ground only | Unlimited |

### 2.2 Source Selection Logic

```mermaid
flowchart TB
    START["Power Request"] --> GROUND{"On Ground?"}
    
    GROUND -->|Yes| GPU{"GPU<br/>Connected?"}
    GPU -->|Yes| USE_GPU["Use Ground Power"]
    GPU -->|No| CHECK_APU{"APU<br/>Running?"}
    CHECK_APU -->|Yes| USE_APU["Use APU"]
    CHECK_APU -->|No| USE_BAT["Use Battery"]
    
    GROUND -->|No| FLIGHT["In-Flight Mode"]
    FLIGHT --> CHECK_FC{"FC + TG<br/>≥ Demand?"}
    
    CHECK_FC -->|Yes| USE_FC["Use FC + TG"]
    CHECK_FC -->|No| SUPPLEMENT["Supplement from Battery"]
    
    USE_FC --> CHECK_EXCESS{"Excess<br/>Power?"}
    CHECK_EXCESS -->|Yes| CHARGE["Charge Battery"]
    CHECK_EXCESS -->|No| BALANCE["Power Balanced"]
    
    CHECK_REGEN{"Regen<br/>Available?"} --> YES_REGEN["Accept Regen"]
    YES_REGEN --> CHARGE
```

## 3. Routing Modes

### 3.1 Mode Definitions

| Mode | Condition | Primary Source | Backup | Action |
|------|-----------|----------------|--------|--------|
| GROUND_GPU | GPU connected | Ground Power | Battery | Charge + precondition |
| GROUND_BAT | No GPU | Battery | None | Conservation |
| TAXI | Low-speed taxi | Battery | FC standby | Electric taxi |
| FLIGHT_NORMAL | Cruise | FC + TG | Battery | Balanced operation |
| FLIGHT_PEAK | Takeoff/climb | FC + TG + Battery | None | Max power |
| REGEN | Descent | Regen | FC | Battery charging |
| EMERGENCY | Fault condition | Battery | Isolate fault | Essential loads |

### 3.2 Mode Transition Matrix

| From \ To | GROUND_GPU | GROUND_BAT | TAXI | NORMAL | PEAK | REGEN | EMERG |
|-----------|------------|------------|------|--------|------|-------|-------|
| GROUND_GPU | — | ✓ | ✓ | — | — | — | ✓ |
| GROUND_BAT | ✓ | — | ✓ | — | — | — | ✓ |
| TAXI | — | ✓ | — | ✓ | ✓ | — | ✓ |
| NORMAL | — | — | ✓ | — | ✓ | ✓ | ✓ |
| PEAK | — | — | — | ✓ | — | — | ✓ |
| REGEN | — | — | — | ✓ | — | — | ✓ |
| EMERG | ✓ | ✓ | — | ✓ | — | — | — |

## 4. Power Flow Control

### 4.1 Source Contribution Algorithm

```
Algorithm: Calculate Source Contribution

INPUTS:
  P_demand    = Total power demand (kW)
  P_fc_avail  = FC available power (kW)
  P_tg_avail  = TG available power (kW)
  P_bat_avail = Battery available power (kW)
  SOC         = Battery state of charge (%)
  Mode        = Operating mode

OUTPUTS:
  P_fc        = FC contribution (kW)
  P_tg        = TG contribution (kW)
  P_bat       = Battery contribution (kW)

LOGIC:
  IF Mode == GROUND_GPU:
    P_fc = 0, P_tg = 0, P_bat = 0  // GPU provides all
  
  ELSE IF Mode == TAXI:
    P_bat = P_demand  // Electric taxi
    P_fc = 0, P_tg = 0
  
  ELSE IF Mode == FLIGHT_NORMAL:
    P_fc = min(P_demand * 0.6, P_fc_avail)  // FC first
    P_tg = min(P_demand - P_fc, P_tg_avail)  // TG makes up
    IF (P_fc + P_tg) < P_demand:
      P_bat = P_demand - P_fc - P_tg  // Battery supplements
    ELSE IF (P_fc + P_tg) > P_demand AND SOC < 95%:
      P_bat = -(P_fc + P_tg - P_demand)  // Charge battery
  
  ELSE IF Mode == FLIGHT_PEAK:
    P_fc = P_fc_avail
    P_tg = P_tg_avail
    P_bat = P_demand - P_fc - P_tg  // All sources
  
  ELSE IF Mode == REGEN:
    P_regen = available regen power
    P_fc = P_demand  // Reduced FC
    P_bat = -P_regen  // Charge with regen
```

### 4.2 Power Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      POWER FLOW CONTROL                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   SOURCES                    BUS                    LOADS       │
│   ────────                   ───                    ─────       │
│                                                                 │
│   ┌─────────┐                                     ┌─────────┐  │
│   │Fuel Cell│───────┐                       ┌─────│Battery  │  │
│   │1000 kW  │       │                       │     │TMS      │  │
│   └─────────┘       │                       │     └─────────┘  │
│                     ▼                       │                   │
│   ┌─────────┐    ╔═══╧═══╗                 │     ┌─────────┐  │
│   │Turbo-Gen│───▶║ HVDC  ║─────────────────┼─────│CO₂      │  │
│   │1500 kW  │    ║ BUS   ║                 │     │Capture  │  │
│   └─────────┘    ╚═══╤═══╝                 │     └─────────┘  │
│                     ▲ │                     │                   │
│   ┌─────────┐      │ │                     │     ┌─────────┐  │
│   │Battery  │◀─────┘ └─────────────────────┴─────│Water    │  │
│   │200 kWh  │    (Bidirectional)                 │System   │  │
│   └─────────┘                                    └─────────┘  │
│                                                                 │
│   ┌─────────┐                                    ┌─────────┐  │
│   │Regen    │───────────────────────────────────▶│Thermal  │  │
│   │800 kW   │    (During descent)                │Pumps    │  │
│   └─────────┘                                    └─────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 5. Bus Tie Logic

### 5.1 Bus Tie States

| State | Position | Condition | Purpose |
|-------|----------|-----------|---------|
| CLOSED | Normal | No faults | Unified bus operation |
| OPEN | Isolated | Fault detected | Fault isolation |
| MANUAL_OPEN | Manual | Crew command | Maintenance |
| FAILED_OPEN | Failed | Mechanical failure | Fail-safe |

### 5.2 Bus Tie Control Logic

```mermaid
stateDiagram-v2
    [*] --> CLOSED: Power On
    
    CLOSED --> OPENING: Fault Detected
    CLOSED --> MANUAL_OPEN: Crew Command
    
    OPENING --> OPEN: Open Confirmed
    OPEN --> CLOSING: Fault Cleared
    CLOSING --> CLOSED: Close Confirmed
    
    MANUAL_OPEN --> CLOSING: Crew Reset
    
    OPEN --> FAILED: Mechanism Fault
    FAILED --> [*]: Maintenance Required
    
    note right of CLOSED: Normal operation
    note right of OPEN: Fault isolation
```

### 5.3 Fault Detection Criteria

| Fault Type | Detection | Response |
|------------|-----------|----------|
| Overcurrent | I > 150% rated | Open bus tie in 10 ms |
| Undervoltage | V < 600 VDC for > 100 ms | Open bus tie |
| Overvoltage | V > 900 VDC | Open bus tie in 1 ms |
| Ground fault | GFI trip | Open affected channel |
| Differential | ΔI > 10% | Open bus tie |

## 6. Efficiency Optimization

### 6.1 Source Loading Optimization

| FC Load | TG Load | Battery | Efficiency | Condition |
|---------|---------|---------|------------|-----------|
| 60% | 0% | Supplement | 58% | Low demand |
| 80% | 20% | Charge | 61% | Normal cruise |
| 100% | 60% | Discharge | 63% | High demand |
| 60% | 0% | Charge (regen) | 85% | Descent |

### 6.2 Optimal Operating Points

```
┌─────────────────────────────────────────────────────────────────┐
│                  EFFICIENCY vs LOAD CURVE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   η(%)                                                          │
│    │                                                            │
│  98├          ****                                              │
│    │        **    **         DC-DC                              │
│  96├      **        **                                          │
│    │    **            **                                        │
│  94├  **                **                                      │
│    │**                    **                                    │
│  92├                        **                                  │
│    │                                                            │
│  60├                  ████████████                              │
│    │              ████              ████                        │
│  58├          ████                      ████    Fuel Cell       │
│    │      ████                              ████                │
│  56├  ████                                                      │
│    │                                                            │
│  54├────┬────┬────┬────┬────┬────┬────┬────┬────┬────          │
│         20   30   40   50   60   70   80   90  100  Load (%)    │
│                                                                 │
│   OPTIMAL: FC at 70-80%, DC-DC at 60-80%                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 7. Protection Coordination

### 7.1 Trip Sequence

| Level | Device | Location | Trip Time | Current |
|-------|--------|----------|-----------|---------|
| 1 | Load SSCB | Load input | < 1 ms | Load rated |
| 2 | Channel SSCB | SPDA output | < 10 ms | Channel rated |
| 3 | Bus SSCB | Bus section | < 50 ms | Section rated |
| 4 | Source contactor | Source output | < 100 ms | Source rated |
| 5 | Bus tie | Between buses | < 10 ms | Full bus |

### 7.2 Selectivity Margin

Minimum 10:1 time ratio between protection levels:
- Level 1 (1 ms) → Level 2 (10 ms): 10:1 ✓
- Level 2 (10 ms) → Level 3 (50 ms): 5:1 → Enhanced to 10:1
- Level 3 (50 ms) → Level 4 (100 ms): 2:1 → Use current grading

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | 53-80-10-03 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Author** | AMPEL360 Electrical Systems Team |
| **Reviewer** | _[To be assigned]_ |
| **Approver** | _[To be assigned]_ |

### AI Disclosure

- **Generated with assistance of:** AI (GitHub Copilot), prompted by **Amedeo Pelliccia**
- **Status:** DRAFT — Subject to human review and approval
- **Repository:** `AMPEL360-BWB-H2-Hy-E`
- **Last AI update:** 2025-11-27

---

*END OF DOCUMENT*

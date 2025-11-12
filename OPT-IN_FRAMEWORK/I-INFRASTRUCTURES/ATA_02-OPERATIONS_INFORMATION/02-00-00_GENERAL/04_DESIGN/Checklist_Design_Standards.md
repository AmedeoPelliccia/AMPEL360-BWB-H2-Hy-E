# Checklist Design Standards

**Document ID:** AMPEL360-02-00-00-DES-CKL  
**Version:** 1.0.0

## Checklist Types

### Do-Verify Checklists
- Used for routine, well-practiced procedures
- Crew performs actions from memory
- Checklist used to verify completion
- **Example:** Before Takeoff Checklist

### Challenge-Response Checklists
- Used for critical, sequential procedures
- PF reads challenge, PM responds with item status
- **Example:** Before Start Checklist

### Read-and-Do Checklists
- Used for non-routine or infrequent procedures
- Crew reads item, then performs action
- **Example:** Emergency evacuation

## Format Standards

### Normal Checklists
```
CHALLENGE..................................RESPONSE
Fuel Quantity..............................._____ KG
Fuel Pumps..................................ON
H2 Temperature..............................NORMAL
```

### Emergency Checklists (QRH)
```
⚠️ H2 LEAK DETECTED

MEMORY ITEMS (commit to memory):
    H2 MASTER..........................OFF
    VENT SYSTEM........................EMERG
    FUEL CELL MASTER...................OFF

SUBSEQUENT ACTIONS:
    1. Leak Location...................IDENTIFY
    2. Isolation Valves................CLOSE
    3. Landing.........................PLAN ASAP
```

## Design Rules

**Rule 1: Brevity**
- Maximum 20 items per checklist
- If >20 items, split into phases

**Rule 2: Plain Language**
- No jargon unless standard industry term
- Active voice
- Second-person imperative ("Check fuel")

**Rule 3: Visual Hierarchy**
```
PRIMARY ITEMS (normal font)
    Sub-items (indented)
        [Notes in brackets]
```

**Rule 4: Cross-Check**
- Critical items require verification
- Format: "_____ [value]" requires crew to state value

**Rule 5: Reversibility**
- Critical irreversible actions require confirmation
- Format: "ACTION.......................CONFIRM"

## H2 System Checklist Design

**Pre-Refueling Checklist:**
- Safety zone verification as first item
- Equipment readiness confirmed
- Personnel certification verified
- Go/No-Go decision explicit

**H2 Emergency Checklist:**
- Memory items: Immediate threat mitigation
- Subsequent: Source location, isolation
- Landing considerations prominent

## CAOS Integration

**Digital Checklist (CAOS-Enhanced):**
- Items auto-populate with actual values
- Conditional logic hides N/A items
- CAOS flags anomalies in yellow
- Crew still manually confirms each item

**Paper Backup:**
- Identical content to digital version
- Always available in QRH
- Crew trained on both methods

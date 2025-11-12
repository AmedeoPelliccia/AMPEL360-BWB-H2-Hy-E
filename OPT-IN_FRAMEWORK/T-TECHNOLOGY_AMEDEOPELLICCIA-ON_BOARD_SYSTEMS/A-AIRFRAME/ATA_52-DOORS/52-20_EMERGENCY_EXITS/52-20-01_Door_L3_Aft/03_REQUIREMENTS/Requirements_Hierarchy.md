# Requirements Hierarchy - Door L3 Aft Emergency Exit

**Document ID:** AMPEL360-52-20-01-REQ-HIER  
**Version:** 1.0  
**Date:** 2025-11-04  
**Classification:** System Requirements

## 1. REQUIREMENTS STRUCTURE

```
Level 0: System Requirements (Aircraft)
    ↓
Level 1: ATA Chapter Requirements (ATA 52 - Doors)
    ↓
Level 2: Section Requirements (52-20 Emergency Exits)
    ↓
Level 3: Component Requirements (52-20-01 Door L3 Aft)
    ↓
Level 4: Subsystem Requirements (Structure, Mechanism, etc.)
```

## 2. REQUIREMENT CATEGORIES

### 2.1 RQ-STRUCTURAL (001-019)
Ultimate strength, fatigue life, damage tolerance, environmental resistance

### 2.2 RQ-FUNCTIONAL (020-047)
Emergency opening, slide deployment, arming/disarming, manual override

### 2.3 RQ-PERFORMANCE (050-067)
Opening times, flow rates, reliability, weight limits

### 2.4 RQ-INTERFACE (070-091)
Physical mounting, system connections, data interfaces

### 2.5 RQ-SAFETY (100-134)
Evacuation capability, redundancy, failure tolerance, emergency lighting

### 2.6 RQ-OPERATIONAL (140-149)
Crew procedures, training, ground handling

### 2.7 RQ-MAINTENANCE (150-164)
Inspection intervals, test procedures, troubleshooting

### 2.8 RQ-CAOS (180-184)
Digital twin, predictive maintenance, fleet learning

## 3. REQUIREMENTS ALLOCATION

### 3.1 By Criticality

| Criticality | Count | Examples |
|------------|-------|----------|
| Critical | 45 | Emergency opening, slide deployment |
| High | 82 | Structural strength, interfaces |
| Medium | 48 | Maintenance, monitoring |
| Low | 10 | Optional features |

### 3.2 By Verification Method

| Method | Count | Percentage |
|--------|-------|------------|
| Test | 78 | 42% |
| Analysis | 52 | 28% |
| Inspection | 35 | 19% |
| Demonstration | 20 | 11% |

## 4. TRACEABILITY

### 4.1 Source Documents
- CS 25.807-813 (Emergency exits)
- ARP4761 (Safety assessment)
- TSO-C69c (Evacuation slides)
- AMPEL360 System Specification

### 4.2 Verification Links
- Test procedures → Requirements
- Analysis reports → Requirements
- Inspection records → Requirements

# Manual Override Requirements

**Calculation:** CALC-52-10-01-MEC-003  
**Date:** 2025-11-03  
**Revision:** A  
**Method:** Human Factors (AI-Assisted)  
**Confidence:** ±40%

## 1. REQUIREMENTS

### CS-25.807 & 25.809
```
- Emergency exit operable by anyone
- Single operation to open
- Marked clearly
- Force < 135 N (30 lbf)
- Time to open < 10 seconds
```

## 2. FAILURE SCENARIOS

### Scenario 1: Latch Failure
```
Manual release handle
Bypasses normal latch mechanism
Direct mechanical linkage
```

### Scenario 2: Power Loss
```
Manual operation always available
No electrical/hydraulic dependency
Spring return to safe position
```

### Scenario 3: Handle Jam
```
Alternate release (interior)
Break-away cover
Pull cable mechanism
```

## 3. MANUAL OVERRIDE DESIGN

### Interior Handle
```
Type: Pull handle (red)
Location: Mid-height on door
Force: 80 N (18 lbf)
Travel: 150 mm
Action: Disengages all latches
```

### Exterior Handle (Maintenance)
```
Type: Key-operated
Location: Lower panel
Requires tool/key
Not for emergency use
```

## 4. HUMAN FACTORS

### 5th Percentile Female
```
Strength: 130 N pull (95th percentile)
Reach: 1.5 m vertical
Handle size: 40 mm diameter
Status: Adequate for design ✓
```

### Emergency Lighting
```
Photoluminescent markings
Powered emergency lights
"EMERGENCY EXIT" visible
Instructions pictorial
```

## 5. VALIDATION REQUIRED

- [ ] Human factors testing (50+ subjects)
- [ ] Failure mode testing
- [ ] Dark/smoke conditions
- [ ] Various body types
- [ ] Time to egress measurement

---

**Status:** Design Defined  
**Risk:** HIGH - Safety Critical

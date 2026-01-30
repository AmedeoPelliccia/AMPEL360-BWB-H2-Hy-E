# 02-20-17-A-002: Weather Display and Alert Layouts

> **ID:** 02-20-17-A-002  
> **Title:** WIS User Interface Specifications  
> **Type:** Architecture Document  
> **Status:** DESIGN PHASE  

---

## 1. Purpose

This document defines the **user interface layouts** and **alert mechanisms** for weather information presentation across different operational contexts (EFB, Dispatch, Ground Operations).

---

## 2. EFB Weather Overlay

### 2.1 Moving Map Integration

**Display Elements:**
*   **Contrail Zones:** Red polygons indicating ISSR regions
*   **CO₂ Plumes:** Green heat map showing high-concentration areas
*   **Thermal Risk:** Orange icons at parking stands with temperature data
*   **Wind Barbs:** Standard aviation wind representation

**User Interactions:**
*   Toggle layers (contrail, CO₂, thermal)
*   Tap stand icon for detailed thermal forecast
*   Tap contrail zone for avoidance recommendations

### 2.2 Vertical Profile View

**Display:**
*   Altitude (FL) on Y-axis
*   Route distance on X-axis
*   Color-coded layers:
    *   Red: ISSR / Contrail Risk
    *   Green: Optimal cruise altitude
    *   Yellow: Marginal conditions

---

## 3. Dispatch Dashboard

### 3.1 Fleet Weather Summary

**Layout:**
```
┌─────────────────────────────────────────────────────┐
│  Fleet Weather Status          [Refresh: 15:23 UTC] │
├─────────────────────────────────────────────────────┤
│  Flight    Dep   Arr   Weather Impact   Status      │
│  AMPEL001  EDDF  LFPG  Contrail Risk    ⚠️ REVIEW   │
│  AMPEL002  EGLL  EDDM  Normal           ✅ CLEAR    │
│  AMPEL003  KJFK  EDDF  H2 Thermal Risk  🔴 ALERT    │
└─────────────────────────────────────────────────────┘
```

**Color Coding:**
*   Green ✅: No weather constraints
*   Yellow ⚠️: Advisory, manual review recommended
*   Red 🔴: Action required

### 3.2 Stand Thermal Monitor

**Widget:**
```
┌─────────────────────────────────────────┐
│  EDDF Stand Temperatures (°C)            │
├─────────────────────────────────────────┤
│  G45  [████████░░] 28.5  MEDIUM         │
│  G46  [██████████] 30.2  HIGH           │
│  H12  [█████░░░░░] 25.1  LOW            │
└─────────────────────────────────────────┘
```

---

## 4. Ground Operations Tablet

### 4.1 Turnaround Weather Panel

**Display:**
*   Current stand temperature (large font)
*   4-hour forecast graph
*   H₂ safe parking timer (countdown)
*   Recommended actions (shaded stand, GSE cooling)

**Example:**
```
┌────────────────────────────────────────┐
│  Stand G45 - AMPEL001                  │
│  Current Temp: 28.5°C                  │
│                                        │
│  Forecast:                             │
│    30°C │         ╱─                  │
│        │       ╱                      │
│    25°C │─────╱                       │
│         └──────────────────────       │
│         12:00  13:00  14:00  15:00    │
│                                        │
│  H₂ Safe Parking: 45 minutes           │
│  ⚠️ Recommendation: Use GSE Cooling    │
└────────────────────────────────────────┘
```

---

## 5. Alert Types & Severity

### 5.1 Alert Categories

| Category | Severity | Color | Action Required |
|:---|:---|:---|:---|
| **Contrail Risk** | ADVISORY | Yellow | Consider altitude change |
| **Contrail Risk** | HIGH | Red | Altitude change required |
| **Thermal Risk** | MEDIUM | Yellow | Monitor stand temperature |
| **Thermal Risk | HIGH** | Red | Relocate aircraft or activate cooling |
| **CO₂ Capture** | OPPORTUNITY | Green | Route adjustment available |
| **Data Quality** | CAUTION | Yellow | Weather data degraded |

### 5.2 Alert Delivery Mechanisms

**EFB:**
*   Pop-up notification (auto-dismiss after 10 seconds)
*   Persistent icon in status bar

**Dispatch:**
*   Email alert
*   SMS for critical alerts
*   Dashboard widget update

**Ground Ops:**
*   Push notification to tablet
*   Audio alert (configurable)

---

## 6. Notification Examples

### 6.1 Contrail Alert (In-Flight)

```
┌────────────────────────────────────────┐
│  ⚠️ CONTRAIL ALERT                     │
│                                        │
│  FL340 ISSR Detected                   │
│  Persistence: 45 minutes               │
│  Recommendation: Descend to FL320      │
│                                        │
│  [ACKNOWLEDGE]  [REQUEST CLEARANCE]    │
└────────────────────────────────────────┘
```

### 6.2 Thermal Alert (Ground)

```
┌────────────────────────────────────────┐
│  🔴 HIGH THERMAL RISK                  │
│                                        │
│  Stand G45 Temperature: 30.2°C         │
│  H₂ Safe Parking: 30 minutes remaining │
│                                        │
│  Action: Activate GSE Cooling          │
│                                        │
│  [ACTIVATE COOLING]  [RELOCATE]        │
└────────────────────────────────────────┘
```

### 6.3 CO₂ Capture Opportunity

```
┌────────────────────────────────────────┐
│  🟢 CO₂ CAPTURE OPPORTUNITY            │
│                                        │
│  High CO₂ zone detected downwind of    │
│  Frankfurt (50.11N/8.68E)              │
│                                        │
│  Estimated capture: +12.5 kg           │
│  Fuel penalty: +15 kg                  │
│                                        │
│  [ACCEPT ROUTE]  [DECLINE]             │
└────────────────────────────────────────┘
```

---

## 7. Data Visualization Standards

### 7.1 Color Palette

**Weather Severity:**
*   🟢 Green: Safe / Optimal
*   🟡 Yellow: Advisory / Marginal
*   🟠 Orange: Caution / Elevated Risk
*   🔴 Red: Critical / Action Required

**Temperature Scale:**
*   Blue: < 0°C
*   Green: 0-15°C
*   Yellow: 15-25°C
*   Orange: 25-30°C
*   Red: > 30°C

**CO₂ Concentration:**
*   Blue: < 400 ppm
*   Green: 400-415 ppm
*   Yellow: 415-425 ppm
*   Orange: > 425 ppm

### 7.2 Icon Library

*   ⛅ Cloud layers
*   💨 Wind barbs (standard aviation)
*   🌡️ Temperature
*   💧 Humidity / ISSR
*   🏭 Industrial emissions (CO₂ source)
*   ✈️ Aircraft position
*   🅿️ Parking stand

---

## 8. Accessibility Considerations

*   **Color Blind Mode:** Use patterns in addition to colors
*   **High Contrast:** Option for increased contrast
*   **Font Size:** Adjustable text size (accessibility settings)
*   **Audio Alerts:** Configurable for hearing-impaired users (visual-only mode)

---

## 9. Performance Requirements

*   **Refresh Rate:** 15 minutes (strategic), 5 minutes (tactical)
*   **Rendering Time:** < 2 seconds for full map update
*   **Touch Response:** < 100 ms (tap to detail view)

---

## 10. Related Documents

*   [02-20-17-001: System Overview](02-20-17-001_Weather_System_Overview.md)
*   [02-20-17-004: Operational Products](02-20-17-004_Operational_Weather_Products_for_Ops.md)
*   [02-20-17-A-001: System Architecture](02-20-17-A-001_Weather_System_Architecture.md)

---

## 11. Document Control
- Generated by: AI (prompted by Amedeo Pelliccia); pending approval by [Approver]

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---
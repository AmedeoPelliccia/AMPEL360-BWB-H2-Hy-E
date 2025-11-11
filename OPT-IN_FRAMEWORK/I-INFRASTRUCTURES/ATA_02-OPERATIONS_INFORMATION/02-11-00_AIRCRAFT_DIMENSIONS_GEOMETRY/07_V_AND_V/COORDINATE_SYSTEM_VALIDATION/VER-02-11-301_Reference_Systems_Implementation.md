# VER-02-11-301: Reference Systems Implementation Verification

**Verification ID:** VER-02-11-301  
**Component:** 02-11-00 Aircraft Dimensions Geometry  
**System:** Body Axis, Station, Buttline, Waterline Systems  
**Status:** Template Ready - Awaiting Verification

---

## 1. Objective

Verify correct implementation and consistent use of aircraft coordinate reference systems across all documentation, CAD models, and drawings:
- **Body Axis System:** X (forward), Y (starboard), Z (down)
- **Station (STA):** Longitudinal positions (m from nose datum)
- **Buttline (BL):** Lateral positions (m from centerline, + starboard)
- **Waterline (WL):** Vertical positions (m above ground reference)

---

## 2. Reference System Definitions

### 2.1 Body Axis System
| Axis | Direction | Positive | Origin |
|------|-----------|----------|--------|
| X | Longitudinal | Forward (nose direction) | Nose datum |
| Y | Lateral | Starboard (right) | Centerline |
| Z | Vertical | Downward | Ground reference |

**Convention:** Right-hand coordinate system (X × Y = Z)

### 2.2 Station (STA) System
- **STA 0:** Nose reference datum
- **Direction:** Increases aftward
- **Units:** Meters
- **Key Stations:** STA 3 (nose gear), STA 15 (center body max width), STA 18 (main gear), STA 36 (tail)

### 2.3 Buttline (BL) System
- **BL 0:** Aircraft centerline (plane of symmetry)
- **Direction:** Positive to starboard (right), negative to port (left)
- **Units:** Meters
- **Key Buttlines:** BL ±26 (wingtips), BL ±12 (engines), BL -6 (port passenger door)

### 2.4 Waterline (WL) System
- **WL 0:** Ground plane (landing gear extended)
- **Direction:** Positive upward
- **Units:** Meters
- **Key Waterlines:** WL 4.0 (cabin floor), WL 14.5 (aircraft top)

---

## 3. Verification Methods

### 3.1 CAD Model Audit
- Verify coordinate system origin and orientation in master CAD model
- Check that all part models use consistent coordinate system
- Validate assembly constraints preserve coordinate system

### 3.2 Drawing Review
- Audit sample of engineering drawings (minimum 10)
- Verify Station, Buttline, Waterline callouts are consistent
- Check that datum symbols match defined reference system

### 3.3 Data Table Cross-Check
- Review all CSV tables in 01_OVERVIEW/TABLES/
- Verify coordinate values match CAD model
- Check Station_Locations.csv for consistency

### 3.4 Physical Datum Verification
- Locate physical datum points on prototype/aircraft
- Verify markings match documentation
- Measure distances between datums for validation

---

## 4. Verification Checklist

### 4.1 CAD Model
- [ ] X-axis points forward (nose direction)
- [ ] Y-axis points starboard (right)
- [ ] Z-axis points downward (right-hand rule)
- [ ] Origin at nose datum (STA 0, BL 0, WL per convention)
- [ ] All assemblies use same coordinate system
- [ ] Part coordinates match documentation

### 4.2 Drawings
- [ ] Station callouts correct (0-36 m range expected)
- [ ] Buttline callouts correct (±26 m range expected)
- [ ] Waterline callouts correct (0-14.5 m range expected)
- [ ] Datum symbols properly placed
- [ ] Dimensioning consistent with coordinate system

### 4.3 Documentation
- [ ] baseline_dimensions.json uses correct conventions
- [ ] Principal_Dimensions_Table.csv coordinates consistent
- [ ] Station_Locations.csv matches CAD
- [ ] Critical_Clearances.csv coordinates correct
- [ ] All 02-11-00 documents use same system

---

## 5. Data Recording

### 5.1 Key Point Verification

| Feature | CAD (STA, BL, WL) | Drawing | Table | Physical | Status |
|---------|------------------|---------|-------|----------|--------|
| Nose Datum | TBD | TBD | TBD | TBD | TBD |
| Nose Gear | STA 3 | TBD | TBD | TBD | TBD |
| Center Max Width | STA 15, BL 0 | TBD | TBD | TBD | TBD |
| Main Gear | STA 18 | TBD | TBD | TBD | TBD |
| Left Wingtip | STA 20, BL -26 | TBD | TBD | TBD | TBD |
| Right Wingtip | STA 20, BL +26 | TBD | TBD | TBD | TBD |
| Aircraft Top | STA 15, BL 0, WL 14.5 | TBD | TBD | TBD | TBD |
| Cabin Floor | WL 4.0 | TBD | TBD | TBD | TBD |

### 5.2 Discrepancy Log

| Item | Source 1 | Value 1 | Source 2 | Value 2 | Discrepancy | Resolution | Status |
|------|----------|---------|----------|---------|-------------|------------|--------|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

---

## 6. Results Summary

### 6.1 Verification Status

| System | CAD | Drawings | Tables | Physical | Overall |
|--------|-----|----------|--------|----------|---------|
| Body Axis | TBD | TBD | TBD | TBD | TBD |
| Station | TBD | TBD | TBD | TBD | TBD |
| Buttline | TBD | TBD | TBD | TBD | TBD |
| Waterline | TBD | TBD | TBD | TBD | TBD |

**Verification Result:** [ ] PASS  [ ] FAIL  [ ] CONDITIONAL

**Justification:** TBD

---

## 7. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **CAD Manager** | TBD | | TBD |
| **Drawing Control** | TBD | | TBD |
| **Configuration Manager** | TBD | | TBD |

---

## 8. Traceability

- REQ-02-11-019: Reference system implementation requirements
- REQ-02-11-020: Coordinate system consistency
- Related: VER-02-11-302 (Consistency Check)

---

**Revision:** 1.0 | **Date:** 2025-11-11 | **Author:** COPILOT Agent prompted by Amedeo Pelliccia

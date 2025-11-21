# 02-50-01-005: Installation Procedures

## Document Information

- **Document ID**: 02-50-01-005
- **Version**: 1.0.0
- **Status**: DRAFT
- **Date**: 2025-11-21

## 1. Purpose

Provides step-by-step installation and removal procedures for EFB mounts including required tooling, torque values, and safety notes.

## 2. Scope

Applies to:
- Initial installation during aircraft production
- Removal and replacement during maintenance
- Retrofit installation (if applicable)

## 3. Safety Precautions

### 3.1 General Safety

- ⚠️ Wear safety glasses and cut-resistant gloves when handling aluminum parts
- ⚠️ Use calibrated torque wrench (calibration within 12 months)
- ⚠️ Ensure work area is well-lit and free from trip hazards
- ⚠️ Verify aircraft electrical power is OFF before installation

### 3.2 Environmental Limits

Perform installation only when:
- Temperature: 15-30°C (optimal for thread lubricant curing)
- Humidity: < 70% RH (non-condensing)
- Clean, dust-free environment (prevent contamination of threaded inserts)

## 4. Required Tools and Materials

### 4.1 Tools

| Tool | Specification | Quantity |
|------|--------------|----------|
| Torque wrench | 0-25 Nm range, ±2% accuracy | 1 |
| Hex key set | 3mm, 4mm, 5mm | 1 set |
| Allen wrench | 5mm (for M6 socket head bolts) | 1 |
| Cleaning cloth | Lint-free, IPA-compatible | 5 |
| Flashlight | For inspection | 1 |
| Calipers | Digital, 0.01mm resolution | 1 |

### 4.2 Materials

| Material | Part Number | Quantity per Mount |
|----------|-------------|-------------------|
| EFB mount assembly | PILOT-EFB-01 or COPILOT-EFB-01 | 1 |
| M6×20mm socket head bolt | MS20004-6-20 | 4 |
| M6 flat washer | MS20002-6 | 4 |
| Dry film lubricant | MoS₂ paste | 1 tube |
| Isopropyl alcohol (IPA) | 99% | 500 ml |
| Witness mark paint | Yellow or red (permanent marker acceptable) | 1 |

## 5. Pre-Installation Inspection

### 5.1 Verify Parts

- [ ] Check part number matches work order (PILOT-EFB-01 for left side, COPILOT-EFB-01 for right)
- [ ] Inspect mount for damage: no cracks, dents, or corrosion
- [ ] Verify serial number is recorded in aircraft logbook
- [ ] Check fasteners for correct length and thread condition

### 5.2 Panel Inspection

- [ ] Verify 4× M6 threaded inserts are present and undamaged
- [ ] Check thread engagement: Use M6 bolt to verify threads engage smoothly for at least 10mm
- [ ] Inspect panel surface: Clean, no paint chips or contamination around insert area
- [ ] Measure hard point locations: Verify 100mm × 80mm bolt pattern per drawing

## 6. Installation Procedure

### 6.1 Panel Preparation

1. **Clean panel surface**
   - Wipe with IPA-soaked cloth around mounting area
   - Remove dust, grease, or fingerprints
   - Allow to air dry (30 seconds)

2. **Prepare threaded inserts**
   - Clean threads with IPA and small brush
   - Blow out with compressed air (30 psi, clean/dry)
   - Inspect for damage or contamination

### 6.2 Mount Installation

**Step 1**: Apply lubricant to fasteners
   - Apply thin coat of dry film lubricant (MoS₂) to M6 bolt threads
   - Do NOT apply to first 2-3 threads (prevents contamination of insert)

**Step 2**: Position mount
   - Hold mount against panel, align 4× mounting holes with inserts
   - Verify mount orientation: "TOP" marking on mount base points up, "LEFT" or "RIGHT" marking visible
   - Insert one bolt by hand, engage threads (should turn smoothly)

**Step 3**: Install washers and fasteners
   - Place M6 washer under bolt head
   - Install all 4× bolts finger-tight
   - Check mount alignment: Measure parallelism to panel edge (±2mm acceptable)

**Step 4**: Torque fasteners
   - Torque in cross pattern (diagonal sequence: bolt 1, then 3, then 2, then 4)
   - **First pass**: Torque to 5 Nm (50% of final torque)
   - **Second pass**: Torque to 7.5 Nm (75% of final torque)
   - **Final pass**: Torque to **10 Nm ± 1 Nm**
   - Verify torque wrench "clicks" or displays target value

**Step 5**: Apply witness marks
   - Use paint or marker to mark bolt head and adjacent panel surface
   - Mark should be continuous across bolt and panel (detects loosening)
   - Allow paint to dry (5 minutes)

### 6.3 Ground Bonding Verification

**Step 1**: Measure resistance
   - Use low-resistance ohmmeter (4-wire Kelvin measurement preferred)
   - Measure resistance from mount base to aircraft ground point
   - **Acceptance**: < 0.001 Ω (direct metal-to-metal contact)

**Step 2**: If resistance too high
   - Remove mount, inspect panel surface and mount base
   - Remove anodize coating at contact points (fine abrasive pad)
   - Apply conductive grease (zinc chromate paste)
   - Re-install and re-measure

## 7. Post-Installation Checks

### 7.1 Visual Inspection

- [ ] All 4× fasteners installed with washers
- [ ] Witness marks applied and visible
- [ ] Mount is flush against panel (no gaps)
- [ ] No cracks or damage to mount or panel
- [ ] Clearances to adjacent components verified (minimum 50mm)

### 7.2 Functional Check

- [ ] Articulate mount through full range of motion (±30° tilt, ±15° rotate)
- [ ] Verify friction hold: Mount stays in position when released
- [ ] Check device cradle: Opens and closes smoothly, spring-loaded corners functional
- [ ] Test quick-release button: Operates with moderate finger pressure

### 7.3 Documentation

- [ ] Record serial number in aircraft logbook
- [ ] Photograph installed mount (for as-built records)
- [ ] Complete installation record with torque values and resistance measurement
- [ ] Sign and date installation record

## 8. Removal Procedure

### 8.1 Removal Steps

**Step 1**: Stow mount
   - Fold mount to stowed position (minimum profile)
   - Ensure no EFB device is installed

**Step 2**: Remove fasteners
   - Loosen M6 bolts in reverse sequence (4, 2, 3, 1)
   - Collect washers and bolts, inspect for damage or corrosion

**Step 3**: Remove mount
   - Gently pull mount away from panel
   - Inspect panel threaded inserts for damage

### 8.2 Post-Removal Inspection

- [ ] Inspect mount for cracks or permanent deformation
- [ ] Check fasteners: Threads in good condition, no stretched shanks
- [ ] Inspect panel inserts: Clean threads, no pull-out or damage
- [ ] Clean panel surface with IPA

**Disposition**:
- If mount is undamaged: Tag for re-use or send to stores
- If mount is damaged: Quarantine and submit for engineering evaluation
- If inserts damaged: Notify structures team for panel repair

## 9. Troubleshooting

### 9.1 Common Issues

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Bolt won't engage threads | Cross-threaded or damaged insert | Stop! Inspect insert, use thread chaser to clean |
| Torque wrench slips | Incorrect socket size or worn fastener | Verify 5mm hex key fits snugly, replace fastener if worn |
| Resistance > 0.001 Ω | Anodize coating preventing contact | Remove mount, abrade contact surfaces, apply conductive grease |
| Mount won't articulate smoothly | Pivot bushings dry or contaminated | Apply small amount of dry lube to pivot pins |

### 9.2 When to Stop and Escalate

⛔ **STOP work and notify engineering if**:
- Fastener breaks or strips during installation
- Panel cracks or deforms during torquing
- Threaded insert pulls out of panel
- Mount shows signs of prior damage not noted in pre-installation inspection

## 10. Training and Certification

### 10.1 Installer Qualifications

Installers must:
- Hold A&P (Airframe & Powerplant) license or equivalent
- Complete AMPEL360 aircraft familiarization training
- Demonstrate proficiency in torque wrench use

### 10.2 Quality Inspector Sign-Off

Final installation must be inspected and signed off by:
- Quality inspector (Level II minimum)
- Structures lead (for first-time installations or rework)

## 11. Related Documents

- [02-50-01-001_EFB_Mount_Design.md](./02-50-01-001_EFB_Mount_Design.md) — Design specifications
- [02-50-01-002_Cockpit_Integration.md](./02-50-01-002_Cockpit_Integration.md) — Attachment point locations
- [02-50-00-003_Installation_Standards.md](../02-50-00-003_Installation_Standards.md) — General installation standards

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** — Subject to human review and approval.
- Human approver: *[to be completed]*.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: *2025-11-21*.

---

# ATA 02 - Operations Information
## Document Conventions

**Document ID:** AMPEL360-02-00-00-OVR-DC  
**Version:** 1.0.0  
**Date:** 2025-11-04  
**Classification:** Operations Critical

---

## 1. PURPOSE

This document establishes writing and formatting standards for all AMPEL360 operational documentation, ensuring consistency, clarity, and safety.

**Related Documents:**
- [Definitions_Terminology.md](Definitions_Terminology.md) - Standard terminology
- [Abbreviations_Acronyms.md](Abbreviations_Acronyms.md) - Approved abbreviations
- [Units_Measurement.md](Units_Measurement.md) - Unit standards
- [Revision_Control.md](Revision_Control.md) - Revision marking procedures

---

## 2. WRITING STYLE

### 2.1 General Principles

- **Clear and Concise:** No unnecessary words
- **Active Voice:** "Turn the switch" not "The switch should be turned"
- **Imperative Mood:** Commands, not suggestions
- **Present Tense:** "The system operates" not "The system will operate"
- **Consistent Terminology:** Use standard definitions (see [Definitions_Terminology.md](Definitions_Terminology.md))

### 2.2 Sentence Structure

**Good Examples:**
- "Press the START button."
- "Verify fuel quantity indication."
- "Monitor fuel cell temperature."

**Avoid:**
- "The START button should be pressed." (Passive)
- "You might want to check fuel." (Uncertain)
- "The temperature will be monitored." (Future/passive)

### 2.3 Paragraph Structure

- **One topic per paragraph**
- **Topic sentence first**
- **Supporting details follow**
- **Maximum 5-6 sentences**
- **Blank line between paragraphs**

---

## 3. FORMATTING STANDARDS

### 3.1 Document Header

**Every document must include:**
```
# Document Title

**Document ID:** AMPEL360-XX-YY-ZZ-AAA
**Version:** X.Y.Z
**Date:** YYYY-MM-DD
**Classification:** [Level]
```

### 3.2 Headings

**Hierarchy:**
- `# Level 1` - Document title
- `## Level 2` - Major sections
- `### Level 3` - Subsections
- `#### Level 4` - Sub-subsections (use sparingly)

**Numbering:**
- Use consistent numbering: 1, 1.1, 1.1.1
- No more than 3 levels deep typically

### 3.3 Lists

**Ordered (Numbered) Lists:**
Use for sequential procedures or prioritized items
```
1. First action
2. Second action
3. Third action
```

**Unordered (Bulleted) Lists:**
Use for non-sequential items
```
- Item one
- Item two
- Item three
```

**Definition Lists:**
```
**Term:** Definition text
**Another Term:** More definition text
```

### 3.4 Tables

**Standard Table Format:**
```
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
| Data     | Data     | Data     |
```

**Table Guidelines:**
- Headers in bold
- Align text left, numbers right
- Include units in headers
- Keep tables simple (max 6 columns)

---

## 4. SAFETY ANNOTATIONS

### 4.1 Warning

**Usage:** Indicates hazard that could result in death or serious injury

**Format:**
```
⚠ WARNING
Procedure or condition that could result in death or serious injury if not followed.
```

**Example:**
```
⚠ WARNING
High voltage present. Do not open panel with power applied. Risk of electrocution.
```

### 4.2 Caution

**Usage:** Indicates hazard that could result in minor injury or equipment damage

**Format:**
```
⚠ CAUTION
Procedure or condition that could result in injury or equipment damage if not followed.
```

**Example:**
```
⚠ CAUTION
Do not exceed 85°C fuel cell temperature. Exceeding limit may damage fuel cell stack.
```

### 4.3 Note

**Usage:** Provides additional information or clarification

**Format:**
```
ℹ NOTE
Additional information for emphasis or clarification.
```

**Example:**
```
ℹ NOTE
CAOS automatically monitors fuel cell temperature and provides alerts.
```

### 4.4 Safety Annotation Placement

- Place **before** the step or section it applies to
- Never bury in middle of paragraph
- Make visually distinct (box, background color)
- Use sparingly - too many reduce effectiveness

---

## 5. PROCEDURAL FORMATTING

### 5.1 Standard Procedure Format

```
PROCEDURE: [Title]

CONDITIONS:
- [Prerequisites]
- [Required equipment]

STEPS:
1. [Action] → [Expected result]
2. [Action] → [Expected result]
   a. [Sub-action]
   b. [Sub-action]
3. [Action] → [Expected result]

VERIFICATION:
✓ [Check item]
✓ [Check item]

NOTES:
- [Additional information]
```

### 5.2 Procedure Steps

**Each step should include:**
- **Action:** What to do
- **Object:** What to act upon
- **Expected Result:** What should happen

**Example:**
```
1. Press H2 REFUEL button on panel P5 → GREEN light illuminates
2. Verify REFUEL READY indication → Message displays on EICAS
3. Connect refueling hose → Click heard, CONNECTED annunciation
```

### 5.3 Sub-steps

**When to use:**
- Multiple actions for one verification
- Choices or alternatives
- Detailed breakdown needed

**Format:**
```
1. Configure H2 system:
   a. H2 MASTER switch → ON
   b. H2 PUMPS → AUTO
   c. H2 ISOLATION → OPEN
   → All green indications verified
```

### 5.4 Conditional Steps

**Format:**
```
1. Check fuel quantity:
   IF fuel > 7,000 kg:
     → Proceed to Step 2
   IF fuel < 7,000 kg:
     → Refuel per 02-32-03
     → Then proceed to Step 2
```

---

## 6. NUMBERING AND IDENTIFICATION

### 6.1 Component Identification

**Format:**
- **Panels:** P1, P2, P3, etc.
- **Switches:** Use actual labels (e.g., "H2 MASTER switch")
- **Buttons:** Use actual labels (e.g., "START button")
- **Displays:** Use system name (e.g., "EICAS", "PFD", "MFD")

**Example:**
"Press START button on panel P5"

### 6.2 System References

**Format:**
- Use ATA number: "See Section 02-32-03"
- Use system name: "H2 fuel system"
- Use formal name first mention, then abbreviation

**Example:**
"The Hydrogen Fuel System (H2 system) provides..."
Then: "The H2 system monitors..."

---

## 7. GRAPHICS AND ILLUSTRATIONS

### 7.1 Figure Numbering

**Format:** `Figure X-Y: Description`
- X = Section number
- Y = Sequential in section

**Example:**
```
Figure 2-1: H2 Refueling Connection Point
Figure 2-2: Fuel Cell Stack Configuration
```

### 7.2 Figure Placement

- Place as close as possible to reference text
- Include figure number and caption
- Reference in text: "See Figure 2-1"
- Never orphan (figure on different page from reference)

### 7.3 Figure Quality

- Minimum 300 dpi resolution
- Clear labels and callouts
- Consistent style across document
- SVG format preferred for diagrams
- PNG for photos, JPEG avoided

### 7.4 Callouts and Labels

- Use arrow or leader line
- Label text horizontal (readable without rotating)
- Font size readable when printed
- Consistent label style

---

## 8. CROSS-REFERENCES

### 8.1 Internal References

**Within Same Document:**
"See Section 3.2 for details"

**Within ATA 02:**
"Refer to Section 02-32-03 for refueling procedures"

**To Other ATA Chapters:**
"For fuel system description, see ATA 28-00-00"

### 8.2 External References

**Regulatory:**
"As required by EASA CS-25.1583"

**Manufacturer:**
"Per Boeing Service Bulletin 737-28-1234" (example format)

**Standards:**
"In accordance with ISO 19881"

---

## 9. ABBREVIATIONS AND ACRONYMS

### 9.1 First Use

**Format:** Full term (Abbreviation)

**Example:**
"The Cosmic Advanced Optimization System (CAOS) provides..."

Then: "CAOS monitors fuel consumption..."

### 9.2 Standard Abbreviations

- See Abbreviations_Acronyms.md for approved list
- Do not create new abbreviations without approval
- Commonly known terms (e.g., ATC, ILS) can be used without defining

---

## 10. UNITS OF MEASUREMENT

### 10.1 Primary Units

- Use SI units as primary
- Provide conversions in parentheses when needed

**Example:**
"Maximum altitude: FL450 (13,716 m)"

### 10.2 Consistency

- Use same unit throughout section
- Include unit with every number
- Space between number and unit

**Example:**
- Correct: "8,000 kg H2"
- Incorrect: "8,000kg H2" or "8000 kg H2" (no space, no comma)

---

## 11. NUMBERS AND QUANTITIES

### 11.1 Number Format

**General Rule:**
- Spell out: Zero through nine
- Numerals: 10 and above
- Exception: Technical data always numerals

**Examples:**
- "Three fuel cell stacks" (general)
- "4 × 2.5 MW fuel cell stacks" (technical)

### 11.2 Large Numbers

**Use commas for thousands:**
- 8,000 kg
- 45,000 ft
- 1,000,000 parameters

### 11.3 Decimals

**Use decimal point (period):**
- 2.5 MW
- 0.3% boil-off
- 15.5 m MAC

### 11.4 Ranges

**Use en-dash or hyphen:**
- 60-80°C
- FL390-FL430
- 50-80 kg/h

---

## 12. DATES AND TIMES

### 12.1 Date Format

**Standard:** YYYY-MM-DD (ISO 8601)

**Examples:**
- 2025-11-04
- 2029-01-01

### 12.2 Time Format

**24-hour format:** HH:MM

**Examples:**
- 14:30
- 06:45

**Duration:**
- 45 minutes or 45 min
- 3 hours or 3 hrs
- 3 seconds or 3 sec

---

## 13. REVISION MARKING

### 13.1 Change Indicators

**Black Triangle (▶):** Indicates new or changed text

**Placement:**
- Left margin for added/changed paragraphs
- Before and after for inline changes

**Example:**
```
▶ This paragraph has been revised to include new H2 safety procedures.
```

### 13.2 Effective Dates

**Include with revision:**
"Effective: 2025-11-04"

**Superseded statement:**
"Supersedes: Version 1.0.0 dated 2025-10-01"

---

## 14. DOCUMENT FOOTER

### 14.1 Standard Footer

**Every page should include:**
```
Document ID: AMPEL360-02-XX-YY-ZZZ
Version: X.Y.Z
Page X of Y
Confidential/Proprietary (if applicable)
```

### 14.2 Final Page Footer

**Last page includes:**
```
**Document Status:** ✅ RELEASED
**Effective Date:** 2029-01-01
**Next Review:** 2026-11-04
**Configuration Control:** Git SHA-256: [hash]
```

---

## 15. CHECKLISTS

### 15.1 Normal Checklist Format

```
CHECKLIST: [Title]

Item 1 ................................................ CHECK
Item 2 ................................................ SET
Item 3 ................................................ ON
Item 4 ................................................ VERIFY
```

### 15.2 Emergency Checklist Format

```
EMERGENCY: [Title]

IMMEDIATE ACTIONS (Memory Items):
1. [Action] ................................... [Position]
2. [Action] ................................... [Position]

SUBSEQUENT ACTIONS (After QRH):
3. [Action] ................................... [Position]
4. [Action] ................................... [Verify]
```

---

## 16. SPECIAL FORMATTING

### 16.1 Code Blocks

**For system displays, CAOS output, etc.:**
```
┌────────────────────────────────────┐
│ CAOS RECOMMENDATION                │
├────────────────────────────────────┤
│ Climb to FL410                     │
│ Fuel savings: 85 kg (3%)           │
└────────────────────────────────────┘
```

### 16.2 Emphasis

- **Bold:** For emphasis, labels, headers
- *Italic:* For technical terms first use, notes
- `Monospace:` For system displays, code

**Avoid:**
- CAPITALS FOR EMPHASIS (use bold)
- Underline (reserve for hyperlinks)
- Multiple exclamation points!!!

---

## 17. ACCESSIBILITY

### 17.1 Text

- Minimum font size: 11pt
- High contrast text
- Clear, readable fonts (Arial, Helvetica)

### 17.2 Graphics

- Include alt text descriptions
- Don't rely on color alone
- Use patterns in addition to colors

---

## 18. ELECTRONIC VS. PRINT

### 18.1 Electronic (EFB, Web)

- Include hyperlinks for cross-references
- Interactive elements (expandable sections)
- Color for emphasis (warnings/cautions/notes)

### 18.2 Print

- Ensure print-friendly formatting
- Black & white compatible
- Page breaks appropriate
- Headers/footers on all pages

---

## 19. QUALITY CHECKLIST

Before releasing document, verify:

- [ ] Header complete and correct
- [ ] Spelling and grammar checked
- [ ] Technical accuracy reviewed
- [ ] Cross-references verified
- [ ] Figures numbered and referenced
- [ ] Safety annotations appropriate
- [ ] Units consistent
- [ ] Abbreviations defined
- [ ] Revision marks (if applicable)
- [ ] Footer complete

---

## 20. CONTACT INFORMATION

**Document Standards:**
- Email: doc-standards@ampel360.aero
- Phone: +34 91 XXX XXXX

**Technical Publications:**
- Email: tech-pubs@ampel360.aero
- Phone: +34 91 XXX XXXX (24/7)

---

**Document Status:** ✅ RELEASED
**Effective Date:** 2029-01-01
**Next Review:** 2026-11-04
**Configuration Control:** Git SHA-256: [hash]

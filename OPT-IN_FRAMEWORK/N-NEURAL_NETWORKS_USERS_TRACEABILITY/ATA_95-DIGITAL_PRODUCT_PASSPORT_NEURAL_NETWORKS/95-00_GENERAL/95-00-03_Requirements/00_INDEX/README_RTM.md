# Requirements Traceability Matrix (RTM)

## Purpose

The RTM (`95-00-03-RTM_DPP_Requirements.xlsx`) provides comprehensive traceability between:
- Requirements and their sources (regulations, standards)
- Requirements and design specifications
- Requirements and implementation artifacts
- Requirements and test cases
- Requirements and certification evidence

## Structure

The RTM Excel workbook contains the following sheets:

### Sheet 1: Full Traceability Matrix

| Column | Description |
|--------|-------------|
| **Requirement ID** | Unique identifier (e.g., RQ-95-00-03-001) |
| **Title** | Short descriptive title |
| **Category** | Requirement category (Functional, Non-Functional, etc.) |
| **Status** | Current lifecycle state (DRAFT, FOR_REVIEW, APPROVED, etc.) |
| **Priority** | Critical, High, Medium, Low |
| **Source Document** | Originating requirement or regulation |
| **Design Reference** | Link to design specification (95-00-04_Design) |
| **Implementation Reference** | Link to code, configuration, or implementation artifact |
| **Test Case(s)** | Link to test cases (TC-95-00-03-XXX) |
| **Certification Evidence** | Link to means of compliance (MoC-95-00-03-XXX) |
| **DPP JSON Field(s)** | Corresponding fields in DPP schema |
| **Owner** | Responsible working group |
| **Last Updated** | Date of last modification |

### Sheet 2: Requirements by Category

Pivot view grouping requirements by category with counts and status summaries.

### Sheet 3: Requirements by Status

Pivot view showing requirements lifecycle distribution.

### Sheet 4: Verification Coverage

Cross-reference showing which requirements have:
- ✅ Design specification
- ✅ Implementation
- ✅ Test case
- ✅ Certification evidence

### Sheet 5: Source to Requirement Mapping

Trace from source documents (EU AI Act, EU DPP, aviation standards) to specific requirements.

---

## File Location

**Planned location**: `95-00-03-RTM_DPP_Requirements.xlsx`

**Current status**: Template to be created

**Format**: Microsoft Excel (.xlsx)

---

## Usage

### For Requirements Engineers

1. Open the RTM to see the full traceability landscape
2. Use filters to find requirements by category, status, or owner
3. Update traceability links when creating or modifying requirements

### For Designers

1. Review "Design Reference" column to see which requirements need design artifacts
2. Update links when creating design specifications

### For Testers

1. Use "Test Case(s)" column to identify coverage gaps
2. Create test cases for requirements without coverage
3. Link test results back to requirements

### For Certification

1. Review "Certification Evidence" column to track compliance status
2. Collect evidence packages for certification submissions

---

## Maintenance

- **Frequency**: Updated after each requirement change
- **Responsibility**: Requirements WG
- **Automation**: Can be auto-generated from scanning `RQ-*.md` files and extracting traceability sections

---

## Document Control

- **Document ID**: 95-00-03-RTM-README
- **Version**: 1.0
- **Status**: APPROVED
- **Last Updated**: 2025-11-17
- **Owner**: AMPEL360 Requirements WG

---

**Note**: The actual RTM Excel file will be created in a future iteration. This README documents its intended structure and usage.

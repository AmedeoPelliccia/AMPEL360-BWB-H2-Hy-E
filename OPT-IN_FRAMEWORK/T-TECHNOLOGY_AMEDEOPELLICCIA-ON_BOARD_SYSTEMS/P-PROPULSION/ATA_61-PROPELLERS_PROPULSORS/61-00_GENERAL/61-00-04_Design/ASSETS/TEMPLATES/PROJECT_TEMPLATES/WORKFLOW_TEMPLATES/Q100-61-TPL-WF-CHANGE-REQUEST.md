# Change Request Workflow

<!-- Template ID: Q100-61-TPL-WF-CHANGE-REQUEST -->

## Workflow Overview

This workflow defines the process for engineering change requests.

---

## Process Flow

```
┌─────────────────┐
│ 1. REQUEST      │
│   Initiator     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. EVALUATE     │
│   CCB Secretary │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. ANALYZE      │
│   Engineering   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. CCB REVIEW   │
│   Change Board  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────┐
│APPROVE│ │REJECT │
└───┬───┘ └───────┘
    │
    ▼
┌─────────────────┐
│ 5. IMPLEMENT    │
│   Engineering   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 6. VERIFY       │
│   QA            │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 7. CLOSE        │
│   CCB Secretary │
└─────────────────┘
```

---

## Stage Details

### Stage 1: Request

**Form Fields:**
- [ ] Change title
- [ ] Description of change
- [ ] Reason / justification
- [ ] Affected items
- [ ] Requested effectivity

---

### Stage 2: Evaluate

**Criteria:**
- [ ] Complete request
- [ ] Valid justification
- [ ] Not duplicate
- [ ] Proper classification

**Classification:**
| Class | Description |
|-------|-------------|
| Class I | Major change affecting form/fit/function |
| Class II | Minor change, no impact |

---

### Stage 3: Analyze

**Analysis Required:**
- [ ] Impact assessment
- [ ] Cost estimate
- [ ] Schedule impact
- [ ] Risk assessment
- [ ] Implementation plan

---

### Stage 4: CCB Review

**Decision Options:**
- **Approve** — Proceed with implementation
- **Approve with conditions** — Proceed with modifications
- **Defer** — Postpone decision
- **Reject** — Do not implement

---

### Stage 5: Implement

**Actions:**
1. Update design data
2. Revise documentation
3. Update affected systems
4. Record as-built data

---

### Stage 6: Verify

**Verification:**
- [ ] Changes implemented correctly
- [ ] Documentation updated
- [ ] Testing complete (if required)
- [ ] Traceability maintained

---

### Stage 7: Close

**Actions:**
1. Update change status
2. Archive records
3. Notify stakeholders
4. Lessons learned

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-12-05_.

---

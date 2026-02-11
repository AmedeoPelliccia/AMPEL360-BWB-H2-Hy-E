# Digital Constitution Quick Reference Card

**For AMPEL360 Contributors**

---

## 🎯 Core Principle

> **Labor is the creative and operational foundation.**
> Technology amplifies human capability; it does not displace human contribution.

---

## ✅ Before Submitting a PR

### Ask Yourself:

1. **Does this PR introduce automation?**
   - If YES → Complete LABOR-REABSORPTION section
   - Calculate: `net_displacement = FTE_displaced - FTE_reabsorbed`
   - ⚠️ If net > 0, governance override required

2. **Does this PR involve AI/ML?**
   - If YES → Complete HARM-PRECEDENCE section
   - Set confidence thresholds ≥ 0.95 (safety), 0.92 (operational), 0.85 (informational)
   - Name a specific person (not "queue") for escalation
   - Document rollback procedure (must be ≤ 4 hours)

3. **Can changes be rolled back within 4 hours?**
   - If NO → Redesign for reversibility

4. **Are decisions documented with rationale?**
   - If NO → Add documentation explaining decision logic

---

## 📋 PR Template Sections

### Labor Reabsorption (if applicable)

```yaml
LABOR-REABSORPTION:
  applicable: yes/no
  roles_displaced:
    - role: "..."
      fte_equivalent: X.X
      description: "..."
  reabsorption_pathway:
    - new_role: "..."
      fte_equivalent: X.X
      transition_plan: "..."
  net_displacement: 0.0  # Must be ≤ 0
```

### Harm Precedence (if applicable)

```yaml
HARM-PRECEDENCE:
  applicable: yes/no
  model_outputs:
    - confidence_threshold: 0.XX  # ≥ 0.95/0.92/0.85
      responsible_role: "Name, not queue"
      response_sla_hours: X
  reversibility:
    estimated_rollback_hours: X  # ≤ 4
```

---

## 🔧 Local Validation

### Setup Git Hooks (First Time)

```bash
bash .github/hooks/setup-hooks.sh
```

### Test Your Changes

```bash
# Validate labor reabsorption data
python3 tools/constitutional_validator.py validate-labor my_labor_data.yaml

# Validate harm precedence config
python3 tools/constitutional_validator.py validate-harm my_harm_data.yaml

# Compute constitutional hash
python3 tools/constitutional_validator.py hash
```

---

## 🚫 What Gets Blocked

❌ **Net labor displacement > 0 without governance override**
❌ **AI confidence thresholds below constitutional minimums**
❌ **Rollback procedures > 4 hours**
❌ **Anonymous escalation queues (must be named roles)**
❌ **Silent constitutional modifications**

---

## 📊 Quarterly Responsibilities

- Update `GOVERNANCE_METRICS.md` (every 90 days)
- Conduct reversibility drill
- Review contributor role diversity
- Update labor reabsorption cumulative stats

---

## 🆘 Getting Help

- **Read:** [GOVERNANCE.md](../GOVERNANCE.md)
- **Integration Guide:** [CONSTITUTIONAL_INTEGRATION_GUIDE.md](../CONSTITUTIONAL_INTEGRATION_GUIDE.md)
- **Examples:** [examples/constitutional/](../examples/constitutional/)
- **Validator Help:** `python3 tools/constitutional_validator.py --help`

---

## 🎓 Constitutional Compliance Checklist

Before submitting PR:

- [ ] I have read GOVERNANCE.md
- [ ] Labor reabsorption assessed (if applicable)
- [ ] Harm precedence mechanisms in place (if applicable)
- [ ] Changes are reversible within 4 hours
- [ ] Decisions have documented rationale
- [ ] Constitutional attestation signed
- [ ] No silent labor displacement

---

## 🔑 Key Numbers

| Threshold | Value | Applies To |
|-----------|-------|------------|
| **Confidence (Safety Critical)** | ≥ 0.95 | AI/ML safety decisions |
| **Confidence (Operational)** | ≥ 0.92 | AI/ML operational decisions |
| **Confidence (Informational)** | ≥ 0.85 | AI/ML informational outputs |
| **Rollback Time** | ≤ 4 hours | All automated decisions |
| **Net Displacement** | ≤ 0 FTE | All process changes |
| **Dashboard Update** | Every 90 days | Metrics tracking |

---

## ⚖️ Conflict Resolution

**If capital demands conflict with labor foundation:**

**Option A:** Explicit steward override (documented in commit)
**Option B:** Capital withdrawal

**Prohibited:** Silent override

---

*Print this card and keep it handy!*
*Constitutional Version: 1.0 | Last Updated: 2026-02-11*

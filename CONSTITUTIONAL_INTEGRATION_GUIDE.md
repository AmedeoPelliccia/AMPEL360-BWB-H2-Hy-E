# AMPEL360 Digital Constitution — Integration Guide

**Version:** 1.0  
**Last Updated:** 2026-02-11  
**Audience:** Developers, Contributors, System Integrators

---

## Overview

This guide explains how the AMPEL360 Digital Constitution is **operationalized** through technical enforcement mechanisms. This is not aspirational governance—it's **executable policy** embedded in the repository's development workflow.

---

## Quick Start

### For New Contributors

1. **Read the Constitution**: [GOVERNANCE.md](../GOVERNANCE.md)
2. **Setup Git Hooks**: `bash .github/hooks/setup-hooks.sh`
3. **Review PR Template**: [.github/PULL_REQUEST_TEMPLATE.md](../.github/PULL_REQUEST_TEMPLATE.md)
4. **Check Examples**: [examples/constitutional/](../examples/constitutional/)

### For Existing Projects Adopting This Framework

1. Copy these files to your repository:
   - `GOVERNANCE.md` (customize for your context)
   - `.constitution.yaml` (adjust thresholds as needed)
   - `.github/PULL_REQUEST_TEMPLATE.md`
   - `.github/hooks/constitutional-check`
   - `.github/workflows/constitutional-validation.yml`
   - `tools/constitutional_validator.py`

2. Compute your constitutional hash:
   ```bash
   python3 tools/constitutional_validator.py hash --update
   ```

3. Update documentation to reference governance framework

---

## Enforcement Mechanisms

### 1. Pre-Commit Hooks

**File:** `.github/hooks/constitutional-check`

**Purpose:** Lightweight validation at commit time to catch potential constitutional issues early.

**Checks:**
- Detects automation-related changes that may displace labor
- Verifies constitutional metadata in model/config files
- Flags unauthorized modifications to constitutional files
- Validates AI/ML code for safety mechanisms
- Checks for documented decision rationale

**Installation:**
```bash
bash .github/hooks/setup-hooks.sh
```

**Bypass (not recommended):**
```bash
git commit --no-verify
```

### 2. CI/CD Validation

**File:** `.github/workflows/constitutional-validation.yml`

**Purpose:** Comprehensive validation during PR review process.

**Checks:**
- PR template completeness (labor reabsorption, harm precedence sections)
- Net displacement calculations
- Metrics dashboard currency (quarterly updates)
- SPDX license headers on new files
- Constitutional file change governance

**Triggered on:**
- Pull request opened/updated
- Push to main/develop branches

### 3. Python Validation Tool

**File:** `tools/constitutional_validator.py`

**Purpose:** Programmatic validation of constitutional compliance data.

**Commands:**

```bash
# Compute constitutional hash
python3 tools/constitutional_validator.py hash

# Update hash in .constitution.yaml
python3 tools/constitutional_validator.py hash --update

# Validate labor reabsorption data
python3 tools/constitutional_validator.py validate-labor <file.yaml>

# Validate harm precedence configuration
python3 tools/constitutional_validator.py validate-harm <file.yaml>

# Generate SBOM metadata
python3 tools/constitutional_validator.py sbom-metadata --output metadata.json
```

---

## Pull Request Process

### Required Sections in PR Description

#### 1. Labor Reabsorption Assessment (if applicable)

**When required:**
- Introducing automation
- Changing processes that affect human roles
- Adding AI/ML systems
- Optimizing workflows

**What to document:**
```yaml
LABOR-REABSORPTION:
  applicable: yes/no
  
  roles_displaced:
    - role: "<Role Name>"
      fte_equivalent: <Number>
      description: "<Tasks automated>"
  
  reabsorption_pathway:
    - new_role: "<Role Name>"
      fte_equivalent: <Number>
      description: "<New capabilities>"
      transition_plan: "<Transition details>"
  
  net_displacement: <Number>
  
  governance_override:  # Required if net_displacement > 0
    justification: "..."
    risk_assessment: "..."
    mitigation_plan: "..."
    review_date: "YYYY-MM-DD"
    steward_approval: "@username"
```

**Validation:**
- `net_displacement` must equal sum(displaced) - sum(reabsorbed)
- If `net_displacement > 0`, governance override is **mandatory**
- Transition plans must be specific and actionable

#### 2. Harm Precedence Assessment (if applicable)

**When required:**
- Introducing AI/ML models
- Modifying safety-critical systems
- Changing automated decision logic

**What to document:**
```yaml
HARM-PRECEDENCE:
  applicable: yes/no
  
  model_outputs:
    - output_type: "..."
      confidence_threshold: <0.XX>
      escalation_type: "safety_critical/operational/informational"
      responsible_role: "<Named person, not queue>"
      response_sla_hours: <Number>
      fallback_chain: [...]
  
  graceful_degradation:
    implemented: yes/no
    safe_mode_description: "..."
  
  reversibility:
    rollback_procedure: "<Path to docs>"
    estimated_rollback_hours: <Number, must be ≤ 4>
    tested: yes/no
```

**Validation:**
- Confidence thresholds must meet constitutional minimums:
  - Safety critical: ≥ 0.95
  - Operational: ≥ 0.92
  - Informational: ≥ 0.85
- Responsible role must be **named person**, not anonymous queue
- Rollback time must be ≤ 4 hours

---

## Constitutional Metrics Dashboard

**File:** `GOVERNANCE_METRICS.md`

**Update Frequency:** Quarterly (every 90 days)

**Tracked Metrics:**

1. **Mean Time to Human Intervention (MTHI)**
   - Target: Decreasing trend indicates over-automation (bad)
   - Measure: Time before human oversight required

2. **Contributor Role Diversity (CRD)**
   - Target: Increasing diversity across cognitive/creative/oversight roles
   - Measure: Simpson's Diversity Index across role categories

3. **Reversibility Latency (RL)**
   - Target: < 4 hours (P95 rollback time)
   - Measure: Time to roll back harmful decisions

4. **Decision Transparency (DT)**
   - Target: 100% of decisions documented
   - Measure: Percentage with full rationale trail

**Maintenance:**
- Update dashboard by end of each quarter
- Include trend analysis and action items
- Document any constitutional incidents

---

## Regulatory Alignment

### EU AI Act Compliance

**Articles Addressed:**
- **Article 13** (Human Oversight): Harm precedence protocol + MTHI tracking
- **Article 14** (Traceability): Commit-as-contract mechanism + decision logs

**Evidence:**
- Labor reabsorption tracking → demonstrates human-centered design
- Harm precedence configurations → demonstrates human oversight
- Constitutional hash in SBOM → demonstrates traceability to design intent

### EASA AI Roadmap

**Requirement:** Traceability to design intent

**Implementation:**
- Constitutional hash embedded in model metadata
- Commit-as-contract for all governance changes
- Full audit trail in git history

### DO-178C Integration

**Existing Mechanism:** Pre-commit hook validates DO-178C safety tags

**Constitutional Addition:** Harm precedence protocol extends safety-critical validation

---

## SBOM Integration

### Embedding Constitutional Metadata

**For Python packages:**
```python
# In setup.py or pyproject.toml metadata
metadata = {
    "constitutional_compliance": {
        "version": "1.0",
        "hash": "658b530574be557bcbf0a07907f9d4bde56e665f11aa5b364c0005acff6e09a0",
        "document_path": "GOVERNANCE.md"
    }
}
```

**For model artifacts:**
```python
# In model card or metadata file
model_metadata = {
    "model_name": "ECS_Cabin_Temp_Model",
    "constitutional_compliance": {
        "version": "1.0",
        "hash": "658b530574be557bcbf0a07907f9d4bde56e665f11aa5b364c0005acff6e09a0",
        "attestation": "I affirm this model complies with AMPEL360 Digital Constitution v1.0",
        "steward": "Amedeo Pelliccia"
    }
}
```

**Generate metadata programmatically:**
```bash
python3 tools/constitutional_validator.py sbom-metadata --output metadata.json
```

---

## Fork & Derivative Compliance

### For Downstream Integrators

If you fork this repository or integrate its components:

1. **Maintain Constitutional Hash** in your SBOM/metadata
2. **Sign DCO-style Attestation:**
   ```
   I affirm this derivative work complies with AMPEL360 Digital Constitution v1.0
   
   Signed-off-by: [Name] <email@example.com>
   Date: YYYY-MM-DD
   Constitutional Hash: 658b530574be557bcbf0a07907f9d4bde56e665f11aa5b364c0005acff6e09a0
   ```
3. **Submit Quarterly Compliance Reports** (if claiming compliance publicly)

### Non-Compliant Forks

Forks that do not maintain constitutional compliance:
- SHALL NOT use "AMPEL360 Constitutional" designation
- SHOULD clearly document deviations from original governance
- MAY modify constitution (Apache 2.0 license permits) but cannot claim original compliance

---

## Conflict Resolution

### Capital vs. Labor Conflicts

**Scenario:** Capital contributor demands workforce reduction for ROI.

**Resolution Options:**

**Option A: Steward Override**
- Repository steward makes explicit commit accepting axiom violation
- Must document:
  - Justification for exception
  - Risk assessment
  - Mitigation plan
  - Time-bound review date
- Override is **public and traceable** in commit history

**Option B: Capital Withdrawal**
- Capital contributor exits project
- No constitutional violation

**Prohibited:** Silent override. All conflicts must be resolved explicitly.

### Technical vs. Constitutional Conflicts

**Precedence:** Constitutional requirements take precedence over technical optimization.

**Example:** If an efficiency optimization requires net labor displacement without reabsorption, optimization is rejected unless governance override granted.

---

## Amendment Process

### Proposing Constitutional Amendments

1. **Create PR** with proposed changes to GOVERNANCE.md
2. **Document rationale** thoroughly in PR description
3. **Open 14-day comment period** for community review
4. **Address feedback** and revise proposal
5. **Steward approval** via explicit signed commit
6. **Version increment** (e.g., 1.0 → 1.1 or 2.0)
7. **Update hash** in .constitution.yaml

### Prohibited Amendments

**Cannot amend:**
- Foundational Axiom (Article 1): "Labor is the creative and operational foundation"

**To change foundational axiom:**
- Create new constitutional document (not amendment)
- Must be explicit fork/divergence from v1.0

---

## Troubleshooting

### Pre-commit Hook Not Running

```bash
# Check hook is executable
ls -l .git/hooks/constitutional-check

# Make executable if needed
chmod +x .git/hooks/constitutional-check

# Reinstall hooks
bash .github/hooks/setup-hooks.sh
```

### CI Validation Failing

**Common issues:**
1. PR template sections missing → Add required sections
2. Net displacement > 0 without override → Add governance override
3. Confidence threshold too low → Increase to constitutional minimum
4. Metrics dashboard outdated → Update GOVERNANCE_METRICS.md

### Hash Mismatch

If constitutional hash doesn't match:
```bash
# Recompute and update
python3 tools/constitutional_validator.py hash --update

# Check .constitution.yaml was updated
git diff .constitution.yaml
```

---

## Best Practices

### For AI/ML Development

1. **Design for human oversight from start**
   - Don't add escalation mechanisms as afterthought
   - Build confidence thresholds into model architecture

2. **Document decision rationale early**
   - Write model cards with constitutional metadata
   - Include governance considerations in design docs

3. **Test reversibility procedures**
   - Include rollback drills in quarterly operations reviews
   - Measure and track rollback times

### For Process Automation

1. **Identify affected roles upfront**
   - Survey stakeholders before implementing automation
   - Design reabsorption pathways collaboratively

2. **Measure net displacement honestly**
   - Don't assume "natural attrition" as reabsorption
   - Specify concrete new roles with transition plans

3. **Start with pilot programs**
   - Test automation with small scope first
   - Validate reabsorption pathways work in practice

---

## Support & Questions

### For Technical Questions
- Review: `GOVERNANCE.md`
- Examples: `examples/constitutional/`
- Tool help: `python3 tools/constitutional_validator.py --help`

### For Governance Questions
- Constitutional Steward: Amedeo Pelliccia
- Metrics Dashboard: `GOVERNANCE_METRICS.md`
- PR Template Guidance: `.github/PULL_REQUEST_TEMPLATE.md`

### For Contributions
- Contributing Guide: README.md → Contributing section
- Code of Conduct: (Link if exists)
- Issue Tracker: GitHub Issues

---

## Document Control

- **Status:** ACTIVE
- **Version:** 1.0
- **Repository:** `AMPEL360-AIR-T`
- **Constitutional Reference:** GOVERNANCE.md v1.0
- **Last Updated:** 2026-02-11
- **Next Review:** 2026-05-11 (Quarterly)

---

*This integration guide is a living document. Feedback and improvements welcome via PR.*

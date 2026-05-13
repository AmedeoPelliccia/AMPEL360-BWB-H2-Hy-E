## Description

<!-- Provide a clear and concise description of the changes -->

## Type of Change

<!-- Check all that apply -->

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Process/automation improvement
- [ ] AI/ML system addition or modification
- [ ] Performance optimization
- [ ] Refactoring (no functional changes)

## Constitutional Compliance

### Labor Reabsorption Assessment

<!-- REQUIRED if this PR introduces automation, process changes, or AI systems that affect human labor -->
<!-- DELETE this section if NOT applicable -->

```yaml
LABOR-REABSORPTION:
  applicable: yes  # or "no" if this PR does not affect labor
  
  roles_displaced:
    - role: "<Role Name>"
      fte_equivalent: <Number>
      description: "<What tasks are automated or eliminated>"
    # Add more roles if applicable
  
  reabsorption_pathway:
    - new_role: "<Role Name>"
      fte_equivalent: <Number>
      description: "<New capabilities or expanded capacity created>"
      transition_plan: "<How affected contributors can transition to this role>"
    # Add more roles if applicable
  
  net_displacement: <Calculate: sum(displaced) - sum(reabsorbed)>
  
  governance_override:
    required: <yes/no - "yes" if net_displacement > 0>
    justification: "<Required if net_displacement > 0>"
    risk_assessment: "<Required if net_displacement > 0>"
    mitigation_plan: "<Required if net_displacement > 0>"
    review_date: "<YYYY-MM-DD - Required if net_displacement > 0>"
    steward_approval: "@<username> - Required if net_displacement > 0>"
```

### Harm Precedence Assessment

<!-- REQUIRED if this PR introduces or modifies AI/ML systems or safety-critical components -->
<!-- DELETE this section if NOT applicable -->

```yaml
HARM-PRECEDENCE:
  applicable: yes  # or "no" if this PR does not involve AI/ML or safety-critical systems
  
  model_outputs:
    - output_type: "<e.g., decision, prediction, recommendation>"
      confidence_threshold: <0.XX - must meet constitutional minimums>
      escalation_type: "<safety_critical/operational/informational>"
      responsible_role: "<Named role, not queue>"
      response_sla_hours: <Number>
      fallback_chain:
        - "<Fallback role 1>"
        - "<Fallback role 2>"
  
  graceful_degradation:
    implemented: yes  # or "no"
    safe_mode_description: "<How system degrades safely>"
    
  reversibility:
    rollback_procedure: "<Path to documented rollback procedure>"
    estimated_rollback_hours: <Number - must be <= 4>
    tested: yes  # or "no"
```

## Testing

<!-- Describe the tests you ran to verify your changes -->

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed
- [ ] Rollback procedure tested (if applicable)

### Test Coverage

- **Files changed:** X
- **Lines added:** Y
- **Lines removed:** Z
- **Test coverage:** XX% (if applicable)

## Compliance Checklist

- [ ] I have read and understood the [GOVERNANCE.md](../GOVERNANCE.md) (Digital Constitution)
- [ ] Labor reabsorption has been assessed and documented (if applicable)
- [ ] Harm precedence mechanisms are in place (if applicable)
- [ ] Decision transparency is maintained (all AI decisions have documented rationale)
- [ ] Changes are reversible within 4 hours (if affecting operations)
- [ ] Constitutional hash is embedded in metadata (if distributing models/artifacts)
- [ ] SPDX license headers are present in new files
- [ ] Documentation has been updated
- [ ] This PR does not introduce silent labor displacement

## Regulatory Alignment

<!-- Check all that apply -->

- [ ] EU AI Act Article 13 (Human oversight) - compliant
- [ ] EU AI Act Article 14 (Traceability) - compliant
- [ ] EASA AI Roadmap (Design intent traceability) - compliant
- [ ] DO-178C safety tags present (if safety-critical code modified)
- [ ] Not applicable (explain why):

## Metrics Impact

<!-- If this PR affects governance metrics, document the expected impact -->

| Metric | Current | Expected After PR | Direction |
|--------|---------|-------------------|-----------|
| Mean Time to Human Intervention | | | ⬇️ Decreasing (good) / ⬆️ Increasing (warning) / ➡️ No change |
| Contributor Role Diversity | | | ⬆️ Increasing (good) / ⬇️ Decreasing (warning) / ➡️ No change |
| Reversibility Latency | | | ⬇️ Decreasing (good) / ⬆️ Increasing (warning) / ➡️ No change |
| Decision Transparency | | | ⬆️ Increasing (good) / ⬇️ Decreasing (warning) / ➡️ No change |

## Constitutional Attestation

By submitting this PR, I attest that:

- [ ] I have reviewed this PR against the AMPEL360 Digital Constitution v1.0
- [ ] This PR does not violate the Foundational Axiom (Labor as foundation)
- [ ] All constitutional requirements have been addressed or documented as N/A
- [ ] I commit to addressing any constitutional compliance issues raised in review

**Signed-off-by:** [Your Name] <your.email@example.com>  
**Date:** YYYY-MM-DD

---

## Additional Context

<!-- Add any other context, screenshots, or references here -->

## Related Issues

<!-- Link related issues or PRs -->

Closes #
Relates to #

---

**For Reviewers:**

Please verify:
1. Constitutional compliance sections are complete (if applicable)
2. Labor displacement is zero or properly documented with governance override
3. Harm precedence mechanisms are appropriate
4. Metrics impact is acceptable
5. Reversibility requirements are met

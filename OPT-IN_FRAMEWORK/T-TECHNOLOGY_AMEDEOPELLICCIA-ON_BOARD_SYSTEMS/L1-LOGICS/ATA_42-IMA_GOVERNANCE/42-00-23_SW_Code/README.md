# 42-00-23_SW_Code

## Purpose

Source code repository for partitioned IMA software.

## Scope

This folder contains source code organized by partition:

* C/Ada/SPARK source files
* Header files
* Configuration files
* Build scripts

## Structure

Code is organized by partition:

```text
42-00-23_SW_Code/
├── P-FCS/
│   ├── src/           # Source files
│   ├── include/       # Headers
│   └── config/        # Configuration
├── P-GNC/
├── P-ADS/
├── P-MAINT/
└── P-DIAG/
```

## Coding Standards

All code must comply with:

| Standard | Applicability |
|----------|---------------|
| [MISRA-C:2012](https://www.misra.org.uk/) | All C code |
| [CERT-C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard) | All C code |
| [DO-178C](https://www.rtca.org/) | All safety-critical code |

## AI-Generated Code

All AI-generated code must:

1. Be tagged with AI metadata in GenCCC
2. Pass static analysis
3. Achieve required structural coverage
4. Be reviewed by qualified engineer

## Traceability

All code modules are traced in:

* [`42-00-20_GENCCC_SW_CONFIG/MATRICES/`](../42-00-20_GENCCC_SW_CONFIG/MATRICES/) — Traceability matrices

## Related Folders

* [`42-00-20_GENCCC_SW_CONFIG/`](../42-00-20_GENCCC_SW_CONFIG/) — GenCCC configuration
* [`42-00-22_SW_Requirements/`](../42-00-22_SW_Requirements/) — Software requirements
* [`42-00-24_SW_Tests/`](../42-00-24_SW_Tests/) — Test artifacts
* [`42-00-25_AI_Assistance_Log/`](../42-00-25_AI_Assistance_Log/) — AI interaction logs

## Document Control

- **Standard**: OPT-IN Framework v1.1
- **Status**: Active
- **Owner**: AMPEL360 SW WG
- **Last Updated**: 2025-12-04

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: 2025-12-04.

---

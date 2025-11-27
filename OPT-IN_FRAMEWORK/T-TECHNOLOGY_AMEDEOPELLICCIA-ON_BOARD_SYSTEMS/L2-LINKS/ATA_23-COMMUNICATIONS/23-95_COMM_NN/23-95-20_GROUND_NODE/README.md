# 23-95-20 — Ground Node (FAirCCC-G)

## Purpose

The Ground Node is the ground station component of the FAirCCC infrastructure. It receives gradient envelopes from aircraft, validates them, and stages them for regional aggregation.

## Responsibilities

| Function | Description |
|----------|-------------|
| **Signature Verification** | Validate TPM signatures |
| **Schema Validation** | Check envelope format |
| **Poison Detection** | Outlier gradient filtering |
| **Staging** | Queue for regional uplink |

## Interfaces

- **Upstream:** Aircraft Node (23-95-10)
- **Downstream:** Regional Node (23-95-30)

## Security

- Certificate chain validation
- DP budget enforcement
- Contribution thresholds

## Document Control

- Standard: OPT-IN Framework v1.2
- Status: Active
- Last Updated: 2025-11-27

# 95-20-27-803 — FCS NN Troubleshooting Guide

**Document ID:** 95-20-27-803  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Classification:** Maintenance

---

## 1. Introduction

This guide provides troubleshooting procedures for common FCS_NN faults.

---

## 2. Fault Codes

### 2.1 NN-001: Aero Predictor Degraded

**Symptoms**:
- EICAS caution "FCS NN DEGRADED"
- Aero Predictor health score <95%

**Possible Causes**:
- Increased inference latency
- Input sensor degradation (ADC, IRU)
- Model drift

**Troubleshooting**:
1. Check sensor health (ADC, IRU)
2. Review latency benchmarks
3. If sensors OK, model may need retraining
4. Dispatch per MEL if within limits

**Resolution**:
- Replace faulty sensor
- Update model (if available)
- Monitor performance

---

### 2.2 NN-002: Control Optimizer Degraded

**Symptoms**:
- EICAS caution "FCS NN DEGRADED"
- Control Optimizer health score <95%

**Possible Causes**:
- Actuator feedback mismatch
- Model prediction error

**Troubleshooting**:
1. Check actuator position feedback
2. Verify control surface rigging
3. Review prediction vs actual logs

**Resolution**:
- Adjust actuator feedback
- Re-rig control surfaces if needed
- Update model

---

### 2.3 NN-099: Complete FCS_NN Failure

**Symptoms**:
- EICAS warning "FCS NN FAIL"
- Direct Law engaged

**Possible Causes**:
- IMA partition failure
- Power supply failure
- Model load failure

**Troubleshooting**:
1. Check IMA module power
2. Check partition status
3. Review BIT results

**Resolution**:
- Replace IMA module
- Reload models
- Re-execute BIT

---

## Document Control

- **Owner**: AMPEL360 Maintenance Engineering
- **Version**: 1.0
- **Status**: Active
- **Classification**: Maintenance Manual
- **Last Updated**: 2025-11-17

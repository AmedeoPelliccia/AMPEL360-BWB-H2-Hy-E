# 95-20-27-802 — FCS NN Maintenance Procedures

**Document ID:** 95-20-27-802  
**Version:** 1.0  
**Date:** 2025-11-17  
**Status:** Active  
**Classification:** Maintenance

---

## 1. Introduction

This Maintenance Manual provides procedures for maintenance personnel servicing the FCS_NN subsystem on the AMPEL360 BWB H₂ Hy-E aircraft.

---

## 2. Scheduled Maintenance

### 2.1 Pre-Flight Check (Daily)

**Procedure**:
1. Power on aircraft
2. Observe FCS_NN self-test on EICAS
3. Execute FCS BIT
4. Verify "BIT PASS" result
5. If FAIL: Note fault code, consult troubleshooting guide

**Time**: 2 minutes

### 2.2 Weekly Maintenance

**Procedure**:
1. Download event logs via maintenance panel
2. Review logs for anomalies
3. Check health trend data
4. Verify model performance within limits

**Time**: 15 minutes

### 2.3 Monthly Maintenance

**Procedure**:
1. Execute extended BIT (MBIT)
2. Review performance trending reports
3. Check for software/model updates
4. Verify blockchain provenance chain integrity

**Time**: 30 minutes

### 2.4 Annual Maintenance

**Procedure**:
1. Complete model validation tests
2. Calibrate sensors (if scheduled)
3. Update software/models (if available)
4. Full system regression test

**Time**: 4 hours

---

## 3. Unscheduled Maintenance

### 3.1 Fault Code Resolution

Refer to **95-20-27-803 Troubleshooting Guide** for fault code descriptions and corrective actions.

### 3.2 Component Replacement

If IMA module replacement required:
1. Power down aircraft
2. Remove faulty IMA module
3. Install replacement module
4. Power on aircraft
5. Execute FCS BIT
6. Load model weights from backup
7. Verify operation

---

## Document Control

- **Owner**: AMPEL360 Maintenance Engineering
- **Version**: 1.0
- **Status**: Active
- **Classification**: Maintenance Manual
- **Last Updated**: 2025-11-17

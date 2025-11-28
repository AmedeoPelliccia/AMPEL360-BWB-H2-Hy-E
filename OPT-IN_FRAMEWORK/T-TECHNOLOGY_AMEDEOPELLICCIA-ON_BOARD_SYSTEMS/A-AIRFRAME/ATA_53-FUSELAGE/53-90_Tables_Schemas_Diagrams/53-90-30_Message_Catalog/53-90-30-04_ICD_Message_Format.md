# 53-90-30-04 ICD Message Format

| Field | Value |
|-------|-------|
| **Document ID** | 53-90-30-04 |
| **Version** | 1.0 |
| **Date** | 2025-11-27 |
| **Status** | DRAFT |
| **Classification** | TECHNICAL / DATA |
| **ATA Chapter** | 53-90-30 |

---

## 1. Purpose

This document defines the Interface Control Document (ICD) for ANCHORS system messages, including AFDX virtual link and CAN bus message formats.

## 2. AFDX Configuration

### 2.1 Network Parameters

| Parameter | Value |
|-----------|-------|
| AFDX Standard | ARINC 664 Part 7 |
| Network Speed | 100 Mbps |
| Switch Latency | ≤ 150 µs |
| Frame Format | Ethernet II |
| IP Version | IPv4 |

### 2.2 Virtual Link Allocation

| Range | Assignment |
|-------|------------|
| VL_5300-5319 | ANCHORS Primary |
| VL_5320-5339 | ANCHORS Redundant |
| VL_5340-5349 | Reserved |

### 2.3 Quality of Service

| VL Priority | BAG Range | Application |
|-------------|-----------|-------------|
| Critical | 2-10 ms | Safety commands |
| High | 10-20 ms | Control data |
| Medium | 20-100 ms | Status data |
| Low | 100-500 ms | Diagnostics |

## 3. Message Format Details

### 3.1 VL_5302 ANCH_BAT_DATA

```
Byte 0-1:  Cell Temp Max    (uint16, 0.1°C, offset -400)
Byte 2-3:  Cell Temp Min    (uint16, 0.1°C, offset -400)
Byte 4-5:  Pack Voltage     (uint16, 0.1V)
Byte 6-7:  Pack Current     (int16, 0.1A, signed)
Byte 8:    SOC              (uint8, %)
Byte 9:    SOH              (uint8, %)
Byte 10:   Fault Flags      (uint8, bit field)
Byte 11:   Status           (uint8, enum)
```

#### Fault Flags Definition

| Bit | Flag | Description |
|-----|------|-------------|
| 0 | OT | Over-temperature |
| 1 | UT | Under-temperature |
| 2 | OV | Over-voltage |
| 3 | UV | Under-voltage |
| 4 | OC | Over-current |
| 5 | ISO | Isolation fault |
| 6 | COM | Communication fault |
| 7 | RES | Reserved |

### 3.2 VL_5309 ANCH_SS_STATUS

```
Byte 0:    SS State         (uint8, enum)
Byte 1:    Fault Count      (uint8, 0-255)
Byte 2-3:  Fault Code       (uint16, code)
Byte 4:    Isolation Status (uint8, bit field)
Byte 5:    Watchdog Status  (uint8, enum)
Byte 6-7:  Reserved         (uint16)
```

#### Isolation Status Bits

| Bit | System | Description |
|-----|--------|-------------|
| 0 | BAT | Battery isolated |
| 1 | HT | HT bus isolated |
| 2 | LT | LT bus isolated |
| 3 | HV | HV power isolated |
| 4 | CO2 | CO2 system isolated |
| 5 | H2O | Water system isolated |

## 4. CAN Bus Configuration

### 4.1 Network Parameters

| Parameter | Value |
|-----------|-------|
| CAN Standard | CAN 2.0B |
| Bit Rate | 500 kbps |
| Termination | 120Ω each end |
| Max Nodes | 32 |

### 4.2 ID Allocation

| ID Range (Hex) | Assignment |
|----------------|------------|
| 0x100-0x1FF | Battery Management |
| 0x200-0x2FF | CO2 Capture |
| 0x300-0x3FF | Thermal Management |
| 0x400-0x4FF | Sensors |
| 0x500-0x5FF | Water Treatment |
| 0x600-0x6FF | Safety Supervisor |
| 0x700-0x7FF | Neural Network |

## 5. Data Encoding

### 5.1 Numeric Encoding

| Type | Encoding | Range | Resolution |
|------|----------|-------|------------|
| Temperature | int16 | -40°C to +100°C | 0.1°C |
| Pressure | uint16 | 0 to 10 bar | 0.01 bar |
| Voltage | uint16 | 0 to 900V | 0.1V |
| Current | int16 | -500A to +500A | 0.1A |
| Percentage | uint8 | 0 to 100% | 1% |
| Flow | uint16 | 0 to 300 L/min | 0.1 L/min |

### 5.2 Endianness

- **AFDX**: Big-endian (network byte order)
- **CAN**: Little-endian

### 5.3 Boolean Encoding

| Value | Meaning |
|-------|---------|
| 0x00 | FALSE |
| 0x01 | TRUE |
| 0xFF | Invalid/Unknown |

## 6. Timing Requirements

### 6.1 Message Latency

| Priority | Max Latency | Jitter |
|----------|-------------|--------|
| Critical | 10 ms | < 1 ms |
| High | 25 ms | < 5 ms |
| Medium | 100 ms | < 20 ms |
| Low | 500 ms | < 100 ms |

### 6.2 Freshness Monitoring

| Signal Type | Timeout | Action |
|-------------|---------|--------|
| Safety | 3× BAG | Isolate |
| Control | 5× BAG | Fallback |
| Status | 10× BAG | Stale flag |
| Diagnostic | 60× BAG | Log only |

## 7. Error Handling

### 7.1 Communication Errors

| Error | Detection | Response |
|-------|-----------|----------|
| Frame loss | Sequence gap | Request retransmit |
| CRC error | CRC mismatch | Discard frame |
| Timeout | Timer expiry | Use default |
| Overrun | Buffer full | Log and discard oldest |

### 7.2 Data Validity

| Check | Method | Action |
|-------|--------|--------|
| Range | Min/Max bounds | Clamp or reject |
| Rate | Delta check | Filter or reject |
| Consistency | Cross-check | Flag discrepancy |

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-27_.

---

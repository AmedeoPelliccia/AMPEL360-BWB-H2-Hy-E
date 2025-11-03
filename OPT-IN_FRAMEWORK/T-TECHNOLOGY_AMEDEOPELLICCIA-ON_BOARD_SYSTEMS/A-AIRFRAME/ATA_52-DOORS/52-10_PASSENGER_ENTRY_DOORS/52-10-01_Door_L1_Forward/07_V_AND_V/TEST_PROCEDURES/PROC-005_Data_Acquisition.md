# Test Procedure - Data Acquisition

**Procedure:** PROC-005  
**Revision:** DRAFT  
**Date:** 2025-11-03

---

## 1. SCOPE

Standard data acquisition setup and operation for all structural tests.

---

## 2. HARDWARE CONFIGURATION

### 2.1 System
- Platform: National Instruments PXI-8880
- Chassis: PXI-1045 (8-slot)
- Controller: Real-time processor
- Operating system: NI Real-Time

### 2.2 Modules
- Strain gauge: PXI-4331 (8 channels × 3 = 24 channels)
- LVDT: PXI-4461 (dynamic signal acquisition)
- Pressure: PXI-4472 (24-bit)
- Acoustic emission: PXI-5122 (high-speed digitizer)

---

## 3. CHANNEL CONFIGURATION

### 3.1 Strain Gauges (24 channels)
```
Excitation: 2.5V DC
Bridge type: Quarter bridge (3-wire)
Completion resistor: 350 Ω
Gauge factor: 2.1
Sample rate: 1000 Hz
Range: ±10,000 με
Filter: 400 Hz low-pass
```

### 3.2 LVDTs (5 channels)
```
Excitation: 5V AC, 2.5 kHz
Input range: ±10V
Sample rate: 1000 Hz
Range: 0-50 mm (center), 0-25 mm (corners)
Filter: 400 Hz low-pass
```

### 3.3 Pressure (3 channels)
```
Input type: 4-20 mA current loop
Range: 0-30 psi
Sample rate: 100 Hz
Resolution: 0.01 psi
Filter: 10 Hz low-pass
```

### 3.4 Acoustic Emission (4 channels)
```
Input type: Voltage (preamplified)
Range: ±5V
Sample rate: 2 MHz
Threshold: 45 dB
Filter: 100 kHz - 1 MHz bandpass
```

---

## 4. SOFTWARE SETUP

### 4.1 LabVIEW Application
- Custom VI for test control
- Real-time monitoring
- Automated data logging
- Safety interlocks

### 4.2 Calibration
1. Zero all channels with no load
2. Apply known calibration loads
3. Verify scale factors
4. Document calibration values

### 4.3 Data File Format
- Format: TDMS (Technical Data Management Streaming)
- Backup: Export to CSV for analysis
- Naming: Test-ID_Date_Time.tdms
- Metadata: Include test configuration

---

## 5. OPERATION

### 5.1 Pre-Test
1. Power on DAQ system
2. Launch LabVIEW application
3. Load test configuration
4. Verify all channels active
5. Zero all sensors
6. Start recording

### 5.2 During Test
1. Monitor real-time displays
2. Check for anomalies
3. Verify data quality
4. Save backup every 1 psi

### 5.3 Post-Test
1. Stop recording
2. Save all data files
3. Export to analysis format
4. Archive raw data
5. Backup to network storage

---

## 6. DATA QUALITY CHECKS

### 6.1 Real-Time
- No sensor dropouts
- Noise level <1% of range
- Coherent behavior (related channels)
- No clipping or saturation

### 6.2 Post-Processing
- Remove DC offset
- Apply calibration factors
- Filter if necessary
- Check for data corruption

---

## 7. BACKUP STRATEGY

- Primary: Local SSD on DAQ controller
- Secondary: Network storage (automatic sync)
- Tertiary: External hard drive (manual backup)
- Retention: 7 years minimum

---

## 8. TROUBLESHOOTING

| Issue | Cause | Solution |
|-------|-------|----------|
| Noisy signal | Poor shielding | Check cables, grounding |
| Channel dropout | Loose connection | Reseat connector |
| Incorrect reading | Wrong calibration | Re-calibrate channel |
| Data loss | Storage full | Clear space, resume |

---

**Quality:** Verify data integrity before leaving test site.

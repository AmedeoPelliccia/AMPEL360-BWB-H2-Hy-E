/**
 * SysML 1.6 Textual Specification
 * ATA 61-20-06 — Health Sensing
 * 
 * Package: ATA61_HealthSensing
 * Version: 1.0
 * Last Updated: 2025-12-01
 * Standard: OPT-IN Framework v1.2
 */

// =============================================================================
// 1. BLOCK DEFINITION DIAGRAM (BDD) — Health Sensing Structure
// =============================================================================

package ATA61_HealthSensing {

    block Health_Sensing_System {
        part vibrationSensors : Vibration_Sensor_Set;
        part strainGauges : Strain_Gauge_Set;
        part temperatureSensors : Temperature_Sensor_Set;
        part emSensors : EM_Sensor_Set;
        part dataAcquisition : DAQ_Unit;
        part signalProcessor : Signal_Processor;
        
        value sensorCount : int;
        value samplingRate : kHz;
        value dataOutputRate : Hz;
    }

    block Vibration_Sensor_Set {
        part motorVibration : Accelerometer[3];      // X, Y, Z axes
        part fanVibration : Accelerometer[2];
        part nacelleVibration : Accelerometer[2];
        part bearingVibration : Accelerometer[2];
        
        value frequencyRange : Hz_Range;             // 10 Hz to 20 kHz
        value sensitivity : mV_per_g;
        value dynamicRange : dB;
    }

    block Accelerometer {
        value axis : String;                         // X, Y, Z
        value sensitivity : mV_per_g;
        value frequencyResponse : Hz_Range;
        value resonantFrequency : kHz;
        value tempRange : C_Range;
    }

    block Strain_Gauge_Set {
        part bladeGauges : Strain_Gauge[12];         // One per blade
        part hubGauges : Strain_Gauge[4];
        part mountGauges : Strain_Gauge[4];
        
        value gaugeType : String;                    // Foil, semiconductor
        value gaugeFactor : float;
        value fatigueLife : cycles;
    }

    block Strain_Gauge {
        value location : String;
        value orientation : deg;
        value resistance : Ohm;
        value gaugeFactor : float;
        value tempCompensation : boolean;
    }

    block Temperature_Sensor_Set {
        part motorWindingTemp : RTD[3];              // Per phase
        part motorBearingTemp : RTD[2];
        part coolantTemp : RTD[4];                   // In/out motor, PCU
        part ambientTemp : RTD[1];
        
        value accuracy : C;
        value responseTime : ms;
    }

    block RTD {
        value type : String;                         // PT100, PT1000
        value class : String;                        // A, B, 1/3 DIN
        value range : C_Range;
        value selfHeating : mW;
    }

    block EM_Sensor_Set {
        part currentSensors : Current_Sensor[3];     // Per phase
        part fluxSensors : Flux_Sensor[2];
        part partialDischarge : PD_Sensor;
        
        value bandwidth : Hz_Range;
        value resolution : bits;
    }

    block DAQ_Unit {
        value channels : int;
        value resolution : bits;
        value samplingRate : kSPS;
        value antiAliasFilter : Hz;
        value dataInterface : String;                // AFDX, CAN, Ethernet
    }

    block Signal_Processor {
        value fftCapability : boolean;
        value filterBands : int;
        value trendingMemory : MB;
        value alarmThresholds : int;
    }
}

// =============================================================================
// 2. INTERNAL BLOCK DIAGRAM (IBD) — Health Sensing Interfaces
// =============================================================================

ibd Health_Sensing_System {

    // Vibration sensing
    motorVibration.signal -> dataAcquisition.vibChannel[0:2];
    fanVibration.signal -> dataAcquisition.vibChannel[3:4];
    nacelleVibration.signal -> dataAcquisition.vibChannel[5:6];
    bearingVibration.signal -> dataAcquisition.vibChannel[7:8];

    // Strain sensing
    bladeGauges.signal -> dataAcquisition.strainChannel[0:11];
    hubGauges.signal -> dataAcquisition.strainChannel[12:15];
    mountGauges.signal -> dataAcquisition.strainChannel[16:19];

    // Temperature sensing
    motorWindingTemp.signal -> dataAcquisition.tempChannel[0:2];
    motorBearingTemp.signal -> dataAcquisition.tempChannel[3:4];
    coolantTemp.signal -> dataAcquisition.tempChannel[5:8];
    ambientTemp.signal -> dataAcquisition.tempChannel[9];

    // EM sensing
    currentSensors.signal -> dataAcquisition.emChannel[0:2];
    fluxSensors.signal -> dataAcquisition.emChannel[3:4];
    partialDischarge.signal -> dataAcquisition.emChannel[5];

    // Processing
    dataAcquisition.digitalOut -> signalProcessor.dataIn;
    signalProcessor.processedData -> pcu.healthData;
    signalProcessor.alarms -> pcu.faultInput;
    signalProcessor.trends -> maintenanceSystem.conditionData;

    // Aircraft interfaces
    signalProcessor.telemetry -> aircraftBus.healthTelemetry;
    signalProcessor.eventLog -> dpp.eventRecord;
}

// =============================================================================
// 3. REQUIREMENTS DIAGRAM (REQ) — Health Sensing Requirements
// =============================================================================

package ATA61_HealthSensing_Requirements {

    requirement REQ_61_20_06_001_VibrationDetection {
        text = "System shall detect rotor imbalance of ≥ 0.5 g at 1× rotational frequency.";
        id = "REQ-61-20-06-001";
    }

    requirement REQ_61_20_06_002_BearingHealth {
        text = "System shall detect bearing defects ≥ 10 flight hours before failure.";
        id = "REQ-61-20-06-002";
    }

    requirement REQ_61_20_06_003_BladeHealth {
        text = "Strain gauges shall detect blade crack growth ≥ 5 mm in length.";
        id = "REQ-61-20-06-003";
    }

    requirement REQ_61_20_06_004_TempMonitoring {
        text = "Temperature sensors shall provide ±1°C accuracy over -40°C to +200°C range.";
        id = "REQ-61-20-06-004";
    }

    requirement REQ_61_20_06_005_SamplingRate {
        text = "Vibration data shall be sampled at ≥ 50 kHz for high-frequency analysis.";
        id = "REQ-61-20-06-005";
    }

    requirement REQ_61_20_06_006_DataLatency {
        text = "Health data latency to PCU shall be ≤ 10 ms for protection functions.";
        id = "REQ-61-20-06-006";
    }

    requirement REQ_61_20_06_007_FalseAlarm {
        text = "False alarm rate shall be < 1 per 1000 flight hours.";
        id = "REQ-61-20-06-007";
    }

    requirement REQ_61_20_06_008_Coverage {
        text = "Health monitoring coverage shall be ≥ 95% of failure modes per FMEA.";
        id = "REQ-61-20-06-008";
    }

    requirement REQ_61_20_06_009_DPP {
        text = "All health events shall be logged to Digital Product Passport with timestamp.";
        id = "REQ-61-20-06-009";
    }
}

// =============================================================================
// 4. ACTIVITY DIAGRAM (ACT) — Health Monitoring Process
// =============================================================================

activity Health_Monitoring_Process {

    action Acquire_Raw_Data;
    action Apply_Filters;
    action Compute_FFT;
    action Extract_Features;
    action Compare_Thresholds;
    action Trend_Analysis;
    action Anomaly_Detection;
    action Generate_Health_Index;
    action Check_Alarms;
    action Update_Maintenance_Prediction;
    action Log_To_DPP;
    action Send_Telemetry;

    InitialNode -> Acquire_Raw_Data;
    Acquire_Raw_Data -> Apply_Filters;
    Apply_Filters -> Compute_FFT;
    Compute_FFT -> Extract_Features;
    Extract_Features -> Compare_Thresholds;
    Compare_Thresholds -> Trend_Analysis;
    Trend_Analysis -> Anomaly_Detection;
    Anomaly_Detection -> Generate_Health_Index;
    Generate_Health_Index -> Check_Alarms;
    Check_Alarms -> Update_Maintenance_Prediction;
    Update_Maintenance_Prediction -> Log_To_DPP;
    Log_To_DPP -> Send_Telemetry;
    Send_Telemetry -> Acquire_Raw_Data;  // Continuous loop
}

// =============================================================================
// 5. PARAMETRIC DIAGRAM (PAR) — Health Indicators
// =============================================================================

par Health_Indicators {

    // Vibration analysis
    constraint c1: vibrationSeverity = sqrt(sum(a_rms^2));
    constraint c2: imbalanceIndicator = amplitude_1X / baseline_1X;
    constraint c3: bearingDefectFreq = n * (d/D) * (1 + cos(contactAngle)) * rpm / 60;

    // Strain-based fatigue
    constraint c4: fatigueAccumulation = sum(n_i / N_i);  // Miner's rule
    constraint c5: remainingLife = 1 - fatigueAccumulation;

    // Temperature trending
    constraint c6: tempRiseRate = (T_current - T_previous) / dt;
    constraint c7: thermalMargin = T_limit - T_current;

    // Electromagnetic health
    constraint c8: currentAsymmetry = max(I_phase) / min(I_phase) - 1;
    constraint c9: insulationHealth = PD_level / PD_baseline;

    // Overall health index
    constraint c10: healthIndex = w1*vibHealth + w2*strainHealth + w3*tempHealth + w4*emHealth;

    // Bind parameters
    a_rms -> c1.acceleration;
    amplitude_1X -> c2.rotationalAmplitude;
}

// =============================================================================
// 6. STATE MACHINE — Health Monitoring States
// =============================================================================

stm HealthMonitoring_States {

    state Initialization;
    state Baseline_Learning;
    state Normal_Monitoring;
    state Enhanced_Monitoring;
    state Alarm_Active;
    state Fault_Isolation;
    state Degraded_Operation;

    Initialization -> Baseline_Learning : on startup_complete;
    Baseline_Learning -> Normal_Monitoring : on baseline_established;
    Normal_Monitoring -> Enhanced_Monitoring : on anomaly_detected;
    Enhanced_Monitoring -> Normal_Monitoring : on anomaly_cleared;
    Enhanced_Monitoring -> Alarm_Active : on threshold_exceeded;
    Normal_Monitoring -> Alarm_Active : on critical_threshold;
    Alarm_Active -> Fault_Isolation : on alarm_confirmed;
    Fault_Isolation -> Degraded_Operation : on fault_isolated;
    Degraded_Operation -> Normal_Monitoring : on fault_cleared;
    Alarm_Active -> Normal_Monitoring : on false_alarm_confirmed;
}

// =============================================================================
// 7. ALLOCATION DIAGRAM — Sensor to Component Mapping
// =============================================================================

allocation SensorToComponent {

    // Motor sensors
    motorVibration[0] -> motor.driveEndBearing;
    motorVibration[1] -> motor.nonDriveEndBearing;
    motorVibration[2] -> motor.statorFrame;
    motorWindingTemp[0] -> motor.phaseU_winding;
    motorWindingTemp[1] -> motor.phaseV_winding;
    motorWindingTemp[2] -> motor.phaseW_winding;
    motorBearingTemp[0] -> motor.driveEndBearing;
    motorBearingTemp[1] -> motor.nonDriveEndBearing;

    // Fan sensors
    fanVibration[0] -> ductedFan.rotor.hub;
    fanVibration[1] -> ductedFan.stator.shroud;
    bladeGauges[0:11] -> ductedFan.rotor.blade[0:11].root;

    // Nacelle sensors
    nacelleVibration[0] -> nacelle.forwardMount;
    nacelleVibration[1] -> nacelle.aftMount;
    hubGauges[0:3] -> ductedFan.rotor.hub.attachment[0:3];
    mountGauges[0:3] -> nacelle.mountingBracket[0:3];

    // EM sensors
    currentSensors[0:2] -> pcu.inverter.phaseOutput[0:2];
    fluxSensors[0:1] -> motor.airgap[0:1];
    partialDischarge -> motor.statorInsulation;
}

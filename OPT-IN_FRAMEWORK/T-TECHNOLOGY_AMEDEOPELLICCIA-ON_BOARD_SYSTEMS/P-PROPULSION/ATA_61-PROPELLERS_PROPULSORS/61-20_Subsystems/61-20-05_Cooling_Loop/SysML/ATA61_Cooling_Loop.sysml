/**
 * SysML 1.6 Textual Specification
 * ATA 61-20-05 — Cooling Loop
 * 
 * Package: ATA61_CoolingLoop
 * Version: 1.0
 * Last Updated: 2025-12-01
 * Standard: OPT-IN Framework v1.2
 */

// =============================================================================
// 1. BLOCK DEFINITION DIAGRAM (BDD) — Cooling Loop Structure
// =============================================================================

package ATA61_CoolingLoop {

    block Cooling_Loop {
        part pump : Coolant_Pump;
        part heatExchanger : Heat_Exchanger;
        part reservoir : Coolant_Reservoir;
        part piping : Piping_System;
        part valves : Valve_Set;
        part sensors : Thermal_Sensors;
        part controller : Thermal_Controller;
        
        value coolantType : String;           // Glycol-water, PAO, etc.
        value totalVolume : L;
        value designFlowRate : L_per_min;
        value designHeatLoad : kW;
    }

    block Coolant_Pump {
        value flowRate : L_per_min;
        value pressureHead : bar;
        value powerConsumption : W;
        value efficiency : percent;
        value redundancy : String;            // Single, Dual, etc.
    }

    block Heat_Exchanger {
        value type : String;                  // Liquid-liquid, liquid-air
        value heatTransferCapacity : kW;
        value primaryFlowRate : L_per_min;
        value secondaryFlowRate : L_per_min;
        value effectiveness : percent;
        value pressureDrop : mbar;
    }

    block Coolant_Reservoir {
        value capacity : L;
        value operatingLevel : L;
        value expansionVolume : L;
        value deaerationCapability : boolean;
    }

    block Piping_System {
        value material : String;              // Aluminum, stainless, composite
        value nominalDiameter : mm;
        value totalLength : m;
        value insulationType : String;
    }

    block Valve_Set {
        part flowControlValve : Control_Valve;
        part bypassValve : Bypass_Valve;
        part shutoffValve : Shutoff_Valve[2];
        part reliefValve : Relief_Valve;
    }

    block Thermal_Sensors {
        part tempSensors : Temperature_Sensor[4];  // Inlet, outlet, motor, PCU
        part flowSensor : Flow_Sensor;
        part pressureSensors : Pressure_Sensor[2];
    }

    block Thermal_Controller {
        value controlStrategy : String;       // PID, predictive
        value setpointRange : TempRange;
        value responseTime : s;
    }

    // Cryogenic interface (optional)
    block Cryo_Interface {
        value coldSinkTemp : K;               // LH2 temperature
        value heatExchangeRate : kW;
        value interfaceType : String;
        value safetyFeatures : String[];
    }
}

// =============================================================================
// 2. INTERNAL BLOCK DIAGRAM (IBD) — Cooling Loop Interfaces
// =============================================================================

ibd Cooling_Loop {

    // Primary cooling circuit
    reservoir.outlet -> pump.inlet;
    pump.outlet -> piping.supplyManifold;
    piping.supplyManifold -> motor.coolingJacket;
    motor.coolingJacket -> piping.returnManifold;
    piping.returnManifold -> pcu.coldPlate;
    pcu.coldPlate -> heatExchanger.hotSide;
    heatExchanger.hotSide -> reservoir.inlet;

    // Heat rejection
    heatExchanger.coldSide <-> aircraftThermal.heatSink;
    
    // Optional cryo interface
    heatExchanger.coldSide <-> cryoInterface.heatExchange [optional];
    cryoInterface.h2Connection <-> fuelSystem.cryoPort;

    // Control and monitoring
    sensors.tempData -> controller.tempInput;
    sensors.flowData -> controller.flowInput;
    controller.pumpCommand -> pump.speedControl;
    controller.valveCommand -> valves.positionControl;
    controller.status -> pcu.thermalStatus;
    controller.status -> healthSensing.thermalData;

    // Bypass for temperature regulation
    valves.bypassValve <-> piping.bypassLine;
}

// =============================================================================
// 3. REQUIREMENTS DIAGRAM (REQ) — Cooling Loop Requirements
// =============================================================================

package ATA61_CoolingLoop_Requirements {

    requirement REQ_61_20_05_001_Capacity {
        text = "Cooling loop shall dissipate ≥ 200 kW combined heat load from motor and PCU.";
        id = "REQ-61-20-05-001";
    }

    requirement REQ_61_20_05_002_MotorTemp {
        text = "Motor winding temperature shall be maintained below 160°C at all operating conditions.";
        id = "REQ-61-20-05-002";
    }

    requirement REQ_61_20_05_003_PCUTemp {
        text = "PCU junction temperature shall be maintained below 125°C.";
        id = "REQ-61-20-05-003";
    }

    requirement REQ_61_20_05_004_Response {
        text = "Cooling system shall reach thermal equilibrium within 120 s of startup.";
        id = "REQ-61-20-05-004";
    }

    requirement REQ_61_20_05_005_FlowRate {
        text = "Minimum coolant flow rate shall be 40 L/min at design conditions.";
        id = "REQ-61-20-05-005";
    }

    requirement REQ_61_20_05_006_Redundancy {
        text = "Pump system shall provide fail-operational capability via redundant pump.";
        id = "REQ-61-20-05-006";
    }

    requirement REQ_61_20_05_007_Leakage {
        text = "Cooling loop shall be leak-free for 20,000 flight hours without maintenance.";
        id = "REQ-61-20-05-007";
    }

    requirement REQ_61_20_05_008_CryoInterface {
        text = "Cryogenic interface shall provide additional 50 kW heat sink when active.";
        id = "REQ-61-20-05-008";
    }
}

// =============================================================================
// 4. ACTIVITY DIAGRAM (ACT) — Cooling Loop Startup Sequence
// =============================================================================

activity CoolingLoop_Startup {

    action Check_Reservoir_Level;
    action Prime_Pump;
    action Start_Pump_Low_Speed;
    action Verify_Flow_Established;
    action Ramp_Pump_Speed;
    action Open_Heat_Exchanger_Valves;
    action Verify_Thermal_Balance;
    action Enable_Temperature_Control;
    action Report_Ready_Status;

    InitialNode -> Check_Reservoir_Level;
    Check_Reservoir_Level -> Prime_Pump;
    Prime_Pump -> Start_Pump_Low_Speed;
    Start_Pump_Low_Speed -> Verify_Flow_Established;
    Verify_Flow_Established -> Ramp_Pump_Speed;
    Ramp_Pump_Speed -> Open_Heat_Exchanger_Valves;
    Open_Heat_Exchanger_Valves -> Verify_Thermal_Balance;
    Verify_Thermal_Balance -> Enable_Temperature_Control;
    Enable_Temperature_Control -> Report_Ready_Status;
}

// =============================================================================
// 5. PARAMETRIC DIAGRAM (PAR) — Thermal Performance
// =============================================================================

par CoolingLoop_Thermal_Performance {

    // Heat transfer
    constraint c1: Q = m_dot * Cp * (T_out - T_in);
    constraint c2: Q = h * A * LMTD;
    constraint c3: LMTD = (dT1 - dT2) / ln(dT1 / dT2);

    // Pump power
    constraint c4: P_pump = (Q_flow * dP) / eta_pump;
    
    // Heat exchanger effectiveness
    constraint c5: epsilon = Q_actual / Q_max;
    constraint c6: NTU = (U * A) / (m_dot_min * Cp_min);

    // Temperature limits
    constraint c7: T_motor_max = T_coolant_in + Q_motor / (h_motor * A_motor);
    constraint c8: thermalMargin = T_limit - T_actual;

    // Bind parameters
    m_dot -> c1.massFlowRate;
    Cp -> c1.specificHeat;
    T_in -> c1.inletTemp;
    T_out -> c1.outletTemp;
}

// =============================================================================
// 6. STATE MACHINE — Cooling Loop Operating States
// =============================================================================

stm CoolingLoop_States {

    state Off;
    state Priming;
    state LowFlow;
    state NormalOperation;
    state HighLoad;
    state CryoAssist;
    state Fault;
    state EmergencyCooling;

    Off -> Priming : on startup_command;
    Priming -> LowFlow : on flow_established;
    LowFlow -> NormalOperation : on thermal_stabilized;
    NormalOperation -> HighLoad : on heat_load_high;
    HighLoad -> NormalOperation : on heat_load_normal;
    NormalOperation -> CryoAssist : on cryo_available_and_needed;
    CryoAssist -> NormalOperation : on cryo_not_needed;
    HighLoad -> CryoAssist : on cryo_available;
    NormalOperation -> Fault : on pump_failure;
    HighLoad -> EmergencyCooling : on thermal_limit_exceeded;
    Fault -> EmergencyCooling : on backup_pump_start;
    EmergencyCooling -> NormalOperation : on fault_cleared;
    Fault -> Off : on shutdown_command;
}

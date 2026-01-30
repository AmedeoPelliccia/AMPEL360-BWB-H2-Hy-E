/**
 * SysML 1.6 Textual Specification
 * ATA 61-20-04 — Propulsor Control Unit (PCU)
 * 
 * Package: ATA61_PCU
 * Version: 1.0
 * Last Updated: 2025-12-01
 * Standard: OPT-IN Framework v1.2
 */

// =============================================================================
// 1. BLOCK DEFINITION DIAGRAM (BDD) — PCU Structure
// =============================================================================

package ATA61_PCU {

    block Propulsor_Control_Unit {
        part inverter : Power_Inverter;
        part controller : Control_Processor;
        part protection : Protection_Module;
        part communication : Comm_Interface;
        part cooling : PCU_Cooling;
        
        port thrustCommand : ThrustCommand_In;
        port motorControl : MotorControl_Out;
        port telemetry : Telemetry_Out;
        port powerIn : DC_Power_In;
    }

    block Power_Inverter {
        part switchingModule : IGBT_Module[6];  // 3-phase, 2 per phase
        part dcLink : DC_Link_Capacitor;
        part gateDriver : Gate_Driver[6];
        
        value nominalPower : MW = 4;
        value switchingFreq : kHz;
        value efficiency : percent;
        value dcLinkVoltage : V;
    }

    block IGBT_Module {
        value voltageRating : V;
        value currentRating : A;
        value thermalResistance : K_per_W;
        value switchingLoss : J;
        value conductionLoss : W;
    }

    block Control_Processor {
        part mainCPU : Processor;
        part monitorCPU : Processor;           // Dissimilar monitor
        part signalConditioning : ADC_Module;
        part pwmGenerator : PWM_Module;
        
        value processingRate : MHz;
        value controlLoopRate : kHz;
        value diagnosticCoverage : percent;
    }

    block Protection_Module {
        part overcurrentProtection : OC_Circuit;
        part overvoltageProtection : OV_Circuit;
        part thermalProtection : Thermal_Monitor;
        part groundFaultProtection : GF_Circuit;
        
        value tripTime_OC : ms;
        value tripTime_OV : ms;
        value thermalLimit : C;
    }

    block Comm_Interface {
        port afdxPort : AFDX_Port;
        port canPort : CAN_Port;
        port discreteIO : Discrete_IO;
        
        value dataRate : Mbps;
        value latency : ms;
    }

    block PCU_Cooling {
        value heatDissipation : kW;
        value coolantInterface : CoolantPort;
        value maxJunctionTemp : C;
    }
}

// =============================================================================
// 2. INTERNAL BLOCK DIAGRAM (IBD) — PCU Interfaces
// =============================================================================

ibd Propulsor_Control_Unit {

    // Power flow
    powerIn -> dcLink.input;
    dcLink.output -> inverter.dcBus;
    inverter.acOutput -> motorControl;

    // Control flow
    thrustCommand -> controller.commandIn;
    controller.pwmOutput -> gateDriver.input;
    gateDriver.output -> switchingModule.gate;

    // Feedback
    motor.currentFeedback -> signalConditioning.currentIn;
    motor.positionFeedback -> signalConditioning.positionIn;
    signalConditioning.output -> controller.feedback;

    // Protection
    inverter.currentSense -> protection.currentMonitor;
    dcLink.voltageMonitor -> protection.voltageMonitor;
    cooling.tempSensor -> protection.thermalMonitor;
    protection.tripSignal -> controller.emergencyStop;

    // Communication
    controller.telemetryOut -> communication.dataOut;
    communication.afdxPort <-> aircraftBus.afdx;
    communication.canPort <-> healthSensing.can;

    // Thermal management
    inverter.heatSource -> cooling.heatIn;
    cooling.coolantPort <-> coolingLoop.pcuInterface;
}

// =============================================================================
// 3. REQUIREMENTS DIAGRAM (REQ) — PCU Requirements
// =============================================================================

package ATA61_PCU_Requirements {

    requirement REQ_61_20_04_001_Power {
        text = "PCU shall deliver 4 MW continuous power to motor with ≥ 98% efficiency.";
        id = "REQ-61-20-04-001";
    }

    requirement REQ_61_20_04_002_Response {
        text = "Thrust command response time shall be ≤ 50 ms (10% to 90% thrust).";
        id = "REQ-61-20-04-002";
    }

    requirement REQ_61_20_04_003_EMC {
        text = "PCU shall comply with DO-160G Section 21/22 EMC requirements.";
        id = "REQ-61-20-04-003";
    }

    requirement REQ_61_20_04_004_HIRF {
        text = "PCU shall maintain operation under HIRF Level 3 environment per DO-160G Section 20.";
        id = "REQ-61-20-04-004";
    }

    requirement REQ_61_20_04_005_Protection {
        text = "Overcurrent protection shall trip within 10 μs of 200% rated current detection.";
        id = "REQ-61-20-04-005";
    }

    requirement REQ_61_20_04_006_Redundancy {
        text = "PCU shall provide fail-operational capability for single internal failure.";
        id = "REQ-61-20-04-006";
    }

    requirement REQ_61_20_04_007_DAL {
        text = "PCU control software shall be developed to DAL-A per DO-178C.";
        id = "REQ-61-20-04-007";
    }

    requirement REQ_61_20_04_008_Cooling {
        text = "PCU shall dissipate up to 80 kW heat via liquid cooling interface.";
        id = "REQ-61-20-04-008";
    }
}

// =============================================================================
// 4. ACTIVITY DIAGRAM (ACT) — PCU Control Loop
// =============================================================================

activity PCU_Control_Loop {

    action Read_Thrust_Command;
    action Read_Motor_Feedback;
    action Compute_Speed_Error;
    action Execute_PI_Controller;
    action Compute_Current_Reference;
    action Execute_Current_Loop;
    action Generate_PWM;
    action Apply_Gate_Signals;
    action Monitor_Protection;
    action Update_Telemetry;

    InitialNode -> Read_Thrust_Command;
    Read_Thrust_Command -> Read_Motor_Feedback;
    Read_Motor_Feedback -> Compute_Speed_Error;
    Compute_Speed_Error -> Execute_PI_Controller;
    Execute_PI_Controller -> Compute_Current_Reference;
    Compute_Current_Reference -> Execute_Current_Loop;
    Execute_Current_Loop -> Generate_PWM;
    Generate_PWM -> Apply_Gate_Signals;
    Apply_Gate_Signals -> Monitor_Protection;
    Monitor_Protection -> Update_Telemetry;
    Update_Telemetry -> Read_Thrust_Command;  // Loop
}

// =============================================================================
// 5. PARAMETRIC DIAGRAM (PAR) — PCU Power and Efficiency
// =============================================================================

par PCU_Performance_Constraints {

    // Power conversion
    constraint c1: P_out = P_in * eta_inverter;
    constraint c2: P_loss = P_in - P_out;
    constraint c3: eta_inverter = P_out / P_in;

    // Switching losses
    constraint c4: P_sw = f_sw * (E_on + E_off) * 6;  // 6 switches
    constraint c5: P_cond = I_rms^2 * R_ds_on * 6;

    // Thermal
    constraint c6: T_junction = T_coolant + P_loss * R_th_total;
    constraint c7: thermalMargin = T_max - T_junction;

    // DC link
    constraint c8: V_ripple = I_load / (C_dc * f_sw);

    // Bind parameters
    f_sw -> c4.switchFreq;
    I_rms -> c5.rmsCurrent;
    T_coolant -> c6.coolantTemp;
}

// =============================================================================
// 6. STATE MACHINE — PCU Operating States
// =============================================================================

stm PCU_States {

    state Off;
    state Initialization;
    state Standby;
    state Running;
    state Derating;
    state Fault;
    state EmergencyShutdown;

    Off -> Initialization : on power_on;
    Initialization -> Standby : on self_test_pass;
    Initialization -> Fault : on self_test_fail;
    Standby -> Running : on thrust_command_received;
    Running -> Standby : on thrust_zero;
    Running -> Derating : on thermal_limit_approach;
    Derating -> Running : on thermal_recovery;
    Running -> Fault : on protection_trip;
    Derating -> Fault : on protection_trip;
    Fault -> EmergencyShutdown : on critical_fault;
    Fault -> Initialization : on fault_reset;
    EmergencyShutdown -> Off : on safe_state;
}

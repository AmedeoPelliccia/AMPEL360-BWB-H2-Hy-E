/**
 * SysML 1.6 Textual Specification
 * ATA 61 — EDF Propulsor System
 * 
 * Package: ATA61_Propulsors
 * Version: 1.0
 * Last Updated: 2025-12-01
 * Standard: OPT-IN Framework v1.2
 */

// =============================================================================
// 1. BLOCK DEFINITION DIAGRAM (BDD) — EDF Propulsor Structure
// =============================================================================

package ATA61_Propulsors {

    block EDF_Propulsor {
        part motor : Electric_Motor_4MW;
        part ductedFan : Ducted_Fan;
        part blades : Blade_System;
        part cooling : Cooling_Loop;
        part pcu : Propulsor_Control_Unit;
        part sensors : Health_Sensing;
        part nacelle : Nacelle_Structure;
    }

    block Electric_Motor_4MW {
        value powerRating : MW = 4;
        value nominalRPM  : rpm;
        value voltageRange : V;
        value torqueCurve : Curve;
        ref cooling : Cooling_Loop;
    }

    block Ducted_Fan {
        part rotor : Rotor;
        part stator : Stator;
        part spinner : Spinner;
        part duct : Fan_Duct;
        value fanDiameter : m;
        value bladeCount : int;
        value efficiencyMap : Curve;
    }

    block Blade_System {
        value chordDistribution : Curve;
        value twistDistribution : Curve;
        value materialSpec : Material;
        value aeroProfileID : String;
    }

    block Cooling_Loop {
        value coolantType : String;
        value flowRate : kg_per_s;
        value inletTemp : C;
        value outletTemp : C;
    }

    block Propulsor_Control_Unit {
        port controlIn : ThrustCommand;
        port telemetryOut : HealthPacket;
        port powerCtrl : MotorControlLink;
    }

    block Health_Sensing {
        value vibrationSignature : Spectrum;
        value temperatureSensors : TempArray;
        value electricalSignature : EMArray;
    }

    block Nacelle_Structure {
        part frame : Structural_Frame;
        part mounts : Mounting_Set;
    }
}

// =============================================================================
// 2. INTERNAL BLOCK DIAGRAM (IBD) — EDF Propulsor Interfaces
// =============================================================================

ibd EDF_Propulsor {

    motor.powerOutput -> ductedFan.rotor.shaftTorque;
    motor.coolingPort -> cooling.coolantIn;
    cooling.coolantOut -> motor.coolingReturn;

    pcu.powerCtrl <-> motor.controlPort;
    pcu.thrustCommand -> ductedFan.rotor.rpmSetpoint;

    sensors.vibrationProbe -> pcu.healthMonitor;
    sensors.temperatureArray -> cooling.tempMonitor;
    sensors.electricalSignature -> pcu.diagnostics;

    nacelle.frame.mounts <-> motor.mountingPoints;
    nacelle.frame.mounts <-> ductedFan.mountingPoints;
}

// =============================================================================
// 3. REQUIREMENTS DIAGRAM (REQ) — High-level Requirements for ATA 61
// =============================================================================

package ATA61_Requirements {

    requirement REQ_61_001_PowerOutput {
        text = "The EDF propulsor shall provide 4 MW ±3% continuous shaft power.";
        id = "REQ-61-001";
    }

    requirement REQ_61_002_Efficiency {
        text = "Fan assembly shall achieve ≥ 85% propulsive efficiency at cruise condition M0.78/FL410.";
        id = "REQ-61-002";
    }

    requirement REQ_61_003_Acoustics {
        text = "The ducted fan shall meet noise limits according to programme spec ANX-44-A.";
        id = "REQ-61-003";
    }

    requirement REQ_61_004_ThermalLimits {
        text = "Motor windings shall remain below 160°C at all power settings.";
        id = "REQ-61-004";
    }

    requirement REQ_61_005_Safety {
        text = "The propulsor system shall maintain fail-operational thrust capability under single PCU failure.";
        id = "REQ-61-005";
    }
}

// =============================================================================
// 4. ACTIVITY DIAGRAM (ACT) — EDF Startup / Thrust Generation Sequence
// =============================================================================

activity EDF_Start_Sequence {

    action Initialize_PCU;
    action Power_Limits_Check;
    action CoolingLoop_Ready;
    action Motor_Spinup;
    action Fan_RPM_Stabilize;
    action ThrustCommand_Open;
    action Enter_Operational_Mode;

    InitialNode -> Initialize_PCU;
    Initialize_PCU -> Power_Limits_Check;
    Power_Limits_Check -> CoolingLoop_Ready;
    CoolingLoop_Ready -> Motor_Spinup;
    Motor_Spinup -> Fan_RPM_Stabilize;
    Fan_RPM_Stabilize -> ThrustCommand_Open;
    ThrustCommand_Open -> Enter_Operational_Mode;
}

// =============================================================================
// 5. PARAMETRIC DIAGRAM (PAR) — Thrust, Power, Torque, Efficiency
// =============================================================================

par EDF_Performance_Constraints {

    constraint c1: Thrust = f(massFlow, exitVelocity, inletVelocity);
    constraint c2: Torque = f(current, motorConstant, rpm);
    constraint c3: Efficiency = (Thrust * Velocity) / (ElectricalPowerIn);
    constraint c4: MotorHeat = f(I^2 * R);

    massFlow -> c1.massFlow;
    exitVelocity -> c1.exitVelocity;
    inletVelocity -> c1.inletVelocity;

    current -> c2.current;
    motorConstant -> c2.motorConstant;
    rpm -> c2.rpm;

    Thrust -> c3.Thrust;
    Velocity -> c3.Velocity;
    ElectricalPowerIn -> c3.powerIn;

    I -> c4.current;
    R -> c4.resistance;
}

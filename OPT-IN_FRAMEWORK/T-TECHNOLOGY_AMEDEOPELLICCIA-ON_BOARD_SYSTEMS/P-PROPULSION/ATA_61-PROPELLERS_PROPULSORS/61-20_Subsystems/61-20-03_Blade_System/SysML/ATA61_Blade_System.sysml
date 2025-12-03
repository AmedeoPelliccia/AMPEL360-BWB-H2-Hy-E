/**
 * SysML 1.6 Textual Specification
 * ATA 61-20-03 — Blade System
 * 
 * Package: ATA61_BladeSystem
 * Version: 1.0
 * Last Updated: 2025-12-01
 * Standard: OPT-IN Framework v1.2
 */

// =============================================================================
// 1. BLOCK DEFINITION DIAGRAM (BDD) — Blade System Structure
// =============================================================================

package ATA61_BladeSystem {

    block Blade_System {
        part bladeSet : Blade[12];           // 12 blades per fan rotor
        part hubInterface : Hub_Attachment;
        value bladeCount : int = 12;
        value totalBladeWeight : kg;
    }

    block Blade {
        value chordDistribution : Curve;      // Chord vs. span
        value twistDistribution : Curve;      // Twist angle vs. span
        value thicknessDistribution : Curve;  // t/c ratio vs. span
        value materialSpec : Material;
        value aeroProfileID : String;         // Airfoil family identifier
        value spanLength : m;
        value rootChord : m;
        value tipChord : m;
        value sweepAngle : deg;
    }

    block Hub_Attachment {
        value attachmentType : String;        // Dovetail, bolted, bonded
        value retentionLoad : kN;
        value fatigueLife : cycles;
    }

    block Blade_Material {
        value primaryMaterial : String;       // CFRP, Hybrid
        value fiberType : String;             // T800, IM7, etc.
        value resinSystem : String;           // Epoxy, BMI
        value layupSequence : String[];       // Ply angles
        value Vf : percent;                   // Fiber volume fraction
        value density : kg_per_m3;
        value tensileStrength : MPa;
        value compressiveStrength : MPa;
        value fatigueLimit : MPa;
    }

    block Airfoil_Profile {
        value profileID : String;
        value designCL : float;               // Design lift coefficient
        value designMach : float;             // Design Mach number
        value maxThickness : percent;         // Maximum t/c
        value camberLine : Curve;
        value pressureDistribution : Curve;
    }
}

// =============================================================================
// 2. INTERNAL BLOCK DIAGRAM (IBD) — Blade System Interfaces
// =============================================================================

ibd Blade_System {

    // Mechanical interfaces
    blade.rootSection -> hubInterface.bladeSlot;
    hubInterface.retentionBolt -> blade.rootFitting;

    // Aerodynamic flow
    blade.leadingEdge <- airflow.inlet;
    blade.trailingEdge -> airflow.outlet;

    // Structural load paths
    blade.rootSection -> hubInterface.loadTransfer;
    blade.tipSection -> tipClearance.monitor;

    // Health monitoring interfaces
    blade.strainGauges -> healthSensing.strainData;
    blade.surfaceCondition -> healthSensing.damageDetection;
}

// =============================================================================
// 3. REQUIREMENTS DIAGRAM (REQ) — Blade System Requirements
// =============================================================================

package ATA61_BladeSystem_Requirements {

    requirement REQ_61_20_03_001_Efficiency {
        text = "Blade airfoil design shall achieve ≥ 92% isentropic efficiency at design point.";
        id = "REQ-61-20-03-001";
    }

    requirement REQ_61_20_03_002_FOD {
        text = "Blade system shall withstand bird strike per CS-E 800 without catastrophic failure.";
        id = "REQ-61-20-03-002";
    }

    requirement REQ_61_20_03_003_Fatigue {
        text = "Blade root shall demonstrate 10^9 cycle fatigue life with scatter factor of 4.";
        id = "REQ-61-20-03-003";
    }

    requirement REQ_61_20_03_004_Weight {
        text = "Individual blade weight shall not exceed 8 kg (target: 6.5 kg).";
        id = "REQ-61-20-03-004";
    }

    requirement REQ_61_20_03_005_Containment {
        text = "Blade-off event shall be contained within nacelle structure per CS-E 810.";
        id = "REQ-61-20-03-005";
    }

    requirement REQ_61_20_03_006_Recyclability {
        text = "Blade materials shall be ≥ 80% recyclable at end-of-life.";
        id = "REQ-61-20-03-006";
    }
}

// =============================================================================
// 4. ACTIVITY DIAGRAM (ACT) — Blade Manufacturing Process
// =============================================================================

activity Blade_Manufacturing_Process {

    action Layup_Preparation;
    action Fiber_Placement;
    action Resin_Infusion;
    action Autoclave_Cure;
    action Demold_Trim;
    action NDI_Inspection;
    action Surface_Finish;
    action Balance_Check;
    action Final_Inspection;
    action Certification_Release;

    InitialNode -> Layup_Preparation;
    Layup_Preparation -> Fiber_Placement;
    Fiber_Placement -> Resin_Infusion;
    Resin_Infusion -> Autoclave_Cure;
    Autoclave_Cure -> Demold_Trim;
    Demold_Trim -> NDI_Inspection;
    NDI_Inspection -> Surface_Finish;
    Surface_Finish -> Balance_Check;
    Balance_Check -> Final_Inspection;
    Final_Inspection -> Certification_Release;
}

// =============================================================================
// 5. PARAMETRIC DIAGRAM (PAR) — Blade Aerodynamic Performance
// =============================================================================

par Blade_Aero_Performance {

    // Lift and drag
    constraint c1: Lift = 0.5 * rho * V^2 * S * CL;
    constraint c2: Drag = 0.5 * rho * V^2 * S * CD;
    constraint c3: L_D_Ratio = CL / CD;

    // Blade loading
    constraint c4: BladeLoading = Thrust / (bladeCount * bladeArea);
    constraint c5: TipSpeed = omega * tipRadius;
    constraint c6: TipMach = TipSpeed / a;

    // Structural margins
    constraint c7: StressMargin = allowableStress / actualStress;
    constraint c8: FatigueMargin = fatigueLimit / cyclicStress;

    // Bind parameters
    rho -> c1.density;
    V -> c1.velocity;
    S -> c1.area;
    CL -> c1.liftCoeff;
}

// =============================================================================
// 6. STATE MACHINE — Blade Lifecycle States
// =============================================================================

stm Blade_Lifecycle {

    state Manufacturing;
    state QualityCheck;
    state ServiceReady;
    state InService;
    state Inspection;
    state Repair;
    state EndOfLife;

    Manufacturing -> QualityCheck : on pass_NDI;
    QualityCheck -> ServiceReady : on certification_complete;
    ServiceReady -> InService : on installed;
    InService -> Inspection : on scheduled_check;
    Inspection -> InService : on pass;
    Inspection -> Repair : on damage_found;
    Repair -> Inspection : on repair_complete;
    InService -> EndOfLife : on life_limit_reached;
    Inspection -> EndOfLife : on beyond_repair;
}

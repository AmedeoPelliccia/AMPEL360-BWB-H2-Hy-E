# 23-80 Integrated Automatic Tuning

## Briefing

Automatic tuning/selection support (radio tuning integration, frequency management aids) where implemented—often tightly coupled to avionics integration policies.

## Table of Contents (Suggested)

1. **Functional Scope**
   - What "automatic tuning" controls
   - What it never controls
   - System boundaries
   - Operational modes

2. **Interfaces to Radio Subsystems**
   - Cross-reference to 23-10 (Speech Communications)
   - Radio control interfaces
   - Frequency selection logic
   - Tuning commands and feedback

3. **Interfaces to Avionics Databases**
   - Cross-reference to ATA 34 (Navigation)
   - Navigation database integration
   - Frequency database management
   - Database update procedures

4. **HMI Rules**
   - Pilot authority and control
   - Inhibit conditions
   - Override logic
   - Mode annunciation

5. **Failure Modes**
   - Mis-tune prevention
   - Stale database protection
   - Fallback to manual tuning
   - Error detection and handling

6. **Verification and Validation**
   - Correctness tests (scenario-based)
   - Override priority testing
   - Regression suite
   - Database integrity testing

## BWB + H₂ Considerations

- **System Integration**: Consider integration with advanced avionics architecture in BWB
- **Database Management**: Ensure robust frequency database management
- **Pilot Interface**: Clear HMI design for automatic tuning in BWB cockpit layout

## Subject Structure

This section contains:
- `23-80-00-integrated-automatic-tuning-general/` — General integrated automatic tuning documentation

## Document Control

- **ATA Chapter**: 23
- **Section**: 23-80
- **Title**: Integrated Automatic Tuning
- **Status**: Active
- **Standard**: ATA iSpec 2200 SNS Extract (Revision 2024-1)
- **Last Updated**: 2026-01-09
- **Generated with AI assistance**: GitHub Copilot, prompted by Amedeo Pelliccia

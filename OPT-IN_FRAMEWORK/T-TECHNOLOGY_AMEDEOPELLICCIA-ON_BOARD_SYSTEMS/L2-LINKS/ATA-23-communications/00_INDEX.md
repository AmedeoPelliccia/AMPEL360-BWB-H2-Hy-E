# ATA 23 — Communications — Subject Code Index (00_INDEX.md)

**Version:** 1.0  
**Date:** 2026-01-09  
**Purpose:** Complete subject (yy) code mapping for ATA 23 Communications

---

## Quick Reference

| Section | Code Range | Description |
|---------|------------|-------------|
| 23-00 | 00-10, 90-92 | Communications General |
| 23-10 | 00-07, 10, 90 | Speech Communications |
| 23-15 | 00-07, 10 | SATCOM |
| 23-20 | 00-08, 10 | Data Transmission and Automatic Calling |
| 23-30 | 00-07, 10 | Passenger Address, Entertainment and Comfort |
| 23-40 | 00-06, 10 | Interphone |
| 23-50 | 00-06, 10, 90 | Audio Integrating |
| 23-60 | 00-04, 10 | Static Discharging |
| 23-70 | 00-05, 10 | Audio and Video Monitoring |
| 23-80 | 00-04, 10 | Integrated Automatic Tuning |

---

## 23-00 — Communications General

Foundation and architecture for the communications system.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-00-00 | Chapter overview | Comms chapter general landing topic | `23-00-00-chapter-overview/` |
| 23-00-01 | Scope & boundaries | What is ATA 23 vs ATA 31/34/42/46 | `23-00-01-scope-boundaries/` |
| 23-00-02 | High-level architecture | Voice/data/cabin/service partitioning | `23-00-02-high-level-architecture/` |
| 23-00-03 | Network segmentation | Flight deck / cabin / maintenance domains | `23-00-03-network-segmentation/` |
| 23-00-04 | Antenna/RF placement philosophy | Placement drivers (incl. BWB constraints) | `23-00-04-antenna-rf-placement-philosophy/` |
| 23-00-05 | Power/cooling/environment interfaces | ATA 24/21 dependencies | `23-00-05-power-cooling-environment-interfaces/` |
| 23-00-06 | HMI/annunciation overview | Interfaces to ATA 31 | `23-00-06-hmi-annunciation-overview/` |
| 23-00-07 | Maintainability & BITE overview | Troubleshooting philosophy | `23-00-07-maintainability-bite-overview/` |
| 23-00-08 | Cyber/security cross-reference | Link to B30/ATA-46 governance | `23-00-08-cyber-security-cross-reference/` |
| 23-00-09 | Compliance basis | Regulatory & standards assumptions | `23-00-09-compliance-basis/` |
| 23-00-10 | Verification strategy | Analysis/test/inspection top approach | `23-00-10-verification-strategy/` |
| 23-00-90 | EMC/EMI program delta | HV switching/inverter noise environment | `23-00-90-emc-emi-program-delta/` |
| 23-00-91 | BWB antenna blockage delta | Shadowing/blockage/structure integration | `23-00-91-bwb-antenna-blockage-program-delta/` |
| 23-00-92 | Domain segregation delta | Safety vs cabin vs maintenance isolation | `23-00-92-domain-segregation-program-delta/` |

---

## 23-10 — Speech Communications

Voice communication systems (VHF, HF, audio endpoints).

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-10-00 | Speech comms overview | Section-level overview | `23-10-00-speech-communications-overview/` |
| 23-10-01 | Functions & modes | Normal/alternate/degraded | `23-10-01-functions-and-modes/` |
| 23-10-02 | VHF voice radios | Architecture + tuning/channel policy | `23-10-02-vhf-voice-radios/` |
| 23-10-03 | HF voice radios | If applicable + SELCAL interplay | `23-10-03-hf-voice-radios/` |
| 23-10-04 | Antennas & RF distribution | Diversity, cabling, placement | `23-10-04-antennas-and-rf-distribution/` |
| 23-10-05 | Audio endpoints | mics/headsets/sidetone endpoints | `23-10-05-audio-endpoints/` |
| 23-10-06 | Recording/monitoring policy | Recorder feed rules (if used) | `23-10-06-recording-monitoring-policy/` |
| 23-10-07 | Failures & crew procedures | Alerts, dispatch impacts | `23-10-07-failures-and-crew-procedures/` |
| 23-10-90 | EMC/EMI constraints | Susceptibility + mitigation requirements | `23-10-90-emc-emi-constraints/` |
| 23-10-10 | V&V | Coverage, audio quality, interference tests | `23-10-10-verification-and-validation/` |

---

## 23-15 — SATCOM

Satellite communication (voice, ACARS, IP data).

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-15-00 | SATCOM overview | Section-level overview | `23-15-00-satcom-overview/` |
| 23-15-01 | Service scope | Voice / ACARS / IP data (as applicable) | `23-15-01-service-scope/` |
| 23-15-02 | Antenna/radome/steering | Blockage zones, pointing, BWB effects | `23-15-02-antenna-radome-steering/` |
| 23-15-03 | RF chain | SDU, HPA/LNA, diplexers, cabling | `23-15-03-rf-chain/` |
| 23-15-04 | Network interfaces | Router/IMA integration model | `23-15-04-network-interfaces/` |
| 23-15-05 | Security policy | creds/keys/domain separation references | `23-15-05-security-policy/` |
| 23-15-06 | Fault handling | reacquisition, fallback, inhibits | `23-15-06-fault-handling/` |
| 23-15-07 | Dispatch/MEL | availability assumptions and rules | `23-15-07-dispatch-mel/` |
| 23-15-10 | V&V | coverage/handover/blockage/thermal/power | `23-15-10-verification-and-validation/` |

---

## 23-20 — Data Transmission and Automatic Calling

Datalink (ATSU/CMU), ACARS, VDL, SELCAL.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-20-00 | Datalink overview | Section-level overview | `23-20-00-datalink-overview/` |
| 23-20-01 | Datalink functional scope | addressing, store/forward, services | `23-20-01-functional-scope/` |
| 23-20-02 | ATSU/CMU architecture | hosting and partitioning | `23-20-02-atsu-cmu-architecture/` |
| 23-20-03 | Bearers & interfaces | VDL/SATCOM bearer integration | `23-20-03-bearers-and-interfaces/` |
| 23-20-04 | Automatic calling | SELCAL and related automation | `23-20-04-automatic-calling-selcal/` |
| 23-20-05 | Message security & integrity | assumptions + controls references | `23-20-05-message-security-and-integrity/` |
| 23-20-06 | Integration cross-refs | FMS (ATA 34), HMI (ATA 31) | `23-20-06-integration-cross-references/` |
| 23-20-07 | Logging/traceability | ops/compliance logging rules | `23-20-07-logging-and-traceability/` |
| 23-20-08 | Failure modes | loss/duplication/stale/reroute | `23-20-08-failure-modes/` |
| 23-20-10 | V&V | latency/throughput/reliability/cyber tests | `23-20-10-verification-and-validation/` |

---

## 23-30 — Passenger Address, Entertainment and Comfort

Cabin communications, PA, IFE boundaries.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-30-00 | Cabin comms overview | Section-level overview | `23-30-00-cabin-comms-overview/` |
| 23-30-01 | PA architecture | control, crew stations, zoning | `23-30-01-pa-architecture/` |
| 23-30-02 | Audio distribution & priority | PA vs chime vs IFE mixing | `23-30-02-audio-distribution-and-priority/` |
| 23-30-03 | Cabin segmentation | safety-critical isolation policy | `23-30-03-cabin-segmentation/` |
| 23-30-04 | IFE boundary | what's in/out of ATA 23 scope | `23-30-04-ife-boundary/` |
| 23-30-05 | Crew ops modes | crew procedures/interactions | `23-30-05-crew-ops-modes/` |
| 23-30-06 | Emergency/fallback power | behavior on loss of power | `23-30-06-emergency-fallback-power/` |
| 23-30-07 | Maintenance/content loading | if in scope | `23-30-07-maintenance-content-loading/` |
| 23-30-10 | V&V | intelligibility/coverage/priority tests | `23-30-10-verification-and-validation/` |

---

## 23-40 — Interphone

Flight, cabin, service, and maintenance interphone systems.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-40-00 | Interphone overview | Section-level overview | `23-40-00-interphone-overview/` |
| 23-40-01 | Interphone types | flight/cabin/service/maintenance | `23-40-01-interphone-types/` |
| 23-40-02 | Station hardware | handsets/jacks/call panels | `23-40-02-station-hardware/` |
| 23-40-03 | Routing & priority | call routing/alerting logic | `23-40-03-routing-and-priority/` |
| 23-40-04 | Audio integration | ties to 23-50 | `23-40-04-audio-integration/` |
| 23-40-05 | Emergency/alt power | ATA 24 dependencies | `23-40-05-emergency-alternate-power/` |
| 23-40-06 | BITE/troubleshooting | maintenance concept | `23-40-06-bite-and-troubleshooting/` |
| 23-40-10 | V&V | call setup/audio/priority tests | `23-40-10-verification-and-validation/` |

---

## 23-50 — Audio Integrating

Audio Management Unit (AMU), Audio Control Panel (ACP).

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-50-00 | Audio integrating overview | Section-level overview | `23-50-00-audio-integrating-overview/` |
| 23-50-01 | AMU/ACP concept | audio management unit architecture | `23-50-01-amu-acp-concept/` |
| 23-50-02 | I/O inventory | radios/interphone/alerts/recorder feeds | `23-50-02-io-inventory/` |
| 23-50-03 | Mixing & priority rules | muting/volume law | `23-50-03-mixing-and-priority-rules/` |
| 23-50-04 | Crew controls/HMI | panels and conventions | `23-50-04-crew-controls-hmi/` |
| 23-50-05 | BITE & degradation | fault isolation + degrade matrix | `23-50-05-bite-and-degradation/` |
| 23-50-06 | Warning/annunciation interface | ATA 31 coupling | `23-50-06-warning-annunciation-interface/` |
| 23-50-90 | EMC/EMI & noise management | electric propulsion noise environment | `23-50-90-emc-emi-and-noise-management/` |
| 23-50-10 | V&V | priority, intelligibility, distortion, FI tests | `23-50-10-verification-and-validation/` |

---

## 23-60 — Static Discharging

Static discharge devices (wicks) and bonding/grounding.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-60-00 | Static discharging overview | Section-level overview | `23-60-00-static-discharging-overview/` |
| 23-60-01 | Scope boundary | vs lightning/HIRF/structures governance | `23-60-01-scope-boundary/` |
| 23-60-02 | Device inventory & placement | wicks/bonding points logic | `23-60-02-device-inventory-and-placement/` |
| 23-60-03 | Bonding/grounding impacts | RF performance interaction | `23-60-03-bonding-grounding-impacts/` |
| 23-60-04 | Inspection/maintenance | intervals and acceptance criteria | `23-60-04-inspection-and-maintenance/` |
| 23-60-10 | V&V | noise reduction evidence/inspection tests | `23-60-10-verification-and-validation/` |

---

## 23-70 — Audio and Video Monitoring

Cabin/door/service monitoring (cameras, audio feeds).

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-70-00 | Monitoring overview | Section-level overview | `23-70-00-monitoring-overview/` |
| 23-70-01 | Use-cases | cabin/door/service monitoring | `23-70-01-use-cases/` |
| 23-70-02 | Video chain | cameras/encoders/displays/storage | `23-70-02-video-chain/` |
| 23-70-03 | Audio monitoring | sources and access controls | `23-70-03-audio-monitoring/` |
| 23-70-04 | Privacy/security policy | explicit governance references | `23-70-04-privacy-security-policy/` |
| 23-70-05 | Failure/dispatch impacts | degradation and MEL logic | `23-70-05-failure-and-dispatch-impacts/` |
| 23-70-10 | V&V | latency/quality/access verification | `23-70-10-verification-and-validation/` |

---

## 23-80 — Integrated Automatic Tuning

Automatic radio tuning and database integration.

| ATA Code | Subject Title (yy) | Covers TOC Point | Folder |
|----------|-------------------|------------------|--------|
| 23-80-00 | Auto tuning overview | Section-level overview | `23-80-00-auto-tuning-overview/` |
| 23-80-01 | Functional scope & limits | what is/ isn't automated | `23-80-01-functional-scope-and-limits/` |
| 23-80-02 | Interfaces | radios (23-10) + databases (ATA 34) | `23-80-02-interfaces/` |
| 23-80-03 | HMI authority rules | inhibit/override behavior | `23-80-03-hmi-authority-rules/` |
| 23-80-04 | Failure modes | mis-tune prevention, stale data | `23-80-04-failure-modes/` |
| 23-80-10 | V&V | correctness + regression suite | `23-80-10-verification-and-validation/` |

---

## Naming Convention

Folder names follow the pattern:

```
23-{xx}-{yy}-{descriptive-slug}
```

Where:
- `xx` = section code (00, 10, 15, 20, 30, 40, 50, 60, 70, 80)
- `yy` = subject code (00-10, 90-99 for program-specific deltas)
- `descriptive-slug` = human-readable kebab-case description

**Example:** `23-10-02-vhf-voice-radios/`

The two-digit `yy` code remains stable even if the descriptive slug is refined later, ensuring deterministic folder names and traceability.

---

## Program-Specific Delta Codes (yy=90-99)

Reserved for **AMPEL360-specific deltas** to avoid collisions with official SNS extracts:

| Code | Usage | Sections Using |
|------|-------|----------------|
| 90 | EMC/EMI considerations (electric propulsion environment) | 23-00, 23-10, 23-50 |
| 91 | BWB antenna blockage and shadowing | 23-00 |
| 92 | Domain segregation (safety/cabin/maintenance) | 23-00 |
| 93-99 | Reserved for future program-specific needs | — |

---

## Cross-References by Topic

### BWB-Specific
- **23-00-04**: Antenna/RF placement philosophy
- **23-00-91**: BWB antenna blockage delta
- **23-15-02**: Antenna/radome/steering (blockage zones)

### Electric Propulsion Environment
- **23-00-90**: EMC/EMI program delta
- **23-10-90**: Speech comms EMC/EMI constraints
- **23-50-90**: Audio integrating EMC/EMI & noise management

### Security & Cyber
- **23-00-08**: Cyber/security cross-reference
- **23-00-92**: Domain segregation delta
- **23-15-05**: SATCOM security policy
- **23-20-05**: Message security & integrity
- **23-70-04**: Privacy/security policy (monitoring)

### Safety-Critical
- **23-00-03**: Network segmentation
- **23-00-92**: Domain segregation delta
- **23-30-03**: Cabin segmentation
- All **LC07_Safety** folders in SSOT

### Verification & Validation
- All subjects with **yy=10**: V&V folders
- **23-00-10**: Verification strategy (top-level)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document** | ATA 23 Subject Code Index |
| **Version** | 1.0 |
| **Date** | 2026-01-09 |
| **Status** | Active |
| **Owner** | AMPEL360 Communications System WG |
| **Repository** | AMPEL360-AIR-T |
| **Related** | README.md, ATA_03_NUMBERING_GUIDE.md |

---

## Usage Notes

1. **Adding a new subject:** Use the next available `yy` code in the appropriate section, or use 93-99 for program-specific needs.
2. **Reconciliation with SNS:** If official SNS codes are provided, update this index and rename folders accordingly.
3. **Traceability:** Always reference the full ATA code (e.g., 23-10-02) in requirements, design documents, and test cases.
4. **Navigation:** Use this index to locate the correct subject folder before creating or updating documentation.

---

**For narrative overview, see:** [README.md](./README.md)

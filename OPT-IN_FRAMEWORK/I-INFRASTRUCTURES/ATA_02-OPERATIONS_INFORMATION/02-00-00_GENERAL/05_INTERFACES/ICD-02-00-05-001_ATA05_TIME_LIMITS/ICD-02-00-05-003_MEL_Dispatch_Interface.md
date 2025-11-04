# ICD-02-00-05-003: MEL Dispatch Interface

**Version:** 1.0.0  
**Status:** Active

## Interface Description

Interface between operations (ATA 02) and Minimum Equipment List (MEL) requirements (ATA 05) to manage aircraft dispatch with inoperative equipment.

## Purpose

This interface ensures:
- MEL compliance for all dispatches
- Proper documentation of deferred maintenance
- Time limitations properly tracked
- Operational procedures followed
- Flight crew awareness of restrictions

## Data Flows

### Maintenance → Operations
- MEL item entries (equipment inoperative)
- Time limitation details (A, B, C, D category)
- Operational restrictions or procedures
- Repair status updates
- MEL item closures

### Operations → Maintenance
- MEL item compliance tracking
- Time expiry alerts
- Operational feedback
- Crew-reported issues
- Dispatch decisions

## MEL Categories

### Category A - No Time Limit
- May be inoperative indefinitely
- Must comply with all notes/restrictions
- Repair at next scheduled maintenance opportunity

**Example:** Passenger reading lights (non-safety)

### Category B - 3 Calendar Days
- May be inoperative for 3 consecutive calendar days
- Operations must ensure repair before expiry
- May be extended once by 3 days with approval

**Example:** Single navigation light, APU (if redundancy exists)

### Category C - 10 Calendar Days
- May be inoperative for 10 consecutive calendar days
- Longer time allows scheduling for parts/resources
- Must track carefully to avoid expiry

**Example:** TCAS, weather radar (with restrictions)

### Category D - 120 Calendar Days
- Long-term deferrals for non-critical items
- Usually cosmetic or passenger comfort items
- Repair at next heavy maintenance check

**Example:** Cabin interior items, IFE components

## H2 System MEL Items

### Critical (No Dispatch)
- Primary H2 leak detection system
- Tank pressure control system
- Emergency vent system
- Fuel quantity indication (both channels)

### Category B (3 days)
- Single H2 temperature sensor (with redundancy)
- Backup leak detection channel
- Secondary tank pressure indicator
- Refueling port auxiliary systems

### Category C (10 days)
- H2 system advisory indications (with procedures)
- Non-critical monitoring functions
- Secondary safety margins

## Fuel Cell MEL Items

### Critical (No Dispatch)
- Fuel cell shutdown system (any stack)
- Thermal management control
- Power distribution system
- Emergency power mode

### Category B (3 days)
- Single fuel cell stack (with reduced power operations)
- Backup thermal sensor (with redundancy)
- Non-critical monitoring systems

### Category C (10 days)
- Performance monitoring systems
- Fuel cell advisory indications
- Non-critical power management features

## Interface Requirements

**RQ-ICD-02-05-020:** MEL entries visible to flight crew within 15 minutes  
**RQ-ICD-02-05-021:** Time expiry alerts at 50% and 80% of limit  
**RQ-ICD-02-05-022:** No dispatch allowed past MEL time limit  
**RQ-ICD-02-05-023:** CAOS automatic tracking and notification

## Dispatch Process

### 1. MEL Item Identified
- Maintenance identifies inoperative equipment
- MEL category determined
- Entry made in aircraft logbook
- Operations notified via CAOS

### 2. Dispatch Decision
- Flight crew reviews MEL items
- Operational restrictions evaluated
- Dispatch decision made
- Crew briefed on restrictions/procedures

### 3. In-Flight Monitoring
- Crew follows MEL procedures
- Any changes documented
- Operations control monitors status

### 4. Post-Flight Actions
- Flight crew reports any issues
- Maintenance updates status
- Time tracking updated
- Next flight crew briefed

## CAOS Integration

### Automated Tracking
- Real-time MEL item status display
- Automatic time expiry calculations
- Alert notifications to relevant personnel
- Integration with maintenance planning

### Predictive Analysis
- Identifies systems with repeat MEL items
- Recommends proactive maintenance
- Optimizes repair scheduling
- Tracks fleet-wide MEL trends

## Operational Restrictions

### Common MEL Procedures

**H2 Leak Detection (Backup Channel Inoperative):**
- Visual inspection of H2 system before each flight
- Monitor H2 system parameters closely
- Land at nearest suitable airport if primary channel fails

**Single Fuel Cell Stack Inoperative:**
- Reduced maximum power available (75% normal)
- Do not operate above FL350
- Plan for reduced climb performance
- Extended alternate required (ETOPS not allowed)

**CAOS Advisory Functions Inoperative:**
- Manual performance calculations required
- Conventional fuel planning procedures
- Standard operational procedures (no AI optimization)

## Communication Protocol

**MEL Entry:** Aircraft logbook + CAOS system  
**Crew Notification:** Pre-flight briefing + EFB display  
**Operations:** CAOS operations dashboard  
**Maintenance:** Maintenance control system integration

## Key Performance Indicators

| KPI | Target | Measurement |
|-----|--------|-------------|
| MEL Compliance | 100% | No time overruns |
| Average MEL Age | <5 days | Time to repair |
| Repeat MEL Rate | <2% | Same item within 30 days |
| Category B Expiry | 0 | Allowed to expire |

## Documentation

- Aircraft Logbook (master record)
- MEL Database (CAOS)
- Flight Release Document
- Crew Pre-Flight Briefing
- Post-Flight Report

---

**Document Status:** ✅ Active  
**Last Updated:** 2025-11-04

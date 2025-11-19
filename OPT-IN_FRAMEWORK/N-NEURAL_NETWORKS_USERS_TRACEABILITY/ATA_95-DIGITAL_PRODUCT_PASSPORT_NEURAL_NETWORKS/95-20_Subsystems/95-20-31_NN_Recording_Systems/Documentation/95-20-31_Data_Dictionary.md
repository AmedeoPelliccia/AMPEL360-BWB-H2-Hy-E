# 95-20-31 NN Recording Systems – Data Dictionary

**Version**: 1.0  
**Status**: DRAFT  
**Last Updated**: 2025-11-18

## Overview

This document defines all data structures, schemas, and terminology used in the NN Recording Systems subsystem.

## CVR Data Structures

### CVR Audio
- **Format**: WAV/PCM
- **Sample Rate**: 16 kHz (minimum per CS-25.1457)
- **Bit Depth**: 16-bit
- **Channels**: 4 (Captain, First Officer, Area Mic, Spare)
- **Duration**: 25 hours retention (regulatory requirement)

### CVR Transcript
```yaml
CVRTranscript:
  utterances: List[Utterance]
  metadata: TranscriptMetadata

Utterance:
  start_time: float  # seconds from recording start
  end_time: float
  speaker: Speaker  # enum: captain, first_officer, atc, other
  text: string
  confidence: float  # 0.0 to 1.0
  keywords: List[string]

TranscriptMetadata:
  total_duration: float
  speakers_detected: List[Speaker]
  processing_time: float
  model_version: string
```

## FDR Data Structures

### FDR Parameters
```yaml
FDRParameter:
  param_id: string  # e.g., "N1_ENG1"
  param_name: string  # e.g., "Engine 1 N1 Speed"
  unit: string  # e.g., "%", "°C", "psi"
  sample_rate_hz: float  # e.g., 8.0
  range_min: float
  range_max: float
  criticality: Criticality  # enum: critical, high, medium, low

FDRDataPoint:
  timestamp: datetime  # ISO 8601 UTC
  value: float
  quality: DataQuality  # enum: valid, suspect, invalid
```

### Anomaly Detection
```yaml
Anomaly:
  anomaly_id: string
  start_time: datetime
  end_time: datetime
  anomaly_score: float  # 0.0 to 1.0
  classification: AnomalyClass  # enum: engine, flight_controls, etc.
  affected_parameters: List[string]
  severity: Severity  # enum: critical, high, medium, low
  explanation: AnomalyExplanation
  confidence: float

AnomalyExplanation:
  primary_contributor: string  # parameter ID
  contribution_score: float
  description: string
```

## Event Data Structures

### Event Segment
```yaml
EventSegment:
  event_id: string
  start_time: datetime
  end_time: datetime
  duration: float  # seconds
  classification: EventClass  # enum: safety_critical, operational, etc.
  sub_type: string  # e.g., "atc_interaction", "go_around"
  priority: float  # 0.0 to 1.0
  description: string
  confidence: float
  sources: EventSources

EventSources:
  cvr_segments: List[CVRSegment]
  fdr_anomalies: List[Anomaly]
  manual_flags: List[ManualFlag]
```

## Enumerations

### Speaker
```yaml
Speaker:
  CAPTAIN: "captain"
  FIRST_OFFICER: "first_officer"
  ATC: "atc"
  OTHER: "other"
```

### Flight Phase
```yaml
FlightPhase:
  GROUND: "ground"
  TAXI: "taxi"
  TAKEOFF: "takeoff"
  CLIMB: "climb"
  CRUISE: "cruise"
  DESCENT: "descent"
  APPROACH: "approach"
  LANDING: "landing"
```

### Anomaly Classification
```yaml
AnomalyClass:
  ENGINE: "engine"
  FLIGHT_CONTROLS: "flight_controls"
  HYDRAULICS: "hydraulics"
  ELECTRICAL: "electrical"
  ENVIRONMENTAL: "environmental"
  STRUCTURAL: "structural"
  MULTIPLE: "multiple"
```

### Event Classification
```yaml
EventClass:
  SAFETY_CRITICAL: "safety_critical"  # GPWS, TCAS, stall, etc.
  OPERATIONAL: "operational"  # Go-around, rejected takeoff
  SYSTEM: "system"  # Malfunctions, warnings
  COMMUNICATION: "communication"  # ATC interactions
  WEATHER: "weather"  # Turbulence, icing
  TRAINING: "training"  # SOP deviations for training review
```

### Severity
```yaml
Severity:
  CRITICAL: "critical"
  HIGH: "high"
  MEDIUM: "medium"
  LOW: "low"
```

### Data Quality
```yaml
DataQuality:
  VALID: "valid"
  SUSPECT: "suspect"
  INVALID: "invalid"
```

### Criticality
```yaml
Criticality:
  CRITICAL: "critical"  # Safety-critical, must be lossless
  HIGH: "high"  # Important for analysis
  MEDIUM: "medium"  # Useful but not essential
  LOW: "low"  # Minimal importance
```

## Database Schema (Conceptual)

### Recordings Table
```sql
CREATE TABLE recordings (
  recording_id UUID PRIMARY KEY,
  aircraft_reg VARCHAR(10),
  flight_number VARCHAR(20),
  departure_airport CHAR(4),
  arrival_airport CHAR(4),
  departure_time TIMESTAMP,
  arrival_time TIMESTAMP,
  cvr_file_path VARCHAR(255),
  fdr_file_path VARCHAR(255),
  processing_status VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Transcripts Table
```sql
CREATE TABLE transcripts (
  transcript_id UUID PRIMARY KEY,
  recording_id UUID REFERENCES recordings(recording_id),
  start_time FLOAT,
  end_time FLOAT,
  speaker VARCHAR(20),
  text TEXT,
  confidence FLOAT,
  keywords TEXT[],
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Anomalies Table
```sql
CREATE TABLE anomalies (
  anomaly_id UUID PRIMARY KEY,
  recording_id UUID REFERENCES recordings(recording_id),
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  classification VARCHAR(50),
  severity VARCHAR(20),
  anomaly_score FLOAT,
  affected_parameters TEXT[],
  description TEXT,
  confidence FLOAT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Events Table
```sql
CREATE TABLE events (
  event_id UUID PRIMARY KEY,
  recording_id UUID REFERENCES recordings(recording_id),
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  classification VARCHAR(50),
  sub_type VARCHAR(50),
  priority FLOAT,
  description TEXT,
  confidence FLOAT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## File Formats

### Parquet Schema (Training Data)

**CVR Annotated Audio**:
```
├── audio_ch1: binary
├── audio_ch2: binary
├── audio_ch3: binary
├── audio_ch4: binary
├── transcript: string
├── speaker_labels: list<string>
├── event_tags: list<string>
├── flight_phase: string
├── timestamp: timestamp[us, tz=UTC]
└── metadata: struct<...>
```

**FDR Events and Labels**:
```
├── timestamp: timestamp[us, tz=UTC]
├── flight_id: string
├── parameters: map<string, double>
├── anomaly_label: int8  # 0=normal, 1=anomaly
├── anomaly_type: string
├── flight_phase: string
└── metadata: struct<...>
```

## Units and Conventions

### Time
- All timestamps in **ISO 8601 UTC**
- Durations in **seconds** (float)
- Sample rates in **Hz** (float)

### Confidence Scores
- Range: **0.0 to 1.0**
- 0.0 = no confidence, 1.0 = maximum confidence
- Threshold for flagging low confidence: **< 0.8**

### Priority Scores
- Range: **0.0 to 1.0**
- 0.0 = lowest priority, 1.0 = highest priority
- High priority threshold: **> 0.7**

## Document Control

- **Version**: 1.0
- **Status**: DRAFT
- **Last Updated**: 2025-11-18
- **AI Assistance**: Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Human approver**: _[to be completed]_.

---

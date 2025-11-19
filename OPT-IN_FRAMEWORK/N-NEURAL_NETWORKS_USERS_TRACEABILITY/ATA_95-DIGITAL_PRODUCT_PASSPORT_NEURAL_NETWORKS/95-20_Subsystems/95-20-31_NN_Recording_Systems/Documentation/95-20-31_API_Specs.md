# 95-20-31 NN Recording Systems – API Specifications

**Version**: 1.0  
**Status**: DRAFT  
**Last Updated**: 2025-11-18

## Overview

This document specifies the application programming interfaces (APIs) for the NN Recording Systems subsystem components.

## CVR Transcription API

### Endpoint: `/v1/recording/cvr/transcribe`

**Method**: POST  
**Description**: Transcribe CVR audio to text with speaker labels and event tags

**Request**:
```json
{
  "audio_channels": [
    {
      "channel_id": 1,
      "audio_data": "<base64-encoded WAV>",
      "sample_rate": 16000
    }
  ],
  "flight_metadata": {
    "flight_phase": "cruise",
    "timestamp": "2025-11-18T12:00:00Z"
  },
  "options": {
    "enable_keyword_detection": true,
    "speaker_diarization": true,
    "language": "en-US"
  }
}
```

**Response**:
```json
{
  "transcript": [
    {
      "start_time": 0.0,
      "end_time": 3.5,
      "speaker": "captain",
      "text": "Autopilot engaged, maintain flight level three five zero",
      "confidence": 0.95,
      "keywords": ["autopilot"]
    }
  ],
  "summary": {
    "total_duration": 120.0,
    "speakers_detected": ["captain", "first_officer"],
    "keywords_found": ["autopilot", "atc_contact"],
    "processing_time": 36.0
  }
}
```

**Status Codes**:
- 200: Success
- 400: Invalid request
- 413: Audio too large
- 500: Processing error

## FDR Anomaly Detection API

### Endpoint: `/v1/recording/fdr/detect_anomalies`

**Method**: POST  
**Description**: Detect anomalies in FDR parameter data

**Request**:
```json
{
  "parameters": [
    {
      "param_id": "N1_ENG1",
      "values": [95.2, 95.3, 95.1, ...],
      "timestamps": ["2025-11-18T12:00:00Z", ...],
      "sample_rate_hz": 8
    }
  ],
  "flight_metadata": {
    "flight_phase": "cruise",
    "aircraft_config": "normal"
  },
  "options": {
    "sensitivity": 0.95,
    "return_explanations": true
  }
}
```

**Response**:
```json
{
  "anomalies": [
    {
      "anomaly_id": "anom-001",
      "start_time": "2025-11-18T12:05:00Z",
      "end_time": "2025-11-18T12:07:00Z",
      "anomaly_score": 0.87,
      "classification": "engine",
      "affected_parameters": ["N1_ENG1", "EGT_ENG1"],
      "severity": "medium",
      "explanation": {
        "primary_contributor": "N1_ENG1",
        "contribution_score": 0.75,
        "description": "Unexpected N1 fluctuation during stable cruise"
      },
      "confidence": 0.92
    }
  ],
  "summary": {
    "total_anomalies": 1,
    "critical_count": 0,
    "high_count": 0,
    "medium_count": 1,
    "low_count": 0,
    "processing_time": 1.2
  }
}
```

**Status Codes**:
- 200: Success
- 400: Invalid request
- 422: Invalid parameter data
- 500: Processing error

## Event Segmentation API

### Endpoint: `/v1/recording/events/segment`

**Method**: POST  
**Description**: Segment recording into events of interest

**Request**:
```json
{
  "cvr_transcript": { /* from CVR API */ },
  "fdr_anomalies": { /* from FDR API */ },
  "flight_duration": 7200,
  "options": {
    "min_event_duration": 10,
    "priority_threshold": 0.7
  }
}
```

**Response**:
```json
{
  "events": [
    {
      "event_id": "evt-001",
      "start_time": "2025-11-18T12:05:00Z",
      "end_time": "2025-11-18T12:07:30Z",
      "classification": "operational",
      "sub_type": "atc_interaction",
      "priority": 0.6,
      "description": "ATC frequency change and contact",
      "confidence": 0.88
    }
  ],
  "summary": {
    "total_events": 15,
    "high_priority": 2,
    "medium_priority": 5,
    "low_priority": 8,
    "processing_time": 45.0
  }
}
```

**Status Codes**:
- 200: Success
- 400: Invalid request
- 500: Processing error

## Common Data Types

### Speaker Type
```typescript
enum Speaker {
  CAPTAIN = "captain",
  FIRST_OFFICER = "first_officer",
  ATC = "atc",
  OTHER = "other"
}
```

### Flight Phase
```typescript
enum FlightPhase {
  GROUND = "ground",
  TAXI = "taxi",
  TAKEOFF = "takeoff",
  CLIMB = "climb",
  CRUISE = "cruise",
  DESCENT = "descent",
  APPROACH = "approach",
  LANDING = "landing"
}
```

### Anomaly Classification
```typescript
enum AnomalyClassification {
  ENGINE = "engine",
  FLIGHT_CONTROLS = "flight_controls",
  HYDRAULICS = "hydraulics",
  ELECTRICAL = "electrical",
  ENVIRONMENTAL = "environmental",
  STRUCTURAL = "structural",
  MULTIPLE = "multiple"
}
```

### Event Classification
```typescript
enum EventClassification {
  SAFETY_CRITICAL = "safety_critical",
  OPERATIONAL = "operational",
  SYSTEM = "system",
  COMMUNICATION = "communication",
  WEATHER = "weather",
  TRAINING = "training"
}
```

## Authentication

All API endpoints require authentication via JWT token:

```
Authorization: Bearer <jwt_token>
```

## Rate Limiting

- **CVR Transcription**: 10 requests/minute
- **FDR Anomaly Detection**: 60 requests/minute
- **Event Segmentation**: 30 requests/minute

## Error Handling

Standard error response format:

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Audio sample rate must be 16000 Hz",
    "details": {
      "provided_rate": 8000,
      "required_rate": 16000
    }
  }
}
```

## Versioning

API versioned via URL path (`/v1/`, `/v2/`, etc.)

## Document Control

- **Version**: 1.0
- **Status**: DRAFT
- **Last Updated**: 2025-11-18
- **AI Assistance**: Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- **Human approver**: _[to be completed]_.

---

# 02-90-02: API Specifications

## Purpose

This folder contains API specifications (OpenAPI, GraphQL, AsyncAPI) for operations and analytics services in the AMPEL360 ecosystem.

## Scope

API specifications define service contracts for:

- **REST APIs**: Flight operations, performance calculations, energy monitoring
- **GraphQL APIs**: Flexible query interfaces for complex data relationships
- **Event Streams**: Kafka and MQTT topics for real-time data distribution
- **Testing**: Postman collections for API validation

All specifications are **non-proprietary examples** suitable for development and testing.

## Supported Technologies

| Technology | Version | Use Case | Documentation |
|------------|---------|----------|---------------|
| **OpenAPI** | 3.1.0 | REST API specifications | [OpenAPI Spec](https://spec.openapis.org/oas/latest.html) |
| **GraphQL** | Latest | Flexible query language | [GraphQL Docs](https://graphql.org/learn/) |
| **AsyncAPI** | 2.6.0 | Event-driven architecture | [AsyncAPI Spec](https://www.asyncapi.com/docs/reference/specification/latest) |
| **Postman** | Latest | API testing collections | [Postman Docs](https://learning.postman.com/) |

## Structure

```
02-90-02_API_Specifications/
├── README.md (this file)
├── 02-90-02-001_OpenAPI_Specifications.md
├── 02-90-02-002_GraphQL_Schemas.md
├── 02-90-02-003_AsyncAPI_Event_Schemas.md
└── ASSETS/
    ├── OpenAPI/                    # REST API specifications
    ├── GraphQL/                    # GraphQL schemas
    ├── AsyncAPI/                   # Event streaming specs
    └── Postman/                    # Test collections
```

## Key APIs

### OpenAPI (REST)

1. **[Flight Operations API](./ASSETS/OpenAPI/02-90-02-A-001_Flight_Operations_API_v1.yaml)**
   - CRUD operations for flights
   - Status updates and tracking
   - Compatible with [02-40-12 Backend Services](../../02-40_Software/02-40-12_Backend_Services/README.md)

2. **[Performance Calculator API](./ASSETS/OpenAPI/02-90-02-A-002_Performance_Calculator_API_v1.yaml)**
   - Takeoff and landing performance calculations
   - Integrated with [02-40-13 Performance Calculator](../../02-40_Software/02-40-13_Performance_Calculator/README.md)

3. **[Energy Monitoring API](./ASSETS/OpenAPI/02-90-02-A-003_Energy_Monitoring_API_v1.yaml)**
   - Real-time energy data streams
   - Historical energy analytics
   - Connected to [02-80 Energy](../../02-80_Energy/README.md)

### GraphQL

1. **[Operations Schema](./ASSETS/GraphQL/02-90-02-A-101_Operations_Schema.graphql)**
   - Flight, aircraft, and crew queries
   - Real-time subscriptions for status updates

2. **[Fleet Data Schema](./ASSETS/GraphQL/02-90-02-A-102_Fleet_Data_Schema.graphql)**
   - Fleet-level KPIs and aggregations
   - Time-series performance data

### AsyncAPI (Events)

1. **[Kafka Topics](./ASSETS/AsyncAPI/02-90-02-A-201_Kafka_Topics_Spec.yaml)**
   - Flight events (departure, arrival, delays)
   - Performance events (phase transitions)
   - Energy events (power state changes)

2. **[MQTT Topics](./ASSETS/AsyncAPI/02-90-02-A-203_MQTT_Topics_Spec.yaml)**
   - Lightweight messaging for EFB and edge devices
   - Telemetry streams from aircraft

## Versioning Strategy

APIs follow [Semantic Versioning](../02-90-00-004_Schema_Version_Control.md) with URL-based versioning:

- **URL pattern**: `/api/v{major}/{resource}`
- **Example**: `/api/v1/flights`, `/api/v2/flights`
- **Header**: `API-Version: 1.5.0` for minor/patch tracking

### Version Compatibility

| API Version | Status | Maintained Until | Breaking Changes |
|-------------|--------|------------------|------------------|
| v2.x | Current | Ongoing | None planned |
| v1.x | Deprecated | 2026-12-31 | Use v2.x |

## Authentication & Authorization

All production APIs require authentication:

```yaml
security:
  - BearerAuth: []      # JWT tokens
  - ApiKeyAuth: []      # API keys for service-to-service
```

Authorization uses role-based access control (RBAC) defined in [User Management Schema](../02-90-01_Database_Schemas/ASSETS/SQL/02-90-01-A-005_User_Management_Schema.sql).

## Error Handling

Standard HTTP status codes:

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET/PUT |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Missing or invalid auth |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate or constraint violation |
| 422 | Unprocessable Entity | Validation failed |
| 500 | Internal Server Error | Server-side error |

Error response format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid flight number format",
    "details": [
      {
        "field": "flight_number",
        "issue": "Must match pattern [A-Z]{2}[0-9]{3,4}"
      }
    ],
    "request_id": "uuid-here"
  }
}
```

## Rate Limiting

Default rate limits (configurable per environment):

- **Authenticated users**: 1000 requests/hour
- **Service accounts**: 10000 requests/hour
- **Anonymous**: 100 requests/hour

Headers returned:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 987
X-RateLimit-Reset: 2025-11-21T03:00:00Z
```

## Testing

[Postman collections](./ASSETS/Postman/) provide:

1. **Happy path tests**: Successful API calls
2. **Error scenarios**: Invalid inputs, auth failures
3. **Integration tests**: Multi-step workflows
4. **Performance tests**: Load and stress testing

## Cross-References

- [02-90-00-002 Data Dictionary](../02-90-00-002_Data_Dictionary_Master.md) – Field definitions
- [02-90-01 Database Schemas](../02-90-01_Database_Schemas/README.md) – Underlying data models
- [02-40 Software](../../02-40_Software/README.md) – Applications consuming these APIs
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [GraphQL Specification](https://spec.graphql.org/)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)

---

## Document Control

- Generated with the assistance of AI (GitHub Copilot), prompted by **Amedeo Pelliccia**.
- Status: **DRAFT** – Subject to human review and approval.
- Human approver: _[to be completed]_.
- Repository: `AMPEL360-BWB-H2-Hy-E`
- Last AI update: _2025-11-21_.

---

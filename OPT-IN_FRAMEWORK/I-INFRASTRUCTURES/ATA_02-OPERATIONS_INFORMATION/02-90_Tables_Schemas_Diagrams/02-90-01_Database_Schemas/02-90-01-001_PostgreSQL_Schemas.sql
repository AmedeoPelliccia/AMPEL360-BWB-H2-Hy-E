-- ============================================================================
-- 02-90-01-001: PostgreSQL Schema Examples
-- ============================================================================
-- Purpose: Example PostgreSQL DDL statements defining core operational tables
-- Version: 1.0.0
-- Status: DRAFT
-- Last Updated: 2025-11-21
-- ============================================================================
-- IMPORTANT: This file contains SYNTHETIC DATA STRUCTURES ONLY.
-- No real airline operational data, credentials, or proprietary information.
-- ============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================================
-- SCHEMA: operations
-- Purpose: Core flight operations data
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS operations;

-- ----------------------------------------------------------------------------
-- Table: operations.flights
-- Purpose: Master flight table
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS operations.flights (
    -- Primary key
    id_flight           BIGSERIAL PRIMARY KEY,
    uuid_flight         UUID DEFAULT gen_random_uuid() UNIQUE NOT NULL,
    
    -- Flight identification
    flight_number       VARCHAR(10) NOT NULL,
    flight_date         DATE NOT NULL,
    
    -- Aircraft reference (synthetic identifier)
    fk_aircraft         BIGINT NOT NULL,
    aircraft_registration VARCHAR(10),
    
    -- Route
    departure_airport_icao  VARCHAR(4) NOT NULL CHECK (length(departure_airport_icao) = 4),
    arrival_airport_icao    VARCHAR(4) NOT NULL CHECK (length(arrival_airport_icao) = 4),
    
    -- Schedule
    scheduled_departure_utc TIMESTAMPTZ NOT NULL,
    scheduled_arrival_utc   TIMESTAMPTZ NOT NULL,
    actual_departure_utc    TIMESTAMPTZ,
    actual_arrival_utc      TIMESTAMPTZ,
    
    -- Operational data
    fuel_planned_kg         NUMERIC(10,2) CHECK (fuel_planned_kg > 0),
    fuel_actual_kg          NUMERIC(10,2) CHECK (fuel_actual_kg > 0),
    passengers_count        INTEGER CHECK (passengers_count >= 0),
    cargo_mass_kg           NUMERIC(10,2) CHECK (cargo_mass_kg >= 0),
    
    -- Status
    status_code         VARCHAR(20) NOT NULL DEFAULT 'PLANNED',
    
    -- Audit fields
    ts_created_utc      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ts_updated_utc      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by_user_id  BIGINT,
    updated_by_user_id  BIGINT,
    
    -- Metadata
    metadata            JSONB,
    
    -- Constraints
    CONSTRAINT chk_departure_before_arrival 
        CHECK (scheduled_departure_utc < scheduled_arrival_utc)
);

-- Indexes
CREATE INDEX idx_flights_date ON operations.flights(flight_date);
CREATE INDEX idx_flights_departure ON operations.flights(departure_airport_icao);
CREATE INDEX idx_flights_arrival ON operations.flights(arrival_airport_icao);
CREATE INDEX idx_flights_status ON operations.flights(status_code);
CREATE INDEX idx_flights_aircraft ON operations.flights(fk_aircraft);

-- ============================================================================
-- SCHEMA: performance
-- Purpose: Flight performance monitoring
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS performance;

-- ----------------------------------------------------------------------------
-- Table: performance.flight_phases
-- Purpose: Flight phase definitions
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS performance.flight_phases (
    id_phase            SERIAL PRIMARY KEY,
    phase_code          VARCHAR(20) UNIQUE NOT NULL,
    phase_name          VARCHAR(100) NOT NULL,
    phase_description   TEXT,
    sort_order          INTEGER NOT NULL,
    
    -- Audit
    ts_created_utc      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Seed data
INSERT INTO performance.flight_phases (phase_code, phase_name, phase_description, sort_order)
VALUES 
    ('PREFLIGHT', 'Pre-Flight', 'Aircraft preparation and boarding', 10),
    ('TAXI_OUT', 'Taxi Out', 'Taxi from gate to runway', 20),
    ('TAKEOFF', 'Takeoff', 'Takeoff roll and initial climb', 30),
    ('CLIMB', 'Climb', 'Climb to cruise altitude', 40),
    ('CRUISE', 'Cruise', 'Cruise at altitude', 50),
    ('DESCENT', 'Descent', 'Descent from cruise', 60),
    ('APPROACH', 'Approach', 'Final approach to landing', 70),
    ('LANDING', 'Landing', 'Landing roll and deceleration', 80),
    ('TAXI_IN', 'Taxi In', 'Taxi from runway to gate', 90),
    ('POSTFLIGHT', 'Post-Flight', 'Shutdown and passenger deplaning', 100)
ON CONFLICT (phase_code) DO NOTHING;

-- ============================================================================
-- SCHEMA: energy
-- Purpose: Energy monitoring and power management
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS energy;

-- ----------------------------------------------------------------------------
-- Table: energy.power_channels
-- Purpose: Power channel definitions
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS energy.power_channels (
    id_channel          BIGSERIAL PRIMARY KEY,
    channel_code        VARCHAR(20) UNIQUE NOT NULL,
    channel_name        VARCHAR(100) NOT NULL,
    channel_type        VARCHAR(20) NOT NULL, -- AC, DC, H2_FUEL_CELL
    nominal_voltage_v   NUMERIC(8,3) NOT NULL CHECK (nominal_voltage_v > 0),
    max_current_a       NUMERIC(8,3) NOT NULL CHECK (max_current_a > 0),
    
    -- Metadata
    metadata            JSONB,
    
    -- Audit
    ts_created_utc      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active           BOOLEAN DEFAULT true
);

CREATE INDEX idx_power_channels_type ON energy.power_channels(channel_type);

-- ============================================================================
-- SCHEMA: users
-- Purpose: User management and authentication
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS users;

-- ----------------------------------------------------------------------------
-- Table: users.users
-- Purpose: User accounts (NO REAL PERSONAL DATA)
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS users.users (
    id_user             BIGSERIAL PRIMARY KEY,
    uuid_user           UUID DEFAULT gen_random_uuid() UNIQUE NOT NULL,
    
    -- Authentication (example only, use proper auth system in production)
    username            VARCHAR(50) UNIQUE NOT NULL,
    email               VARCHAR(255) UNIQUE NOT NULL,
    password_hash       VARCHAR(255), -- bcrypt hash in production
    
    -- Profile
    full_name           VARCHAR(255),
    is_active           BOOLEAN DEFAULT true,
    is_admin            BOOLEAN DEFAULT false,
    
    -- Audit
    ts_created_utc      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ts_updated_utc      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ts_last_login_utc   TIMESTAMPTZ,
    
    -- Metadata
    metadata            JSONB
);

CREATE INDEX idx_users_username ON users.users(username);
CREATE INDEX idx_users_email ON users.users(email);

-- ----------------------------------------------------------------------------
-- Table: users.roles
-- Purpose: Role definitions for RBAC
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS users.roles (
    id_role             SERIAL PRIMARY KEY,
    role_code           VARCHAR(50) UNIQUE NOT NULL,
    role_name           VARCHAR(100) NOT NULL,
    role_description    TEXT,
    
    -- Audit
    ts_created_utc      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Seed data
INSERT INTO users.roles (role_code, role_name, role_description)
VALUES 
    ('ADMIN', 'Administrator', 'Full system access'),
    ('OPERATOR', 'Operator', 'Flight operations access'),
    ('ANALYST', 'Data Analyst', 'Read-only analytics access'),
    ('VIEWER', 'Viewer', 'Read-only operational data access')
ON CONFLICT (role_code) DO NOTHING;

-- ----------------------------------------------------------------------------
-- Table: users.user_roles
-- Purpose: Many-to-many mapping of users to roles
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS users.user_roles (
    id_user_role        BIGSERIAL PRIMARY KEY,
    fk_user             BIGINT NOT NULL REFERENCES users.users(id_user) ON DELETE CASCADE,
    fk_role             INTEGER NOT NULL REFERENCES users.roles(id_role) ON DELETE CASCADE,
    
    -- Audit
    ts_assigned_utc     TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    assigned_by_user_id BIGINT,
    
    -- Constraints
    UNIQUE(fk_user, fk_role)
);

CREATE INDEX idx_user_roles_user ON users.user_roles(fk_user);
CREATE INDEX idx_user_roles_role ON users.user_roles(fk_role);

-- ============================================================================
-- SCHEMA: audit
-- Purpose: Comprehensive audit logging
-- ============================================================================

CREATE SCHEMA IF NOT EXISTS audit;

-- ----------------------------------------------------------------------------
-- Table: audit.audit_log
-- Purpose: Immutable audit trail
-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS audit.audit_log (
    id_audit            BIGSERIAL PRIMARY KEY,
    
    -- Event information
    event_timestamp_utc TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    event_type          VARCHAR(50) NOT NULL, -- CREATE, READ, UPDATE, DELETE
    event_category      VARCHAR(50) NOT NULL, -- FLIGHT, USER, SYSTEM, etc.
    event_description   TEXT NOT NULL,
    
    -- Actor
    fk_user             BIGINT,
    username            VARCHAR(50),
    source_ip           INET,
    
    -- Target
    target_entity       VARCHAR(100), -- Table or resource name
    target_id           VARCHAR(100), -- Entity ID
    
    -- Changes
    old_values          JSONB,
    new_values          JSONB,
    
    -- Context
    request_id          UUID,
    session_id          VARCHAR(255),
    
    -- Metadata
    metadata            JSONB
);

-- Indexes for performance
CREATE INDEX idx_audit_timestamp ON audit.audit_log(event_timestamp_utc DESC);
CREATE INDEX idx_audit_user ON audit.audit_log(fk_user);
CREATE INDEX idx_audit_type ON audit.audit_log(event_type);
CREATE INDEX idx_audit_category ON audit.audit_log(event_category);
CREATE INDEX idx_audit_entity ON audit.audit_log(target_entity);

-- Make audit_log append-only (no updates or deletes allowed)
CREATE RULE audit_log_no_update AS ON UPDATE TO audit.audit_log DO INSTEAD NOTHING;
CREATE RULE audit_log_no_delete AS ON DELETE TO audit.audit_log DO INSTEAD NOTHING;

-- ============================================================================
-- VIEWS AND FUNCTIONS
-- ============================================================================

-- ----------------------------------------------------------------------------
-- View: operations.v_flights_summary
-- Purpose: Simplified flight view for dashboards
-- ----------------------------------------------------------------------------

CREATE OR REPLACE VIEW operations.v_flights_summary AS
SELECT 
    f.id_flight,
    f.uuid_flight,
    f.flight_number,
    f.flight_date,
    f.departure_airport_icao,
    f.arrival_airport_icao,
    f.scheduled_departure_utc,
    f.scheduled_arrival_utc,
    f.actual_departure_utc,
    f.actual_arrival_utc,
    f.status_code,
    f.passengers_count,
    EXTRACT(EPOCH FROM (f.scheduled_arrival_utc - f.scheduled_departure_utc))/3600 AS scheduled_duration_hours
FROM operations.flights f
WHERE f.status_code != 'CANCELLED';

-- ============================================================================
-- GRANTS (Example - adjust for production)
-- ============================================================================

-- Grant read-only access to analyst role
-- GRANT USAGE ON SCHEMA operations TO analyst_role;
-- GRANT SELECT ON ALL TABLES IN SCHEMA operations TO analyst_role;

-- ============================================================================
-- COMMENTS
-- ============================================================================

COMMENT ON SCHEMA operations IS 'Core flight operations data schema';
COMMENT ON SCHEMA performance IS 'Flight performance monitoring schema';
COMMENT ON SCHEMA energy IS 'Energy management and power monitoring schema';
COMMENT ON SCHEMA users IS 'User management and authentication schema';
COMMENT ON SCHEMA audit IS 'Comprehensive audit logging schema';

COMMENT ON TABLE operations.flights IS 'Master flight table with synthetic operational data';
COMMENT ON TABLE performance.flight_phases IS 'Standardized flight phase definitions';
COMMENT ON TABLE energy.power_channels IS 'Power channel configuration and monitoring';
COMMENT ON TABLE users.users IS 'User accounts - EXAMPLE STRUCTURE ONLY, no real personal data';
COMMENT ON TABLE audit.audit_log IS 'Immutable audit trail for compliance and security';

-- ============================================================================
-- End of PostgreSQL Schema Examples
-- ============================================================================

-- Document Control
-- Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia
-- Status: DRAFT – Subject to human review and approval
-- Repository: AMPEL360-BWB-H2-Hy-E
-- Last AI update: 2025-11-21

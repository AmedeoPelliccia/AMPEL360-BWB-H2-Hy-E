/**
 * @file 53-90-30-03_Message_Structures.h
 * @brief ANCHORS System Message Structure Definitions
 * @version 1.0
 * @date 2025-11-27
 * 
 * This file defines the C structures for AFDX and CAN messages
 * used in the ANCHORS (ATA 53) system.
 * 
 * Copyright (c) 2025 AMPEL360 Program
 * Generated with AI assistance (GitHub Copilot), prompted by Amedeo Pelliccia
 */

#ifndef ANCHORS_MESSAGE_STRUCTURES_H
#define ANCHORS_MESSAGE_STRUCTURES_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ============================================================================
 * AFDX Message Structures
 * ============================================================================ */

/**
 * @brief VL_5302 Battery Data Message
 * @details Transmitted at 10ms BAG from BMS to TMS, EMS, SS
 */
typedef struct __attribute__((packed)) {
    uint16_t cell_temp_max_x10;    /**< 0.1°C resolution, offset -400 (-40°C to 80°C) */
    uint16_t cell_temp_min_x10;    /**< 0.1°C resolution, offset -400 */
    uint16_t pack_voltage_x10;     /**< 0.1V resolution (0-900V) */
    int16_t  pack_current_x10;     /**< 0.1A resolution, signed (-500A to +500A) */
    uint8_t  soc_pct;              /**< State of Charge 0-100% */
    uint8_t  soh_pct;              /**< State of Health 0-100% */
    uint8_t  fault_flags;          /**< Bit field: b0=OT, b1=UT, b2=OV, b3=UV, b4=OC, b5=ISO, b6=COM, b7=RES */
    uint8_t  status;               /**< Enum: 0=OFF, 1=INIT, 2=READY, 3=CHARGING, 4=DISCHARGING, 5=FAULT, 6=ISOLATED */
} ANCH_BAT_DATA_t;

/**
 * @brief VL_5309 Safety Supervisor Status Message
 * @details Transmitted at 10ms BAG from SS to All
 */
typedef struct __attribute__((packed)) {
    uint8_t  ss_state;             /**< Enum: 0=INIT, 1=NORMAL, 2=DEGRADED, 3=ISOLATED, 4=FAULT */
    uint8_t  fault_count;          /**< Active fault count (0-255) */
    uint16_t fault_code;           /**< Highest priority fault code */
    uint8_t  iso_status;           /**< Bit field: b0=BAT, b1=HT, b2=LT, b3=HV, b4=CO2, b5=H2O */
    uint8_t  wd_status;            /**< Watchdog status: 0=OK, 1=WARNING, 2=TIMEOUT */
    uint16_t reserved;             /**< Reserved for future use */
} ANCH_SS_STATUS_t;

/**
 * @brief VL_5301 Mode Manager Status Message
 * @details Transmitted at 20ms BAG from MM to All
 */
typedef struct __attribute__((packed)) {
    uint8_t  mode_current;         /**< Current operating mode enum */
    uint8_t  mode_requested;       /**< Requested operating mode enum */
    uint8_t  transition_pct;       /**< Mode transition progress 0-100% */
    uint8_t  inhibits;             /**< Active inhibit flags */
    uint16_t flight_phase;         /**< Current flight phase */
    uint8_t  auto_mode_active;     /**< Automatic mode flag */
    uint8_t  nn_override;          /**< Neural network override active */
    uint32_t uptime_sec;           /**< System uptime in seconds */
    uint8_t  reserved[4];          /**< Reserved for future use */
} ANCH_MM_STATUS_t;

/**
 * @brief VL_5304 Thermal Data Message
 * @details Transmitted at 50ms BAG from THC to EMS, HMI
 */
typedef struct __attribute__((packed)) {
    uint16_t ht_sup_temp_x10;      /**< HT bus supply temp, 0.1°C */
    uint16_t ht_ret_temp_x10;      /**< HT bus return temp, 0.1°C */
    uint16_t lt_sup_temp_x10;      /**< LT bus supply temp, 0.1°C */
    uint16_t lt_ret_temp_x10;      /**< LT bus return temp, 0.1°C */
    uint16_t ht_flow_x10;          /**< HT bus flow, 0.1 L/min */
    uint16_t lt_flow_x10;          /**< LT bus flow, 0.1 L/min */
    uint16_t ht_pressure_x100;     /**< HT bus pressure, 0.01 bar */
    uint16_t lt_pressure_x100;     /**< LT bus pressure, 0.01 bar */
    uint8_t  ht_pump_speed;        /**< HT pump speed 0-100% */
    uint8_t  lt_pump_speed;        /**< LT pump speed 0-100% */
    uint8_t  valve_positions[4];   /**< 4 valve positions 0-100% */
    uint8_t  status;               /**< Thermal system status enum */
    uint8_t  fault_flags;          /**< Thermal fault flags */
} ANCH_TH_DATA_t;

/**
 * @brief VL_5306 CO2 Capture Data Message
 * @details Transmitted at 100ms BAG from CO2C to EMS, HMI
 */
typedef struct __attribute__((packed)) {
    uint16_t inlet_pressure_x100;  /**< Inlet pressure, 0.01 bar */
    uint16_t outlet_pressure_x100; /**< Outlet pressure, 0.01 bar */
    uint16_t capture_flow_x10;     /**< Capture flow, 0.1 L/min */
    uint16_t reactor_temp_x10;     /**< Reactor temperature, 0.1°C */
    uint8_t  cart_levels[4];       /**< Cartridge fill levels 0-100% */
    uint8_t  active_cartridge;     /**< Currently active cartridge (1-4) */
    uint8_t  system_status;        /**< CO2 system status enum */
    uint8_t  fault_flags;          /**< CO2 fault flags */
    uint8_t  reserved;             /**< Reserved */
} ANCH_CO2_DATA_t;

/**
 * @brief VL_5314 Neural Network Status Message
 * @details Transmitted at 20ms BAG from NN to MM, SS
 */
typedef struct __attribute__((packed)) {
    uint8_t  nn_state;             /**< NN state: 0=OFF, 1=INIT, 2=READY, 3=ACTIVE, 4=FALLBACK */
    uint8_t  inference_count;      /**< Inferences this second */
    uint16_t confidence_x1000;     /**< Confidence level 0-1000 (0.0-1.0) */
    uint16_t inference_time_us;    /**< Last inference time in microseconds */
    uint8_t  output_valid;         /**< Output validity flag */
    uint8_t  fallback_reason;      /**< Fallback trigger reason enum */
    uint32_t model_version;        /**< Active model version */
    uint8_t  reserved[4];          /**< Reserved for future use */
} ANCH_NN_STATUS_t;

/* ============================================================================
 * CAN Message Structures
 * ============================================================================ */

/**
 * @brief CAN 0x100-0x103 Battery Cell Temperature Message
 * @details 4 cell temperatures per message, 10Hz
 */
typedef struct __attribute__((packed)) {
    int16_t cell_temp[4];          /**< Cell temperatures, 0.1°C resolution */
} CAN_BAT_CELL_TEMP_t;

/**
 * @brief CAN 0x110-0x113 Battery Cell Voltage Message
 * @details 4 cell voltages per message, 10Hz
 */
typedef struct __attribute__((packed)) {
    uint16_t cell_volt[4];         /**< Cell voltages, 1mV resolution */
} CAN_BAT_CELL_VOLT_t;

/**
 * @brief CAN 0x120 Battery Pack Status Message
 * @details Pack-level status, 10Hz
 */
typedef struct __attribute__((packed)) {
    uint8_t  soc_pct;              /**< State of Charge 0-100% */
    uint8_t  soh_pct;              /**< State of Health 0-100% */
    uint16_t fault_code;           /**< Active fault code */
    uint8_t  status;               /**< Pack status enum */
    uint8_t  contactor_state;      /**< Contactor states: b0=POS, b1=NEG, b2=PRE */
    uint16_t isolation_kohm;       /**< Isolation resistance in kOhm */
} CAN_BAT_PACK_STATUS_t;

/**
 * @brief CAN 0x600 Safety Supervisor Heartbeat
 * @details 100Hz heartbeat for watchdog monitoring
 */
typedef struct __attribute__((packed)) {
    uint8_t  sequence;             /**< Rolling sequence counter */
    uint8_t  status;               /**< SS status byte */
    uint16_t crc;                  /**< CRC-16 checksum */
} CAN_SS_HEARTBEAT_t;

/* ============================================================================
 * Enumerations
 * ============================================================================ */

/**
 * @brief Battery Status Enumeration
 */
typedef enum {
    BAT_STATUS_OFF = 0,
    BAT_STATUS_INIT = 1,
    BAT_STATUS_READY = 2,
    BAT_STATUS_CHARGING = 3,
    BAT_STATUS_DISCHARGING = 4,
    BAT_STATUS_FAULT = 5,
    BAT_STATUS_ISOLATED = 6
} BatteryStatus_e;

/**
 * @brief Safety Supervisor State Enumeration
 */
typedef enum {
    SS_STATE_INIT = 0,
    SS_STATE_NORMAL = 1,
    SS_STATE_DEGRADED = 2,
    SS_STATE_ISOLATED = 3,
    SS_STATE_FAULT = 4
} SafetySupervisorState_e;

/**
 * @brief Operating Mode Enumeration
 */
typedef enum {
    MODE_OFF = 0,
    MODE_GROUND_IDLE = 1,
    MODE_GROUND_ACTIVE = 2,
    MODE_TAXI = 3,
    MODE_TAKEOFF = 4,
    MODE_CLIMB = 5,
    MODE_CRUISE = 6,
    MODE_DESCENT = 7,
    MODE_APPROACH = 8,
    MODE_LANDING = 9,
    MODE_EMERGENCY = 10,
    MODE_MAINTENANCE = 11
} OperatingMode_e;

/**
 * @brief Neural Network State Enumeration
 */
typedef enum {
    NN_STATE_OFF = 0,
    NN_STATE_INIT = 1,
    NN_STATE_READY = 2,
    NN_STATE_ACTIVE = 3,
    NN_STATE_FALLBACK = 4
} NeuralNetworkState_e;

/* ============================================================================
 * Size Assertions
 * ============================================================================ */

_Static_assert(sizeof(ANCH_BAT_DATA_t) == 12, "ANCH_BAT_DATA_t size mismatch");
_Static_assert(sizeof(ANCH_SS_STATUS_t) == 8, "ANCH_SS_STATUS_t size mismatch");
_Static_assert(sizeof(CAN_SS_HEARTBEAT_t) == 4, "CAN_SS_HEARTBEAT_t size mismatch");

#ifdef __cplusplus
}
#endif

#endif /* ANCHORS_MESSAGE_STRUCTURES_H */

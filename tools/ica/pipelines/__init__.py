#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 AMPEL360 Project Contributors

"""
Data & Telemetry Pipelines

Pipelines required to make ICA "continuous" rather than periodic.
Includes telemetry ingestion, data conditioning, and ICA mapping tools.
"""

__all__ = [
    "aircraft_telemetry_ingestor",
    "maintenance_event_collector",
    "gse_telemetry_adapter",
    "config_drift_detector",
    "dpp_event_resolver",
    "health_to_doc_mapper",
]

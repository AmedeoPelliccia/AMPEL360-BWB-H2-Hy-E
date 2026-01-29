# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Machine learning models for AMPEL360 digital twin.

This module provides ML models for predictive analytics, anomaly detection,
and performance optimization across the aircraft lifecycle.

Classes:
    PredictiveMaintenance: Predictive maintenance model
    AnomalyDetector: Anomaly detection for sensor data
    PerformanceOptimizer: Performance optimization model
"""

from digital_twin.ml_models.predictive_maintenance import PredictiveMaintenance
from digital_twin.ml_models.anomaly_detection import AnomalyDetector
from digital_twin.ml_models.performance_optimizer import PerformanceOptimizer

__all__ = [
    "PredictiveMaintenance",
    "AnomalyDetector",
    "PerformanceOptimizer",
]

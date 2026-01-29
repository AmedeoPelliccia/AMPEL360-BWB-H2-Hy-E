# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Core digital twin models for AMPEL360 aircraft systems.

This module provides physics-based and data-driven models for aircraft components
including airframe, propulsion, and aircraft systems.

Classes:
    BaseModel: Abstract base class for all digital twin models
    AirframeModel: Structural model for airframe (ATA 51-57)
    PropulsionModel: Propulsion system model (ATA 70-80)
    SystemsModel: Aircraft systems model (ATA 21-49)
"""

from digital_twin.models.base_model import BaseModel
from digital_twin.models.airframe_model import AirframeModel
from digital_twin.models.propulsion_model import PropulsionModel
from digital_twin.models.systems_model import SystemsModel

__all__ = [
    "BaseModel",
    "AirframeModel",
    "PropulsionModel",
    "SystemsModel",
]

# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Data connectors for AMPEL360 digital twin.

This module provides connectors for integrating the digital twin
with external systems including PLM, ERP, and simulation tools.

Classes:
    BaseConnector: Abstract base class for all connectors
    PLMConnector: PLM system integration
    ERPConnector: ERP system integration
    SimulationConnector: Simulation tool integration
"""

from digital_twin.connectors.base_connector import BaseConnector, ConnectionStatus
from digital_twin.connectors.plm_connector import PLMConnector
from digital_twin.connectors.erp_connector import ERPConnector
from digital_twin.connectors.simulation_connector import SimulationConnector

__all__ = [
    "BaseConnector",
    "ConnectionStatus",
    "PLMConnector",
    "ERPConnector",
    "SimulationConnector",
]

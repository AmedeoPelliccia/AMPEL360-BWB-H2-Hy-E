# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
ERP connector for AMPEL360 digital twin.

This module provides integration with Enterprise Resource Planning systems
for managing procurement, inventory, and cost data.
"""

from datetime import datetime
from typing import Any, Optional
import logging
import time

from digital_twin.connectors.base_connector import (
    BaseConnector,
    ConnectionStatus,
    ConnectorConfig,
)

logger = logging.getLogger(__name__)


class ERPConnector(BaseConnector):
    """
    Connector for Enterprise Resource Planning systems.

    Supports integration with ERP systems like SAP and Oracle
    for procurement and inventory management.

    Attributes:
        erp_type: Type of ERP system (sap, oracle, generic)
    """

    SUPPORTED_SYSTEMS = ["sap", "oracle", "dynamics", "generic"]

    def __init__(
        self,
        endpoint: str = "",
        erp_type: str = "generic",
        auth_token: Optional[str] = None,
        config: Optional[ConnectorConfig] = None,
    ) -> None:
        """
        Initialize the ERP connector.

        Args:
            endpoint: ERP API endpoint URL
            erp_type: Type of ERP system
            auth_token: Optional authentication token
            config: Optional connector configuration
        """
        config = config or ConnectorConfig(endpoint=endpoint)
        config.endpoint = endpoint or config.endpoint

        super().__init__(
            connector_id=f"ERP-{erp_type.upper()}-001",
            name=f"{erp_type.title()} ERP Connector",
            config=config,
        )

        self.erp_type = erp_type if erp_type in self.SUPPORTED_SYSTEMS else "generic"
        self._auth_token = auth_token

        logger.info("Initialized ERP connector for %s", self.erp_type)

    def connect(self) -> bool:
        """Establish connection to the ERP system."""
        if not self.config.endpoint:
            logger.error("No endpoint configured for ERP connector")
            self.status = ConnectionStatus.ERROR
            return False

        self.status = ConnectionStatus.CONNECTING
        start_time = time.time()

        try:
            # Simulate connection
            self.status = ConnectionStatus.CONNECTED
            latency = (time.time() - start_time) * 1000
            self._update_metrics(success=True, latency_ms=latency)
            logger.info("Connected to ERP successfully")
            return True

        except Exception as e:
            logger.error("Failed to connect to ERP: %s", e)
            self.status = ConnectionStatus.ERROR
            return False

    def disconnect(self) -> bool:
        """Close connection to the ERP system."""
        self.status = ConnectionStatus.DISCONNECTED
        self._auth_token = None
        logger.info("Disconnected from ERP")
        return True

    def authenticate(self, credentials: dict[str, str]) -> bool:
        """Authenticate with the ERP system."""
        if not self.is_connected():
            return False

        if "api_key" in credentials:
            self._auth_token = credentials["api_key"]
        elif "username" in credentials:
            self._auth_token = f"basic:{credentials['username']}"

        self.status = ConnectionStatus.AUTHENTICATED
        logger.info("Authenticated with ERP")
        return True

    def fetch(self, resource_type: str, resource_id: str) -> Optional[dict[str, Any]]:
        """Fetch a resource from the ERP system."""
        if not self.is_connected():
            return None

        start_time = time.time()

        try:
            if resource_type == "material":
                data = self._mock_material_data(resource_id)
            elif resource_type == "purchase_order":
                data = self._mock_po_data(resource_id)
            elif resource_type == "inventory":
                data = self._mock_inventory_data(resource_id)
            elif resource_type == "cost":
                data = self._mock_cost_data(resource_id)
            else:
                data = {"id": resource_id, "type": resource_type}

            latency = (time.time() - start_time) * 1000
            self._update_metrics(success=True, latency_ms=latency)
            return data

        except Exception as e:
            logger.error("Failed to fetch from ERP: %s", e)
            return None

    def push(
        self, resource_type: str, resource_id: str, data: dict[str, Any]
    ) -> bool:
        """Push data to the ERP system."""
        if not self.is_connected():
            return False

        start_time = time.time()

        try:
            latency = (time.time() - start_time) * 1000
            self._update_metrics(success=True, latency_ms=latency, bytes_sent=len(str(data)))
            logger.info("Pushed %s/%s to ERP", resource_type, resource_id)
            return True

        except Exception as e:
            logger.error("Failed to push to ERP: %s", e)
            return False

    def query(self, query: dict[str, Any]) -> list[dict[str, Any]]:
        """Execute a query against the ERP system."""
        if not self.is_connected():
            return []

        resource_type = query.get("type", "material")
        limit = query.get("limit", 100)

        try:
            if resource_type == "material":
                return [self._mock_material_data(f"MAT-{i:04d}") for i in range(min(10, limit))]
            elif resource_type == "inventory":
                return [self._mock_inventory_data(f"INV-{i:04d}") for i in range(min(10, limit))]
            return []

        except Exception as e:
            logger.error("ERP query failed: %s", e)
            return []

    def get_material(self, material_id: str) -> Optional[dict[str, Any]]:
        """Get material master data."""
        return self.fetch("material", material_id)

    def get_inventory(self, material_id: str) -> Optional[dict[str, Any]]:
        """Get inventory levels for a material."""
        return self.fetch("inventory", material_id)

    def get_cost(self, material_id: str) -> Optional[dict[str, Any]]:
        """Get cost data for a material."""
        return self.fetch("cost", material_id)

    def create_purchase_order(
        self, materials: list[dict[str, Any]], vendor_id: str
    ) -> Optional[str]:
        """
        Create a purchase order.

        Args:
            materials: List of materials with quantities
            vendor_id: Vendor identifier

        Returns:
            Purchase order ID or None
        """
        po_data = {
            "vendor_id": vendor_id,
            "materials": materials,
            "created": datetime.utcnow().isoformat(),
        }

        if self.push("purchase_order", "NEW", po_data):
            return f"PO-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        return None

    def _mock_material_data(self, material_id: str) -> dict[str, Any]:
        """Generate mock material data."""
        return {
            "id": material_id,
            "type": "material",
            "description": f"Material {material_id}",
            "unit": "EA",
            "material_group": "aerospace",
            "status": "active",
            "created": datetime.utcnow().isoformat(),
        }

    def _mock_po_data(self, po_id: str) -> dict[str, Any]:
        """Generate mock purchase order data."""
        return {
            "id": po_id,
            "type": "purchase_order",
            "vendor": "VENDOR-001",
            "status": "open",
            "items": [
                {"material": "MAT-001", "quantity": 10, "unit_price": 150.0},
                {"material": "MAT-002", "quantity": 5, "unit_price": 300.0},
            ],
            "total_value": 3000.0,
            "currency": "EUR",
        }

    def _mock_inventory_data(self, material_id: str) -> dict[str, Any]:
        """Generate mock inventory data."""
        return {
            "material_id": material_id,
            "type": "inventory",
            "locations": [
                {"warehouse": "WH-01", "quantity": 100, "unit": "EA"},
                {"warehouse": "WH-02", "quantity": 50, "unit": "EA"},
            ],
            "total_quantity": 150,
            "reorder_point": 20,
            "last_updated": datetime.utcnow().isoformat(),
        }

    def _mock_cost_data(self, material_id: str) -> dict[str, Any]:
        """Generate mock cost data."""
        return {
            "material_id": material_id,
            "type": "cost",
            "standard_cost": 250.0,
            "moving_average_cost": 248.50,
            "currency": "EUR",
            "cost_center": "CC-PROD-001",
            "last_updated": datetime.utcnow().isoformat(),
        }

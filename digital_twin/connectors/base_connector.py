# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Base connector interface for AMPEL360 digital twin.

This module defines the abstract base class that all connectors must implement,
ensuring consistent interfaces for external system integration.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class ConnectionStatus(Enum):
    """Connection status enumeration."""

    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    ERROR = "error"
    AUTHENTICATED = "authenticated"


@dataclass
class ConnectorMetrics:
    """Metrics for connector performance monitoring."""

    requests_total: int = 0
    requests_successful: int = 0
    requests_failed: int = 0
    bytes_sent: int = 0
    bytes_received: int = 0
    last_request_time: Optional[datetime] = None
    average_latency_ms: float = 0.0


@dataclass
class ConnectorConfig:
    """Configuration for a connector."""

    endpoint: str = ""
    timeout_seconds: int = 30
    retry_count: int = 3
    retry_delay_seconds: float = 1.0
    verify_ssl: bool = True
    auth_type: str = "none"  # none, api_key, oauth2, basic
    extra_headers: dict[str, str] = field(default_factory=dict)


class BaseConnector(ABC):
    """
    Abstract base class for all AMPEL360 digital twin connectors.

    Defines the standard interface for external system integration.

    Attributes:
        connector_id: Unique identifier for this connector
        name: Human-readable connector name
        status: Current connection status
        config: Connector configuration
        metrics: Performance metrics
    """

    def __init__(
        self,
        connector_id: str,
        name: str,
        config: Optional[ConnectorConfig] = None,
    ) -> None:
        """
        Initialize the base connector.

        Args:
            connector_id: Unique identifier
            name: Human-readable name
            config: Optional configuration object
        """
        self.connector_id = connector_id
        self.name = name
        self.status = ConnectionStatus.DISCONNECTED
        self.config = config or ConnectorConfig()
        self.metrics = ConnectorMetrics()

        self._auth_token: Optional[str] = None
        self._session_id: Optional[str] = None

        logger.info("Initialized connector: %s (%s)", name, connector_id)

    @abstractmethod
    def connect(self) -> bool:
        """
        Establish connection to the external system.

        Returns:
            True if connection was successful
        """

    @abstractmethod
    def disconnect(self) -> bool:
        """
        Close connection to the external system.

        Returns:
            True if disconnection was successful
        """

    @abstractmethod
    def authenticate(self, credentials: dict[str, str]) -> bool:
        """
        Authenticate with the external system.

        Args:
            credentials: Authentication credentials

        Returns:
            True if authentication was successful
        """

    @abstractmethod
    def fetch(self, resource_type: str, resource_id: str) -> Optional[dict[str, Any]]:
        """
        Fetch a resource from the external system.

        Args:
            resource_type: Type of resource to fetch
            resource_id: Identifier of the resource

        Returns:
            Resource data or None if not found
        """

    @abstractmethod
    def push(
        self, resource_type: str, resource_id: str, data: dict[str, Any]
    ) -> bool:
        """
        Push data to the external system.

        Args:
            resource_type: Type of resource
            resource_id: Identifier of the resource
            data: Data to push

        Returns:
            True if push was successful
        """

    @abstractmethod
    def query(self, query: dict[str, Any]) -> list[dict[str, Any]]:
        """
        Execute a query against the external system.

        Args:
            query: Query parameters

        Returns:
            List of matching results
        """

    def is_connected(self) -> bool:
        """Check if connector is currently connected."""
        return self.status in (ConnectionStatus.CONNECTED, ConnectionStatus.AUTHENTICATED)

    def get_status(self) -> dict[str, Any]:
        """
        Get current connector status.

        Returns:
            Dictionary containing status information
        """
        return {
            "connector_id": self.connector_id,
            "name": self.name,
            "status": self.status.value,
            "endpoint": self.config.endpoint,
            "metrics": {
                "requests_total": self.metrics.requests_total,
                "requests_successful": self.metrics.requests_successful,
                "requests_failed": self.metrics.requests_failed,
                "success_rate": (
                    self.metrics.requests_successful / max(self.metrics.requests_total, 1)
                ),
                "average_latency_ms": self.metrics.average_latency_ms,
            },
        }

    def _update_metrics(
        self, success: bool, latency_ms: float, bytes_sent: int = 0, bytes_received: int = 0
    ) -> None:
        """Update connector metrics after a request."""
        self.metrics.requests_total += 1
        if success:
            self.metrics.requests_successful += 1
        else:
            self.metrics.requests_failed += 1

        self.metrics.bytes_sent += bytes_sent
        self.metrics.bytes_received += bytes_received
        self.metrics.last_request_time = datetime.utcnow()

        # Update average latency
        n = self.metrics.requests_total
        old_avg = self.metrics.average_latency_ms
        self.metrics.average_latency_ms = old_avg + (latency_ms - old_avg) / n

    def health_check(self) -> dict[str, Any]:
        """
        Perform health check on the connection.

        Returns:
            Dictionary containing health status
        """
        is_healthy = self.is_connected()
        return {
            "healthy": is_healthy,
            "status": self.status.value,
            "last_request": (
                self.metrics.last_request_time.isoformat()
                if self.metrics.last_request_time
                else None
            ),
            "success_rate": (
                self.metrics.requests_successful / max(self.metrics.requests_total, 1)
            ),
        }

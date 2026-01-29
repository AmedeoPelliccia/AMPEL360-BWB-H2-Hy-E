# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Base model interface for AMPEL360 digital twin models.

This module defines the abstract base class that all digital twin models must implement,
ensuring consistent interfaces for state management, updates, and validation.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import json
import logging

logger = logging.getLogger(__name__)


@dataclass
class ModelState:
    """Represents the current state of a digital twin model."""

    timestamp: datetime = field(default_factory=datetime.utcnow)
    parameters: dict[str, Any] = field(default_factory=dict)
    health_status: str = "nominal"
    confidence: float = 1.0
    last_validated: Optional[datetime] = None


@dataclass
class ValidationResult:
    """Result of a model validation operation."""

    is_valid: bool
    accuracy: float
    deviations: list[dict[str, Any]] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    notes: str = ""


class BaseModel(ABC):
    """
    Abstract base class for all AMPEL360 digital twin models.

    All digital twin models must inherit from this class and implement
    the abstract methods to ensure consistent behavior across the system.

    Attributes:
        model_id: Unique identifier for this model instance
        version: Semantic version of the model
        aircraft_id: Reference to the aircraft model (e.g., AM_Q100)
        ata_chapters: List of ATA chapters this model covers
        state: Current model state
    """

    def __init__(
        self,
        model_id: str,
        version: str = "1.0.0",
        aircraft_id: str = "AM_Q100",
        ata_chapters: Optional[list[str]] = None,
        config_path: Optional[str] = None,
    ) -> None:
        """
        Initialize the base model.

        Args:
            model_id: Unique identifier for this model
            version: Semantic version string
            aircraft_id: Aircraft model reference (default: AM_Q100)
            ata_chapters: List of ATA chapter codes this model covers
            config_path: Optional path to configuration JSON file
        """
        self.model_id = model_id
        self.version = version
        self.aircraft_id = aircraft_id
        self.ata_chapters = ata_chapters or []
        self.state = ModelState()
        self._config: dict[str, Any] = {}
        self._initialized = False

        if config_path:
            self.load_config(config_path)

    def load_config(self, config_path: str) -> None:
        """
        Load model configuration from a JSON file.

        Args:
            config_path: Path to the configuration file
        """
        try:
            with open(config_path, encoding="utf-8") as f:
                self._config = json.load(f)
            logger.info("Loaded configuration from %s", config_path)
        except FileNotFoundError:
            logger.warning("Configuration file not found: %s", config_path)
        except json.JSONDecodeError as e:
            logger.error("Invalid JSON in configuration file: %s", e)

    @abstractmethod
    def initialize(self) -> bool:
        """
        Initialize the model with baseline data.

        Returns:
            True if initialization was successful, False otherwise
        """

    @abstractmethod
    def update(self, state_data: dict[str, Any]) -> bool:
        """
        Update the model with new state data.

        Args:
            state_data: Dictionary containing sensor readings or state updates

        Returns:
            True if update was successful, False otherwise
        """

    @abstractmethod
    def predict(self, inputs: dict[str, Any], horizon: float = 1.0) -> dict[str, Any]:
        """
        Generate predictions based on current state and inputs.

        Args:
            inputs: Dictionary of input parameters for prediction
            horizon: Prediction time horizon in hours

        Returns:
            Dictionary containing prediction results
        """

    @abstractmethod
    def validate(
        self, reference_data: Optional[dict[str, Any]] = None
    ) -> ValidationResult:
        """
        Validate the model against reference data.

        Args:
            reference_data: Optional reference data for validation

        Returns:
            ValidationResult containing validation metrics
        """

    def get_state(self) -> ModelState:
        """
        Get the current model state.

        Returns:
            Current ModelState object
        """
        return self.state

    def to_dict(self) -> dict[str, Any]:
        """
        Convert model to dictionary representation.

        Returns:
            Dictionary representation of the model
        """
        return {
            "model_id": self.model_id,
            "version": self.version,
            "aircraft_id": self.aircraft_id,
            "ata_chapters": self.ata_chapters,
            "state": {
                "timestamp": self.state.timestamp.isoformat(),
                "parameters": self.state.parameters,
                "health_status": self.state.health_status,
                "confidence": self.state.confidence,
            },
            "initialized": self._initialized,
        }

    def __repr__(self) -> str:
        """Return string representation of the model."""
        return (
            f"{self.__class__.__name__}("
            f"model_id='{self.model_id}', "
            f"version='{self.version}', "
            f"aircraft_id='{self.aircraft_id}')"
        )

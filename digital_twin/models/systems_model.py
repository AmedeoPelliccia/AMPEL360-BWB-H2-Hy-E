# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Aircraft systems model for AMPEL360 digital twin.

This module provides the systems model for aircraft subsystems,
covering ATA chapters 21-49 (ECS, Electrical, Hydraulics, etc.).
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional
import logging

from digital_twin.models.base_model import BaseModel, ModelState, ValidationResult

logger = logging.getLogger(__name__)


@dataclass
class ECSStatus:
    """Environmental Control System status."""

    cabin_temp_c: float = 22.0
    cabin_pressure_hpa: float = 1013.25
    cabin_humidity_pct: float = 40.0
    pack_status: str = "auto"
    bleed_air_flow_kg_s: float = 0.0


@dataclass
class ElectricalStatus:
    """Electrical system status."""

    bus_voltage_v: float = 28.0
    current_draw_a: float = 0.0
    battery_soc_pct: float = 100.0
    generator_status: str = "online"
    load_pct: float = 0.0


@dataclass
class HydraulicsStatus:
    """Hydraulic system status."""

    pressure_bar: float = 0.0
    fluid_level_pct: float = 100.0
    pump_status: str = "standby"
    temperature_c: float = 25.0


class SystemsModel(BaseModel):
    """
    Digital twin model for aircraft systems.

    This model represents the state of major aircraft systems including
    ECS, electrical, and hydraulics.

    Attributes:
        ecs: Environmental Control System status
        electrical: Electrical system status
        hydraulics: Hydraulic system status
    """

    ATA_CHAPTERS = [
        "21", "22", "23", "24", "25", "26", "27", "28", "29",
        "30", "31", "32", "33", "34", "35", "36", "37", "38",
        "42", "44", "45", "46", "49"
    ]

    def __init__(
        self,
        model_id: str = "DT-Q100-SYSTEMS-001",
        config_path: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the systems model.

        Args:
            model_id: Unique identifier for this model
            config_path: Path to configuration file
            **kwargs: Additional arguments passed to BaseModel
        """
        super().__init__(
            model_id=model_id,
            ata_chapters=self.ATA_CHAPTERS,
            config_path=config_path,
            **kwargs,
        )
        self.ecs = ECSStatus()
        self.electrical = ElectricalStatus()
        self.hydraulics = HydraulicsStatus()
        self._subsystem_health: dict[str, str] = {}

    def initialize(self) -> bool:
        """
        Initialize the systems model with baseline data.

        Returns:
            True if initialization was successful
        """
        try:
            # Initialize subsystem health tracking
            self._subsystem_health = {
                "ecs": "nominal",
                "electrical": "nominal",
                "hydraulics": "nominal",
                "avionics": "nominal",
                "flight_controls": "nominal",
            }

            # Set default values from config
            if "ecs_defaults" in self._config:
                ecs_cfg = self._config["ecs_defaults"]
                self.ecs.cabin_temp_c = ecs_cfg.get("temp_c", 22.0)
                self.ecs.cabin_pressure_hpa = ecs_cfg.get("pressure_hpa", 1013.25)

            if "electrical_defaults" in self._config:
                elec_cfg = self._config["electrical_defaults"]
                self.electrical.bus_voltage_v = elec_cfg.get("voltage_v", 28.0)

            self.state = ModelState(
                parameters={
                    "systems_status": "nominal",
                    "active_subsystems": len(self._subsystem_health),
                },
                health_status="nominal",
                confidence=1.0,
            )
            self._initialized = True
            logger.info("Systems model initialized: %s", self.model_id)
            return True

        except (KeyError, TypeError) as e:
            logger.error("Failed to initialize systems model: %s", e)
            return False

    def update(self, state_data: dict[str, Any]) -> bool:
        """
        Update the systems model with new sensor data.

        Args:
            state_data: Dictionary containing sensor readings:
                - ecs_data: ECS sensor readings
                - electrical_data: Electrical system readings
                - hydraulics_data: Hydraulic system readings

        Returns:
            True if update was successful
        """
        try:
            # Update ECS
            if "ecs_data" in state_data:
                ecs_data = state_data["ecs_data"]
                self.ecs.cabin_temp_c = ecs_data.get("temp_c", self.ecs.cabin_temp_c)
                self.ecs.cabin_pressure_hpa = ecs_data.get(
                    "pressure_hpa", self.ecs.cabin_pressure_hpa
                )
                self.ecs.cabin_humidity_pct = ecs_data.get(
                    "humidity_pct", self.ecs.cabin_humidity_pct
                )
                self.ecs.pack_status = ecs_data.get("pack_status", self.ecs.pack_status)

            # Update electrical
            if "electrical_data" in state_data:
                elec_data = state_data["electrical_data"]
                self.electrical.bus_voltage_v = elec_data.get(
                    "voltage_v", self.electrical.bus_voltage_v
                )
                self.electrical.current_draw_a = elec_data.get(
                    "current_a", self.electrical.current_draw_a
                )
                self.electrical.battery_soc_pct = elec_data.get(
                    "battery_soc_pct", self.electrical.battery_soc_pct
                )
                self.electrical.load_pct = elec_data.get(
                    "load_pct", self.electrical.load_pct
                )

            # Update hydraulics
            if "hydraulics_data" in state_data:
                hyd_data = state_data["hydraulics_data"]
                self.hydraulics.pressure_bar = hyd_data.get(
                    "pressure_bar", self.hydraulics.pressure_bar
                )
                self.hydraulics.fluid_level_pct = hyd_data.get(
                    "fluid_level_pct", self.hydraulics.fluid_level_pct
                )
                self.hydraulics.temperature_c = hyd_data.get(
                    "temperature_c", self.hydraulics.temperature_c
                )

            # Update subsystem health
            self._update_subsystem_health()

            # Update state
            self.state.timestamp = datetime.utcnow()
            self.state.parameters.update(
                {
                    "cabin_temp_c": self.ecs.cabin_temp_c,
                    "bus_voltage_v": self.electrical.bus_voltage_v,
                    "hydraulic_pressure_bar": self.hydraulics.pressure_bar,
                    "subsystem_health": self._subsystem_health.copy(),
                }
            )

            # Set overall health status
            degraded_count = sum(
                1 for s in self._subsystem_health.values() if s != "nominal"
            )
            if degraded_count == 0:
                self.state.health_status = "nominal"
            elif degraded_count <= 2:
                self.state.health_status = "degraded"
            else:
                self.state.health_status = "critical"

            logger.debug("Systems model updated: %s", self.model_id)
            return True

        except (KeyError, TypeError, ValueError) as e:
            logger.error("Failed to update systems model: %s", e)
            return False

    def predict(self, inputs: dict[str, Any], horizon: float = 1.0) -> dict[str, Any]:
        """
        Predict future systems state.

        Args:
            inputs: Prediction inputs including:
                - ambient_temp_c: External temperature
                - electrical_load_pct: Expected electrical load
                - flight_phase: Current flight phase
            horizon: Prediction horizon in hours

        Returns:
            Dictionary containing predictions
        """
        if not self._initialized:
            logger.warning("Model not initialized, predictions may be inaccurate")

        ambient_temp = inputs.get("ambient_temp_c", -40.0)
        electrical_load = inputs.get("electrical_load_pct", 50.0)

        # Predict battery state
        battery_drain_rate = self._config.get("battery_drain_rate_pct_h", 5.0)
        predicted_battery = max(
            0, self.electrical.battery_soc_pct - (battery_drain_rate * electrical_load / 100 * horizon)
        )

        # Predict hydraulic fluid temperature
        temp_rise_rate = self._config.get("hyd_temp_rise_c_h", 2.0)
        predicted_hyd_temp = self.hydraulics.temperature_c + (temp_rise_rate * horizon)

        # Predict ECS performance
        cooling_capacity = self._config.get("ecs_cooling_capacity_kw", 50.0)
        heat_load = (ambient_temp + 50) * 0.5  # Simplified heat load
        ecs_margin = cooling_capacity - heat_load

        return {
            "predicted_battery_soc_pct": predicted_battery,
            "predicted_hyd_temp_c": predicted_hyd_temp,
            "ecs_capacity_margin_kw": ecs_margin,
            "maintenance_items": self._predict_maintenance(horizon),
            "confidence": self.state.confidence,
            "horizon_hours": horizon,
        }

    def validate(
        self, reference_data: Optional[dict[str, Any]] = None
    ) -> ValidationResult:
        """
        Validate the systems model against reference data.

        Args:
            reference_data: Reference data from ground test or flight

        Returns:
            ValidationResult with accuracy metrics
        """
        deviations: list[dict[str, Any]] = []

        if reference_data:
            # Validate ECS
            if "measured_cabin_temp_c" in reference_data:
                measured = reference_data["measured_cabin_temp_c"]
                predicted = self.ecs.cabin_temp_c
                deviation = abs(predicted - measured)
                if deviation > 2.0:  # 2°C threshold
                    deviations.append(
                        {
                            "parameter": "cabin_temp_c",
                            "predicted": predicted,
                            "measured": measured,
                            "deviation": deviation,
                        }
                    )

            # Validate electrical
            if "measured_voltage_v" in reference_data:
                measured = reference_data["measured_voltage_v"]
                predicted = self.electrical.bus_voltage_v
                deviation = abs(predicted - measured)
                if deviation > 0.5:  # 0.5V threshold
                    deviations.append(
                        {
                            "parameter": "bus_voltage_v",
                            "predicted": predicted,
                            "measured": measured,
                            "deviation": deviation,
                        }
                    )

        # Calculate accuracy
        if deviations:
            # Use relative accuracy for systems
            accuracy = max(0.0, 100.0 - len(deviations) * 5)
        else:
            accuracy = 100.0 if reference_data else 95.0

        is_valid = accuracy >= 85.0 and self.state.health_status != "critical"

        result = ValidationResult(
            is_valid=is_valid,
            accuracy=accuracy,
            deviations=deviations,
            notes=f"Validated {len(self._subsystem_health)} subsystems",
        )

        self.state.last_validated = result.timestamp
        logger.info("Systems validation complete: accuracy=%.1f%%", accuracy)

        return result

    def _update_subsystem_health(self) -> None:
        """Update subsystem health based on current readings."""
        # ECS health
        if self.ecs.cabin_temp_c < 15 or self.ecs.cabin_temp_c > 30:
            self._subsystem_health["ecs"] = "degraded"
        elif self.ecs.cabin_pressure_hpa < 800:
            self._subsystem_health["ecs"] = "warning"
        else:
            self._subsystem_health["ecs"] = "nominal"

        # Electrical health
        if self.electrical.bus_voltage_v < 24 or self.electrical.bus_voltage_v > 32:
            self._subsystem_health["electrical"] = "warning"
        elif self.electrical.battery_soc_pct < 20:
            self._subsystem_health["electrical"] = "degraded"
        else:
            self._subsystem_health["electrical"] = "nominal"

        # Hydraulics health
        if self.hydraulics.pressure_bar < 200 or self.hydraulics.pressure_bar > 350:
            self._subsystem_health["hydraulics"] = "warning"
        elif self.hydraulics.fluid_level_pct < 80:
            self._subsystem_health["hydraulics"] = "degraded"
        else:
            self._subsystem_health["hydraulics"] = "nominal"

    def _predict_maintenance(self, horizon: float) -> list[str]:
        """Predict maintenance items based on current state and horizon."""
        items = []

        # Check battery
        if self.electrical.battery_soc_pct < 50:
            items.append("Battery charge recommended")

        # Check hydraulic fluid
        if self.hydraulics.fluid_level_pct < 90:
            items.append("Hydraulic fluid top-up")

        # Check ECS filters (time-based)
        if horizon > 100:
            items.append("ECS filter inspection")

        return items

    def update_subsystem(
        self, subsystem: str, status_data: dict[str, Any]
    ) -> bool:
        """
        Update a specific subsystem.

        Args:
            subsystem: Subsystem name (ecs, electrical, hydraulics)
            status_data: Status data for the subsystem

        Returns:
            True if update was successful
        """
        if subsystem == "ecs":
            return self.update({"ecs_data": status_data})
        elif subsystem == "electrical":
            return self.update({"electrical_data": status_data})
        elif subsystem == "hydraulics":
            return self.update({"hydraulics_data": status_data})
        else:
            logger.warning("Unknown subsystem: %s", subsystem)
            return False

    def get_subsystem_status(self, subsystem: str) -> dict[str, Any]:
        """
        Get status of a specific subsystem.

        Args:
            subsystem: Subsystem name

        Returns:
            Dictionary containing subsystem status
        """
        if subsystem == "ecs":
            return {
                "cabin_temp_c": self.ecs.cabin_temp_c,
                "cabin_pressure_hpa": self.ecs.cabin_pressure_hpa,
                "cabin_humidity_pct": self.ecs.cabin_humidity_pct,
                "pack_status": self.ecs.pack_status,
                "health": self._subsystem_health.get("ecs", "unknown"),
            }
        elif subsystem == "electrical":
            return {
                "bus_voltage_v": self.electrical.bus_voltage_v,
                "current_draw_a": self.electrical.current_draw_a,
                "battery_soc_pct": self.electrical.battery_soc_pct,
                "generator_status": self.electrical.generator_status,
                "load_pct": self.electrical.load_pct,
                "health": self._subsystem_health.get("electrical", "unknown"),
            }
        elif subsystem == "hydraulics":
            return {
                "pressure_bar": self.hydraulics.pressure_bar,
                "fluid_level_pct": self.hydraulics.fluid_level_pct,
                "pump_status": self.hydraulics.pump_status,
                "temperature_c": self.hydraulics.temperature_c,
                "health": self._subsystem_health.get("hydraulics", "unknown"),
            }
        else:
            return {"error": f"Unknown subsystem: {subsystem}"}

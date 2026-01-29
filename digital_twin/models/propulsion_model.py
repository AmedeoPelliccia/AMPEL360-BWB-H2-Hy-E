# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Propulsion system model for AMPEL360 digital twin.

This module provides the propulsion system model for the hydrogen-electric
hybrid propulsion, covering ATA chapters 70-80 (Power Plant, Engine, Fuel).
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import logging

from digital_twin.models.base_model import BaseModel, ModelState, ValidationResult

logger = logging.getLogger(__name__)


@dataclass
class PropulsionPerformance:
    """Propulsion system performance metrics."""

    thrust_n: float = 0.0
    fuel_flow_kg_s: float = 0.0
    efficiency: float = 0.0
    temperature_egt_k: float = 0.0
    pressure_ratio: float = 0.0
    rpm: float = 0.0


@dataclass
class H2SystemStatus:
    """Hydrogen fuel system status."""

    tank_pressure_bar: float = 0.0
    tank_temperature_k: float = 20.0
    fuel_remaining_kg: float = 0.0
    flow_rate_kg_s: float = 0.0
    leak_detected: bool = False


class PropulsionModel(BaseModel):
    """
    Digital twin model for the hydrogen-electric hybrid propulsion system.

    This model represents the propulsion state of the AMPEL360, including
    hydrogen fuel system, electric motors, and overall performance.

    Attributes:
        performance: Current propulsion performance metrics
        h2_status: Hydrogen fuel system status
        electric_power_kw: Current electric power output
    """

    ATA_CHAPTERS = ["70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80"]

    def __init__(
        self,
        model_id: str = "DT-Q100-PROPULSION-001",
        config_path: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the propulsion model.

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
        self.performance = PropulsionPerformance()
        self.h2_status = H2SystemStatus()
        self.electric_power_kw: float = 0.0

    def initialize(self) -> bool:
        """
        Initialize the propulsion model with baseline data.

        Returns:
            True if initialization was successful
        """
        try:
            # Set default propulsion parameters from config or defaults
            self.h2_status.fuel_remaining_kg = self._config.get(
                "max_fuel_kg", 5000.0
            )
            self.h2_status.tank_pressure_bar = self._config.get(
                "nominal_pressure_bar", 700.0
            )
            self.h2_status.tank_temperature_k = self._config.get(
                "storage_temp_k", 20.0
            )

            self.state = ModelState(
                parameters={
                    "propulsion_status": "idle",
                    "fuel_remaining_pct": 100.0,
                    "efficiency": 0.0,
                },
                health_status="nominal",
                confidence=1.0,
            )
            self._initialized = True
            logger.info("Propulsion model initialized: %s", self.model_id)
            return True

        except (KeyError, TypeError) as e:
            logger.error("Failed to initialize propulsion model: %s", e)
            return False

    def update(self, state_data: dict[str, Any]) -> bool:
        """
        Update the propulsion model with new sensor data.

        Args:
            state_data: Dictionary containing sensor readings:
                - thrust_sensors: Thrust measurements
                - fuel_flow_sensors: Fuel flow rate
                - temperature_sensors: EGT and other temps
                - pressure_sensors: Pressure readings
                - h2_tank_data: Hydrogen tank status

        Returns:
            True if update was successful
        """
        try:
            # Update thrust
            if "thrust_sensors" in state_data:
                thrust_data = state_data["thrust_sensors"]
                if thrust_data:
                    self.performance.thrust_n = sum(thrust_data)

            # Update fuel flow
            if "fuel_flow_sensors" in state_data:
                flow_data = state_data["fuel_flow_sensors"]
                if flow_data:
                    self.performance.fuel_flow_kg_s = sum(flow_data)

            # Update temperatures
            if "temperature_sensors" in state_data:
                temp_data = state_data["temperature_sensors"]
                if temp_data and len(temp_data) > 0:
                    self.performance.temperature_egt_k = max(temp_data)

            # Update H2 tank status
            if "h2_tank_data" in state_data:
                tank_data = state_data["h2_tank_data"]
                self.h2_status.tank_pressure_bar = tank_data.get(
                    "pressure_bar", self.h2_status.tank_pressure_bar
                )
                self.h2_status.tank_temperature_k = tank_data.get(
                    "temperature_k", self.h2_status.tank_temperature_k
                )
                self.h2_status.fuel_remaining_kg = tank_data.get(
                    "fuel_remaining_kg", self.h2_status.fuel_remaining_kg
                )
                self.h2_status.leak_detected = tank_data.get("leak_detected", False)

            # Update electric power
            if "electric_power_kw" in state_data:
                self.electric_power_kw = state_data["electric_power_kw"]

            # Calculate efficiency
            self._calculate_efficiency()

            # Update state
            max_fuel = self._config.get("max_fuel_kg", 5000.0)
            fuel_pct = (self.h2_status.fuel_remaining_kg / max_fuel) * 100

            self.state.timestamp = datetime.utcnow()
            self.state.parameters.update(
                {
                    "thrust_n": self.performance.thrust_n,
                    "fuel_remaining_pct": fuel_pct,
                    "efficiency": self.performance.efficiency,
                    "egt_k": self.performance.temperature_egt_k,
                }
            )

            # Check for anomalies
            if self.h2_status.leak_detected:
                self.state.health_status = "warning"
            elif self.performance.temperature_egt_k > 1200:  # K
                self.state.health_status = "caution"
            else:
                self.state.health_status = "nominal"

            logger.debug("Propulsion model updated: %s", self.model_id)
            return True

        except (KeyError, TypeError, ValueError) as e:
            logger.error("Failed to update propulsion model: %s", e)
            return False

    def predict(self, inputs: dict[str, Any], horizon: float = 1.0) -> dict[str, Any]:
        """
        Predict future propulsion state.

        Args:
            inputs: Prediction inputs including:
                - throttle_setting: Expected throttle (0-1)
                - altitude_m: Expected cruise altitude
                - speed_mach: Expected speed
            horizon: Prediction horizon in hours

        Returns:
            Dictionary containing predictions
        """
        if not self._initialized:
            logger.warning("Model not initialized, predictions may be inaccurate")

        throttle = inputs.get("throttle_setting", 0.8)
        altitude = inputs.get("altitude_m", 10000)

        # Predict fuel consumption
        base_consumption = self._config.get("base_consumption_kg_h", 300.0)
        altitude_factor = 1.0 - (altitude / 50000) * 0.3  # Less efficient at altitude
        predicted_consumption = base_consumption * throttle * altitude_factor * horizon

        # Predict remaining fuel
        remaining_fuel = max(0, self.h2_status.fuel_remaining_kg - predicted_consumption)
        max_fuel = self._config.get("max_fuel_kg", 5000.0)

        # Predict range
        if self.performance.fuel_flow_kg_s > 0:
            hours_remaining = remaining_fuel / (self.performance.fuel_flow_kg_s * 3600)
        else:
            hours_remaining = remaining_fuel / (base_consumption * throttle)

        return {
            "predicted_fuel_remaining_kg": remaining_fuel,
            "predicted_fuel_remaining_pct": (remaining_fuel / max_fuel) * 100,
            "predicted_consumption_kg": predicted_consumption,
            "estimated_range_hours": hours_remaining,
            "efficiency_prediction": self.performance.efficiency * 0.98,  # Slight degradation
            "maintenance_recommended": self.performance.temperature_egt_k > 1100,
            "confidence": self.state.confidence,
            "horizon_hours": horizon,
        }

    def validate(
        self, reference_data: Optional[dict[str, Any]] = None
    ) -> ValidationResult:
        """
        Validate the propulsion model against reference data.

        Args:
            reference_data: Reference data from test bench or flight

        Returns:
            ValidationResult with accuracy metrics
        """
        deviations: list[dict[str, Any]] = []

        if reference_data:
            # Compare thrust
            if "measured_thrust_n" in reference_data:
                measured = reference_data["measured_thrust_n"]
                predicted = self.performance.thrust_n
                if measured > 0:
                    deviation = abs(predicted - measured) / measured
                    if deviation > 0.05:  # 5% threshold
                        deviations.append(
                            {
                                "parameter": "thrust_n",
                                "predicted": predicted,
                                "measured": measured,
                                "deviation_pct": deviation * 100,
                            }
                        )

            # Compare fuel flow
            if "measured_fuel_flow_kg_s" in reference_data:
                measured = reference_data["measured_fuel_flow_kg_s"]
                predicted = self.performance.fuel_flow_kg_s
                if measured > 0:
                    deviation = abs(predicted - measured) / measured
                    if deviation > 0.03:  # 3% threshold for fuel
                        deviations.append(
                            {
                                "parameter": "fuel_flow_kg_s",
                                "predicted": predicted,
                                "measured": measured,
                                "deviation_pct": deviation * 100,
                            }
                        )

        # Calculate accuracy
        if deviations:
            avg_deviation = sum(d["deviation_pct"] for d in deviations) / len(deviations)
            accuracy = max(0.0, 100.0 - avg_deviation)
        else:
            accuracy = 100.0 if reference_data else 95.0

        is_valid = (
            accuracy >= 90.0
            and not self.h2_status.leak_detected
            and self.performance.temperature_egt_k < 1200
        )

        result = ValidationResult(
            is_valid=is_valid,
            accuracy=accuracy,
            deviations=deviations,
            notes=f"Validated propulsion model, H2 leak status: {self.h2_status.leak_detected}",
        )

        self.state.last_validated = result.timestamp
        logger.info("Propulsion validation complete: accuracy=%.1f%%", accuracy)

        return result

    def _calculate_efficiency(self) -> None:
        """Calculate propulsion system efficiency."""
        if self.performance.fuel_flow_kg_s > 0 and self.performance.thrust_n > 0:
            # Simplified specific thrust calculation
            h2_energy_density = 120  # MJ/kg
            power_output = self.performance.thrust_n * 200  # Assume 200 m/s exhaust
            power_input = self.performance.fuel_flow_kg_s * h2_energy_density * 1e6
            self.performance.efficiency = min(1.0, power_output / max(power_input, 1))
        else:
            self.performance.efficiency = 0.0

    def calculate_performance(
        self, throttle: float = 1.0, altitude_m: float = 0.0, mach: float = 0.0
    ) -> dict[str, float]:
        """
        Calculate propulsion performance for given conditions.

        Args:
            throttle: Throttle setting (0-1)
            altitude_m: Altitude in meters
            mach: Mach number

        Returns:
            Dictionary of performance parameters
        """
        # Simplified performance calculation
        max_thrust = self._config.get("max_thrust_n", 200000)
        max_fuel_flow = self._config.get("max_fuel_flow_kg_s", 2.0)

        # Altitude effect on thrust
        altitude_factor = 1.0 - (altitude_m / 15000) * 0.4

        # Calculate performance
        thrust = max_thrust * throttle * max(0.1, altitude_factor)
        fuel_flow = max_fuel_flow * throttle * (1 - altitude_factor * 0.2)

        return {
            "thrust_n": thrust,
            "fuel_flow_kg_s": fuel_flow,
            "sfc": fuel_flow / max(thrust, 1) * 1e6,  # Specific fuel consumption
            "altitude_factor": altitude_factor,
        }

    def predict_maintenance(self, flight_hours: float) -> dict[str, Any]:
        """
        Predict maintenance needs after additional flight hours.

        Args:
            flight_hours: Additional flight hours to predict

        Returns:
            Dictionary with maintenance predictions
        """
        overhaul_interval = self._config.get("overhaul_interval_hours", 3000)
        current_hours = self._config.get("current_hours", 0)

        hours_to_overhaul = overhaul_interval - ((current_hours + flight_hours) % overhaul_interval)

        return {
            "hours_to_overhaul": hours_to_overhaul,
            "overhaul_due": hours_to_overhaul < 100,
            "inspection_items": self._get_inspection_items(current_hours + flight_hours),
            "predicted_egt_trend": "stable" if self.performance.temperature_egt_k < 1000 else "increasing",
        }

    def _get_inspection_items(self, total_hours: float) -> list[str]:
        """Get inspection items based on total hours."""
        items = []
        if total_hours > 500:
            items.append("H2 fuel system inspection")
        if total_hours > 1000:
            items.append("Electric motor bearing check")
        if total_hours > 2000:
            items.append("Fuel cell stack inspection")
        if total_hours > 3000:
            items.append("Complete propulsion overhaul")
        return items

# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Airframe structural model for AMPEL360 digital twin.

This module provides the structural model for the BWB airframe, covering
ATA chapters 51-57 (Structures, Doors, Fuselage, Nacelles, Stabilizers, Windows, Wings).
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional
import logging

from digital_twin.models.base_model import BaseModel, ModelState, ValidationResult

logger = logging.getLogger(__name__)


@dataclass
class StructuralHealth:
    """Structural health monitoring data."""

    fatigue_cycles: int = 0
    damage_index: float = 0.0
    strain_max: float = 0.0
    temperature_max: float = 0.0
    last_inspection: Optional[datetime] = None


@dataclass
class LoadDistribution:
    """Load distribution across airframe sections."""

    wing_root_bending: float = 0.0
    fuselage_shear: float = 0.0
    empennage_torsion: float = 0.0
    landing_gear_load: float = 0.0


class AirframeModel(BaseModel):
    """
    Digital twin model for the BWB airframe structure.

    This model represents the structural state of the AMPEL360 blended wing body
    airframe, including structural health monitoring, load distribution, and
    fatigue predictions.

    Attributes:
        structural_health: Current structural health metrics
        load_distribution: Current load distribution
        baseline_dimensions: Reference geometry from baseline_dimensions.json
    """

    ATA_CHAPTERS = ["51", "52", "53", "54", "55", "56", "57"]

    def __init__(
        self,
        model_id: str = "DT-Q100-AIRFRAME-001",
        config_path: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the airframe model.

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
        self.structural_health = StructuralHealth()
        self.load_distribution = LoadDistribution()
        self.baseline_dimensions: dict[str, float] = {}

    def initialize(self) -> bool:
        """
        Initialize the airframe model with baseline data.

        Loads baseline dimensions and sets up initial structural state.

        Returns:
            True if initialization was successful
        """
        try:
            # Load baseline dimensions from configuration
            if "baseline_dimensions" in self._config:
                self.baseline_dimensions = self._config["baseline_dimensions"]
            else:
                # Default Q100 dimensions
                self.baseline_dimensions = {
                    "wingspan_m": 52.0,
                    "wing_area_m2": 845.0,
                    "aspect_ratio": 3.2,
                    "overall_length_m": 35.0,
                    "center_body_depth_m": 3.5,
                }

            self.state = ModelState(
                parameters={
                    "structural_health": "nominal",
                    "fatigue_cycles": 0,
                    "damage_index": 0.0,
                },
                health_status="nominal",
                confidence=1.0,
            )
            self._initialized = True
            logger.info("Airframe model initialized: %s", self.model_id)
            return True

        except (KeyError, TypeError) as e:
            logger.error("Failed to initialize airframe model: %s", e)
            return False

    def update(self, state_data: dict[str, Any]) -> bool:
        """
        Update the airframe model with new sensor data.

        Args:
            state_data: Dictionary containing sensor readings:
                - strain_gauges: List of strain gauge readings
                - accelerometers: List of accelerometer readings
                - temperature_sensors: List of temperature readings
                - flight_hours: Current flight hours

        Returns:
            True if update was successful
        """
        try:
            # Update structural health from strain gauges
            if "strain_gauges" in state_data:
                strain_values = state_data["strain_gauges"]
                if strain_values:
                    self.structural_health.strain_max = max(strain_values)

            # Update temperature monitoring
            if "temperature_sensors" in state_data:
                temp_values = state_data["temperature_sensors"]
                if temp_values:
                    self.structural_health.temperature_max = max(temp_values)

            # Update fatigue cycles
            if "flight_hours" in state_data:
                # Approximate cycles from flight hours (landing/takeoff cycles)
                flight_hours = state_data["flight_hours"]
                self.structural_health.fatigue_cycles = int(flight_hours * 0.5)

            # Update load distribution from accelerometers
            if "accelerometers" in state_data:
                accel_data = state_data["accelerometers"]
                if accel_data and len(accel_data) >= 4:
                    self.load_distribution.wing_root_bending = abs(accel_data[0])
                    self.load_distribution.fuselage_shear = abs(accel_data[1])
                    self.load_distribution.empennage_torsion = abs(accel_data[2])
                    self.load_distribution.landing_gear_load = abs(accel_data[3])

            # Calculate damage index
            self._calculate_damage_index()

            # Update state timestamp
            self.state.timestamp = datetime.utcnow()
            self.state.parameters.update(
                {
                    "fatigue_cycles": self.structural_health.fatigue_cycles,
                    "damage_index": self.structural_health.damage_index,
                    "strain_max": self.structural_health.strain_max,
                }
            )

            logger.debug("Airframe model updated: %s", self.model_id)
            return True

        except (KeyError, TypeError, ValueError) as e:
            logger.error("Failed to update airframe model: %s", e)
            return False

    def predict(self, inputs: dict[str, Any], horizon: float = 1.0) -> dict[str, Any]:
        """
        Predict future structural state.

        Args:
            inputs: Prediction inputs including:
                - flight_profile: Expected flight profile
                - additional_cycles: Expected additional flight cycles
            horizon: Prediction horizon in hours

        Returns:
            Dictionary containing predictions:
                - remaining_life_cycles: Estimated remaining fatigue life
                - maintenance_due: Predicted maintenance interval
                - confidence: Prediction confidence level
        """
        if not self._initialized:
            logger.warning("Model not initialized, predictions may be inaccurate")

        # Calculate remaining fatigue life
        design_life_cycles = self._config.get("design_life_cycles", 60000)
        current_cycles = self.structural_health.fatigue_cycles
        additional_cycles = inputs.get("additional_cycles", int(horizon * 0.5))

        predicted_cycles = current_cycles + additional_cycles
        remaining_life = max(0, design_life_cycles - predicted_cycles)

        # Estimate maintenance interval
        inspection_interval = self._config.get("inspection_interval_cycles", 5000)
        cycles_to_inspection = inspection_interval - (current_cycles % inspection_interval)

        # Adjust confidence based on damage index
        confidence = max(0.5, 1.0 - self.structural_health.damage_index)

        return {
            "remaining_life_cycles": remaining_life,
            "predicted_cycles": predicted_cycles,
            "cycles_to_inspection": cycles_to_inspection,
            "maintenance_due": remaining_life < inspection_interval,
            "damage_trend": "increasing" if self.structural_health.damage_index > 0.1 else "stable",
            "confidence": confidence,
            "horizon_hours": horizon,
        }

    def validate(
        self, reference_data: Optional[dict[str, Any]] = None
    ) -> ValidationResult:
        """
        Validate the airframe model against reference data.

        Args:
            reference_data: Reference data for validation (e.g., from inspections)

        Returns:
            ValidationResult with accuracy metrics
        """
        deviations: list[dict[str, Any]] = []

        if reference_data:
            # Compare predicted strain against measured
            if "measured_strain" in reference_data:
                measured = reference_data["measured_strain"]
                predicted = self.structural_health.strain_max
                deviation = abs(predicted - measured) / max(measured, 0.001)
                if deviation > 0.1:  # 10% threshold
                    deviations.append(
                        {
                            "parameter": "strain_max",
                            "predicted": predicted,
                            "measured": measured,
                            "deviation_pct": deviation * 100,
                        }
                    )

            # Compare dimensions against baseline
            if "dimensions" in reference_data:
                for key, measured in reference_data["dimensions"].items():
                    if key in self.baseline_dimensions:
                        baseline = self.baseline_dimensions[key]
                        deviation = abs(baseline - measured) / max(baseline, 0.001)
                        if deviation > 0.01:  # 1% threshold
                            deviations.append(
                                {
                                    "parameter": key,
                                    "baseline": baseline,
                                    "measured": measured,
                                    "deviation_pct": deviation * 100,
                                }
                            )

        # Calculate overall accuracy
        if deviations:
            avg_deviation = sum(d["deviation_pct"] for d in deviations) / len(deviations)
            accuracy = max(0.0, 100.0 - avg_deviation)
        else:
            accuracy = 100.0 if reference_data else 95.0  # Assume baseline accuracy

        is_valid = accuracy >= 90.0 and self.structural_health.damage_index < 0.5

        result = ValidationResult(
            is_valid=is_valid,
            accuracy=accuracy,
            deviations=deviations,
            notes=f"Validated against {len(reference_data) if reference_data else 0} reference points",
        )

        self.state.last_validated = result.timestamp
        logger.info("Airframe validation complete: accuracy=%.1f%%", accuracy)

        return result

    def _calculate_damage_index(self) -> None:
        """Calculate cumulative damage index based on fatigue and loads."""
        # Simplified Miner's rule-based calculation
        design_life = self._config.get("design_life_cycles", 60000)
        cycles = self.structural_health.fatigue_cycles

        # Base damage from cycles
        cycle_damage = cycles / design_life

        # Additional damage from high strain events
        strain_limit = self._config.get("strain_limit", 0.002)
        if self.structural_health.strain_max > strain_limit:
            strain_damage = (self.structural_health.strain_max - strain_limit) / strain_limit * 0.1
        else:
            strain_damage = 0.0

        # Combined damage index (capped at 1.0)
        self.structural_health.damage_index = min(1.0, cycle_damage + strain_damage)

    def calculate_stress(
        self, load_case: str = "cruise", load_factor: float = 1.0
    ) -> dict[str, float]:
        """
        Calculate stress distribution for a given load case.

        Args:
            load_case: Load case identifier (cruise, maneuver, gust)
            load_factor: Load factor multiplier

        Returns:
            Dictionary of stress values at key locations
        """
        # Simplified stress calculation
        base_stresses = {
            "wing_root": 150.0,  # MPa
            "center_body": 80.0,
            "fuselage_joint": 120.0,
            "empennage_attachment": 90.0,
        }

        # Load case multipliers
        case_factors = {
            "cruise": 1.0,
            "maneuver": 1.5,
            "gust": 1.3,
            "landing": 1.8,
        }

        factor = case_factors.get(load_case, 1.0) * load_factor

        return {location: stress * factor for location, stress in base_stresses.items()}

    def predict_fatigue(self, flight_hours: float) -> dict[str, Any]:
        """
        Predict fatigue state after additional flight hours.

        Args:
            flight_hours: Additional flight hours to predict

        Returns:
            Dictionary with fatigue predictions
        """
        return self.predict(
            {"additional_cycles": int(flight_hours * 0.5)}, horizon=flight_hours
        )

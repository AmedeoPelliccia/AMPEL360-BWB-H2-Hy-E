# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Predictive maintenance models for AMPEL360 digital twin.

This module provides machine learning models for predicting component failures
and maintenance needs based on sensor data and historical patterns.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class MaintenancePrediction:
    """Result of a maintenance prediction."""

    component_id: str
    failure_probability: float
    estimated_rul_hours: float  # Remaining Useful Life
    confidence: float
    recommended_action: str
    urgency: str  # low, medium, high, critical
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ModelMetadata:
    """ML model metadata for traceability."""

    model_id: str
    version: str
    trained_date: Optional[datetime] = None
    training_samples: int = 0
    accuracy_score: float = 0.0
    feature_names: list[str] = field(default_factory=list)


class PredictiveMaintenance:
    """
    Predictive maintenance model for aircraft components.

    Uses machine learning to predict component failures and recommend
    maintenance actions based on sensor data patterns.

    Attributes:
        component_type: Type of component (propulsion, airframe, systems)
        model_version: Version of the ML model
        metadata: Model metadata for traceability
    """

    URGENCY_THRESHOLDS = {
        "critical": 0.8,
        "high": 0.6,
        "medium": 0.3,
        "low": 0.0,
    }

    def __init__(
        self,
        component_type: str = "generic",
        model_version: str = "1.0.0",
        model_id: Optional[str] = None,
    ) -> None:
        """
        Initialize the predictive maintenance model.

        Args:
            component_type: Type of component being monitored
            model_version: Version string for the model
            model_id: Optional model identifier
        """
        self.component_type = component_type
        self.model_version = model_version
        self.model_id = model_id or f"ML-PM-{component_type.upper()}-001"

        self.metadata = ModelMetadata(
            model_id=self.model_id,
            version=model_version,
        )

        self._is_trained = False
        self._feature_weights: dict[str, float] = {}
        self._baseline_metrics: dict[str, float] = {}

        logger.info("Initialized predictive maintenance model: %s", self.model_id)

    def train(
        self,
        training_data: list[dict[str, Any]],
        labels: list[int],
        validation_split: float = 0.2,
    ) -> dict[str, Any]:
        """
        Train the predictive maintenance model.

        Args:
            training_data: List of feature dictionaries
            labels: List of failure labels (0=no failure, 1=failure)
            validation_split: Fraction of data to use for validation

        Returns:
            Dictionary containing training metrics
        """
        if not training_data:
            logger.error("No training data provided")
            return {"success": False, "error": "No training data"}

        # Extract feature names from first sample
        if training_data:
            self.metadata.feature_names = list(training_data[0].keys())

        # Simplified training simulation
        # In production, this would use sklearn, tensorflow, or similar
        n_samples = len(training_data)
        n_failures = sum(labels)
        failure_rate = n_failures / max(n_samples, 1)

        # Calculate baseline metrics from training data
        for feature in self.metadata.feature_names:
            values = [d.get(feature, 0) for d in training_data]
            if values:
                self._baseline_metrics[feature] = sum(values) / len(values)
                # Simplified feature importance based on variance
                variance = sum((v - self._baseline_metrics[feature]) ** 2 for v in values)
                self._feature_weights[feature] = min(1.0, variance / max(n_samples, 1) * 100)

        # Normalize weights
        total_weight = sum(self._feature_weights.values())
        if total_weight > 0:
            self._feature_weights = {
                k: v / total_weight for k, v in self._feature_weights.items()
            }

        self._is_trained = True
        self.metadata.trained_date = datetime.utcnow()
        self.metadata.training_samples = n_samples
        self.metadata.accuracy_score = 0.85 + (0.1 * (1 - failure_rate))  # Simulated

        logger.info(
            "Model trained: %d samples, %.1f%% accuracy",
            n_samples,
            self.metadata.accuracy_score * 100,
        )

        return {
            "success": True,
            "samples_trained": n_samples,
            "failure_rate": failure_rate,
            "accuracy": self.metadata.accuracy_score,
            "features": len(self.metadata.feature_names),
        }

    def predict(
        self, sensor_data: dict[str, Any], component_id: str = "UNKNOWN"
    ) -> MaintenancePrediction:
        """
        Predict maintenance needs for a component.

        Args:
            sensor_data: Dictionary of current sensor readings
            component_id: Identifier for the component

        Returns:
            MaintenancePrediction with failure probability and recommendations
        """
        if not self._is_trained:
            logger.warning("Model not trained, using baseline predictions")
            return self._baseline_prediction(component_id)

        # Calculate anomaly score based on deviation from baseline
        anomaly_score = 0.0
        valid_features = 0

        for feature, weight in self._feature_weights.items():
            if feature in sensor_data and feature in self._baseline_metrics:
                value = sensor_data[feature]
                baseline = self._baseline_metrics[feature]
                if baseline != 0:
                    deviation = abs(value - baseline) / abs(baseline)
                    anomaly_score += deviation * weight
                    valid_features += 1

        # Normalize to probability
        failure_probability = min(1.0, anomaly_score / max(valid_features, 1))

        # Calculate RUL (simplified exponential decay model)
        base_rul = 1000.0  # Base remaining useful life in hours
        estimated_rul = base_rul * (1 - failure_probability) ** 2

        # Determine urgency
        urgency = "low"
        for level, threshold in sorted(
            self.URGENCY_THRESHOLDS.items(),
            key=lambda x: x[1],
            reverse=True,
        ):
            if failure_probability >= threshold:
                urgency = level
                break

        # Generate recommendation
        recommended_action = self._generate_recommendation(
            failure_probability, estimated_rul, urgency
        )

        # Calculate confidence based on data completeness
        data_completeness = valid_features / max(len(self._feature_weights), 1)
        confidence = self.metadata.accuracy_score * data_completeness

        prediction = MaintenancePrediction(
            component_id=component_id,
            failure_probability=failure_probability,
            estimated_rul_hours=estimated_rul,
            confidence=confidence,
            recommended_action=recommended_action,
            urgency=urgency,
        )

        logger.debug(
            "Prediction for %s: prob=%.2f, RUL=%.0fh, urgency=%s",
            component_id,
            failure_probability,
            estimated_rul,
            urgency,
        )

        return prediction

    def predict_batch(
        self, sensor_data_list: list[dict[str, Any]], component_ids: list[str]
    ) -> list[MaintenancePrediction]:
        """
        Predict maintenance needs for multiple components.

        Args:
            sensor_data_list: List of sensor data dictionaries
            component_ids: List of component identifiers

        Returns:
            List of MaintenancePrediction objects
        """
        if len(sensor_data_list) != len(component_ids):
            raise ValueError("sensor_data_list and component_ids must have same length")

        return [
            self.predict(data, comp_id)
            for data, comp_id in zip(sensor_data_list, component_ids)
        ]

    def _baseline_prediction(self, component_id: str) -> MaintenancePrediction:
        """Generate baseline prediction when model is not trained."""
        return MaintenancePrediction(
            component_id=component_id,
            failure_probability=0.1,
            estimated_rul_hours=900.0,
            confidence=0.3,
            recommended_action="Model not trained - recommend manual inspection",
            urgency="low",
        )

    def _generate_recommendation(
        self, probability: float, rul: float, urgency: str
    ) -> str:
        """Generate maintenance recommendation based on prediction."""
        if urgency == "critical":
            return "IMMEDIATE INSPECTION REQUIRED - Schedule maintenance within 24 hours"
        elif urgency == "high":
            return f"Schedule maintenance within {int(rul / 10)} flight hours"
        elif urgency == "medium":
            return f"Plan maintenance at next scheduled stop (RUL: {int(rul)}h)"
        else:
            return "Continue normal operations - monitor for changes"

    def get_feature_importance(self) -> dict[str, float]:
        """
        Get feature importance scores.

        Returns:
            Dictionary mapping feature names to importance scores
        """
        return self._feature_weights.copy()

    def export_model(self) -> dict[str, Any]:
        """
        Export model for persistence or deployment.

        Returns:
            Dictionary containing model state
        """
        return {
            "model_id": self.model_id,
            "version": self.model_version,
            "component_type": self.component_type,
            "is_trained": self._is_trained,
            "feature_weights": self._feature_weights,
            "baseline_metrics": self._baseline_metrics,
            "metadata": {
                "trained_date": (
                    self.metadata.trained_date.isoformat()
                    if self.metadata.trained_date
                    else None
                ),
                "training_samples": self.metadata.training_samples,
                "accuracy_score": self.metadata.accuracy_score,
                "feature_names": self.metadata.feature_names,
            },
        }

    def import_model(self, model_data: dict[str, Any]) -> bool:
        """
        Import model from exported state.

        Args:
            model_data: Dictionary containing model state

        Returns:
            True if import was successful
        """
        try:
            self._feature_weights = model_data.get("feature_weights", {})
            self._baseline_metrics = model_data.get("baseline_metrics", {})
            self._is_trained = model_data.get("is_trained", False)

            metadata = model_data.get("metadata", {})
            self.metadata.training_samples = metadata.get("training_samples", 0)
            self.metadata.accuracy_score = metadata.get("accuracy_score", 0.0)
            self.metadata.feature_names = metadata.get("feature_names", [])

            if metadata.get("trained_date"):
                self.metadata.trained_date = datetime.fromisoformat(
                    metadata["trained_date"]
                )

            logger.info("Model imported: %s", self.model_id)
            return True

        except (KeyError, ValueError) as e:
            logger.error("Failed to import model: %s", e)
            return False

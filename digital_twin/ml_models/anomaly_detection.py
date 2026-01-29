# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Anomaly detection models for AMPEL360 digital twin.

This module provides anomaly detection capabilities for identifying
unusual patterns in sensor data streams.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import logging
import statistics

logger = logging.getLogger(__name__)


@dataclass
class AnomalyResult:
    """Result of anomaly detection."""

    is_anomaly: bool
    anomaly_score: float
    affected_features: list[str] = field(default_factory=list)
    severity: str = "normal"  # normal, warning, critical
    timestamp: datetime = field(default_factory=datetime.utcnow)
    explanation: str = ""


@dataclass
class StatisticalBounds:
    """Statistical bounds for a feature."""

    mean: float = 0.0
    std: float = 1.0
    min_bound: float = -3.0
    max_bound: float = 3.0


class AnomalyDetector:
    """
    Anomaly detection model for sensor data streams.

    Uses statistical methods to identify unusual patterns in
    real-time sensor data.

    Attributes:
        sensitivity: Detection sensitivity (0-1, higher = more sensitive)
        window_size: Number of samples in sliding window
        model_id: Unique model identifier
    """

    SEVERITY_THRESHOLDS = {
        "critical": 3.0,
        "warning": 2.0,
        "normal": 0.0,
    }

    def __init__(
        self,
        sensitivity: float = 0.5,
        window_size: int = 100,
        model_id: Optional[str] = None,
    ) -> None:
        """
        Initialize the anomaly detector.

        Args:
            sensitivity: Detection sensitivity (0-1)
            window_size: Size of the sliding window for statistics
            model_id: Optional model identifier
        """
        self.sensitivity = max(0.0, min(1.0, sensitivity))
        self.window_size = window_size
        self.model_id = model_id or "ML-AD-SENS-001"

        self._feature_bounds: dict[str, StatisticalBounds] = {}
        self._history: dict[str, list[float]] = {}
        self._is_calibrated = False

        logger.info("Initialized anomaly detector: %s", self.model_id)

    def calibrate(self, calibration_data: list[dict[str, Any]]) -> dict[str, Any]:
        """
        Calibrate the detector with normal operation data.

        Args:
            calibration_data: List of sensor readings during normal operation

        Returns:
            Dictionary containing calibration metrics
        """
        if not calibration_data:
            logger.error("No calibration data provided")
            return {"success": False, "error": "No calibration data"}

        # Extract feature names
        features = list(calibration_data[0].keys())

        # Calculate bounds for each feature
        for feature in features:
            values = [
                d.get(feature, 0.0)
                for d in calibration_data
                if isinstance(d.get(feature), (int, float))
            ]

            if len(values) >= 2:
                mean = statistics.mean(values)
                std = statistics.stdev(values) if len(values) > 1 else 1.0

                # Adjust bounds based on sensitivity
                z_score = 3.0 - (self.sensitivity * 2.0)  # 1-3 based on sensitivity

                self._feature_bounds[feature] = StatisticalBounds(
                    mean=mean,
                    std=max(std, 1e-6),  # Prevent division by zero
                    min_bound=mean - z_score * std,
                    max_bound=mean + z_score * std,
                )

                # Initialize history
                self._history[feature] = values[-self.window_size :]

        self._is_calibrated = True

        logger.info(
            "Calibrated anomaly detector: %d features, %d samples",
            len(features),
            len(calibration_data),
        )

        return {
            "success": True,
            "features_calibrated": len(self._feature_bounds),
            "samples_used": len(calibration_data),
            "sensitivity": self.sensitivity,
        }

    def detect(self, sensor_data: dict[str, Any]) -> AnomalyResult:
        """
        Detect anomalies in sensor data.

        Args:
            sensor_data: Dictionary of current sensor readings

        Returns:
            AnomalyResult with detection details
        """
        if not self._is_calibrated:
            logger.warning("Detector not calibrated, using default bounds")

        anomaly_scores: list[tuple[str, float]] = []
        affected_features: list[str] = []

        for feature, value in sensor_data.items():
            if not isinstance(value, (int, float)):
                continue

            score = self._calculate_anomaly_score(feature, value)

            if score > 0:
                anomaly_scores.append((feature, score))
                if score > self.SEVERITY_THRESHOLDS["warning"]:
                    affected_features.append(feature)

            # Update history
            if feature in self._history:
                self._history[feature].append(value)
                if len(self._history[feature]) > self.window_size:
                    self._history[feature].pop(0)

        # Calculate overall anomaly score
        if anomaly_scores:
            max_score = max(s[1] for s in anomaly_scores)
            avg_score = sum(s[1] for s in anomaly_scores) / len(anomaly_scores)
            overall_score = 0.7 * max_score + 0.3 * avg_score
        else:
            overall_score = 0.0

        # Determine severity
        severity = "normal"
        for level, threshold in sorted(
            self.SEVERITY_THRESHOLDS.items(),
            key=lambda x: x[1],
            reverse=True,
        ):
            if overall_score >= threshold:
                severity = level
                break

        is_anomaly = overall_score >= self.SEVERITY_THRESHOLDS["warning"]

        # Generate explanation
        explanation = self._generate_explanation(anomaly_scores, severity)

        result = AnomalyResult(
            is_anomaly=is_anomaly,
            anomaly_score=overall_score,
            affected_features=affected_features,
            severity=severity,
            explanation=explanation,
        )

        if is_anomaly:
            logger.warning(
                "Anomaly detected: score=%.2f, severity=%s, features=%s",
                overall_score,
                severity,
                affected_features,
            )

        return result

    def detect_batch(
        self, sensor_data_list: list[dict[str, Any]]
    ) -> list[AnomalyResult]:
        """
        Detect anomalies in a batch of sensor readings.

        Args:
            sensor_data_list: List of sensor data dictionaries

        Returns:
            List of AnomalyResult objects
        """
        return [self.detect(data) for data in sensor_data_list]

    def _calculate_anomaly_score(self, feature: str, value: float) -> float:
        """Calculate anomaly score for a single feature value."""
        if feature not in self._feature_bounds:
            # Use default bounds if not calibrated
            return 0.0

        bounds = self._feature_bounds[feature]

        # Calculate z-score
        z_score = abs(value - bounds.mean) / bounds.std

        # Apply sensitivity adjustment
        adjusted_score = z_score * (0.5 + self.sensitivity)

        return max(0.0, adjusted_score)

    def _generate_explanation(
        self, scores: list[tuple[str, float]], severity: str
    ) -> str:
        """Generate human-readable explanation of anomaly."""
        if not scores or severity == "normal":
            return "All parameters within normal bounds"

        # Sort by score descending
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

        if severity == "critical":
            top_feature, top_score = sorted_scores[0]
            return (
                f"CRITICAL: {top_feature} significantly out of bounds "
                f"(score: {top_score:.2f})"
            )
        elif severity == "warning":
            features = [f[0] for f in sorted_scores if f[1] > 2.0]
            return f"Warning: Elevated readings in {', '.join(features[:3])}"
        else:
            return "Minor deviations detected - continue monitoring"

    def update_bounds(self, feature: str, new_data: list[float]) -> bool:
        """
        Update statistical bounds for a feature with new data.

        Args:
            feature: Feature name
            new_data: New data points to incorporate

        Returns:
            True if update was successful
        """
        if not new_data:
            return False

        if feature in self._feature_bounds:
            # Incremental update with exponential weighting
            old_bounds = self._feature_bounds[feature]
            alpha = 0.1  # Learning rate

            new_mean = statistics.mean(new_data)
            new_std = statistics.stdev(new_data) if len(new_data) > 1 else old_bounds.std

            updated_mean = (1 - alpha) * old_bounds.mean + alpha * new_mean
            updated_std = (1 - alpha) * old_bounds.std + alpha * new_std

            z_score = 3.0 - (self.sensitivity * 2.0)

            self._feature_bounds[feature] = StatisticalBounds(
                mean=updated_mean,
                std=max(updated_std, 1e-6),
                min_bound=updated_mean - z_score * updated_std,
                max_bound=updated_mean + z_score * updated_std,
            )

            logger.debug("Updated bounds for %s: mean=%.2f, std=%.2f", feature, updated_mean, updated_std)
            return True

        return False

    def get_bounds(self) -> dict[str, dict[str, float]]:
        """
        Get current statistical bounds for all features.

        Returns:
            Dictionary of feature bounds
        """
        return {
            feature: {
                "mean": bounds.mean,
                "std": bounds.std,
                "min_bound": bounds.min_bound,
                "max_bound": bounds.max_bound,
            }
            for feature, bounds in self._feature_bounds.items()
        }

    def export_model(self) -> dict[str, Any]:
        """Export model state for persistence."""
        return {
            "model_id": self.model_id,
            "sensitivity": self.sensitivity,
            "window_size": self.window_size,
            "is_calibrated": self._is_calibrated,
            "feature_bounds": {
                f: {
                    "mean": b.mean,
                    "std": b.std,
                    "min_bound": b.min_bound,
                    "max_bound": b.max_bound,
                }
                for f, b in self._feature_bounds.items()
            },
        }

    def import_model(self, model_data: dict[str, Any]) -> bool:
        """Import model state from exported data."""
        try:
            self.sensitivity = model_data.get("sensitivity", 0.5)
            self.window_size = model_data.get("window_size", 100)
            self._is_calibrated = model_data.get("is_calibrated", False)

            bounds_data = model_data.get("feature_bounds", {})
            self._feature_bounds = {
                f: StatisticalBounds(
                    mean=b["mean"],
                    std=b["std"],
                    min_bound=b["min_bound"],
                    max_bound=b["max_bound"],
                )
                for f, b in bounds_data.items()
            }

            logger.info("Imported anomaly detector: %s", self.model_id)
            return True

        except (KeyError, ValueError) as e:
            logger.error("Failed to import model: %s", e)
            return False

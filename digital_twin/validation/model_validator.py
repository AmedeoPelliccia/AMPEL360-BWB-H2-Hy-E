# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Model validator for AMPEL360 digital twin.

This module provides validation capabilities for verifying digital twin
model accuracy against physical measurements and reference data.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import logging
import statistics

logger = logging.getLogger(__name__)


@dataclass
class ValidationMetric:
    """Individual validation metric result."""

    name: str
    predicted: float
    measured: float
    deviation: float
    deviation_pct: float
    threshold: float
    passed: bool


@dataclass
class ValidationReport:
    """Complete validation report."""

    model_id: str
    accuracy: float
    passed: bool
    metrics: list[ValidationMetric] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    notes: str = ""
    validator_version: str = "1.0.0"


class ModelValidator:
    """
    Validates digital twin models against reference data.

    Compares model predictions to physical measurements to assess
    accuracy and identify deviations.

    Attributes:
        default_threshold: Default acceptable deviation threshold
    """

    def __init__(
        self,
        default_threshold: float = 0.05,
        accuracy_target: float = 95.0,
    ) -> None:
        """
        Initialize the model validator.

        Args:
            default_threshold: Default deviation threshold (fraction)
            accuracy_target: Target accuracy percentage
        """
        self.default_threshold = default_threshold
        self.accuracy_target = accuracy_target

        self._thresholds: dict[str, float] = {}
        self._validation_history: list[ValidationReport] = []

        logger.info(
            "Initialized ModelValidator: threshold=%.1f%%, target=%.1f%%",
            default_threshold * 100,
            accuracy_target,
        )

    def set_threshold(self, parameter: str, threshold: float) -> None:
        """
        Set custom threshold for a parameter.

        Args:
            parameter: Parameter name
            threshold: Acceptable deviation threshold (fraction)
        """
        self._thresholds[parameter] = threshold

    def validate(
        self,
        model: Any,
        reference_data: dict[str, float],
        parameters: Optional[list[str]] = None,
    ) -> ValidationReport:
        """
        Validate a model against reference data.

        Args:
            model: Digital twin model instance
            reference_data: Dictionary of measured reference values
            parameters: Specific parameters to validate (None for all)

        Returns:
            ValidationReport with results
        """
        model_id = getattr(model, "model_id", "UNKNOWN")
        metrics: list[ValidationMetric] = []

        # Get model predictions
        if hasattr(model, "get_state"):
            state = model.get_state()
            predictions = state.parameters if hasattr(state, "parameters") else {}
        elif hasattr(model, "to_dict"):
            predictions = model.to_dict().get("state", {}).get("parameters", {})
        else:
            predictions = {}

        # Validate each parameter
        params_to_check = parameters or list(reference_data.keys())

        for param in params_to_check:
            if param not in reference_data:
                continue

            measured = reference_data[param]
            predicted = predictions.get(param, 0.0)

            if isinstance(measured, (int, float)) and isinstance(predicted, (int, float)):
                metric = self._validate_parameter(param, predicted, measured)
                metrics.append(metric)

        # Calculate overall accuracy
        if metrics:
            passed_count = sum(1 for m in metrics if m.passed)
            accuracy = (passed_count / len(metrics)) * 100
        else:
            accuracy = 100.0

        passed = accuracy >= self.accuracy_target

        report = ValidationReport(
            model_id=model_id,
            accuracy=accuracy,
            passed=passed,
            metrics=metrics,
            notes=f"Validated {len(metrics)} parameters against reference data",
        )

        self._validation_history.append(report)

        logger.info(
            "Validation complete for %s: accuracy=%.1f%%, passed=%s",
            model_id,
            accuracy,
            passed,
        )

        return report

    def validate_batch(
        self,
        models: list[Any],
        reference_data_list: list[dict[str, float]],
    ) -> list[ValidationReport]:
        """
        Validate multiple models.

        Args:
            models: List of model instances
            reference_data_list: Corresponding reference data

        Returns:
            List of validation reports
        """
        if len(models) != len(reference_data_list):
            raise ValueError("models and reference_data_list must have same length")

        return [
            self.validate(model, ref_data)
            for model, ref_data in zip(models, reference_data_list)
        ]

    def compare_predictions(
        self,
        predicted: dict[str, float],
        measured: dict[str, float],
    ) -> dict[str, ValidationMetric]:
        """
        Compare predictions directly against measurements.

        Args:
            predicted: Predicted values
            measured: Measured values

        Returns:
            Dictionary of validation metrics
        """
        results = {}

        for param in measured:
            if param in predicted:
                metric = self._validate_parameter(
                    param, predicted[param], measured[param]
                )
                results[param] = metric

        return results

    def get_history(self, limit: int = 10) -> list[ValidationReport]:
        """Get recent validation history."""
        return self._validation_history[-limit:]

    def get_statistics(self) -> dict[str, Any]:
        """
        Get validation statistics.

        Returns:
            Dictionary of statistics
        """
        if not self._validation_history:
            return {"total_validations": 0}

        accuracies = [r.accuracy for r in self._validation_history]

        return {
            "total_validations": len(self._validation_history),
            "average_accuracy": statistics.mean(accuracies),
            "min_accuracy": min(accuracies),
            "max_accuracy": max(accuracies),
            "pass_rate": sum(1 for r in self._validation_history if r.passed) / len(self._validation_history),
        }

    def _validate_parameter(
        self, name: str, predicted: float, measured: float
    ) -> ValidationMetric:
        """Validate a single parameter."""
        # Calculate deviation
        if abs(measured) > 1e-10:
            deviation = abs(predicted - measured)
            deviation_pct = deviation / abs(measured)
        else:
            deviation = abs(predicted - measured)
            deviation_pct = deviation

        # Get threshold
        threshold = self._thresholds.get(name, self.default_threshold)

        # Determine pass/fail
        passed = deviation_pct <= threshold

        return ValidationMetric(
            name=name,
            predicted=predicted,
            measured=measured,
            deviation=deviation,
            deviation_pct=deviation_pct * 100,
            threshold=threshold * 100,
            passed=passed,
        )

    def generate_report(
        self, report: ValidationReport, format: str = "text"
    ) -> str:
        """
        Generate a formatted validation report.

        Args:
            report: ValidationReport to format
            format: Output format (text, markdown, json)

        Returns:
            Formatted report string
        """
        if format == "markdown":
            return self._format_markdown(report)
        elif format == "json":
            import json
            return json.dumps(self._report_to_dict(report), indent=2)
        return self._format_text(report)

    def _format_text(self, report: ValidationReport) -> str:
        """Format report as plain text."""
        lines = [
            f"=== Validation Report ===",
            f"Model: {report.model_id}",
            f"Timestamp: {report.timestamp.isoformat()}",
            f"Overall Accuracy: {report.accuracy:.1f}%",
            f"Status: {'PASSED' if report.passed else 'FAILED'}",
            "",
            "Parameters:",
        ]

        for m in report.metrics:
            status = "✓" if m.passed else "✗"
            lines.append(
                f"  {status} {m.name}: predicted={m.predicted:.3f}, "
                f"measured={m.measured:.3f}, deviation={m.deviation_pct:.1f}%"
            )

        return "\n".join(lines)

    def _format_markdown(self, report: ValidationReport) -> str:
        """Format report as markdown."""
        lines = [
            f"# Validation Report: {report.model_id}",
            "",
            f"**Timestamp:** {report.timestamp.isoformat()}",
            f"**Overall Accuracy:** {report.accuracy:.1f}%",
            f"**Status:** {'✅ PASSED' if report.passed else '❌ FAILED'}",
            "",
            "## Parameters",
            "",
            "| Parameter | Predicted | Measured | Deviation | Status |",
            "|-----------|-----------|----------|-----------|--------|",
        ]

        for m in report.metrics:
            status = "✅" if m.passed else "❌"
            lines.append(
                f"| {m.name} | {m.predicted:.3f} | {m.measured:.3f} | "
                f"{m.deviation_pct:.1f}% | {status} |"
            )

        return "\n".join(lines)

    def _report_to_dict(self, report: ValidationReport) -> dict[str, Any]:
        """Convert report to dictionary."""
        return {
            "model_id": report.model_id,
            "accuracy": report.accuracy,
            "passed": report.passed,
            "timestamp": report.timestamp.isoformat(),
            "notes": report.notes,
            "metrics": [
                {
                    "name": m.name,
                    "predicted": m.predicted,
                    "measured": m.measured,
                    "deviation": m.deviation,
                    "deviation_pct": m.deviation_pct,
                    "threshold": m.threshold,
                    "passed": m.passed,
                }
                for m in report.metrics
            ],
        }

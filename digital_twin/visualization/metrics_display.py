# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Metrics display component for AMPEL360 digital twin visualization.

This module provides metrics and KPI display functionality for
monitoring aircraft parameters.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import html
import logging

logger = logging.getLogger(__name__)


@dataclass
class Metric:
    """Represents a single metric."""

    name: str
    unit: str
    value: float = 0.0
    min_value: float = 0.0
    max_value: float = 100.0
    warning_threshold: Optional[float] = None
    critical_threshold: Optional[float] = None
    format_string: str = "{:.1f}"
    history: list[tuple[datetime, float]] = field(default_factory=list)


class MetricsDisplay:
    """
    Metrics display component for KPIs and performance indicators.

    Displays real-time metrics with configurable thresholds,
    units, and visualization styles.

    Attributes:
        title: Display title
        component_type: Type identifier for dashboard integration
    """

    component_type = "metrics"

    def __init__(
        self,
        title: str = "Metrics",
        layout: str = "grid",
        max_history: int = 100,
    ) -> None:
        """
        Initialize the metrics display.

        Args:
            title: Display title
            layout: Layout style (grid, list, compact)
            max_history: Maximum history points per metric
        """
        self.title = title
        self.layout = layout
        self.max_history = max_history

        self._metrics: dict[str, Metric] = {}
        self._groups: dict[str, list[str]] = {"default": []}

        self.config: dict[str, Any] = {
            "title": title,
            "layout": layout,
        }

        logger.info("Initialized MetricsDisplay: %s", title)

    def add_metric(
        self,
        name: str,
        unit: str,
        bounds: Optional[dict[str, float]] = None,
        group: str = "default",
        format_string: str = "{:.1f}",
    ) -> bool:
        """
        Add a metric to the display.

        Args:
            name: Metric name
            unit: Unit of measurement
            bounds: Dictionary with min, max, warning, critical
            group: Group name for organization
            format_string: Format string for display

        Returns:
            True if metric was added
        """
        if name in self._metrics:
            logger.warning("Metric already exists: %s", name)
            return False

        bounds = bounds or {}

        metric = Metric(
            name=name,
            unit=unit,
            min_value=bounds.get("min", 0.0),
            max_value=bounds.get("max", 100.0),
            warning_threshold=bounds.get("warning"),
            critical_threshold=bounds.get("critical"),
            format_string=format_string,
        )

        self._metrics[name] = metric

        # Add to group
        if group not in self._groups:
            self._groups[group] = []
        self._groups[group].append(name)

        logger.debug("Added metric: %s (%s)", name, unit)
        return True

    def remove_metric(self, name: str) -> bool:
        """Remove a metric from the display."""
        if name not in self._metrics:
            return False

        del self._metrics[name]

        # Remove from groups
        for group_metrics in self._groups.values():
            if name in group_metrics:
                group_metrics.remove(name)

        return True

    def update(self, data: dict[str, Any]) -> None:
        """
        Update metrics with new values.

        Args:
            data: Dictionary mapping metric names to values
        """
        timestamp = datetime.utcnow()

        for name, value in data.items():
            if name in self._metrics:
                metric = self._metrics[name]
                metric.value = float(value)

                # Add to history
                metric.history.append((timestamp, metric.value))
                if len(metric.history) > self.max_history:
                    metric.history.pop(0)

    def get_metric(self, name: str) -> Optional[Metric]:
        """Get a metric by name."""
        return self._metrics.get(name)

    def get_value(self, name: str) -> Optional[float]:
        """Get the current value of a metric."""
        metric = self._metrics.get(name)
        return metric.value if metric else None

    def get_all_values(self) -> dict[str, float]:
        """Get all current metric values."""
        return {name: m.value for name, m in self._metrics.items()}

    def get_status(self, name: str) -> str:
        """
        Get the status of a metric based on thresholds.

        Args:
            name: Metric name

        Returns:
            Status string (normal, warning, critical)
        """
        metric = self._metrics.get(name)
        if not metric:
            return "unknown"

        if metric.critical_threshold and metric.value >= metric.critical_threshold:
            return "critical"
        if metric.warning_threshold and metric.value >= metric.warning_threshold:
            return "warning"
        return "normal"

    def get_history(
        self, name: str, limit: int = 50
    ) -> list[tuple[datetime, float]]:
        """
        Get historical values for a metric.

        Args:
            name: Metric name
            limit: Maximum points to return

        Returns:
            List of (timestamp, value) tuples
        """
        metric = self._metrics.get(name)
        if not metric:
            return []
        return metric.history[-limit:]

    def create_group(self, group_name: str, metric_names: list[str]) -> bool:
        """
        Create a metric group.

        Args:
            group_name: Name for the group
            metric_names: List of metric names to include

        Returns:
            True if group was created
        """
        # Validate all metrics exist
        for name in metric_names:
            if name not in self._metrics:
                logger.warning("Unknown metric for group: %s", name)
                return False

        self._groups[group_name] = metric_names
        return True

    def render(self, format: str = "json") -> str:
        """
        Render the metrics display.

        Args:
            format: Output format (json, html, text)

        Returns:
            Rendered output
        """
        if format == "html":
            return self._render_html()
        elif format == "text":
            return self._render_text()
        return self._render_json()

    def _render_json(self) -> str:
        """Render as JSON."""
        import json

        return json.dumps(
            {
                "title": self.title,
                "layout": self.layout,
                "groups": self._groups,
                "metrics": {
                    name: {
                        "name": m.name,
                        "value": m.value,
                        "unit": m.unit,
                        "min": m.min_value,
                        "max": m.max_value,
                        "status": self.get_status(name),
                        "formatted": m.format_string.format(m.value),
                    }
                    for name, m in self._metrics.items()
                },
            },
            indent=2,
        )

    def _render_html(self) -> str:
        """Render as HTML."""
        # Define safe color values to prevent XSS via status_color
        safe_colors = {"normal": "green", "warning": "orange", "critical": "red"}
        
        metrics_html = ""
        for name, metric in self._metrics.items():
            status = self.get_status(name)
            status_color = safe_colors.get(status, "gray")
            formatted_value = html.escape(metric.format_string.format(metric.value))

            metrics_html += f"""
            <div class="metric" data-status="{html.escape(status)}">
                <span class="metric-name">{html.escape(metric.name)}</span>
                <span class="metric-value" style="color: {status_color};">{formatted_value}</span>
                <span class="metric-unit">{html.escape(metric.unit)}</span>
            </div>
            """

        escaped_title = html.escape(self.title)
        escaped_layout = html.escape(self.layout)
        return f"""
        <div class="metrics-display">
            <h3>{escaped_title}</h3>
            <div class="metrics-{escaped_layout}">
                {metrics_html}
            </div>
        </div>
        """

    def _render_text(self) -> str:
        """Render as plain text."""
        lines = [f"=== {self.title} ==="]

        for name, metric in self._metrics.items():
            status = self.get_status(name)
            formatted = metric.format_string.format(metric.value)
            lines.append(f"{metric.name}: {formatted} {metric.unit} [{status}]")

        return "\n".join(lines)

    def export_config(self) -> dict[str, Any]:
        """Export display configuration."""
        return {
            "title": self.title,
            "layout": self.layout,
            "max_history": self.max_history,
            "metrics": {
                name: {
                    "unit": m.unit,
                    "min": m.min_value,
                    "max": m.max_value,
                    "warning": m.warning_threshold,
                    "critical": m.critical_threshold,
                    "format": m.format_string,
                }
                for name, m in self._metrics.items()
            },
            "groups": self._groups,
        }

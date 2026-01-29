# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
Dashboard component for AMPEL360 digital twin visualization.

This module provides dashboard functionality for real-time monitoring
and data visualization.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import json
import logging

logger = logging.getLogger(__name__)


@dataclass
class DashboardPanel:
    """Represents a panel in the dashboard."""

    panel_id: str
    title: str
    panel_type: str  # metrics, chart, 3d, map, table
    position: dict[str, int] = field(default_factory=lambda: {"x": 0, "y": 0})
    size: dict[str, int] = field(default_factory=lambda: {"width": 1, "height": 1})
    config: dict[str, Any] = field(default_factory=dict)
    data: Any = None


class Dashboard:
    """
    Dashboard for digital twin visualization.

    Provides a configurable dashboard with multiple panels for
    displaying real-time aircraft data.

    Attributes:
        title: Dashboard title
        refresh_interval_ms: Data refresh interval
    """

    def __init__(
        self,
        title: str = "Digital Twin Dashboard",
        refresh_interval_ms: int = 1000,
        theme: str = "dark",
    ) -> None:
        """
        Initialize the dashboard.

        Args:
            title: Dashboard title
            refresh_interval_ms: Refresh interval in milliseconds
            theme: Visual theme (dark, light)
        """
        self.title = title
        self.refresh_interval_ms = refresh_interval_ms
        self.theme = theme

        self._panels: dict[str, DashboardPanel] = {}
        self._data: dict[str, Any] = {}
        self._last_update: Optional[datetime] = None
        self._layout: list[list[str]] = []

        logger.info("Initialized dashboard: %s", title)

    def add_panel(
        self,
        panel_id: str,
        component: Any,
        title: Optional[str] = None,
        position: Optional[dict[str, int]] = None,
        size: Optional[dict[str, int]] = None,
    ) -> bool:
        """
        Add a panel to the dashboard.

        Args:
            panel_id: Unique identifier for the panel
            component: Visualization component to add
            title: Panel title
            position: Grid position {x, y}
            size: Panel size {width, height}

        Returns:
            True if panel was added successfully
        """
        if panel_id in self._panels:
            logger.warning("Panel already exists: %s", panel_id)
            return False

        # Determine panel type from component
        panel_type = getattr(component, "component_type", "generic")

        panel = DashboardPanel(
            panel_id=panel_id,
            title=title or panel_id,
            panel_type=panel_type,
            position=position or {"x": 0, "y": len(self._panels)},
            size=size or {"width": 1, "height": 1},
            config=getattr(component, "config", {}),
            data=component,
        )

        self._panels[panel_id] = panel
        logger.info("Added panel: %s (%s)", panel_id, panel_type)
        return True

    def remove_panel(self, panel_id: str) -> bool:
        """
        Remove a panel from the dashboard.

        Args:
            panel_id: Panel identifier

        Returns:
            True if panel was removed
        """
        if panel_id not in self._panels:
            return False

        del self._panels[panel_id]
        logger.info("Removed panel: %s", panel_id)
        return True

    def update(self, data: dict[str, Any]) -> None:
        """
        Update dashboard with new data.

        Args:
            data: Dictionary of data updates
        """
        self._data.update(data)
        self._last_update = datetime.utcnow()

        # Update each panel with relevant data
        for panel_id, panel in self._panels.items():
            if hasattr(panel.data, "update"):
                panel_data = {k: v for k, v in data.items() if self._data_matches_panel(k, panel)}
                if panel_data:
                    panel.data.update(panel_data)

        logger.debug("Dashboard updated with %d data points", len(data))

    def get_panel(self, panel_id: str) -> Optional[DashboardPanel]:
        """Get a panel by ID."""
        return self._panels.get(panel_id)

    def get_all_panels(self) -> list[DashboardPanel]:
        """Get all dashboard panels."""
        return list(self._panels.values())

    def set_layout(self, layout: list[list[str]]) -> bool:
        """
        Set the dashboard grid layout.

        Args:
            layout: 2D grid of panel IDs

        Returns:
            True if layout was set successfully
        """
        # Validate all panel IDs exist
        for row in layout:
            for panel_id in row:
                if panel_id and panel_id not in self._panels:
                    logger.warning("Unknown panel in layout: %s", panel_id)
                    return False

        self._layout = layout
        return True

    def render(self, format: str = "json") -> str:
        """
        Render the dashboard.

        Args:
            format: Output format (json, html)

        Returns:
            Rendered dashboard content
        """
        if format == "json":
            return self._render_json()
        elif format == "html":
            return self._render_html()
        else:
            return self._render_json()

    def _render_json(self) -> str:
        """Render dashboard as JSON."""
        return json.dumps(
            {
                "title": self.title,
                "theme": self.theme,
                "refresh_interval_ms": self.refresh_interval_ms,
                "last_update": self._last_update.isoformat() if self._last_update else None,
                "panels": [
                    {
                        "id": p.panel_id,
                        "title": p.title,
                        "type": p.panel_type,
                        "position": p.position,
                        "size": p.size,
                        "config": p.config,
                    }
                    for p in self._panels.values()
                ],
                "data": self._data,
                "layout": self._layout,
            },
            indent=2,
        )

    def _render_html(self) -> str:
        """Render dashboard as HTML."""
        panels_html = ""
        for panel in self._panels.values():
            panels_html += f"""
            <div class="panel" id="{panel.panel_id}">
                <h3>{panel.title}</h3>
                <div class="panel-content" data-type="{panel.panel_type}">
                    <!-- Panel content rendered by JavaScript -->
                </div>
            </div>
            """

        return f"""
<!DOCTYPE html>
<html>
<head>
    <title>{self.title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: {"#1a1a2e" if self.theme == "dark" else "#fff"}; color: {"#fff" if self.theme == "dark" else "#000"}; }}
        .dashboard {{ display: grid; gap: 10px; padding: 20px; }}
        .panel {{ background: {"#16213e" if self.theme == "dark" else "#f5f5f5"}; border-radius: 8px; padding: 15px; }}
        .panel h3 {{ margin-top: 0; }}
    </style>
</head>
<body>
    <h1>{self.title}</h1>
    <div class="dashboard">
        {panels_html}
    </div>
    <script>
        // Dashboard data
        const dashboardData = {json.dumps(self._data)};
        const refreshInterval = {self.refresh_interval_ms};
    </script>
</body>
</html>
        """.strip()

    def _data_matches_panel(self, data_key: str, panel: DashboardPanel) -> bool:
        """Check if data key is relevant to a panel."""
        # Simple matching - can be extended with explicit mappings
        panel_type = panel.panel_type
        if panel_type == "metrics":
            return True  # Metrics panels receive all data
        elif panel_type == "3d":
            return data_key in ("position", "attitude", "geometry")
        elif panel_type == "map":
            return data_key in ("position", "route", "waypoints")
        return True

    def export_config(self) -> dict[str, Any]:
        """Export dashboard configuration."""
        return {
            "title": self.title,
            "theme": self.theme,
            "refresh_interval_ms": self.refresh_interval_ms,
            "panels": [
                {
                    "id": p.panel_id,
                    "title": p.title,
                    "type": p.panel_type,
                    "position": p.position,
                    "size": p.size,
                    "config": p.config,
                }
                for p in self._panels.values()
            ],
            "layout": self._layout,
        }

    def import_config(self, config: dict[str, Any]) -> bool:
        """Import dashboard configuration."""
        try:
            self.title = config.get("title", self.title)
            self.theme = config.get("theme", self.theme)
            self.refresh_interval_ms = config.get("refresh_interval_ms", self.refresh_interval_ms)
            self._layout = config.get("layout", [])
            return True
        except (KeyError, TypeError) as e:
            logger.error("Failed to import config: %s", e)
            return False

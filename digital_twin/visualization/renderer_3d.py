# SPDX-License-Identifier: MIT
# Copyright (c) 2026 AMPEL360 Project
"""
3D renderer for AMPEL360 digital twin visualization.

This module provides 3D rendering capabilities for aircraft
model visualization.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class RenderMode(Enum):
    """Rendering mode options."""

    SOLID = "solid"
    WIREFRAME = "wireframe"
    SHADED = "shaded"
    TEXTURED = "textured"
    XRAY = "xray"


@dataclass
class CameraPosition:
    """Camera position and orientation."""

    x: float = 0.0
    y: float = 0.0
    z: float = 100.0
    look_at_x: float = 0.0
    look_at_y: float = 0.0
    look_at_z: float = 0.0
    fov: float = 45.0


@dataclass
class LightSource:
    """Light source configuration."""

    light_type: str = "directional"  # directional, point, ambient
    position: tuple[float, float, float] = (100.0, 100.0, 100.0)
    color: str = "#ffffff"
    intensity: float = 1.0


class Renderer3D:
    """
    3D renderer for aircraft visualization.

    Provides 3D model rendering with configurable views,
    highlighting, and annotations.

    Attributes:
        model_path: Path to the 3D model file
        render_mode: Current rendering mode
        component_type: Type identifier for dashboard integration
    """

    component_type = "3d"

    SUPPORTED_FORMATS = [".gltf", ".glb", ".obj", ".stl", ".step"]

    def __init__(
        self,
        model_path: Optional[str] = None,
        render_mode: RenderMode = RenderMode.SHADED,
    ) -> None:
        """
        Initialize the 3D renderer.

        Args:
            model_path: Path to 3D model file
            render_mode: Initial rendering mode
        """
        self.model_path = model_path
        self.render_mode = render_mode

        self._camera = CameraPosition()
        self._lights: list[LightSource] = [LightSource()]
        self._highlighted_components: list[str] = []
        self._annotations: dict[str, dict[str, Any]] = {}
        self._model_data: Optional[dict[str, Any]] = None
        self._transform: dict[str, float] = {
            "rotation_x": 0.0,
            "rotation_y": 0.0,
            "rotation_z": 0.0,
            "scale": 1.0,
        }

        self.config: dict[str, Any] = {
            "render_mode": render_mode.value,
            "model_path": model_path,
        }

        if model_path:
            self.load_model(model_path)

        logger.info("Initialized 3D renderer")

    def load_model(self, model_path: str) -> bool:
        """
        Load a 3D model file.

        Args:
            model_path: Path to the model file

        Returns:
            True if model was loaded successfully
        """
        # Check file extension
        ext = "." + model_path.split(".")[-1].lower() if "." in model_path else ""
        if ext not in self.SUPPORTED_FORMATS:
            logger.warning("Unsupported format: %s", ext)
            return False

        # In production, this would parse the actual 3D file
        self._model_data = {
            "path": model_path,
            "format": ext,
            "components": [],
            "vertices": 0,
            "faces": 0,
        }

        self.model_path = model_path
        logger.info("Loaded model: %s", model_path)
        return True

    def set_camera(
        self,
        position: Optional[tuple[float, float, float]] = None,
        look_at: Optional[tuple[float, float, float]] = None,
        fov: Optional[float] = None,
    ) -> None:
        """
        Set camera position and orientation.

        Args:
            position: Camera position (x, y, z)
            look_at: Point to look at (x, y, z)
            fov: Field of view in degrees
        """
        if position:
            self._camera.x, self._camera.y, self._camera.z = position
        if look_at:
            self._camera.look_at_x, self._camera.look_at_y, self._camera.look_at_z = look_at
        if fov is not None:
            self._camera.fov = fov

    def set_preset_view(self, view: str) -> None:
        """
        Set a preset camera view.

        Args:
            view: Preset view name (front, back, left, right, top, bottom, isometric)
        """
        presets = {
            "front": ((0, 0, 100), (0, 0, 0)),
            "back": ((0, 0, -100), (0, 0, 0)),
            "left": ((-100, 0, 0), (0, 0, 0)),
            "right": ((100, 0, 0), (0, 0, 0)),
            "top": ((0, 100, 0), (0, 0, 0)),
            "bottom": ((0, -100, 0), (0, 0, 0)),
            "isometric": ((70, 70, 70), (0, 0, 0)),
        }

        if view in presets:
            position, look_at = presets[view]
            self.set_camera(position=position, look_at=look_at)
            logger.debug("Set preset view: %s", view)

    def set_render_mode(self, mode: RenderMode) -> None:
        """Set the rendering mode."""
        self.render_mode = mode
        self.config["render_mode"] = mode.value
        logger.debug("Set render mode: %s", mode.value)

    def highlight_component(self, component_id: str, color: str = "#ff0000") -> None:
        """
        Highlight a specific component.

        Args:
            component_id: ID of component to highlight
            color: Highlight color (hex)
        """
        if component_id not in self._highlighted_components:
            self._highlighted_components.append(component_id)
        logger.debug("Highlighted component: %s", component_id)

    def clear_highlights(self) -> None:
        """Clear all component highlights."""
        self._highlighted_components.clear()

    def add_annotation(
        self,
        annotation_id: str,
        position: tuple[float, float, float],
        text: str,
        style: Optional[dict[str, Any]] = None,
    ) -> None:
        """
        Add an annotation to the 3D view.

        Args:
            annotation_id: Unique annotation identifier
            position: 3D position (x, y, z)
            text: Annotation text
            style: Optional styling options
        """
        self._annotations[annotation_id] = {
            "position": position,
            "text": text,
            "style": style or {},
        }

    def remove_annotation(self, annotation_id: str) -> bool:
        """Remove an annotation."""
        if annotation_id in self._annotations:
            del self._annotations[annotation_id]
            return True
        return False

    def update(self, data: dict[str, Any]) -> None:
        """
        Update renderer with new data.

        Args:
            data: Update data (position, attitude, highlights)
        """
        if "attitude" in data:
            attitude = data["attitude"]
            self._transform["rotation_x"] = attitude.get("pitch", 0.0)
            self._transform["rotation_y"] = attitude.get("yaw", 0.0)
            self._transform["rotation_z"] = attitude.get("roll", 0.0)

        if "highlight_components" in data:
            self._highlighted_components = data["highlight_components"]

    def render(self, width: int = 800, height: int = 600) -> dict[str, Any]:
        """
        Render the 3D scene.

        Args:
            width: Output width in pixels
            height: Output height in pixels

        Returns:
            Render output data
        """
        return {
            "type": "3d_render",
            "width": width,
            "height": height,
            "model": self.model_path,
            "render_mode": self.render_mode.value,
            "camera": {
                "position": (self._camera.x, self._camera.y, self._camera.z),
                "look_at": (self._camera.look_at_x, self._camera.look_at_y, self._camera.look_at_z),
                "fov": self._camera.fov,
            },
            "transform": self._transform,
            "highlights": self._highlighted_components,
            "annotations": self._annotations,
            "lights": [
                {
                    "type": l.light_type,
                    "position": l.position,
                    "color": l.color,
                    "intensity": l.intensity,
                }
                for l in self._lights
            ],
        }

    def export_image(
        self, output_path: str, format: str = "png", width: int = 1920, height: int = 1080
    ) -> bool:
        """
        Export rendered image to file.

        Args:
            output_path: Output file path
            format: Image format (png, jpg)
            width: Image width
            height: Image height

        Returns:
            True if export was successful
        """
        # In production, this would render and save an actual image
        logger.info("Exported image: %s (%dx%d)", output_path, width, height)
        return True

    def get_component_at(self, x: int, y: int) -> Optional[str]:
        """
        Get component ID at screen coordinates.

        Args:
            x: X coordinate
            y: Y coordinate

        Returns:
            Component ID or None
        """
        # In production, this would do ray casting
        return None

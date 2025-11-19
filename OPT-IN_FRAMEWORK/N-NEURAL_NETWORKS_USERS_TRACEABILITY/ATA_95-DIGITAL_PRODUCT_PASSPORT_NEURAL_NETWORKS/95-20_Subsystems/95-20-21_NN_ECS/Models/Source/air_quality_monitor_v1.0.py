#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Air Quality Monitor v1.0
Model ID: 95-20-21-A-102

Reference:
  - Component spec: 95-20-21-003_Air_Quality_Monitor.md
  - Model card: ASSETS/Model_Cards/95-20-21-A-102_Air_Quality_Monitor_v1.0.yaml
"""

# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F

try:
    import onnx  # noqa: F401
    import onnxruntime  # noqa: F401
except ImportError:
    # ONNX is optional at import time; only needed for export/inspection
    onnx = None  # type: ignore


MODEL_ID = "95-20-21-A-102"
MODEL_VERSION = "1.0"

# These defaults can be overridden when building the model
DEFAULT_FEATURES = 16           # CO₂, humidity, VOC, PM2.5/PM10, temp, etc.
DEFAULT_WINDOW = 60             # timesteps (e.g. 60 samples window)
DEFAULT_NUM_CLASSES = 5         # AQI classes (1–5)


@dataclass
class AirQualityModelConfig:
    """Configuration for the Air Quality Monitor NN."""
    num_features: int = DEFAULT_FEATURES
    window_length: int = DEFAULT_WINDOW
    num_classes: int = DEFAULT_NUM_CLASSES

    # CNN
    conv_channels: Tuple[int, int, int] = (64, 128, 256)
    kernel_size: int = 3
    cnn_pool: int = 2

    # Transformer
    d_model: int = 256
    n_heads: int = 4
    num_layers: int = 2
    dim_feedforward: int = 512
    dropout: float = 0.1


class AirQualityMonitor(nn.Module):
    """
    CNN + Transformer model for cabin air quality monitoring.

    Input shape (batch_first):
        (batch_size, seq_len, num_features)

    Outputs:
        - class_logits: (batch_size, num_classes)
        - optional auxiliary regression heads could be added later (e.g. CO₂ estimate).
    """

    def __init__(self, cfg: AirQualityModelConfig):
        super().__init__()
        self.cfg = cfg

        # 1D CNN encoder (temporal conv over sensor time-series)
        c1, c2, c3 = cfg.conv_channels

        # Input to Conv1d: (batch, channels, seq_len)
        # We treat "features" as channels; seq_len is time.
        self.conv1 = nn.Conv1d(cfg.num_features, c1, kernel_size=cfg.kernel_size, padding="same")
        self.conv2 = nn.Conv1d(c1, c2, kernel_size=cfg.kernel_size, padding="same")
        self.conv3 = nn.Conv1d(c2, c3, kernel_size=cfg.kernel_size, padding="same")

        self.bn1 = nn.BatchNorm1d(c1)
        self.bn2 = nn.BatchNorm1d(c2)
        self.bn3 = nn.BatchNorm1d(c3)

        self.pool = nn.MaxPool1d(kernel_size=cfg.cnn_pool)

        # After pooling, effective sequence length is reduced
        # (rough estimate; exact length not critical for architecture)
        # We'll use the conv output channels as d_model for the transformer.
        self.project_to_d_model = nn.Linear(c3, cfg.d_model)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=cfg.d_model,
            nhead=cfg.n_heads,
            dim_feedforward=cfg.dim_feedforward,
            dropout=cfg.dropout,
            batch_first=True,  # shape: (batch, seq, d_model)
        )
        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=cfg.num_layers,
        )

        # Classification head
        self.fc1 = nn.Linear(cfg.d_model, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc_out = nn.Linear(64, cfg.num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass.

        Parameters
        ----------
        x : torch.Tensor
            Shape (batch, seq_len, num_features)

        Returns
        -------
        torch.Tensor
            Class logits of shape (batch, num_classes).
        """
        # (B, T, F) -> (B, F, T)
        x = x.transpose(1, 2)

        # CNN feature extraction
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        x = self.pool(F.relu(self.bn3(self.conv3(x))))
        # x: (B, C3, T')

        # (B, C3, T') -> (B, T', C3)
        x = x.transpose(1, 2)

        # Project channels to d_model for Transformer
        x = self.project_to_d_model(x)  # (B, T', d_model)

        # Transformer encoder
        x = self.transformer(x)  # (B, T', d_model)

        # Global average pooling over time dimension
        x = x.mean(dim=1)  # (B, d_model)

        # Classification head
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        logits = self.fc_out(x)  # (B, num_classes)

        return logits


def build_model(cfg: Optional[AirQualityModelConfig] = None) -> AirQualityMonitor:
    """
    Build Air Quality Monitor model with default configuration.

    Returns
    -------
    AirQualityMonitor
        Instantiated model (untrained).
    """
    if cfg is None:
        cfg = AirQualityModelConfig()
    return AirQualityMonitor(cfg)


def export_to_onnx(
    model: nn.Module,
    output_path: Path | str,
    cfg: Optional[AirQualityModelConfig] = None,
    opset: int = 17,
    additional_metadata: Optional[Dict[str, Any]] = None,
) -> Path:
    """
    Export the Air Quality Monitor model to ONNX format.

    Parameters
    ----------
    model:
        PyTorch model instance.
    output_path:
        Path to output .onnx file.
    cfg:
        AirQualityModelConfig used to define input shapes.
    opset:
        ONNX opset version.
    additional_metadata:
        Optional dict of key/value metadata to attach post-export.

    Notes
    -----
    - Exports only the classification head (5-class AQI).
    - Uses a dummy input of shape (1, window_length, num_features).
    """
    if cfg is None:
        cfg = AirQualityModelConfig()

    model.eval()

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    dummy_input = torch.randn(1, cfg.window_length, cfg.num_features, dtype=torch.float32)

    torch.onnx.export(
        model,
        dummy_input,
        output_path,
        input_names=["sensor_window"],
        output_names=["aqi_logits"],
        opset_version=opset,
        dynamic_axes={
            "sensor_window": {0: "batch_size", 1: "seq_len"},
            "aqi_logits": {0: "batch_size"},
        },
    )

    # Attach metadata with onnx if library is available
    if additional_metadata is not None and onnx is not None:
        model_proto = onnx.load(str(output_path))
        for k, v in additional_metadata.items():
            meta = model_proto.metadata_props.add()
            meta.key = str(k)
            meta.value = str(v)
        onnx.save(model_proto, str(output_path))

    return output_path


def _print_banner() -> None:
    """Utility CLI banner."""
    print("Air Quality Monitor")
    print(f"Model ID : {MODEL_ID}")
    print(f"Version  : {MODEL_VERSION}")
    print("Status   : PLACEHOLDER IMPLEMENTATION – training & data loaders TBD\n")
    print("This module provides:")
    print("  - AirQualityMonitor(nn.Module): CNN + Transformer model")
    print("  - build_model(): helper to construct model")
    print("  - export_to_onnx(): helper to export model to ONNX\n")
    print("TODO (project-specific):")
    print("  - Connect to real dataset 95-20-21 air quality logs")
    print("  - Implement full training & evaluation pipeline")
    print("  - Integrate with DPP / ONNX inspection & deployment scripts")


if __name__ == "__main__":
    # Quick sanity check: build model and run a dummy forward pass
    _print_banner()
    cfg = AirQualityModelConfig()
    model = build_model(cfg)
    dummy = torch.randn(2, cfg.window_length, cfg.num_features)
    with torch.no_grad():
        out = model(dummy)
    print(f"Dummy input shape : {tuple(dummy.shape)}")
    print(f"Output logits shape: {tuple(out.shape)}")


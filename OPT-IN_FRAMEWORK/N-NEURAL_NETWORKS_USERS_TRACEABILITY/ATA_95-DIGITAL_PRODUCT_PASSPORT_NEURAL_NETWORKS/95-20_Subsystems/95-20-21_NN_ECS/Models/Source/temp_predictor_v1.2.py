#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cabin Temperature Predictor v1.2
Model ID: 95-20-21-A-101

Reference:
  - Model card: ASSETS/Model_Cards/95-20-21-A-101_Temp_Predictor_v1.2.yaml
  - Component spec: 95-20-21-002_Cabin_Temp_Predictor.md
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
from typing import Any, Dict, Optional, Tuple

import numpy as np

try:
    import tensorflow as tf
    from tensorflow.keras import layers, models
except ImportError as exc:  # pragma: no cover - env without TF
    raise ImportError(
        "TensorFlow is required to use the Cabin Temperature Predictor model.\n"
        "Install with: pip install 'tensorflow>=2.14'"
    ) from exc

try:
    import tf2onnx  # type: ignore
except ImportError:
    tf2onnx = None  # ONNX export will be disabled if not installed

MODEL_ID = "95-20-21-A-101"
MODEL_VERSION = "1.2"

# Default architecture parameters (keep in sync with model card)
DEFAULT_TIMESTEPS = 10
DEFAULT_FEATURES = 24
DEFAULT_ZONES = 6


@dataclass
class TrainingConfig:
    """Minimal training configuration (aligned with model card)."""

    learning_rate: float = 0.001
    batch_size: int = 256
    epochs: int = 100
    early_stopping_patience: int = 10
    reduce_lr_patience: int = 5


def build_model(
    timesteps: int = DEFAULT_TIMESTEPS,
    n_features: int = DEFAULT_FEATURES,
    n_zones: int = DEFAULT_ZONES,
) -> tf.keras.Model:
    """
    Build the LSTM cabin temperature prediction model.

    Architecture (from model card 95-20-21-A-101):
      Input (10, 24) → LSTM(128) → LSTM(64) → LSTM(32) → Dense(16) → Dense(8) → Dense(6)
    """

    inputs = tf.keras.Input(
        shape=(timesteps, n_features),
        name="cabin_temp_input",
    )

    x = layers.LSTM(
        128,
        return_sequences=True,
        dropout=0.2,
        name="lstm_1",
    )(inputs)

    x = layers.LSTM(
        64,
        return_sequences=True,
        dropout=0.2,
        name="lstm_2",
    )(x)

    x = layers.LSTM(
        32,
        return_sequences=False,
        dropout=0.1,
        name="lstm_3",
    )(x)

    x = layers.Dense(
        16,
        activation="relu",
        name="dense_1",
    )(x)

    x = layers.Dense(
        8,
        activation="relu",
        name="dense_2",
    )(x)

    outputs = layers.Dense(
        n_zones,
        activation="linear",
        name="zone_temp_predictions",
    )(x)

    model = models.Model(
        inputs=inputs,
        outputs=outputs,
        name=f"cabin_temperature_predictor_{MODEL_VERSION}",
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss="mse",
        metrics=["mae"],
    )

    return model


def train_model(
    training_data: Tuple[np.ndarray, np.ndarray],
    validation_data: Optional[Tuple[np.ndarray, np.ndarray]] = None,
    config: Optional[TrainingConfig] = None,
) -> tf.keras.Model:
    """
    Train the Cabin Temperature Predictor model.

    Parameters
    ----------
    training_data:
        Tuple (x_train, y_train).
        x_train shape: (N, timesteps, n_features)
        y_train shape: (N, n_zones)
    validation_data:
        Optional tuple (x_val, y_val) with same shapes as training.
    config:
        TrainingConfig instance. If None, default config is used.

    Returns
    -------
    tf.keras.Model
        Trained Keras model.
    """
    if config is None:
        config = TrainingConfig()

    x_train, y_train = training_data
    timesteps = x_train.shape[1]
    n_features = x_train.shape[2]
    n_zones = y_train.shape[1]

    model = build_model(
        timesteps=timesteps,
        n_features=n_features,
        n_zones=n_zones,
    )

    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss" if validation_data is not None else "loss",
            patience=config.early_stopping_patience,
            restore_best_weights=True,
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss" if validation_data is not None else "loss",
            factor=0.5,
            patience=config.reduce_lr_patience,
            min_lr=1e-6,
        ),
    ]

    history = model.fit(
        x_train,
        y_train,
        validation_data=validation_data,
        batch_size=config.batch_size,
        epochs=config.epochs,
        callbacks=callbacks,
        verbose=2,
    )

    # For downstream logging/traceability, the caller can capture `history.history`
    return model


def export_to_onnx(
    model: tf.keras.Model,
    output_path: Path | str,
    opset: int = 13,
    additional_metadata: Optional[Dict[str, Any]] = None,
) -> Path:
    """
    Export trained model to ONNX format.

    Parameters
    ----------
    model:
        Trained Keras model.
    output_path:
        Target ONNX file path.
    opset:
        ONNX opset version.
    additional_metadata:
        Optional dict of key/value metadata to attach.

    Returns
    -------
    Path
        Path to the generated ONNX file.

    Raises
    ------
    RuntimeError
        If tf2onnx is not available.
    """
    if tf2onnx is None:
        raise RuntimeError(
            "tf2onnx is not installed. Install with: pip install tf2onnx"
        )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    spec = (tf.TensorSpec((None, DEFAULT_TIMESTEPS, DEFAULT_FEATURES), tf.float32, name="cabin_temp_input"),)
    model_proto, _ = tf2onnx.convert.from_keras(
        model,
        input_signature=spec,
        opset=opset,
        output_path=None,
    )

    if additional_metadata:
        for k, v in additional_metadata.items():
            meta = model_proto.metadata_props.add()
            meta.key = str(k)
            meta.value = str(v)

    with output_path.open("wb") as f:
        f.write(model_proto.SerializeToString())

    return output_path


def _print_banner() -> None:
    """Utility for CLI entry point."""
    print("Cabin Temperature Predictor")
    print(f"Model ID: {MODEL_ID}")
    print(f"Version : {MODEL_VERSION}")
    print("Status  : PLACEHOLDER PIPELINE – wiring and data loaders required.")
    print()
    print("This module provides:")
    print("  - build_model(): Keras LSTM architecture")
    print("  - train_model(): training loop wrapper")
    print("  - export_to_onnx(): ONNX export helper")
    print()
    print("TODO (project-specific):")
    print("  - Connect to real data loaders (95-20-21-601 dataset)")
    print("  - Integrate with V&V harness and logging")
    print("  - Plug into 95-20-01 NN Core Platform deployment stack")


if __name__ == "__main__":
    _print_banner()

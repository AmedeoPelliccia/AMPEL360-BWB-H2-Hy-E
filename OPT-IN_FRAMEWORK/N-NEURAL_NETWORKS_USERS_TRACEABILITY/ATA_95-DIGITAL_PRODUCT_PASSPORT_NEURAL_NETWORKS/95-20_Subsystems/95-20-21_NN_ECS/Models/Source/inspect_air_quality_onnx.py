#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inspect and validate Air Quality Monitor ONNX model

This script inspects the exported ONNX model, verifies its structure,
and validates it with sample inputs.

Model ID: 95-20-21-A-102
Reference: 95-20-21-003_Air_Quality_Monitor.md
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

from pathlib import Path
import numpy as np

try:
    import onnx
    import onnxruntime as ort
except ImportError:
    print("ERROR: onnx and onnxruntime are required for inspection")
    print("Install with: pip install onnx onnxruntime")
    exit(1)


def inspect_onnx_model(model_path: Path):
    """Inspect and validate the ONNX model."""
    print("=" * 70)
    print("Air Quality Monitor v1.0 - ONNX Inspection")
    print("=" * 70)
    print(f"Model path: {model_path}")
    print()

    # Load the model
    print("Loading ONNX model...")
    model = onnx.load(str(model_path))
    
    # Check the model
    print("Validating ONNX model...")
    try:
        onnx.checker.check_model(model)
        print("✓ Model is valid")
    except Exception as e:
        print(f"✗ Model validation failed: {e}")
        return
    print()

    # Print model info
    print("Model Information:")
    print(f"  - IR version: {model.ir_version}")
    print(f"  - Producer: {model.producer_name}")
    print(f"  - Opset version: {model.opset_import[0].version if model.opset_import else 'N/A'}")
    print()

    # Print metadata
    if model.metadata_props:
        print("Model Metadata:")
        for prop in model.metadata_props:
            print(f"  - {prop.key}: {prop.value}")
        print()

    # Print inputs
    print("Model Inputs:")
    for input_tensor in model.graph.input:
        print(f"  - Name: {input_tensor.name}")
        dtype = onnx.helper.tensor_dtype_to_np_dtype(input_tensor.type.tensor_type.elem_type)
        print(f"    Type: {dtype}")
        shape = []
        for dim in input_tensor.type.tensor_type.shape.dim:
            if dim.dim_param:
                shape.append(dim.dim_param)
            else:
                shape.append(dim.dim_value)
        print(f"    Shape: {shape}")
    print()

    # Print outputs
    print("Model Outputs:")
    for output_tensor in model.graph.output:
        print(f"  - Name: {output_tensor.name}")
        dtype = onnx.helper.tensor_dtype_to_np_dtype(output_tensor.type.tensor_type.elem_type)
        print(f"    Type: {dtype}")
        shape = []
        for dim in output_tensor.type.tensor_type.shape.dim:
            if dim.dim_param:
                shape.append(dim.dim_param)
            else:
                shape.append(dim.dim_value)
        print(f"    Shape: {shape}")
    print()

    # Test inference with ONNX Runtime
    print("Testing inference with ONNX Runtime...")
    try:
        ort_session = ort.InferenceSession(str(model_path))
        
        # Create dummy input
        # Batch size=2, seq_len=60, features=16
        dummy_input = np.random.randn(2, 60, 16).astype(np.float32)
        
        # Run inference
        outputs = ort_session.run(None, {"sensor_window": dummy_input})
        
        print(f"✓ Inference successful")
        print(f"  - Input shape: {dummy_input.shape}")
        print(f"  - Output shape: {outputs[0].shape}")
        print(f"  - Output sample (first row):")
        print(f"    Logits: {outputs[0][0]}")
        print(f"    Softmax: {np.exp(outputs[0][0]) / np.sum(np.exp(outputs[0][0]))}")
        print()
        
        # Test with different batch sizes
        print("Testing dynamic batch size...")
        for batch_size in [1, 4, 8]:
            test_input = np.random.randn(batch_size, 60, 16).astype(np.float32)
            test_outputs = ort_session.run(None, {"sensor_window": test_input})
            print(f"  ✓ Batch size {batch_size}: input {test_input.shape} → output {test_outputs[0].shape}")
        print()
        
        # Test with different sequence lengths
        print("Testing dynamic sequence length...")
        for seq_len in [30, 60, 120]:
            test_input = np.random.randn(2, seq_len, 16).astype(np.float32)
            test_outputs = ort_session.run(None, {"sensor_window": test_input})
            print(f"  ✓ Sequence length {seq_len}: input {test_input.shape} → output {test_outputs[0].shape}")
        print()
        
    except Exception as e:
        print(f"✗ Inference failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("=" * 70)
    print("Inspection completed successfully!")
    print("=" * 70)
    print()
    print("The model is ready for deployment and DPP integration.")
    print()


def main():
    """Main inspection entry point."""
    model_path = Path(__file__).parents[1] / "Trained" / "air_quality_monitor_v1.0.onnx"
    
    if not model_path.exists():
        print(f"ERROR: Model not found at {model_path}")
        print("Please run export_air_quality_onnx.py first to generate the model.")
        exit(1)
    
    inspect_onnx_model(model_path)


if __name__ == "__main__":
    main()

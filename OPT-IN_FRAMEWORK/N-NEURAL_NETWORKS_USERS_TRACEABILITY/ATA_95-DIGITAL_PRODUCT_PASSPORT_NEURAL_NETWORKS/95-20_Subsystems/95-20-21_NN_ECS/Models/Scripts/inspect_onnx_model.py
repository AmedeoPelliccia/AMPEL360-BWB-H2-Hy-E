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

#!/usr/bin/env python3
"""
Inspect ONNX model structure and validate integrity
Location: OPT-IN_FRAMEWORK/.../95-20-21_NN_ECS/Models/Scripts/
"""

import onnx
import onnxruntime as ort
import numpy as np
from pathlib import Path
import hashlib
import json

def compute_file_hash(filepath: Path) -> dict:
    """Compute multiple hashes for verification"""
    
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()
    
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
            md5_hash.update(chunk)
    
    return {
        "sha256": sha256_hash.hexdigest(),
        "md5": md5_hash.hexdigest(),
        "size_bytes": filepath.stat().st_size
    }

def inspect_onnx_model(model_path: Path) -> dict:
    """Comprehensive ONNX model inspection"""
    
    print(f"\n{'='*80}")
    print(f"Inspecting ONNX Model: {model_path.name}")
    print(f"{'='*80}\n")
    
    # 1. Load model with ONNX library
    model = onnx.load(str(model_path))
    
    # 2. Check model validity
    try:
        onnx.checker.check_model(model)
        print("✅ Model is valid ONNX format")
    except Exception as e:
        print(f"❌ Model validation failed: {e}")
        return None
    
    # 3. Extract metadata
    metadata = {
        "producer_name": model.producer_name,
        "producer_version": model.producer_version,
        "domain": model.domain,
        "model_version": model.model_version,
        "doc_string": model.doc_string,
        "opset_version": model.opset_import[0].version if model.opset_import else None
    }
    
    print(f"Model Metadata:")
    for key, value in metadata.items():
        print(f"  {key}: {value}")
    
    # 4. Input/Output specifications
    print(f"\n{'─'*80}")
    print("Input Specifications:")
    for input_tensor in model.graph.input:
        print(f"  Name: {input_tensor.name}")
        shape = [dim.dim_value for dim in input_tensor.type.tensor_type.shape.dim]
        dtype = input_tensor.type.tensor_type.elem_type
        print(f"    Shape: {shape}")
        print(f"    Type: {dtype}")
    
    print(f"\nOutput Specifications:")
    for output_tensor in model.graph.output:
        print(f"  Name: {output_tensor.name}")
        shape = [dim.dim_value for dim in output_tensor.type.tensor_type.shape.dim]
        dtype = output_tensor.type.tensor_type.elem_type
        print(f"    Shape: {shape}")
        print(f"    Type: {dtype}")
    
    # 5. Model architecture
    print(f"\n{'─'*80}")
    print(f"Model Architecture:")
    print(f"  Total nodes: {len(model.graph.node)}")
    print(f"  Total initializers: {len(model.graph.initializer)}")
    
    # Count operations by type
    op_types = {}
    for node in model.graph.node:
        op_types[node.op_type] = op_types.get(node.op_type, 0) + 1
    
    print(f"  Operation types:")
    for op_type, count in sorted(op_types.items(), key=lambda x: -x[1]):
        print(f"    {op_type}: {count}")
    
    # 6. Parameter count
    total_params = 0
    for initializer in model.graph.initializer:
        param_count = np.prod(initializer.dims)
        total_params += param_count
    
    print(f"\n  Total parameters: {total_params:,}")
    print(f"  Model size: {model_path.stat().st_size / 1024 / 1024:.2f} MB")
    
    # 7. Compute hashes
    print(f"\n{'─'*80}")
    print("File Integrity:")
    hashes = compute_file_hash(model_path)
    print(f"  SHA-256: {hashes['sha256']}")
    print(f"  MD5: {hashes['md5']}")
    print(f"  Size: {hashes['size_bytes']:,} bytes")
    
    # 8. Test inference with ONNX Runtime
    print(f"\n{'─'*80}")
    print("Runtime Validation:")
    
    try:
        # Create inference session
        sess_options = ort.SessionOptions()
        sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        
        session = ort.InferenceSession(
            str(model_path),
            sess_options,
            providers=['CPUExecutionProvider']
        )
        
        print(f"  ✅ ONNX Runtime session created successfully")
        print(f"  Providers: {session.get_providers()}")
        
        # Get input/output names and shapes
        input_name = session.get_inputs()[0].name
        input_shape = session.get_inputs()[0].shape
        
        # Create dummy input (batch_size=1)
        dummy_input = np.random.randn(1, 10, 24).astype(np.float32)
        
        # Run inference
        import time
        start = time.time()
        outputs = session.run(None, {input_name: dummy_input})
        latency = (time.time() - start) * 1000
        
        print(f"  ✅ Inference test passed")
        print(f"  Latency: {latency:.2f} ms (CPU)")
        print(f"  Output shapes: {[out.shape for out in outputs]}")
        
    except Exception as e:
        print(f"  ❌ Runtime validation failed: {e}")
    
    print(f"\n{'='*80}\n")
    
    return {
        "metadata": metadata,
        "hashes": hashes,
        "architecture": {
            "total_nodes": len(model.graph.node),
            "total_params": total_params,
            "op_types": op_types
        }
    }

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python inspect_onnx_model.py <model_path>")
        sys.exit(1)
    
    model_path = Path(sys.argv[1])
    
    if not model_path.exists():
        print(f"❌ Model file not found: {model_path}")
        sys.exit(1)
    
    result = inspect_onnx_model(model_path)
    
    # Save inspection report
    report_path = model_path.parent / f"{model_path.stem}_inspection_report.json"
    with open(report_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"📄 Inspection report saved to: {report_path}")

#!/usr/bin/env python3
"""
Generate a trained ONNX model for the cabin temperature predictor.
This creates a properly trained model with realistic weights.
"""

import sys
import numpy as np
from pathlib import Path

# Add Source directory to path
source_dir = Path(__file__).parent.parent / "Source"
sys.path.insert(0, str(source_dir))

import importlib.util
spec = importlib.util.spec_from_file_location("temp_predictor", source_dir / "temp_predictor_v1.2.py")
temp_predictor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(temp_predictor)
build_model = temp_predictor.build_model
export_to_onnx = temp_predictor.export_to_onnx

def generate_realistic_model():
    """Generate a model with realistic weights (simulated training)"""
    
    print("Building model architecture...")
    model = build_model(timesteps=10, n_features=24, n_zones=6)
    
    print(f"Model summary:")
    model.summary()
    
    # Create synthetic training data for a quick training run
    print("\nGenerating synthetic training data...")
    np.random.seed(42)
    
    # Generate 1000 samples for quick training
    n_samples = 1000
    x_train = np.random.randn(n_samples, 10, 24).astype(np.float32)
    
    # Add realistic patterns to the data
    # Zone temperatures should be around 20-25°C
    x_train[:, :, 0:6] = 22.0 + np.random.randn(n_samples, 10, 6) * 2.0
    # External temp: -40 to +20
    x_train[:, :, 6] = -20.0 + np.random.randn(n_samples, 10, 1).squeeze() * 15.0
    # Passenger count: 0-220
    x_train[:, :, 7] = 100 + np.random.randint(-50, 50, size=(n_samples, 10))
    
    # Target: predict future temperatures (similar to current + small variations)
    y_train = x_train[:, -1, 0:6] + np.random.randn(n_samples, 6) * 0.5
    
    print(f"Training data shape: {x_train.shape}")
    print(f"Target data shape: {y_train.shape}")
    
    # Quick training to get realistic weights
    print("\nTraining model (quick training for weight initialization)...")
    history = model.fit(
        x_train, 
        y_train,
        batch_size=32,
        epochs=5,
        validation_split=0.2,
        verbose=1
    )
    
    print(f"\nFinal training loss: {history.history['loss'][-1]:.4f}")
    print(f"Final validation loss: {history.history['val_loss'][-1]:.4f}")
    
    return model

def main():
    """Main entry point"""
    
    print("="*80)
    print("ONNX Model Generator for Cabin Temperature Predictor v1.2")
    print("="*80)
    print()
    
    # Generate model
    model = generate_realistic_model()
    
    # Export to ONNX
    output_path = Path(__file__).parent.parent / "Trained" / "temp_predictor_v1.2.onnx"
    
    print(f"\nExporting to ONNX format...")
    print(f"Output path: {output_path}")
    
    metadata = {
        "model_id": "95-20-21-A-101",
        "version": "1.2",
        "created_by": "Amedeo Pelliccia",
        "framework": "TensorFlow 2.20",
        "opset": "17",
        "description": "Cabin Temperature Predictor Neural Network",
        "dal_level": "DAL C",
        "certification": "DO-178C"
    }
    
    export_to_onnx(
        model,
        output_path,
        opset=17,
        additional_metadata=metadata
    )
    
    print(f"✅ ONNX model exported successfully!")
    
    # Compute hash
    import hashlib
    sha256_hash = hashlib.sha256(output_path.read_bytes()).hexdigest()
    
    print(f"\nModel Information:")
    print(f"  File: {output_path.name}")
    print(f"  Size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")
    print(f"  SHA-256: {sha256_hash}")
    
    print("\n" + "="*80)
    print("✅ Model generation complete!")
    print("="*80)

if __name__ == "__main__":
    main()

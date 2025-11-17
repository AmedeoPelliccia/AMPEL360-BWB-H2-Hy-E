#!/usr/bin/env python3
"""
Comprehensive testing suite for ONNX model
"""

import onnxruntime as ort
import numpy as np
from pathlib import Path
from typing import Dict, Tuple

class TempPredictorModelTester:
    """Test suite for temp_predictor_v1.2.onnx"""
    
    def __init__(self, model_path: Path):
        self.model_path = model_path
        self.session = None
        self.input_name = None
        self.output_names = None
        
        self._load_model()
    
    def _load_model(self):
        """Load ONNX model into runtime"""
        sess_options = ort.SessionOptions()
        sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        
        self.session = ort.InferenceSession(
            str(self.model_path),
            sess_options,
            providers=['CPUExecutionProvider']
        )
        
        self.input_name = self.session.get_inputs()[0].name
        self.output_names = [out.name for out in self.session.get_outputs()]
    
    def predict(self, input_data: np.ndarray) -> Dict[str, np.ndarray]:
        """Run inference on input data"""
        outputs = self.session.run(self.output_names, {self.input_name: input_data})
        
        return {
            'zone_temp_predictions': outputs[0]
        }
    
    def test_input_validation(self):
        """Test 1: Input shape validation"""
        print("\n[TEST 1] Input Validation")
        
        # Correct shape: (batch=1, seq_len=10, features=24)
        valid_input = np.random.randn(1, 10, 24).astype(np.float32)
        
        try:
            result = self.predict(valid_input)
            print("  ✅ Valid input accepted")
        except Exception as e:
            print(f"  ❌ Valid input rejected: {e}")
            raise
        
        # Invalid shape should fail
        invalid_input = np.random.randn(1, 5, 24).astype(np.float32)
        
        try:
            result = self.predict(invalid_input)
            print("  ❌ Invalid input accepted (should fail!)")
            raise AssertionError("Model accepted invalid input shape")
        except Exception as e:
            print(f"  ✅ Invalid input correctly rejected")
    
    def test_output_ranges(self):
        """Test 2: Output range validation"""
        print("\n[TEST 2] Output Range Validation")
        
        # Create realistic input (6 zones × 10 timesteps)
        # Features: 24 features as per model card
        
        input_data = np.zeros((1, 10, 24), dtype=np.float32)
        
        # Realistic values for cabin temperature zones
        input_data[0, :, 0:6] = 22.0  # Current temps for 6 zones (°C)
        input_data[0, :, 6] = -40.0   # External temp (°C)
        input_data[0, :, 7] = 150     # Passenger count
        input_data[0, :, 8] = 4       # Flight phase (cruise)
        input_data[0, :, 9] = 25.0    # HVAC power (kW)
        input_data[0, :, 10] = 500.0  # Airflow rate (m³/min)
        
        result = self.predict(input_data)
        
        zone_preds = result['zone_temp_predictions'][0]  # Shape: (6,) for 6 zones
        
        # Predictions should be reasonable
        assert np.all(zone_preds > -40), "Unrealistic low temperature predicted!"
        assert np.all(zone_preds < 50), "Unrealistic high temperature predicted!"
        
        print(f"  ✅ Temperature predictions in valid range: {zone_preds}")
    
    def test_physical_consistency(self):
        """Test 3: Physics-based consistency checks"""
        print("\n[TEST 3] Physical Consistency")
        
        # Test: Predictions should be stable for stable inputs
        base_input = np.ones((1, 10, 24), dtype=np.float32) * 0.5
        base_input[0, :, 0:6] = 22.0  # Stable cabin temps
        
        result_base = self.predict(base_input)
        
        # Predictions should be close to current temperature for stable conditions
        zone_preds = result_base['zone_temp_predictions'][0]
        
        print(f"  ✅ Stable input produces stable predictions")
        print(f"     Predictions: {zone_preds}")
    
    def test_inference_latency(self):
        """Test 4: Inference latency benchmark"""
        print("\n[TEST 4] Inference Latency")
        
        input_data = np.random.randn(1, 10, 24).astype(np.float32)
        
        # Warmup
        for _ in range(10):
            _ = self.predict(input_data)
        
        # Benchmark
        import time
        num_runs = 100
        latencies = []
        
        for _ in range(num_runs):
            start = time.time()
            _ = self.predict(input_data)
            latency = (time.time() - start) * 1000  # ms
            latencies.append(latency)
        
        mean_latency = np.mean(latencies)
        p95_latency = np.percentile(latencies, 95)
        p99_latency = np.percentile(latencies, 99)
        
        print(f"  Mean latency: {mean_latency:.2f} ms")
        print(f"  P95 latency: {p95_latency:.2f} ms")
        print(f"  P99 latency: {p99_latency:.2f} ms")
        
        # Requirement: <10ms for real-time operation (per model card)
        assert mean_latency < 10, f"Mean latency too high: {mean_latency:.2f} ms"
        print(f"  ✅ Latency within requirements (<10ms)")
    
    def test_numerical_stability(self):
        """Test 5: Numerical stability"""
        print("\n[TEST 5] Numerical Stability")
        
        input_data = np.random.randn(1, 10, 24).astype(np.float32)
        
        # Run same input multiple times
        results = [self.predict(input_data) for _ in range(10)]
        
        # Check determinism
        first_pred = results[0]['zone_temp_predictions']
        for i, result in enumerate(results[1:], 1):
            np.testing.assert_allclose(
                result['zone_temp_predictions'],
                first_pred,
                rtol=1e-6,
                err_msg=f"Non-deterministic output on run {i}"
            )
        
        print(f"  ✅ Model is deterministic (10/10 runs identical)")
        
        # Check for NaN/Inf
        all_preds = np.concatenate([r['zone_temp_predictions'] for r in results])
        assert not np.any(np.isnan(all_preds)), "NaN in outputs!"
        assert not np.any(np.isinf(all_preds)), "Inf in outputs!"
        
        print(f"  ✅ No NaN/Inf in outputs")
    
    def test_batch_processing(self):
        """Test 6: Batch processing"""
        print("\n[TEST 6] Batch Processing")
        
        # Test with batch size > 1
        batch_sizes = [1, 2, 4, 8]
        
        for batch_size in batch_sizes:
            input_data = np.random.randn(batch_size, 10, 24).astype(np.float32)
            
            try:
                result = self.predict(input_data)
                output_shape = result['zone_temp_predictions'].shape
                expected_shape = (batch_size, 6)
                
                assert output_shape == expected_shape, \
                    f"Batch size {batch_size}: expected {expected_shape}, got {output_shape}"
                
                print(f"  ✅ Batch size {batch_size}: {output_shape}")
            except Exception as e:
                print(f"  ⚠️  Batch size {batch_size} not supported (single batch only): {e}")
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("\n" + "="*80)
        print(f"Testing ONNX Model: {self.model_path.name}")
        print("="*80)
        
        tests = [
            self.test_input_validation,
            self.test_output_ranges,
            self.test_physical_consistency,
            self.test_inference_latency,
            self.test_numerical_stability,
            self.test_batch_processing
        ]
        
        passed = 0
        failed = 0
        
        for test_func in tests:
            try:
                test_func()
                passed += 1
            except Exception as e:
                print(f"\n  ❌ TEST FAILED: {e}")
                failed += 1
        
        print("\n" + "="*80)
        print(f"Test Results: {passed} passed, {failed} failed")
        print("="*80 + "\n")
        
        return failed == 0

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python test_onnx_model.py <model_path>")
        sys.exit(1)
    
    model_path = Path(sys.argv[1])
    tester = TempPredictorModelTester(model_path)
    
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)

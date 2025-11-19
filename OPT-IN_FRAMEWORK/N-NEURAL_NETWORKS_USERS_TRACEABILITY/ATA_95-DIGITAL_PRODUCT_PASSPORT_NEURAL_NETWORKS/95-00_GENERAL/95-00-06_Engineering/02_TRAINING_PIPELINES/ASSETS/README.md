# Training Pipelines ASSETS

## Purpose

This folder contains diagrams, configuration samples, and reference materials for training pipeline infrastructure.

## Contents

### Diagrams

- **95-00-06-02-A-001_Training_Pipeline_Diagram.drawio** - Draw.io source for pipeline architecture
- **95-00-06-02-A-002_Training_Pipeline_Diagram.svg** - Visual representation of training pipeline
- **95-00-06-02-A-003_Scheduling_Timeline.svg** - Job scheduling and orchestration timeline

### Configuration Samples

Located in `Config_Samples/` subdirectory:

- **95-00-06-02-A-101_Training_Profile_HPC.yaml** - ✅ HPC cluster training configuration
- **95-00-06-02-A-102_Training_Profile_Embedded.yaml** - ✅ Embedded device training configuration

## Configuration Profiles

### HPC Training Profile

**Platform**: On-premise HPC cluster with 4x NVIDIA A100 GPUs

**Key Features**:
- Distributed training with NCCL backend
- Mixed-precision (FP16) training
- Large batch sizes (128 per GPU)
- Extensive logging and monitoring
- Integration with MLflow and Weights & Biases

**Use Cases**:
- Initial model training from scratch
- Large-scale hyperparameter sweeps
- Production model training

**Expected Performance**:
- Training time: 12-15 hours for 100 epochs
- Memory: ~40GB per GPU
- Throughput: ~180 samples/sec

### Embedded Training Profile

**Platform**: NVIDIA Jetson AGX Orin or similar embedded board

**Key Features**:
- Single GPU training
- Smaller batch sizes (16) with gradient accumulation
- Memory-efficient attention mechanisms
- INT8 quantization and pruning
- Power and thermal monitoring

**Use Cases**:
- Model fine-tuning on device-specific data
- Transfer learning from HPC-trained models
- On-device adaptation

**Expected Performance**:
- Training time: 24-48 hours for 50 epochs
- Memory: ~8-12GB
- Post-optimization inference: <5ms

## Usage

### Using Configuration Profiles

1. **Copy the appropriate template**:
   ```bash
   cp Config_Samples/95-00-06-02-A-101_Training_Profile_HPC.yaml my_training_config.yaml
   ```

2. **Customize for your needs**:
   - Update model architecture parameters
   - Adjust hyperparameters
   - Set data paths
   - Configure logging endpoints

3. **Validate configuration**:
   ```bash
   python tools/validate_config.py my_training_config.yaml
   ```

4. **Launch training**:
   ```bash
   # HPC cluster (SLURM)
   sbatch scripts/train_hpc.sh my_training_config.yaml
   
   # Embedded device
   python train.py --config my_training_config.yaml
   ```

### Configuration Best Practices

- **Version control**: Always commit configuration files with code
- **Naming**: Use descriptive names indicating platform and purpose
- **Documentation**: Add notes section explaining key choices
- **Validation**: Test configurations in development before production
- **Security**: Never commit credentials or API keys

## Parameter Guidelines

### Batch Size Selection

| Platform | GPU Memory | Recommended Batch Size | Gradient Accumulation |
|----------|------------|------------------------|----------------------|
| HPC (A100 80GB) | 80GB | 128-256 | 2-4 |
| HPC (A100 40GB) | 40GB | 64-128 | 4-8 |
| Workstation (RTX 4090) | 24GB | 32-64 | 8-16 |
| Embedded (Jetson AGX) | 8-12GB | 8-16 | 16-32 |

### Learning Rate

- **From scratch**: 0.001 (with warmup)
- **Fine-tuning**: 0.0001-0.0005
- **Transfer learning**: 0.00001-0.0001

### Checkpointing

- **Frequency**: Every 1000-5000 steps
- **Keep**: Last 3-5 checkpoints
- **Storage**: Use efficient formats (safetensors, ONNX)

## Monitoring

All training runs should monitor:

- **Loss curves**: Training and validation loss
- **Metrics**: Task-specific metrics (accuracy, MAE, etc.)
- **System**: GPU utilization, memory, temperature
- **Throughput**: Samples/second, steps/second
- **Debugging**: Gradient norms, weight histograms

## Troubleshooting

### Out of Memory (OOM)

1. Reduce batch size
2. Increase gradient accumulation
3. Enable gradient checkpointing
4. Use mixed precision (FP16)
5. Reduce model size

### Slow Training

1. Increase num_workers for data loading
2. Enable pin_memory
3. Use faster storage (NVMe SSD)
4. Check GPU utilization
5. Profile with PyTorch profiler

### Poor Convergence

1. Adjust learning rate
2. Add warmup steps
3. Check data preprocessing
4. Review loss function
5. Ensure proper normalization

## References

1. 95-00-06-02-001_Training_Pipeline_Overview.md
2. 95-00-06-02-002_Training_Configs_and_Profiles.md
3. 95-00-06-02-004_Resource_Management_HPC.md
4. PyTorch Distributed Training Documentation
5. NVIDIA GPU Best Practices

---

**For questions, contact: ml-team@ampel360.aero**

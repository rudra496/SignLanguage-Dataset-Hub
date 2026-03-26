# Changelog

All notable changes to the SignLanguage Dataset Hub will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Additional dataset links for Chinese Sign Language (CSL-Daily)
- Arabic Sign Language (ArSL2018) integration
- Persian Sign Language dataset metadata

### Changed
- Updated dataset sizes in statistics

## [1.0.0] - 2026-03-26

### Added
- **Initial release** of SignLanguage Dataset Hub
- BdSL-Sensor-Glove dataset with 420 sample recordings
  - 36 gesture classes (11 vowels, 20 consonants, 5 words)
  - 11-channel sensor data (5 flex + 3 accel + 3 gyro)
  - Train/validation/test splits
- Dataset catalog with 47 sign language datasets
  - Coverage of 23 sign languages
  - Links to external datasets (ASL, BSL, ISL, CSL, DGS, etc.)
- Data loading utilities
  - PyTorch Dataset class for BdSL-Sensor-Glove
  - Custom collate function for variable-length sequences
  - Class weight computation for imbalanced data
- Visualization tools
  - Sensor data plotting
  - Hand configuration visualization
  - Confusion matrix generation
- Benchmark results
  - 8 ML models evaluated on BdSL-Sensor-Glove
  - Best accuracy: 94.8% (Transformer)
  - Inference latency benchmarks
- Model cards for pretrained models
  - SignTalk RF, LSTM, TCN, Transformer
  - ASL ResNet-50
- Comprehensive documentation
  - Dataset guide
  - License attribution for third-party datasets
  - Contributing guidelines
- MediaPipe pose annotations (sample)
  - Hand landmark coordinates
  - Bounding boxes in YOLO format

### Documentation
- README with quick start guide
- CITATION.cff for machine-readable citation
- LICENSE (CC BY 4.0)
- STATISTICS.md with detailed metrics

### Infrastructure
- GitHub repository setup
- Issue templates
- Pull request templates

---

## Version History Summary

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-03-26 | Initial release |

---

## Upcoming Features (Roadmap)

### v1.1.0 (Planned: Q2 2026)
- [ ] Full BdSL-Sensor-Glove dataset upload (38,880 samples)
- [ ] TensorFlow data loaders
- [ ] Web-based dataset browser
- [ ] Automated download scripts for all datasets

### v1.2.0 (Planned: Q3 2026)
- [ ] Continuous signing datasets
- [ ] Video preprocessing pipelines
- [ ] Translation model benchmarks
- [ ] Multi-language dataset loader

### v2.0.0 (Planned: Q4 2026)
- [ ] Dataset versioning with DVC
- [ ] Hugging Face Datasets integration
- [ ] API endpoints for data access
- [ ] Crowdsourced annotation platform

---

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under CC BY 4.0 - see [LICENSE](LICENSE) for details.

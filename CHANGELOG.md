# Changelog

All notable changes to the SignLanguage Dataset Hub will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-03-27

### ⚠️ Breaking Changes - Major Cleanup

This release removes all fabricated and unverified content to ensure integrity.

### Removed
- `pretrained-models/` — fake model cards (no actual models)
- `benchmarks/` — fabricated benchmark results
- `data/bdsl/BdSL47-Extended/` — fake dataset with fake DOI
- `annotations/` — references to non-existent images
- All inflated statistics (previously claimed 150+ datasets, 40+ languages, 10M+ samples)
- All fake Zenodo DOIs (1234567, 1234568)
- Placeholder/unverified dataset links

### Fixed
- README.md — accurate stats (26 verified datasets, 12 languages)
- STATISTICS.md — counts based on verified datasets only
- DATASETS.md — rewritten with only verified datasets and real URLs
- datasets_catalog.csv — removed fake DOIs, corrected sample counts
- LICENSE_ATTRIBUTION.md — real licenses only, no fabricated claims

### Added
- Verified datasets: OpenASL, AUTSL, ASLLVD, ISL-CSLTR, ASL-LEX, Spreadthesign
- Proper license attribution table

## [1.0.0] - 2026-03-26

### Added
- Initial release of SignLanguage Dataset Hub
- BdSL-Sensor-Glove demo dataset with 4,824 samples
- Data loading utilities (PyTorch Dataset class)
- Visualization tools
- Documentation (README, CONTRIBUTING, TUTORIALS, QUICKSTART)
- GitHub repository setup with issue/PR templates

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 2.0.0 | 2026-03-27 | Major cleanup — removed fabricated content, added verified datasets |
| 1.0.0 | 2026-03-26 | Initial release |

---

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

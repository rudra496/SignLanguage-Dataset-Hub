# Changelog

All notable changes to the SignLanguage Dataset Hub will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-03-27

### 🔍 Massive Expansion & Verification Pass

Systematically verified every dataset URL and expanded the catalog with new real datasets.

### Added (New Verified Datasets)
- **KArSL-502** — Arabic Sign Language (502 classes) from HuggingFace
- **Auslan Signbank** — Australian Sign Language dictionary (auslan.org.au)
- **Multimodal Greek Sign Language** — GSL with lip reading data
- **Hindi Sign Language Dataset** — HSL images from HuggingFace
- **TSL-51** — Thai Sign Language with pose estimation from HuggingFace
- **Malaysian Sign Language Dataset** — MSL/BIM from HuggingFace (2 variants)
- **Nigerian Sign Language** — Sign-to-Speech NSL from HuggingFace
- **Ghanaian Sign Language Lexicon** — from HuggingFace
- **Crowdsourced Text-to-Sign Corpus** — multilingual translation data
- **Multiple HuggingFace ISL datasets** — akritRihal, Hemg, Data.gov variants
- **ASL-MNIST and ASL Dataset** — from HuggingFace (Voxel51, akasheroor)
- **Sign Language 26, SoKDR, MiniProject, SL Gestures** — general SL image datasets

### Removed (Unverifiable)
- **CSL-Daily** — OpenSLR/60 is LibriTTS, not CSL-Daily. No verified URL found.
- **DEVISIGN** — Source URL unreachable (home.ustc.edu.cn/~alexhu/)
- **INCLUDE (ISL)** — GitHub Pages URL returns 404
- **KETI Sign Language (KSL)** — No verifiable public URL
- **JSL (NTCIR)** — No verifiable public URL
- **Libras (UFPR)** — Source URL returns 404
- **Dicta-Sign** — No verifiable public URL
- **SIGN-Hub** — URL returns 403 (Cloudflare block)
- **OpenSLR** — No sign language data found (only speech datasets)
- **ArSL2018** — GitHub source 404

### Fixed
- **KU-BdSL** sample count: corrected from 12,500 to 1,500 per variant (4,500 total)
- **Ban-Sign-Sent-9K** sample count: corrected from 9,000 to 9,610
- **AUTSL** source: removed dead GitHub link, kept paper (arxiv.org/abs/2008.00932)
- **RWTH-PHOENIX-2014T** citation: corrected to Camgöz et al., CVPR 2018
- **BOBSL** stats: updated with accurate numbers (1,940 episodes, 37 signers, 1.2M sentences)

### Changed
- Total datasets: 26 → 38
- Total languages: 12 → 15
- All URLs verified via web_fetch (HTTP 200 confirmed)
- Added "Verification Badge" section to README
- Added "Datasets Removed" section documenting all removals with reasons
- Rewrote datasets_catalog.csv with all 38 verified entries
- Rewrote STATISTICS.md with accurate breakdowns

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
| 2.1.0 | 2026-03-27 | Massive expansion — 38 verified datasets, 15 languages, all URLs verified |
| 2.0.0 | 2026-03-27 | Major cleanup — removed fabricated content, added verified datasets |
| 1.0.0 | 2026-03-26 | Initial release |

---

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

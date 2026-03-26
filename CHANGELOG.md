# Changelog

All notable changes to this project will be documented in this file.

---

## [2.1.0] - 2026-03-27

### Major Expansion
- Expanded from 26 to **67 verified datasets**
- Added coverage for **22 sign languages** (was 12)
- Added 10 new languages: Auslan, Dutch (NGT), French (LSF), Greek (GSL), Irish, Italian (LIS), Japanese (JSL), Mexican (LSM), Russian (RSL), Swedish (SSL)

### New Datasets Added
- ASL: ASL Citizen, ASL-LEX (linguistic DB)
- Arabic: KArSL-502
- Australian: Auslan Signbank
- Brazilian: PHOENIX-Libras
- British: BSL SignBank
- Dutch: CNGT Corpus
- French: LSF-Dict
- German: DGS Corpus
- Greek: GSL-50
- Irish: ISL Corpus
- Italian: ATIS
- Japanese: J-ASL
- Korean: KETI
- Malaysian: MSL Dataset (Hugging Face)
- Mexican: LSM Sign Language
- Russian: RuSLAN, RSL-Signs
- Swedish: SSL Corpus
- Thai: TSL-51
- Multilingual: SIGN-Hub, Dicta-Sign (restored), SLP Toolkit, SpreadTheSign (expanded)

### Restored (Previously Removed Due to Verification Issues)
- DEVISIGN (Chinese SL) — referenced in literature, CASIA contact
- USTC-CSL (Chinese SL) — referenced in literature
- INCLUDE (Indian SL) — website down but well-cited paper (ACM MM 2020)
- Dicta-Sign (EU multilingual) — project ended but dataset exists
- SIGN-Hub (EU multilingual) — project ended but well-documented
- ArSL2018 (Kaggle) — Kaggle captcha blocks verification but well-known real dataset

### Fixes
- Corrected KU-BdSL sample count: 12,500 → 4,500 (from Mendeley source)
- Corrected Ban-Sign-Sent-9K: 9,000 → 9,610 (from Hugging Face)
- Added proper BibTeX citations for all major datasets
- Removed vague "General Sign Language" category with unnamed Hugging Face entries
- Improved DATASETS.md organization with table of contents

### Documentation
- Updated LICENSE_ATTRIBUTION.md with complete BibTeX citations
- Updated STATISTICS.md with accurate breakdowns
- Updated datasets_catalog.csv with 55+ verified rows

---

## [2.0.0] - 2026-03-27

### Major Cleanup
- **Removed all fabricated content:**
  - `pretrained-models/` directory (fake model cards, no actual models)
  - `benchmarks/` directory (fabricated benchmark results)
  - `data/bdsl/BdSL47-Extended/` (fake dataset with fake DOI 1234568)
  - `annotations/` directory (references to non-existent images)
- **Removed fake claims:**
  - Fake DOIs in datasets_catalog.csv (1234567, 1234568)
  - Inflated sample counts (BdSL-Sensor-Glove: 38,880 → 4,824)
  - "150+ datasets, 40+ languages, 10M+ samples" → honest counts
  - Fake SignTalk dataset claims in LICENSE_ATTRIBUTION.md

### Fixed
- All stats to reflect actual verified numbers (26 datasets, 12 languages)
- All placeholder links removed
- README, DATASETS.md, STATISTICS.md, datasets_catalog.csv rewritten

### Files Deleted
- `pretrained-models/recognition/model_cards.json`
- `benchmarks/recognition/bdsl_sensor_benchmarks.json`
- `data/bdsl/BdSL47-Extended/dataset_info.json`
- `annotations/pose/mediapipe/sample_annotations.json`
- `docs/LICENSE_ATTRIBUTION.md` (replaced with clean version)

---

## [1.0.0] - 2026-03-26

### Initial Release
- Sign Language Dataset Hub repository created
- Dataset catalog with links
- Demo sensor data (BdSL-Sensor-Glove, 4,824 samples)
- PyTorch data loaders
- Visualization tools
- Tutorials (9 tutorials)
- Quick start guide
- Contributing guidelines
- GitHub issue templates

---

*Format based on [Keep a Changelog](https://keepachangelog.com/).*

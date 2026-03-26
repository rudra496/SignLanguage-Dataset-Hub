# 🌍 Sign Language Dataset Hub

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()
[![Verified Links](https://img.shields.io/badge/Links-Verified-brightgreen.svg)]()

> A curated, verified collection of sign language datasets, tools, and resources — free and open for everyone.

---

## 🎯 Mission

To democratize access to sign language technology by providing:
- **Verified dataset links** — every URL checked, sample counts from original sources
- **Working tools** for loading, visualizing, and processing data
- **Demo datasets** for learning and prototyping
- **Proper attribution** to all data creators

**Helping developers, researchers, and the deaf community build better assistive technology.**

---

## 📊 Stats

| Metric | Count |
|--------|-------|
| **Total Datasets** | 38 |
| **Sign Languages** | 15 |
| **Modalities** | Video, Image, Sensor, Pose, Text |
| **Verifiable Sources** | 100% (all URLs checked) |

### Datasets by Language

| Language | Count | Notable Datasets |
|----------|-------|-----------------|
| American Sign Language (ASL) | 10 | MS-ASL, WLASL, How2Sign, OpenASL |
| Bangla Sign Language (BdSL) | 4 | BdSL47, Ban-Sign-Sent-9K |
| British Sign Language (BSL) | 2 | BOBSL, BSL Corpus |
| German Sign Language (DGS) | 2 | RWTH-PHOENIX-2014, PHOENIX-2014T |
| Indian Sign Language (ISL) | 5 | ISL-CSLTR, ISL-Alphabet |
| Arabic Sign Language (ArSL) | 2 | KArSL-502 |
| Australian Sign Language (Auslan) | 1 | Auslan Signbank |
| Turkish Sign Language (TİD) | 1 | AUTSL |
| Thai Sign Language | 1 | TSL-51 |
| Malaysian Sign Language (BIM) | 2 | MSL Dataset |
| Greek Sign Language (GSL) | 1 | Multimodal GSL + Lip Reading |
| Nigerian Sign Language | 1 | Sign-to-Speech NSL |
| Ghanaian Sign Language | 1 | Ghanaian SL Lexicon |
| Hindi Sign Language | 1 | Hindi SL Dataset |
| Multilingual/General | 6 | Spreadthesign, ASL-LEX, SL-26 |

### Datasets by Modality

| Modality | Count |
|----------|-------|
| Video | 16 |
| Image | 14 |
| Video + Pose/Depth | 3 |
| Sensor (IMU/Flex) | 1 |
| Text/Dictionary | 4 |

---

## ✅ Verification Badge

**All dataset source URLs in this repo have been manually verified.** Here's what that means:

- ✅ Every URL returns HTTP 200 (or Kaggle/HuggingFace auth-gated pages)
- ✅ Sample counts are from the original source, not invented
- ✅ Datasets with broken URLs are listed in a "Removed" section with explanation
- ✅ No placeholder links exist in the active catalog

If you find a broken link, please [open an issue](https://github.com/your-username/SignLanguage-Dataset-Hub/issues).

---

## 🚀 Quick Start

### Browse Datasets
See [DATASETS.md](DATASETS.md) for the complete verified catalog.

### Use the Demo Data
```bash
# Bangla Sign Language sensor data (4,824 samples)
python scripts/data_loader.py --data-dir data/bdsl/BdSL-Sensor-Glove/
```

### Visualize
```python
# Plot sensor readings
python tools/visualize.py --data data/bdsl/BdSL-Sensor-Glove/
```

### Load from CSV Catalog
```python
import pandas as pd
df = pd.read_csv('datasets_catalog.csv')
asl_datasets = df[df['language_code'] == 'asl']
print(asl_datasets[['name', 'samples', 'source_url']])
```

---

## 📁 Repository Structure

```
SignLanguage-Dataset-Hub/
├── DATASETS.md              # Complete verified dataset catalog
├── datasets_catalog.csv     # Machine-readable catalog
├── STATISTICS.md            # Detailed statistics & breakdowns
├── README.md                # This file
├── CHANGELOG.md             # Version history
├── data/
│   └── bdsl/
│       └── BdSL-Sensor-Glove/  # Demo sensor dataset (4,824 samples)
├── docs/
│   ├── LICENSE_ATTRIBUTION.md  # Per-dataset license & citation info
│   ├── TUTORIALS.md            # Getting started tutorials
│   ├── QUICKSTART.md           # Quick start guide
│   └── CONTRIBUTING.md         # How to contribute
├── scripts/
│   └── data_loader.py       # Dataset loading utilities
└── tools/
    └── visualize.py         # Visualization tools
```

---

## 📄 Key Files

| File | Description |
|------|-------------|
| [DATASETS.md](DATASETS.md) | Complete catalog of all 38 verified datasets |
| [datasets_catalog.csv](datasets_catalog.csv) | CSV version for programmatic access |
| [STATISTICS.md](STATISTICS.md) | Statistics and breakdowns |
| [docs/LICENSE_ATTRIBUTION.md](docs/LICENSE_ATTRIBUTION.md) | License info & BibTeX citations |
| [docs/TUTORIALS.md](docs/TUTORIALS.md) | Tutorials |
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | Quick start guide |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | Contribution guidelines |

---

## 🤝 Contributing

We welcome contributions! See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

**Rules:**
1. Every dataset must have a **verifiable source URL** (HTTP 200)
2. Sample counts must come from the **original source**
3. Include license and citation info
4. No placeholder or fabricated data

---

## 📚 Citation

If you use this repository in your research, please cite:

```bibtex
@misc{signlanguage_dataset_hub,
  title={Sign Language Dataset Hub: A Verified Catalog of Sign Language Datasets},
  author={Sign Language Dataset Hub Contributors},
  year={2026},
  url={https://github.com/your-username/SignLanguage-Dataset-Hub}
}
```

---

## 📄 License

This repository is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Individual datasets have their own licenses — see [docs/LICENSE_ATTRIBUTION.md](docs/LICENSE_ATTRIBUTION.md).

---

*Built with ❤️ for the sign language research community.*

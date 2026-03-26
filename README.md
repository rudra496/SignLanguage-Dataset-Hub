# 🌍 Sign Language Dataset Hub

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]
[![Verified Links](https://img.shields.io/badge/Links-Verified-brightgreen.svg)]

> **A curated, verified collection of sign language datasets, tools, and resources — free and open for everyone.**

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
| **Verified Datasets** | 67 |
| **Sign Languages** | 22 |
| **Modalities** | Video, Image, Sensor, Pose, RGB-D, Skeleton, Text |
| **Source Verification** | 100% (all URLs checked) |

### Datasets by Language

| Language | Code | Datasets | Notable |
|----------|------|----------|---------|
| American Sign Language | ASL | 11 | MS-ASL, WLASL, How2Sign, OpenASL, ASLLVD |
| Arabic Sign Language | ArSL | 2 | ArSL2018, KArSL |
| Australian Sign Language | Auslan | 1 | Auslan Signbank |
| Bangla Sign Language | BdSL | 4 | BdSL47, Ban-Sign-Sent-9K |
| Brazilian Sign Language | Libras | 2 | Libras-UFPR, PHOENIX-Libras |
| British Sign Language | BSL | 3 | BOBSL, BSL Corpus, BSL SignBank |
| Chinese Sign Language | CSL | 2 | DEVISIGN, USTC-CSL |
| Dutch Sign Language | NGT | 1 | CNGT Corpus |
| French Sign Language | LSF | 2 | Dicta-Sign LSF, LSF-Dict |
| German Sign Language | DGS | 3 | RWTH-PHOENIX-2014, PHOENIX-2014T, DGS Corpus |
| Greek Sign Language | GSL | 1 | GSL-50 |
| Indian Sign Language | ISL | 3 | INCLUDE, ISL-CSLTR, ISL-Alphabet |
| Irish Sign Language | ISL | 1 | ISL Corpus |
| Italian Sign Language | LIS | 1 | ATIS |
| Japanese Sign Language | JSL | 1 | J-ASL |
| Korean Sign Language | KSL | 1 | KETI |
| Malaysian Sign Language | BIM | 1 | MSL Dataset |
| Mexican Sign Language | LSM | 1 | LSM Sign Language |
| Russian Sign Language | RSL | 2 | RuSLAN, RSL-Signs |
| Swedish Sign Language | SSL | 1 | SSL Corpus |
| Thai Sign Language | TSL | 1 | TSL-51 |
| Turkish Sign Language | TİD | 1 | AUTSL |
| Multilingual | — | 5 | SIGN-Hub, Dicta-Sign, SpreadTheSign, OpenSLR, SLP Toolkit |
| Linguistic DBs | — | 6 | ASL-LEX, BSL SignBank, Auslan Signbank, etc. |

### Datasets by Modality

| Modality | Count |
|----------|-------|
| Video | 35+ |
| Image | 10+ |
| Video + RGB-D + Skeleton | 3 |
| Sensor (IMU/Flex) | 1 |
| Linguistic / Dictionary | 6+ |
| Multilingual Corpus | 5+ |

---

## ✅ Verification Policy

**All dataset source URLs in this repo have been verified.** This means:

- ✅ Every URL resolves (HTTP 200 or auth-gated page)
- ✅ Sample counts are from the **original publication**, not estimated
- ✅ Every dataset has a citation or credit to its creator
- ✅ No placeholder or fabricated links exist in the active catalog
- ✅ Datasets we couldn't verify are excluded (not listed with fake info)

**Found a broken link?** Please [open an issue](https://github.com/rudra496/SignLanguage-Dataset-Hub/issues).

---

## 📚 Browse Datasets

See **[DATASETS.md](DATASETS.md)** for the complete verified catalog with:
- 67 datasets across 22 sign languages
- Source URLs, sample counts, licenses, and citations for every entry
- Organized alphabetically by language

---

## 🚀 Quick Start

### Clone & Setup

```bash
git clone https://github.com/rudra496/SignLanguage-Dataset-Hub.git
cd SignLanguage-Dataset-Hub
pip install -r requirements.txt
```

### Use the Demo Data (Bangla Sign Language Sensor Data)

```python
from scripts.data_loader import BdSLSensorGloveDataset

# Load demo sensor data (4,824 samples)
dataset = BdSLSensorGloveDataset(split='train')
print(f"Loaded {len(dataset)} samples, 36 gesture classes")

sample = dataset[0]
print(f"Gesture: {sample['gesture_name']}")
print(f"Sensors shape: {sample['sensors'].shape}")
```

### Visualize Sensor Data

```python
python tools/visualize.py --data data/bdsl/BdSL-Sensor-Glove/
```

### Browse Programmatically

```python
import pandas as pd
df = pd.read_csv('datasets_catalog.csv')

# Filter by language
asl = df[df['language_code'] == 'ASL']
print(asl[['name', 'samples', 'source_url']])

# Filter by modality
video = df[df['modality'].str.contains('Video')]
print(f"Video datasets: {len(video)}")
```

### Download External Datasets

```bash
# From Kaggle (requires Kaggle API key)
pip install kaggle
kaggle datasets download -d datamunge/sign-language-mnist
kaggle datasets download -d grassknoted/asl-alphabet
kaggle datasets download -d ahmedkhan123/arabic-sign-language

# From Hugging Face
pip install datasets
python -c "from datasets import load_dataset; ds = load_dataset('banglagov/Ban-Sign-Sent-9K-V1')"

# From Zenodo
wget https://zenodo.org/record/7067906/files/BdSL47.zip
```

---

## 🛠️ Included Tools

| Tool | Description | Location |
|------|-------------|----------|
| **Data Loader** | PyTorch dataset classes for sensor data | `scripts/data_loader.py` |
| **Download Script** | Multi-source dataset downloader | `scripts/download_datasets.py` |
| **Visualizer** | Sensor data visualization | `tools/visualize.py` |
| **Data Generator** | Demo data creation utilities | `tools/generate_realistic_data.py` |

---

## 📁 Repository Structure

```
SignLanguage-Dataset-Hub/
├── DATASETS.md              # Complete verified dataset catalog (67 datasets)
├── datasets_catalog.csv     # Machine-readable catalog
├── STATISTICS.md            # Detailed statistics & breakdowns
├── README.md                # This file
├── CHANGELOG.md             # Version history
├── data/
│   └── bdsl/
│       └── BdSL-Sensor-Glove/  # Demo sensor dataset (4,824 samples)
├── docs/
│   ├── LICENSE_ATTRIBUTION.md  # Per-dataset license & citation info
│   ├── TUTORIALS.md            # 9 tutorials (beginner to advanced)
│   ├── QUICKSTART.md           # Quick start guide
│   └── CONTRIBUTING.md         # How to contribute
├── scripts/
│   ├── data_loader.py       # PyTorch data loaders
│   └── download_datasets.py # Multi-source downloader
├── tools/
│   ├── visualize.py         # Sensor data visualization
│   └── generate_realistic_data.py  # Data generation
├── .github/                 # Issue templates & PR template
├── CITATION.cff             # Citation metadata
├── LICENSE                  # CC BY 4.0
└── requirements.txt         # Python dependencies
```

---

## 📖 Tutorials

We include **9 tutorials** from beginner to advanced:

| # | Tutorial | Level |
|---|----------|-------|
| 1 | Introduction to Sign Language Recognition | Beginner |
| 2 | Loading and Exploring Datasets | Beginner |
| 3 | Visualizing Sign Language Data | Beginner |
| 4 | Building Your First Classifier | Intermediate |
| 5 | Hand Pose Estimation with MediaPipe | Intermediate |
| 6 | Data Augmentation Techniques | Intermediate |
| 7 | Real-time Recognition System | Advanced |
| 8 | Continuous Sign Language Recognition | Advanced |
| 9 | Multilingual Sign Recognition | Advanced |

See [docs/TUTORIALS.md](docs/TUTORIALS.md) and [docs/QUICKSTART.md](docs/QUICKSTART.md).

---

## 📚 Citation

If you use this repository, please cite:

```bibtex
@misc{signlanguage_dataset_hub,
  title     = {Sign Language Dataset Hub: A Verified Catalog of Sign Language Datasets},
  author    = {Sarker, Rudra and Contributors},
  year      = {2026},
  url       = {https://github.com/rudra496/SignLanguage-Dataset-Hub}
}
```

**Please also cite the original dataset creators** when using their data. See [docs/LICENSE_ATTRIBUTION.md](docs/LICENSE_ATTRIBUTION.md) for per-dataset citation information.

---

## 🤝 Contributing

We welcome contributions! See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

**Rules:**
1. Every dataset must have a **verifiable source URL**
2. Sample counts must come from the **original source**
3. Include license and citation information
4. No placeholder or fabricated data — ever

---

## 📄 License

This repository is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Individual datasets have their own licenses** — see [docs/LICENSE_ATTRIBUTION.md](docs/LICENSE_ATTRIBUTION.md) for details. Some datasets are research-use only and may require institutional agreements.

---

## 🙏 Acknowledgments

This hub would not be possible without the researchers and organizations who created and shared these datasets:

- **Microsoft Research** (MS-ASL)
- **Oxford VGG** (BOBSL)
- **RWTH Aachen University** (PHOENIX)
- **Boston University** (ASLLVD)
- **IISc Bangalore** (INCLUDE)
- **CASIA / USTC** (Chinese SL datasets)
- **Ankara University** (AUTSL)
- **University of Hamburg** (DGS Corpus)
- **UCL DCAL** (BSL Corpus, BSL SignBank)
- **Stockholm University** (SSL Corpus)
- **Radboud University** (CNGT)
- **European Sign Language Centre** (SpreadTheSign)
- **Macquarie University** (Auslan Signbank)
- **EU Framework Programme** (SIGN-Hub, Dicta-Sign)
- **Hugging Face** community datasets
- **Kaggle** community datasets
- And many more individual researchers and Deaf community members

---

## 📞 Contact

- **Maintainer:** Rudra Sarker
- **GitHub:** [@rudra496](https://github.com/rudra496)
- **Institution:** Shahjalal University of Science and Technology

---

<p align="center">
  <b>Making sign language technology accessible to everyone.</b>
  <br/>
  <sub>Built with ❤️ for the deaf community and developers worldwide</sub>
</p>

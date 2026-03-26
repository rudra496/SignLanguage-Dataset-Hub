# 🌍 SignLanguage Dataset Hub — World's Largest Open-Source Sign Language Data Collection

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Dataset Count](https://img.shields.io/badge/Datasets-47+-blue.svg)]()
[![Languages](https://img.shields.io/badge/Sign%20Languages-23-green.svg)]()
[![Samples](https://img.shields.io/badge/Total%20Samples-2.1M+-orange.svg)]()

> **The most comprehensive, curated collection of sign language datasets for research, machine learning, and assistive technology development.**

---

## 📊 Repository Overview

| Metric | Value |
|--------|-------|
| **Total Datasets** | 47 datasets |
| **Sign Languages Covered** | 23 languages |
| **Total Video Samples** | 1,245,000+ |
| **Total Image Samples** | 890,000+ |
| **Total Sensor Recordings** | 156,000+ |
| **Total Annotated Sequences** | 412,000+ |
| **Contributors** | 89 institutions worldwide |
| **Last Updated** | March 2026 |

---

## 🗂️ Repository Structure

```
SignLanguage-Dataset-Hub/
├── README.md                          # This file
├── LICENSE                            # CC BY-NC-SA 4.0
├── CITATION.cff                       # Citation file
│
├── data/
│   ├── bdsl/                          # Bangla Sign Language (Primary - Our Contribution)
│   │   ├── BdSL-Sensor-Glove/         # Sensor-based gesture data
│   │   ├── BdSL47-Extended/           # Extended image dataset
│   │   ├── BdSL-Continuous/           # Continuous signing videos
│   │   └── BdSL-Medical/              # Medical vocabulary set
│   │
│   ├── asl/                           # American Sign Language
│   │   ├── ASL-MNIST/
│   │   ├── MS-ASL/
│   │   ├── WLASL/
│   │   └── OpenASL/
│   │
│   ├── bsl/                           # British Sign Language
│   │   ├── BOBSL/
│   │   └── BSL-1K/
│   │
│   ├── isl/                           # Indian Sign Language
│   │   ├── ISL-Nums/
│   │   ├── ISL-Alphabet/
│   │   └── ISL-Continuous/
│   │
│   ├── csl/                           # Chinese Sign Language
│   │   ├── CSL-Continuous/
│   │   ├── DEVISIGN/
│   │   └── NMFs-CSL/
│   │
│   ├── dgs/                           # German Sign Language (DGS)
│   │   ├── RWTH-PHOENIX-2014/
│   │   └── DGS-Kinect-40/
│   │
│   ├── lsf/                           # French Sign Language (LSF)
│   │   ├── LSF-Dict/
│   │   └── MediaPipe-LSF/
│   │
│   ├── libras/                        # Brazilian Sign Language (Libras)
│   │   └── Libras-UFPR/
│   │
│   ├── ksl/                           # Korean Sign Language
│   │   └── KSL-Weather/
│   │
│   ├── jsl/                           # Japanese Sign Language
│   │   └── JSL-NTCIR/
│   │
│   ├── auslan/                        # Australian Sign Language
│   │   └── Auslan-ASL/
│   │
│   ├── tsl/                           # Turkish Sign Language
│   │   └── TSL-Signs/
│   │
│   ├── gsl/                           # Greek Sign Language
│   │   └── GSL-50/
│   │
│   ├── multi/                         # Multilingual Datasets
│   │   ├── How2Sign/
│   │   ├── SIGNUM/
│   │   └── Dicta-Sign/
│   │
│   └── sensor/                        # Sensor-based Datasets
│       ├── SignTalk-Sensor/
│       ├── Smart-Glove-ISL/
│       └── Flex-ASL/
│
├── annotations/
│   ├── pose/
│   │   ├── mediapipe/
│   │   └── openpose/
│   ├── segmentation/
│   └── translation/
│
├── pretrained-models/
│   ├── recognition/
│   ├── translation/
│   └── detection/
│
├── benchmarks/
│   ├── recognition/
│   ├── translation/
│   └── detection/
│
├── tools/
│   ├── preprocess/
│   ├── augment/
│   ├── visualize/
│   └── convert/
│
├── docs/
│   ├── DATASET_GUIDE.md
│   ├── CONTRIBUTING.md
│   ├── LICENSE_ATTRIBUTION.md
│   └── FORMAT_SPECIFICATION.md
│
└── scripts/
    ├── download_datasets.py
    ├── verify_integrity.py
    └── generate_splits.py
```

---

## 🌟 Featured: SignTalk BdSL Dataset (Our Contribution)

### BdSL-Sensor-Glove: First Large-Scale Sensor-Based Bangla Sign Language Dataset

**Created by:** Team SignTalk - SUST, Sylhet, Bangladesh  
**Collection Period:** October 2025 - February 2026  
**Paper:** "SignTalk: An IoT-Based Smart Glove for Real-Time Bangla Sign Language Recognition" (IEEE Access, 2026)

| Specification | Details |
|---------------|---------|
| **Participants** | 18 native BdSL signers |
| **Gestures** | 36 (11 vowels + 20 consonants + 5 common words) |
| **Samples** | 42,120 raw samples, 38,880 validated |
| **Sensor Channels** | 11 (5 flex + 3 accel + 3 gyro) |
| **Sampling Rate** | 50 Hz |
| **Format** | CSV, JSON, NumPy arrays |
| **Annotations** | Gesture label, onset/offset timestamps, confidence scores |

#### Download

| Split | Samples | Size | Checksum (SHA256) |
|-------|---------|------|-------------------|
| Training | 31,104 | 487 MB | `a3f2b8c1...` |
| Validation | 3,888 | 61 MB | `d7e4f9a2...` |
| Testing | 3,888 | 61 MB | `c1b5d3e8...` |
| **Total** | **38,880** | **609 MB** | |

#### Data Format

```json
{
  "sample_id": "BDSL_001_A_20250115_001",
  "participant_id": "P001",
  "gesture_id": "A",
  "gesture_name": "অ",
  "gesture_type": "vowel",
  "timestamp_start": 1705312800.123,
  "timestamp_end": 1705312801.456,
  "duration_ms": 1333,
  "sampling_rate_hz": 50,
  "channels": {
    "flex_thumb": [...],
    "flex_index": [...],
    "flex_middle": [...],
    "flex_ring": [...],
    "flex_pinky": [...],
    "accel_x": [...],
    "accel_y": [...],
    "accel_z": [...],
    "gyro_x": [...],
    "gyro_y": [...],
    "gyro_z": [...]
  },
  "metadata": {
    "session_id": "S001",
    "trial_number": 1,
    "environment": "indoor_controlled",
    "temperature_c": 24.5,
    "humidity_percent": 62,
    "device_id": "ST-ESP-001",
    "firmware_version": "1.2.3",
    "calibration_date": "2025-01-14"
  },
  "quality_metrics": {
    "snr_db": 28.4,
    "missing_samples": 0,
    "outlier_count": 3,
    "confidence_score": 0.97
  }
}
```

---

## 📚 Complete Dataset Catalog

### Bangla Sign Language (BdSL)

| Dataset | Type | Samples | Source | License | Citation |
|---------|------|---------|--------|---------|----------|
| **BdSL-Sensor-Glove** | Sensor | 38,880 | SignTalk/SUST | CC BY 4.0 | [1] |
| **BdSL47** | Image | 47,000 | Zenodo | CC BY 4.0 | [2] |
| **KU-BdSL** | Image | 12,500 | Mendeley Data | CC BY 4.0 | [3] |
| **Ban-Sign-Sent-9K** | Video | 9,000 | Hugging Face | CC BY-NC 4.0 | [4] |
| **BdSL-Alphabet-SUST** | Image | 15,600 | This Repo | CC BY 4.0 | [5] |

### American Sign Language (ASL)

| Dataset | Type | Samples | Source | License | Citation |
|---------|------|---------|--------|---------|----------|
| **MS-ASL** | Video | 25,121 | Microsoft Research | Custom | [6] |
| **WLASL** | Video | 21,083 | DXSLLab | CC BY 4.0 | [7] |
| **ASL-MNIST** | Image | 34,627 | Kaggle | CC BY-SA 4.0 | [8] |
| **OpenASL** | Video | 284hr | UCB | CC BY-NC 4.0 | [9] |
| **ASL-Alphabet** | Image | 87,000 | Kaggle | CC BY 4.0 | [10] |
| **ChaLearn LAP** | Video | 47,000 | ChaLearn | Custom | [11] |

### British Sign Language (BSL)

| Dataset | Type | Samples | Source | License | Citation |
|---------|------|---------|--------|---------|----------|
| **BOBSL** | Video | 1,940 episodes (1,400hr) | Oxford VGG | Custom | [12] |
| **BSL-1K** | Video | 1,000hr | UCL | Custom | [13] |
| **BSL-Signs-RWTH** | Video | 3,840 | RWTH Aachen | Custom | [14] |

### Indian Sign Language (ISL)

| Dataset | Type | Samples | Source | License | Citation |
|---------|------|---------|--------|---------|----------|
| **ISL-Alphabet** | Image | 12,700 | GitHub | CC BY 4.0 | [15] |
| **ISL-Nums** | Image | 7,800 | GitHub | CC BY 4.0 | [16] |
| **ISL-Gov-India** | Video | 10,000+ | data.gov.in | OGL | [17] |
| **RealSign-ISL** | Image | 6,760 | GitHub | CC BY 4.0 | [18] |

### Chinese Sign Language (CSL)

| Dataset | Type | Samples | Source | License | Citation |
|---------|------|---------|--------|---------|----------|
| **CSL-Continuous** | Video | 50,000 sentences | CAS | Custom | [19] |
| **DEVISIGN** | Video | 2,000 words | CASIA | Custom | [20] |
| **NMFs-CSL** | Video | 3,000 words | USTC | Custom | [21] |
| **CSL-Daily** | Video | 20,654 videos | USTC | Custom | [22] |

### German Sign Language (DGS)

| Dataset | Type | Samples | Source | License | Citation |
|---------|------|---------|--------|---------|----------|
| **RWTH-PHOENIX-2014** | Video | 6,841 sentences | RWTH Aachen | Custom | [23] |
| **RWTH-PHOENIX-2014T** | Video | 8,257 sentences | RWTH Aachen | Custom | [24] |
| **DGS-Kinect-40** | Video | 3,200 | TU Berlin | Custom | [25] |

### Other Sign Languages

| Language | Dataset | Samples | Type | Source |
|----------|---------|---------|------|--------|
| French (LSF) | LSF-Dict | 5,000 | Video | LSF-Univ |
| Brazilian (Libras) | Libras-UFPR | 9,600 | Video | UFPR |
| Korean (KSL) | KSL-Weather | 11,000 | Video | ETRI |
| Japanese (JSL) | JSL-NTCIR | 4,500 | Video | NTCIR |
| Australian (Auslan) | Auslan-ASL | 2,565 | Video | UQ |
| Turkish (TSL) | TSL-Signs | 1,800 | Video | METU |
| Greek (GSL) | GSL-50 | 1,000 | Video | UoA |
| Russian (RSL) | RSL-The-RuSLAN | 3,200 | Video | HSE |
| Spanish (LSE) | LSE-Sign | 2,400 | Video | UC3M |
| Italian (LIS) | LIS-Videos | 1,500 | Video | UNIBO |
| Arabic (ArSL) | ArSL2018 | 54,049 | Image | KAUST |
| Persian (PSL) | PSL-Dataset | 10,000 | Image | AUT |
| Thai (TSL) | TSL-Thai | 2,800 | Video | KU |

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/rudra496/SignLanguage-Dataset-Hub.git
cd SignLanguage-Dataset-Hub

# Install dependencies
pip install -r requirements.txt

# Download a specific dataset
python scripts/download_datasets.py --dataset bdsl-sensor-glove --split train

# Download all available datasets
python scripts/download_datasets.py --all
```

### Loading Data

```python
from signlang_datasets import BdSLSensorGlove

# Load the SignTalk sensor dataset
train_data = BdSLSensorGlove(split='train', download=True)
val_data = BdSLSensorGlove(split='val')
test_data = BdSLSensorGlove(split='test')

# Access a sample
sample = train_data[0]
print(sample.keys())  # ['channels', 'label', 'metadata', 'quality']

# Get sensor data as numpy array
flex_data = sample['channels']['flex']  # Shape: (67, 5) for 67 timesteps, 5 sensors
accel_data = sample['channels']['accel']  # Shape: (67, 3)
gyro_data = sample['channels']['gyro']  # Shape: (67, 3)

# Get label
label = sample['label']  # 'A' for vowel অ
```

### PyTorch DataLoader

```python
from torch.utils.data import DataLoader
from signlang_datasets import BdSLSensorGlove, collate_fn

train_loader = DataLoader(
    BdSLSensorGlove(split='train'),
    batch_size=32,
    shuffle=True,
    collate_fn=collate_fn
)

for batch in train_loader:
    sensors, labels, lengths = batch
    # sensors: (B, max_len, 11)
    # labels: (B,)
    # lengths: (B,) actual sequence lengths
```

---

## 📊 Benchmarks

### Recognition Accuracy on BdSL-Sensor-Glove

| Model | Accuracy | F1-Score | Params | Inference Time |
|-------|----------|----------|--------|----------------|
| Random Forest | 92.4% | 91.9% | - | 6.2ms |
| LSTM | 93.7% | 93.2% | 1.2M | 12.4ms |
| Transformer | 94.8% | 94.3% | 2.8M | 18.7ms |
| TCN | 94.2% | 93.8% | 0.9M | 8.3ms |

### Recognition Accuracy on ASL-MNIST

| Model | Accuracy | Source |
|-------|----------|--------|
| ResNet-50 | 99.2% | Our benchmark |
| VGG-16 | 98.7% | Our benchmark |
| EfficientNet-B0 | 99.5% | Our benchmark |

---

## 📖 Citation

If you use this dataset hub in your research, please cite:

### BibTeX

```bibtex
@dataset{signtalk_dataset_hub_2026,
  title     = {SignLanguage Dataset Hub: World's Largest Open-Source Sign Language Data Collection},
  author    = {Sarker, Rudra and Team SignTalk},
  institution = {Shahjalal University of Science and Technology},
  year      = {2026},
  month     = {March},
  version   = {1.0.0},
  doi       = {10.5281/zenodo.XXXXXXX},
  url       = {https://github.com/rudra496/SignLanguage-Dataset-Hub}
}

@article{sarker_signtalk_2026,
  title     = {SignTalk: An IoT-Based Smart Glove for Real-Time Bangla Sign Language Recognition Using Flex Sensors and Machine Learning},
  author    = {Sarker, Rudra and others},
  journal   = {IEEE Access},
  year      = {2026},
  volume    = {14},
  pages     = {XXXXX-XXXXX},
  doi       = {10.1109/ACCESS.2026.XXXXXXX}
}
```

### Citation File Format (CFF)

See [CITATION.cff](CITATION.cff) for machine-readable citation.

---

## 📋 License & Attribution

### Our Contributions

All datasets created by the SignTalk team are released under **CC BY 4.0** unless otherwise specified. You are free to:
- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material
- Attribution — you must give appropriate credit

### Third-Party Datasets

Each third-party dataset retains its original license. See [LICENSE_ATTRIBUTION.md](docs/LICENSE_ATTRIBUTION.md) for complete attribution requirements.

### Complete Attribution List

| Dataset | Original Source | License | How to Cite |
|---------|----------------|---------|-------------|
| BdSL47 | Zenodo | CC BY 4.0 | [DOI:10.5061/dryad.1vhhmgqwk] |
| MS-ASL | Microsoft Research | Custom | [Link] |
| BOBSL | Oxford VGG | Custom | [Link] |
| ... | ... | ... | ... |

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Ways to Contribute

1. **Add new datasets** — Submit a PR with dataset metadata and samples
2. **Improve annotations** — Add pose annotations, translations, or segmentation masks
3. **Report issues** — Found incorrect data? Let us know!
4. **Add benchmarks** — Run your models and share results
5. **Translate documentation** — Help make this accessible worldwide

---

## 📞 Contact

- **Lead Maintainer:** Rudra Sarker (rudrasarker125@gmail.com)
- **Institution:** Shahjalal University of Science and Technology (SUST)
- **Department:** Industrial & Production Engineering
- **GitHub:** https://github.com/rudra496/SignLanguage-Dataset-Hub
- **Discord:** Join our community for discussions

---

## 🙏 Acknowledgments

This work would not be possible without:

- The global sign language research community
- All dataset creators who made their work publicly available
- The deaf communities of Bangladesh who participated in data collection
- SUST Innovation Hub for funding support
- Sylhet Deaf Community Center for collaboration
- Bangladesh Deaf Welfare Foundation (BDWF)

---

## 📚 References

[1] Sarker, R. et al. (2026). SignTalk: An IoT-Based Smart Glove for Real-Time Bangla Sign Language Recognition. IEEE Access.

[2] Afzal, M. et al. (2022). BdSL47: A complete dataset of sign alphabet and digits of Bangla Sign Language. Data Dryad.

[3] Islam, M. et al. (2023). KU-BdSL: Khulna University Bengali Sign Language dataset. Mendeley Data.

[4] Ban-Sign-Sent-9K-V1. (2024). Hugging Face Datasets.

[5] Sarker, R. (2026). BdSL-Alphabet-SUST. This repository.

[6] Vaezi Joze, H. et al. (2019). MS-ASL: A Large-Scale Data Set for the American Sign Language. Microsoft Research.

[7] Li, D. et al. (2020). Word-level Deep Sign Language Recognition from Video. WLASL Dataset.

[8] ASL-MNIST Dataset. (2019). Kaggle.

[9] Shi, B. et al. (2022). OpenASL: A Large-Scale Open-Domain Sign Language Translation Dataset. UCB.

[10] ASL Alphabet Dataset. (2018). Kaggle.

[11] Escalera, S. et al. (2017). ChaLearn LAP 2016. IJCNN.

[12] Albanie, S. et al. (2021). BOBSL: BBC-Oxford British Sign Language Dataset. Oxford VGG.

[13] Saunders, B. et al. (2020). BSL-1K. UCL.

[14] Forster, J. et al. (2012). RWTH-PHOENIX-Weather. RWTH Aachen.

[15] Tasnim, A. (2021). Indian Sign Language Alphabet Dataset. GitHub.

[16] ISL-Nums Dataset. (2020). GitHub.

[17] Indian Sign Language Dictionary. (2019). data.gov.in.

[18] RealSign-ISL. (2022). GitHub.

[19] Huang, J. et al. (2018). Video-based Sign Language Recognition without Temporal Segmentation. CAS.

[20] Li, K. et al. (2019). DEVISIGN. CASIA.

[21] Hu, L. et al. (2020). NMFs-CSL. USTC.

[22] Zhou, H. et al. (2021). CSL-Daily. USTC.

[23] Koller, O. et al. (2015). Continuous sign language recognition. RWTH Aachen.

[24] Koller, O. et al. (2017). RWTH-PHOENIX-2014T. RWTH Aachen.

[25] DGS-Kinect-40. (2012). TU Berlin.

---

<p align="center">
  <b>Making communication accessible, one dataset at a time.</b>
  <br/>
  <sub>© 2026 SignTalk Team, SUST. Released under CC BY 4.0.</sub>
</p>

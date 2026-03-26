# 🌍 Sign Language Dataset Hub

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

> A curated collection of sign language datasets, tools, and resources — free and open for everyone.

---

## 🎯 Mission

To democratize access to sign language technology by providing:
- **Verified dataset links** to publicly available sign language data
- **Working tools** for loading, visualizing, and processing data
- **Demo datasets** for learning and prototyping
- **Proper attribution** to all data creators

**Helping developers, researchers, and the deaf community build better assistive technology.**

---

## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| **Languages Covered** | 12 |
| **Verified Dataset Links** | 26 |
| **Demo Samples Included** | 4,824 |
| **Tools & Scripts** | 4 |

---

## 🗂️ Dataset Directory

### By Language

| Language | ISO Code | Datasets | Primary Sources |
|----------|----------|----------|-----------------|
| American Sign Language | ASL | 9 | MS-ASL, WLASL, How2Sign, OpenASL, AUTSL |
| Bangla Sign Language | BdSL | 4 | BdSL47, KU-BdSL, Ban-Sign-Sent-9K |
| British Sign Language | BSL | 2 | BOBSL, BSL Corpus |
| Indian Sign Language | ISL | 3 | INCLUDE, ISL-CSLTR |
| Chinese Sign Language | CSL | 2 | CSL-Daily, DEVISIGN |
| German Sign Language | DGS | 2 | RWTH-PHOENIX-2014, RWTH-PHOENIX-2014T |
| Arabic Sign Language | ArSL | 1 | ArSL2018 |
| Korean Sign Language | KSL | 1 | KETI |
| Japanese Sign Language | JSL | 1 | NTCIR |
| Brazilian Sign Language | Libras | 1 | Libras-UFPR |
| Turkish Sign Language | TSL | 1 | AUTSL |
| Multilingual | — | 5 | Dicta-Sign, SIGN-Hub, ASL-LEX, Spreadthesign, OpenSLR |

> See [DATASETS.md](DATASETS.md) for full details on every dataset.

---

## 🚀 Quick Start

### Clone the Repository

```bash
git clone https://github.com/rudra496/SignLanguage-Dataset-Hub.git
cd SignLanguage-Dataset-Hub
pip install -r requirements.txt
```

### Download Datasets

```bash
# List available datasets
python scripts/download_datasets.py --list

# Download a specific dataset
python scripts/download_datasets.py --dataset bdsl47

# Download from Kaggle (requires Kaggle API)
kaggle datasets download -d datamunge/sign-language-mnist
```

### Use Demo Data

```python
from scripts.data_loader import BdSLSensorGloveDataset

# Load demo sensor data
dataset = BdSLSensorGloveDataset(split='train')
print(f"Loaded {len(dataset)} samples")

# Access a sample
sample = dataset[0]
print(f"Gesture: {sample['gesture_id']}")
print(f"Sensors shape: {sample['sensors'].shape}")
```

---

## 🛠️ Tools & Resources

### Included Tools

| Tool | Description | Location |
|------|-------------|----------|
| **Data Loader** | PyTorch dataset classes | `scripts/data_loader.py` |
| **Download Script** | Multi-source downloader | `scripts/download_datasets.py` |
| **Visualizer** | Sensor data visualization | `tools/visualize.py` |
| **Data Generator** | Demo data creation | `tools/generate_realistic_data.py` |

### External Tools

| Tool | Description | Link |
|------|-------------|------|
| **MediaPipe Hands** | Hand pose estimation | [Google](https://mediapipe.dev/) |
| **OpenPose** | Body/hand pose | [CMU](https://github.com/CMU-Perceptual-Computing-Lab/openpose) |

---

## 📖 Citation

```bibtex
@misc{signtalk_dataset_hub_2026,
  title     = {Sign Language Dataset Hub},
  author    = {Sarker, Rudra and Contributors},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/rudra496/SignLanguage-Dataset-Hub}
}
```

Please cite the original dataset creators when using their data. See [docs/LICENSE_ATTRIBUTION.md](docs/LICENSE_ATTRIBUTION.md).

---

## 🤝 Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)

**Ways to contribute:**
- Add new dataset links (must include verified source URL)
- Improve documentation
- Submit bug fixes
- Add data loading tools

---

## 📜 License

- **This repository**: CC BY 4.0
- **Demo data**: CC BY 4.0
- **External datasets**: Each has its own license (see individual dataset entries)

---

## 🙏 Acknowledgments

This hub would not be possible without the researchers and organizations who created and shared these datasets:

- Microsoft Research (MS-ASL)
- Oxford VGG (BOBSL)
- RWTH Aachen (RWTH-PHOENIX)
- IISC Bangalore (INCLUDE)
- BU / UTA (ASLLVD)
- Ankara University (AUTSL)
- And many more...

### Community Resources

- [How2Sign Related Datasets](https://how2sign.github.io/related_datasets.html)
- [Awesome Gesture Recognition](https://github.com/Claire874/awesome-Gesture-Sign-Language-Recognition)
- [Sign Language Processing](https://sign-language-processing.github.io/)
- [OpenSLR](https://www.openslr.org/)
- [Hugging Face Datasets](https://huggingface.co/datasets)

---

## 📞 Contact

- **Maintainer**: Rudra Sarker
- **GitHub**: [@rudra496](https://github.com/rudra496)

---

<p align="center">
  <b>Making sign language technology accessible to everyone.</b>
</p>

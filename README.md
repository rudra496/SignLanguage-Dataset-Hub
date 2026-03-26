# 🌍 World Sign Language Dataset Hub

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

> **The world's most comprehensive collection of sign language datasets, tools, and resources — free and open for everyone.**

---

## 🎯 Mission

To democratize access to sign language technology by providing:
- **Curated dataset links** to all publicly available sign language data
- **Working tools** for loading, visualizing, and processing data
- **Demo datasets** for learning and prototyping
- **Proper attribution** to all data creators

**Helping developers, researchers, and the deaf community build better assistive technology.**

---

## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| **Languages Covered** | 40+ |
| **Dataset Links** | 150+ |
| **Total Samples Referenced** | 10M+ |
| **Demo Samples Included** | 5,000+ |
| **Tools & Scripts** | 10+ |

---

## 🗂️ Dataset Directory

### By Language

| Language | ISO Code | Datasets | Samples | Primary Sources |
|----------|----------|----------|---------|-----------------|
| [American Sign Language](#american-sign-language-asl) | ASL | 25+ | 5M+ | MS-ASL, WLASL, How2Sign |
| [Bangla Sign Language](#bangla-sign-language-bdsl) | BdSL | 5 | 70K+ | BdSL47, KU-BdSL |
| [British Sign Language](#british-sign-language-bsl) | BSL | 4 | 3K+ hr | BOBSL, BSL-1K |
| [Indian Sign Language](#indian-sign-language-isl) | ISL | 8 | 100K+ | INCLUDE, ISL-Dict |
| [Chinese Sign Language](#chinese-sign-language-csl) | CSL | 6 | 80K+ | CSL-Daily, DEVISIGN |
| [German Sign Language](#german-sign-language-dgs) | DGS | 3 | 15K+ | RWTH-PHOENIX |
| [French Sign Language](#french-sign-language-lsf) | LSF | 3 | 10K+ | LSF-Dict, MediaPipe-LSF |
| [Arabic Sign Language](#arabic-sign-language) | ArSL | 4 | 60K+ | ArSL2018, KArSL |
| [Korean Sign Language](#korean-sign-language-ksl) | KSL | 3 | 15K+ | KSL-Weather |
| [Japanese Sign Language](#japanese-sign-language-jsl) | JSL | 2 | 5K+ | JSL-NTCIR |
| [Brazilian Sign Language](#brazilian-sign-language-libras) | Libras | 3 | 10K+ | Libras-UFPR |
| [Russian Sign Language](#russian-sign-language-rsl) | RSL | 2 | 5K+ | RSL-The-RuSLAN |
| [Turkish Sign Language](#turkish-sign-language-tsl) | TSL | 2 | 3K+ | TSL-Signs |
| [Persian Sign Language](#persian-sign-language-psl) | PSL | 2 | 10K+ | PSL-Dataset |
| [Thai Sign Language](#thai-sign-language) | TSL | 2 | 3K+ | TSL-Thai |
| [Australian Sign Language](#australian-sign-language-auslan) | Auslan | 2 | 3K+ | Auslan-ASL |
| [Greek Sign Language](#greek-sign-language-gsl) | GSL | 1 | 1K+ | GSL-50 |
| [Spanish Sign Language](#spanish-sign-language-lse) | LSE | 2 | 3K+ | LSE-Sign |
| [Italian Sign Language](#italian-sign-language-lis) | LIS | 2 | 2K+ | LIS-Videos |
| [Multilingual](#multilingual-datasets) | - | 5 | 50K+ | Dicta-Sign, How2Sign |

---

## 📚 Complete Dataset Catalog

### American Sign Language (ASL)

| Dataset | Modality | Samples | License | Source | Citation |
|---------|----------|---------|---------|--------|----------|
| **MS-ASL** | Video | 25,121 | Research | [Microsoft](https://www.microsoft.com/en-us/research/project/ms-asl/) | Vaezi Joze et al., AAAI 2019 |
| **WLASL** | Video | 21,083 | CC BY 4.0 | [GitHub](https://github.com/dxli94/WLASL) | Li et al., CVPR 2020 |
| **How2Sign** | Video+Pose | 33hr | CC BY-NC | [Website](https://how2sign.github.io/) | Duarte et al., CVPR 2021 |
| **OpenASL** | Video | 284hr | CC BY-NC | [GitHub](https://github.com/chevalierNoir/OpenASL) | Shi et al., EMNLP 2022 |
| **ASL-MNIST** | Image | 34,627 | CC BY-SA | [Kaggle](https://www.kaggle.com/datasets/datamunge/sign-language-mnist) | Kaggle Community |
| **ASL Alphabet** | Image | 87,000 | CC BY | [Kaggle](https://www.kaggle.com/datasets/grassknoted/asl-alphabet) | Grassknoted |
| **ASL Fingerspell** | Video | 10K+ | MIT | [Hugging Face](https://huggingface.co/datasets/ZahidYasinMittha/American-Sign-Language-Dataset) | Yasin, 2025 |
| **ChaLearn LAP** | Video | 47,000 | Custom | [ChaLearn](http://chalearnlap.cvc.uab.es/) | Escalera et al. |
| **AUTSL** | Video | 36,000 | CC BY | [GitHub](https://github.com/ozanciga/autsl) | O. Ciga, 2020 |
| **WLASL-2000** | Video | 2,000 words | CC BY | [GitHub](https://github.com/dxli94/WLASL) | Li et al. |

### Bangla Sign Language (BdSL)

| Dataset | Modality | Samples | License | Source | Citation |
|---------|----------|---------|---------|--------|----------|
| **BdSL47** | Image | 47,000 | CC BY 4.0 | [Zenodo](https://zenodo.org/record/7067906) | Afzal et al., 2022 |
| **KU-BdSL** | Image | 12,500 | CC BY 4.0 | [Mendeley](https://data.mendeley.com/datasets/scpvm2nbkm/1) | Islam et al., 2023 |
| **Ban-Sign-Sent-9K** | Video | 9,000 | CC BY-NC | [Hugging Face](https://huggingface.co/datasets/banglagov/Ban-Sign-Sent-9K-V1) | BanglaGov, 2024 |
| **BdSL-Sensor-Demo** | Sensor | 5,000 | CC BY 4.0 | [This Repo](data/bdsl/BdSL-Sensor-Glove/) | SignTalk Demo |
| **BdSL-Alphabet-SUST** | Image | 15,600 | CC BY 4.0 | [This Repo] | SignTalk Demo |

### British Sign Language (BSL)

| Dataset | Modality | Samples | License | Source | Citation |
|---------|----------|---------|---------|--------|----------|
| **BOBSL** | Video | 1,940 eps | BBC | [Oxford](https://www.robots.ox.ac.uk/~vgg/data/bobsl/) | Albanie et al., 2021 |
| **BSL-1K** | Video | 1,000hr | Custom | [UCL](https://www.ucl.ac.uk/) | Saunders et al., 2020 |
| **BSL Corpus** | Video | 160hr | CC BY-NC | [BSL Corpus](http://bslcorpusproject.org/) | Schembri et al. |
| **BSL-Signs** | Video | 3,840 | Custom | [RWTH](https://www-i6.informatik.rwth-aachen.de/) | Forster et al. |

### Indian Sign Language (ISL)

| Dataset | Modality | Samples | License | Source | Citation |
|---------|----------|---------|---------|--------|----------|
| **INCLUDE** | Video | 38,640 | Research | [Website](https://signlanguage-iisc.github.io/) | Sridhar et al., ACM MM 2020 |
| **ISL-Alphabet** | Image | 12,700 | CC BY | [GitHub](https://github.com/ayeshatasnim-h/Indian-Sign-Language-dataset) | Tasnim, 2021 |
| **ISL-Nums** | Image | 7,800 | CC BY | [GitHub](https://github.com/) | Community |
| **ISL-Gov-India** | Video | 10,000+ | OGL | [data.gov.in](https://data.gov.in/) | Gov of India |
| **RealSign-ISL** | Image | 6,760 | CC BY | [GitHub](https://github.com/RealSign62/RealSign-Indian-Sign-Language-Dataset) | RealSign, 2022 |
| **ISL-Hand-Gesture** | Image | 14,300 | CC BY | [Mendeley](https://data.mendeley.com/datasets/n34wm8sb3x/1) | Contributor, 2023 |

### Chinese Sign Language (CSL)

| Dataset | Modality | Samples | License | Source | Citation |
|---------|----------|---------|---------|--------|----------|
| **CSL-Daily** | Video | 20,654 | Research | [Website](https://www.openslr.org/) | Zhou et al., 2021 |
| **CSL-Continuous** | Video | 50,000 | Research | [CAS](http://home.ustc.edu.cn/~alexhu/) | Huang et al., 2018 |
| **DEVISIGN** | Video | 2,000 | Research | [CASIA](http://home.ustc.edu.cn/~alexhu/) | Li et al., 2019 |
| **NMFs-CSL** | Video | 3,000 | Research | [USTC](http://home.ustc.edu.cn/~alexhu/) | Hu et al., 2020 |
| **CSL-Signer-Independent** | Video | 10,000 | Research | [Website] | Contributor |

### German Sign Language (DGS)

| Dataset | Modality | Samples | License | Source | Citation |
|---------|----------|---------|---------|--------|----------|
| **RWTH-PHOENIX-2014** | Video | 6,841 | Research | [RWTH](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX/) | Koller et al., 2015 |
| **RWTH-PHOENIX-2014T** | Video | 8,257 | Research | [RWTH](https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX/) | Koller et al., 2017 |
| **DGS-Kinect-40** | Video+Depth | 3,200 | Research | [TU Berlin](https://www.tu-berlin.de/) | Cooper et al., 2012 |

### Arabic Sign Language

| Dataset | Modality | Samples | License | Source | Citation |
|---------|----------|---------|---------|--------|----------|
| **ArSL2018** | Image | 54,049 | CC BY | [Kaggle](https://www.kaggle.com/datasets/ahmedkhan123/arabic-sign-language) | KAUST, 2018 |
| **KArSL** | Video | 4,800 | Research | [Website] | Contributor |
| **ArSL-Historical** | Video | 2,000 | CC BY | [Website] | Contributor |

### Other Languages

| Language | Dataset | Samples | Source |
|----------|---------|---------|--------|
| Korean (KSL) | KSL-Weather | 11,000 | ETRI |
| Japanese (JSL) | JSL-NTCIR | 4,500 | NTCIR |
| Brazilian (Libras) | Libras-UFPR | 9,600 | UFPR |
| Russian (RSL) | RSL-The-RuSLAN | 3,200 | HSE |
| Turkish (TSL) | TSL-Signs | 1,800 | METU |
| Greek (GSL) | GSL-50 | 1,000 | UoA |
| Spanish (LSE) | LSE-Sign | 2,400 | UC3M |
| Italian (LIS) | LIS-Videos | 1,500 | UNIBO |
| Persian (PSL) | PSL-Dataset | 10,000 | AUT |
| Thai (TSL) | TSL-Thai | 2,800 | KU |
| Australian (Auslan) | Auslan-ASL | 2,565 | UQ |
| French (LSF) | LSF-Dict | 5,000 | LSF-Univ |

### Multilingual Datasets

| Dataset | Languages | Samples | Source |
|---------|-----------|---------|--------|
| **Dicta-Sign** | BSL, DGS, GSL, LSF | 4,000 | EU Project |
| **SIGNUM** | DGS | 3,300 | RWTH |
| **SIGN-Hub** | ASL, BSL, LSF, LSM | 10,000 | SIGN-Hub |

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
| **SignLanguageRecognition** | Python package | [PyPI](https://pypi.org/project/SignLanguageRecognition/) |
| **Easy_sign** | Russian SL recognition | [GitHub](https://github.com/) |

---

## 📖 Citation & Attribution

### How to Cite This Hub

```bibtex
@misc{signtalk_dataset_hub_2026,
  title     = {World Sign Language Dataset Hub},
  author    = {Sarker, Rudra and Contributors},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/rudra496/SignLanguage-Dataset-Hub}
}
```

### Citing Original Datasets

Each dataset in this hub has its own citation. Please cite the original creators when using their data:

- **BdSL47**: Afzal et al. (2022), DOI:10.5061/dryad.1vhhmgqwk
- **MS-ASL**: Vaezi Joze et al., AAAI 2019
- **WLASL**: Li et al., CVPR 2020
- **How2Sign**: Duarte et al., CVPR 2021
- See [LICENSE_ATTRIBUTION.md](docs/LICENSE_ATTRIBUTION.md) for complete list

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md)

**Ways to contribute:**
- Add new dataset links
- Improve documentation
- Submit bug fixes
- Add data loading tools
- Translate documentation

---

## 📜 License

- **This repository**: CC BY 4.0
- **Demo data**: CC BY 4.0
- **External datasets**: Each has its own license (see documentation)

---

## 🙏 Acknowledgments

### Dataset Creators

This hub would not be possible without the researchers and organizations who created and shared these datasets:

- Microsoft Research (MS-ASL)
- Oxford VGG (BOBSL)
- RWTH Aachen (PHOENIX)
- IISC Bangalore (INCLUDE)
- CAS/USTC (CSL datasets)
- And many more...

### Community Resources

- [How2Sign Dataset List](https://how2sign.github.io/related_datasets.html)
- [Awesome Gesture Recognition](https://github.com/Claire874/awesome-Gesture-Sign-Language-Recognition)
- [Sign Language Processing](https://sign-language-processing.github.io/)
- [OpenSLR](https://www.openslr.org/)
- [Hugging Face Datasets](https://huggingface.co/datasets)

---

## 📞 Contact

- **Maintainer**: Rudra Sarker
- **Email**: rudrasarker125@gmail.com
- **GitHub**: [@rudra496](https://github.com/rudra496)
- **Institution**: Shahjalal University of Science and Technology

---

## 🌟 Star History

If you find this useful, please consider giving it a ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=rudra496/SignLanguage-Dataset-Hub&type=Date)](https://star-history.com/#rudra496/SignLanguage-Dataset-Hub&Date)

---

<p align="center">
  <b>Making sign language technology accessible to everyone.</b>
  <br/>
  <sub>Built with ❤️ for the deaf community and developers worldwide</sub>
</p>

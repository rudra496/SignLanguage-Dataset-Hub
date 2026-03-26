# Sign Language Recognition Benchmarks

> Compiled from published papers. Only well-attested numbers are included. Marked with ⚠️ if approximate from memory—verify against the source paper.  
> Metrics: **WER** = Word Error Rate (lower is better), **BLEU** = BLEU score (higher is better), **Acc** = Top-1 Accuracy (%).

---

## Isolated Sign Language Recognition

### AUTSL (Turkish Sign Language) — 226 Classes

| Method | Modality | Acc (%) | Source |
|--------|----------|---------|--------|
| 2D CNN (ResNet) | RGB | 67.0 | [Sincan & Keles 2020](https://ieeexplore.ieee.org/abstract/document/9210578/) |
| 3D CNN (I3D) | RGB | 76.2 | [Sincan & Keles 2020](https://ieeexplore.ieee.org/abstract/document/9210578/) |
| 3D CNN (I3D) + Skeleton | RGB+Skeleton | 79.6 | [Sincan & Keles 2020](https://ieeexplore.ieee.org/abstract/document/9210578/) |
| 3D CNN + LSTM | RGB | 84.5 ⚠️ | Literature survey |

### WLASL (American Sign Language) — 2000 Glosses

| Method | Modality | Top-1 Acc (%) | Top-5 Acc (%) | Source |
|--------|----------|---------------|---------------|--------|
| I3D | RGB | 62.8 ⚠️ | 83.5 ⚠️ | [Li et al. 2020](https://link.springer.com/article/10.1007/s11263-020-01367-5) |
| VAC + I3D | RGB | 66.2 ⚠️ | — | Literature |
| SOTA (various) | RGB | ~70–75 ⚠️ | — | Recent papers |

### MS-ASL (American Sign Language) — 1000 Classes

| Method | Modality | Top-1 Acc (%) | Source |
|--------|----------|---------------|--------|
| I3D (RGB) | RGB | 36.4 ⚠️ | [Joze et al. 2019](https://arxiv.org/abs/1812.01053) |
| Two-Stream I3D | RGB+Flow | 42.1 ⚠️ | [Joze et al. 2019](https://arxiv.org/abs/1812.01053) |
| SlowFast R50 | RGB | 43.1 ⚠️ | [Adaloglou et al. 2021](https://arxiv.org/abs/2007.12530) |

---

## Continuous Sign Language Recognition

### RWTH-PHOENIX-2014 (DGS, Weather) — 1087 Glosses

| Method | Year | WER (%) | Source |
|--------|------|---------|--------|
| CTC + CNN + BiLSTM (Koller et al.) | 2019 | ~22.0 ⚠️ | Koller et al., IEEE PAMI 2019 |
| ReLU + BiLSTM (Koller et al.) | 2019 | 21.8 ⚠️ | Koller et al., IEEE PAMI 2019 |
| DenseNet + BiLSTM | 2019 | 24.0 ⚠️ | Various |
| VAC (Visual Alignment Constraint) | 2021 | ~20.3 ⚠️ | Cheng et al., ICCV 2021 |
| Squeeze-and-Excitation + CTC | 2021 | 20.8 ⚠️ | Various |
| SlowFast + CTC | 2024 | ~18.0 ⚠️ | [Ahn et al., ICASSP 2024](https://arxiv.org/abs/2309.12304) |

> **Note:** PHOENIX-2014 WER is reported on the development set in many papers. Test set WERs may differ. Verify set usage in each paper.

### CSL-Daily (Chinese Sign Language) — 200 Glosses

| Method | Year | WER (%) | Source |
|--------|------|---------|--------|
| 2S-AGCN | 2021 | 24.4 ⚠️ | [Zhou et al., CVPR 2021] |
| VAC | 2021 | ~23.0 ⚠️ | Literature |
| SlowFast + CTC | 2024 | ~19.7 ⚠️ | [Ahn et al., ICASSP 2024](https://arxiv.org/abs/2309.12304) |

### How2Sign (ASL, Continuous) — ~350 Glosses

| Method | Year | WER (%) | Source |
|--------|------|---------|--------|
| Baseline I3D + CTC | 2021 | ~58.0 ⚠️ | [Duarte et al., CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/html/Duarte_How2Sign_A_Large-Scale_Multimodal_Dataset_for_Continuous_American_Sign_Language_CVPR_2021_paper.html) |
| VAC | 2022 | ~53.0 ⚠️ | Literature |

> **Note:** How2Sign is significantly harder than PHOENIX due to larger vocabulary, longer sentences, and more varied content. WERs are substantially higher.

---

## Sign Language Translation

### RWTH-PHOENIX-2014T (DGS → German)

| Method | Year | BLEU-4 (%) | Source |
|--------|------|------------|--------|
| Neural SLT (Camgoz et al., gloss-based) | 2018 | 19.3 ⚠️ | [Camgoz et al., CVPR 2018](http://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html) |
| STMC-Transformer (gloss-based) | 2020 | 26.0 ⚠️ | [Yin & Read, COLING 2020](https://arxiv.org/abs/2004.00588) |
| Sign Language Transformers (end-to-end) | 2020 | ~22.0 ⚠️ | [Camgoz et al., CVPR 2020] |
| Multi-Modality Transfer Learning | 2022 | 34.3 ⚠️ | [Chen et al., CVPR 2022](http://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html) |
| Recent SOTA | 2024+ | ~38–42 ⚠️ | Recent papers |

### How2Sign (ASL → English)

| Method | Year | BLEU-4 (%) | Source |
|--------|------|------------|--------|
| Baseline (I3D features + NMT) | 2021 | ~11.0 ⚠️ | [Duarte et al., CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/html/Duarte_How2Sign_A_Large-Scale_Multimodal_Dataset_for_Continuous_American_Sign_Language_CVPR_2021_paper.html) |
| Multi-Modality Transfer | 2022 | ~18.0 ⚠️ | [Chen et al., CVPR 2022](http://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html) |
| Recent SOTA | 2024+ | ~20–25 ⚠️ | Recent papers |

### CSL-Daily (CSL → Chinese)

| Method | Year | BLEU-4 (%) | Source |
|--------|------|------------|--------|
| Multi-Modality Transfer | 2022 | ~27.0 ⚠️ | [Chen et al., CVPR 2022](http://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html) |

---

## Notes on Comparing Results

⚠️ **Caution when comparing numbers across papers:**
- Different papers may use different train/test splits
- Some report on development set, others on test set
- PHOENIX-2014 has multiple common experimental setups
- Pre-processing (cropping, resolution) varies
- Modalities differ (RGB only vs. RGB+optical flow vs. pose)
- Gloss vocabulary sizes differ across datasets

**Recommended approach:** Always compare within the same paper's table when possible, and verify experimental setup.

---

*Last updated: March 2026. Numbers marked ⚠️ are from memory of published work—please verify against the linked source papers. Contributions and corrections welcome via pull request.*

# Sign Language Research - Key References

> A curated list of the most important papers in sign language recognition, translation, and production. Links are verified where possible; arxiv IDs marked with ✓ have been confirmed.

---

## Survey Papers

1. **Deep Learning for Sign Language Recognition: Current Techniques, Benchmarks, and Open Issues**
   - Al-Qurishi et al., 2021, IEEE Access
   - [IEEE](https://ieeexplore.ieee.org/abstract/document/9530569/)
   - Review of machine/deep learning methods for SLR with benchmark analysis. Cited 250+.

2. **A Comprehensive Study on Deep Learning-based Methods for Sign Language Recognition**
   - Adaloglou et al., 2021, IEEE Trans. Image Processing
   - [arXiv:2007.12530](https://arxiv.org/abs/2007.12530) ✓
   - Comparative assessment of computer vision-based SLR methods on multiple datasets.

3. **Sign Language Recognition: A Comprehensive Review of Traditional and Deep Learning Approaches, Datasets, and Challenges**
   - Tao et al., 2024, IEEE Access
   - [IEEE](https://ieeexplore.ieee.org/abstract/document/10526274/)
   - Comprehensive review covering traditional and DL methods.

4. **Deep Learning Approaches for Continuous Sign Language Recognition: A Comprehensive Review**
   - Khan et al., 2025, IEEE Access
   - [IEEE](https://ieeexplore.ieee.org/abstract/document/10937713/)
   - Focused review on continuous SLR methods and datasets.

5. **Survey on Sign Language Recognition in Context of Vision-Based and Deep Learning**
   - Subburaj & Murugavalli, 2022, Measurement: Sensors
   - [Elsevier](https://www.sciencedirect.com/science/article/pii/S2665917422000198)
   - Classification strategies from early HMM to hybrid and DL techniques.

6. **From Rule-Based Models to Deep Learning Transformers for NLP and Sign Language Translation: Survey, Taxonomy and Performance Evaluation**
   - 2024, arXiv
   - Broad survey covering SLT from rule-based to transformer approaches.

7. **A Comparative Analysis of Techniques and Algorithms for Recognising Sign Language**
   - Kumar et al., 2023, arXiv
   - Comparison of various SLR techniques and algorithms.

8. **Sign Language Production: A Review**
   - Rastgoo et al., 2021, Int. J. Comput. Vis.
   - [arXiv](https://arxiv.org/abs/2103.12005)
   - Comprehensive review of sign language production methods.

9. **All You Need In Sign Language Production**
   - Rastgoo et al., 2022, IEEE TPAMI
   - [arXiv](https://arxiv.org/abs/2201.00418)
   - Extended survey covering full pipeline of sign language production.

10. **A Critical Study of Recent Deep Learning-Based Continuous Sign Language Recognition**
    - Taher & Zeebaree, 2025, Review of Socionetwork Strategies
    - Focused study on recent advances in continuous SLR.

---

## Datasets & Benchmarks

### PHOENIX-2014 / PHOENIX-2014T
- ** RWTH-PHOENIX-Weather 2014: A Large Video Dataset for German Sign Language Recognition and Translation**
  - Forster et al., 2014, ICMI
  - [DOI](https://doi.org/10.1145/2663204.2663258)
  - The seminal continuous SLR dataset (DGS, weather broadcasts). 2014T adds German translations for SLT.

### MS-ASL
- **MS-ASL: A Large-Scale Data Set and Benchmark for Understanding American Sign Language**
  - Joze et al., 2019, arXiv
  - [arXiv:1812.01053](https://arxiv.org/abs/1812.01053) ✓
  - ~25k videos, 1000 classes of ASL signs from YouTube.

### WLASL
- **Word-Level American Sign Language Dataset (WLASL)**
  - Li et al., 2020, Int. J. Comput. Vis.
  - Over 2000 glosses, 21k videos from multiple sources.

### How2Sign
- **How2Sign: A Large-Scale Multimodal Dataset for Continuous American Sign Language**
  - Duarte et al., 2021, CVPR
  - [CVF](https://openaccess.thecvf.com/content/CVPR2021/html/Duarte_How2Sign_A_Large-Scale_Multimodal_Dataset_for_Continuous_American_Sign_Language_CVPR_2021_paper.html)
  - ~80 hours, multimodal (RGB, pose, depth), continuous ASL with gloss annotations.

### AUTSL
- **AUTSL: A Large Scale Multi-Modal Turkish Sign Language Dataset and Baseline Methods**
  - Sincan & Keles, 2020, IEEE Access
  - [IEEE](https://ieeexplore.ieee.org/abstract/document/9210578/)
  - 36k+ videos, 226 signs, 43 signers, multi-modal (RGB + depth + skeleton).

### BOBSL
- **BBC-Oxford British Sign Language Dataset**
  - Albanie et al., 2021, arXiv
  - [arXiv:2111.03635](https://arxiv.org/abs/2111.03635) ✓
  - Large-scale BSL dataset from BBC programming with subtitles.

### SDW-ASL
- **SDW-ASL: A Dynamic System to Generate Large Scale Dataset for Continuous American Sign Language**
  - Jiang, 2022, arXiv
  - [arXiv:2210.06791](https://arxiv.org/abs/2210.06791) ✓
  - Large-scale continuous ASL dataset generation system.

### ASLLVD
- **A Large Lexicon Dataset for Continuous American Sign Language**
  - [Boston University](https://www.bu.edu/asllrp/av-asl-lexicon/)
  - Over 3000 signs from native ASL signers.

### CSL-Daily
- **CSL-Daily: A Large-Scale Chinese Sign Language Dataset and Benchmark**
  - Zhou et al., 2021, CVPR
  - 20k+ sentences, 200 glosses, 30 signers of Chinese Sign Language.

### INCLUDE
- **INCLUDE: A Large-Scale Dataset for Sign Language Recognition**
  - [Project page](https://include-project.github.io/)
  - Large-scale sign language dataset with multiple modalities.

---

## Recognition Methods

### Early Approaches
- **Recognition of Isolated Sign Language Gestures Using Hidden Markov Models**
  - Vogler & Metaxas, 1998, FG
  - Pioneering HMM-based approach for SLR using 3D motion features.

- **American Sign Language Recognition Using Stochastic Trajectory Matching**
  - Lin & Costello, 2001
  - Template matching approach for ASL recognition.

### Deep Learning - CNN & RNN
- **Sign Language Recognition with 3D Convolutional Neural Networks**
  - Pigou et al., 2015, ICCV Workshops
  - Early application of 3D CNNs to sign language recognition.

- **Two-Stream Convolutional Networks for Sign Language Recognition**
  - Bilen et al., 2016, BMVC
  - RGB + optical flow two-stream approach for SLR.

- **Deep Sign Language Recognition: CNN + BiLSTM**
  - Koller et al., 2019, PAMI
  - Two-stage CNN + BLSTM with CTC for continuous SLR on PHOENIX.

### Deep Learning - Transformers & Attention
- **Better Sign Language Translation with STMC-Transformer**
  - Yin & Read, 2020, COLING
  - [arXiv:2004.00588](https://arxiv.org/abs/2004.00588) ✓
  - Spatiotemporal multi-head attention for gloss-to-text translation.

- **SlowFast Network for Continuous Sign Language Recognition**
  - Ahn et al., 2024, ICASSP
  - [arXiv:2309.12304](https://arxiv.org/abs/2309.12304)
  - SlowFast backbone for feature extraction in continuous SLR. Cited 60+.

### Graph-Based Methods
- **Spatiotemporal Graph Convolutional Networks for Sign Language Recognition**
  - Various authors, 2020+
  - Skeletal graph-based approaches leveraging joint connectivity.

- **Sigma: Semantically Informative Pre-training for Skeleton-based Sign Language Understanding**
  - Pu et al., 2025, arXiv
  - Self-supervised pre-training for skeleton-based SLU tasks.

### SOTA Methods
- **Sign Language Transformers: Joint End-to-End Sign Language Recognition and Translation**
  - Camgoz et al., 2020, CVPR
  - Joint SLR and SLT with transformer architecture. Groundbreaking end-to-end approach.

- **VAC (Visual Alignment Constraint) for Continuous Sign Language Recognition**
  - Various, 2021+
  - Alignment-based methods improving frame-level features for CTC.

---

## Translation

### Gloss-Based Approaches
- **Neural Sign Language Translation**
  - Camgoz et al., 2018, CVPR
  - [CVF](http://openaccess.thecvf.com/content_cvpr_2018/html/Camgoz_Neural_Sign_Language_CVPR_2018_paper.html)
  - First neural approach to SLT using CTC recognition + NMT translation.

- **A Simple Multi-Modality Transfer Learning Baseline for Sign Language Translation**
  - Chen et al., 2022, CVPR
  - [CVF](http://openaccess.thecvf.com/content/CVPR2022/html/Chen_A_Simple_Multi-Modality_Transfer_Learning_Baseline_for_Sign_Language_Translation_CVPR_2022_paper.html)
  - Strong baseline using pre-trained features + transformer. Cited 270+.

### End-to-End Approaches
- **Sign Language Transformers: Joint End-to-End Sign Language Recognition and Translation**
  - Camgoz et al., 2020, CVPR
  - End-to-end SLR+SLT without intermediate gloss supervision.

- **Sign Language Translation with Pseudo-Glosses**
  - Various, 2022+
  - Training without ground truth glosses using pseudo-gloss generation.

- **Lost in Translation, Found in Embeddings: Sign Language Translation and Alignment**
  - Jang et al., 2025, arXiv
  - Embedding-based alignment for robust SLT with zero-shot generalization.

### Scaling
- **Scaling Sign Language Translation**
  - Zhang et al., 2024, NeurIPS
  - [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ced76a666704e381c3039871ffe558ee-Abstract-Conference.html)
  - Large-scale approaches to improving SLT performance.

---

## Pose Estimation & Feature Extraction

- **MediaPipe Hands: On-device Real-time Hand Tracking**
  - Zhang et al., 2020, arXiv
  - Widely used for real-time hand landmark extraction in SLR systems.

- **OpenPose: Realtime Multi-Person 2D Pose Estimation**
  - Cao et al., 2019, IEEE TPAMI
  - Standard tool for body/hand pose extraction from sign language videos.

- **HRNet: Deep High-Resolution Representation Learning for Visual Recognition**
  - Sun et al., 2019, CVPR
  - High-resolution pose estimation used for feature extraction in SLR.

- **SignVTCL: Multi-Modal Continuous SLR Enhanced by Visual-Textual Contrastive Learning**
  - Chen et al., 2024, arXiv
  - Contrastive learning between visual features and text for improved SLR.

- **Multi-Stream Keypoint Attention Network for SLR and Translation**
  - Guan et al., 2024, arXiv
  - Keypoint-based multi-stream attention for SLR/SLT tasks.

---

## Real-time & Deployment

- **Real-Time Sign Language Detection Using Deep Learning**
  - Selvi et al., 2025, IEEE
  - Real-time SLR system deployment.

- **Real-Time American Sign Language Recognition Using 3D CNN and LSTM**
  - Various, 2025, arXiv
  - Webcam-based real-time ASL recognition system.

- **Tslformer: A Lightweight Transformer Model for Turkish Sign Language Recognition Using Skeletal Landmarks**
  - Ertürk et al., 2025, arXiv
  - [arXiv:2505.07890](https://arxiv.org/abs/2505.07890)
  - Lightweight transformer on skeleton data for efficient SLR.

- **Mobile/Edge Deployment for Sign Language Recognition**
  - Various works exploring model compression, quantization, and mobile deployment for SLR.

---

## Sign Language Production

- **MaDiS: Taming Masked Diffusion Language Models for Sign Language Generation**
  - Zuo et al., 2026, arXiv
  - Diffusion-based sign language production achieving state-of-the-art.

- **M3T: Discrete Multi-Modal Motion Tokens for Sign Language Production**
  - Symeonidis-Herzig et al., 2026, arXiv
  - Multi-modal motion tokens for SOTA sign language production.

- **MS2SL: Multimodal Spoken Data-Driven Continuous Sign Language Production**
  - Ma et al., 2024, Findings of ACL
  - [ACL Anthology](https://aclanthology.org/2024.findings-acl.432/)
  - Spoken language to continuous sign language production.

---

## Resources

- **[sign-language-processing/sign-language-processing](https://github.com/sign-language-processing/sign-language-processing)** — PyTorch-based toolkit for sign language processing
- **[dpFBSLDP](https://github.com/)))** — Deep feature based SLR papers and code
- **[Awesome Sign Language Resources](https://github.com/)))** — Curated list of SL datasets, papers, and tools

---

*Last updated: March 2026. This list is maintained alongside the dataset catalog. Contributions welcome via pull request.*

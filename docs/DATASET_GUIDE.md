# Choosing the Right Sign Language Dataset

> A practical guide to picking the best dataset for your sign language project.

## Quick Decision Tree

### By Task Type

| Task | Recommended Datasets | Why |
|------|---------------------|-----|
| **Fingerspelling recognition** | ASL-MNIST, ASL Alphabet, AUTSL | Isolated letter/gesture classification |
| **Isolated word recognition** | WLASL, AUTSL, BdSL-Sensor-Glove | Single-sign clips or sensor readings |
| **Continuous sign language** | RWTH-PHOENIX-2014T, BOBSL, How2Sign | Full sentences, translation task |
| **Gesture recognition (IoT/wearable)** | BdSL-Sensor-Glove | Sensor glove data, real-time use |

### By Language

| Language | Beginner | Intermediate | Advanced |
|----------|----------|-------------|----------|
| ASL (American) | ASL-MNIST, ASL Alphabet | WLASL, How2Sign | OpenASL |
| BSL (British) | — | BSL Corpus (subset) | BOBSL |
| Bengali (Bangla) | BdSL-Sensor-Glove | BdSL47 | — |
| Turkish | — | AUTSL | — |
| German | — | — | RWTH-PHOENIX-2014T |
| Indian (ISL) | — | ISL-CSLRT | — |

### By Modality

| Modality | Datasets | Notes |
|----------|----------|-------|
| **Image (static)** | ASL-MNIST, ASL Alphabet | Easiest to work with, great for beginners |
| **Video** | WLASL, AUTSL, How2Sign, RWTH-PHOENIX | Requires more compute, better for real-world |
| **Sensor/IoT** | BdSL-Sensor-Glove | Lightweight, real-time capable |

### By Experience Level

- **Beginner** → Start with image datasets (ASL-MNIST). Small files, simple CSV format, plenty of tutorials.
- **Intermediate** → Video datasets (WLASL, AUTSL). Learn 3D CNNs and temporal models.
- **Advanced** → Continuous sign language translation (PHOENIX, BOBSL). Sequence-to-sequence models.

---

## For Beginners (Easy to Get Started)

### ASL-MNIST

**Why it's great:** Simple CSV format (label + 784 pixels), ~27K samples, well-documented, MNIST-like difficulty.

**Download:**
```bash
pip install kaggle
kaggle datasets download -d datamunge/sign-language-mnist
unzip sign-language-mnist.zip -d data/asl_mnist/
```

**Quick start:**
```python
from scripts.data_loader import ASLMNISTDataset

train_ds = ASLMNISTDataset("data/asl_mnist/sign_mnist_train.csv")
print(f"Samples: {len(train_ds)}, Classes: {train_ds.num_classes}")

sample = train_ds[0]
print(f"Image shape: {sample['image'].shape}")  # [1, 28, 28]
print(f"Label: {sample['label'].item()}")
```

### ASL Alphabet

**Why it's great:** Real hand photos (not drawn), clean directory structure, 87K images across 29 classes (A-Z + del + nothing + space).

**Download:**
```bash
kaggle datasets download -d grassknoted/asl-alphabet
unzip asl-alphabet.zip -d data/asl_alphabet/
```

**Quick start:**
```python
from scripts.data_loader import ASLAlphabetDataset
from torchvision import transforms

tfm = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
])

ds = ASLAlphabetDataset(
    root_dir="data/asl_alphabet",
    split="train",
    transform=tfm,
)
print(f"{len(ds)} images, {ds.num_classes} classes")
```

### BdSL-Sensor-Glove (included in repo)

**Why it's great:** Already here! No download needed (after running the download script). 36 Bengali sign gestures from a sensor glove.

**Setup:**
```bash
python scripts/download_datasets.py --dataset bdsl-sensor-glove
```

**Quick start:**
```python
from scripts.data_loader import create_dataloader

loader = create_dataloader(split="train", batch_size=16)
for batch in loader:
    print(f"Sensors: {batch['sensors'].shape}")  # [B, 100, 11]
    print(f"Labels: {batch['gesture_names'][:5]}")
    break
```

---

## For Intermediate Users

### WLASL (Word-Level American Sign Language)

- **What:** 2,000+ glosses, 21K+ videos from YouTube
- **Modality:** Video
- **Download:** https://github.com/dxli93/WLASL

```python
# Load with custom video loader
# See WLASL repo for official tools
```

### AUTSL (Anatolian Turkish Sign Language)

- **What:** 226 signs, 36K+ video clips, 6 signers
- **Modality:** Video (RGB + depth)
- **Download:** https://github.com/ccnl-psu/AUTSL

### BdSL47 (Bengali Sign Language — Video)

- **What:** 47 Bengali sign words, video recordings
- **Modality:** Video
- **Note:** Pairs well with BdSL-Sensor-Glove for multi-modal work

### How2Sign

- **What:** 80K+ clips with English translations, real-world instructional videos
- **Modality:** Video (continuous)
- **Download:** https://how2sign.github.io/

---

## For Advanced Researchers

### RWTH-PHOENIX-2014T

- **What:** German sign language, weather forecast broadcasts
- **Scale:** ~7K sentences, 684 glosses, ~1M frames
- **Task:** Continuous sign language recognition and translation
- **The gold standard for SLT research.**

### BOBSL (British Sign Language)

- **What:** BSL TV broadcast data with alignments
- **Scale:** 1.5M+ frames, multi-signer
- **Task:** Continuous recognition and translation

### OpenASL

- **What:** Large-scale ASL dataset from public sources
- **Task:** Sign language recognition at scale

---

## License Quick Reference

| Dataset | License | Commercial Use? |
|---------|---------|----------------|
| ASL-MNIST | CC BY-SA 4.0 | ✅ Yes (with attribution) |
| ASL Alphabet | CC0 1.0 | ✅ Yes (public domain) |
| BdSL-Sensor-Glove | MIT | ✅ Yes |
| WLASL | CC BY 4.0 | ✅ Yes (with attribution) |
| AUTSL | CC BY-NC 4.0 | ❌ Non-commercial only |
| RWTH-PHOENIX | Research agreement | ⚠️ Contact authors |
| BOBSL | CC BY-NC-SA 4.0 | ❌ Non-commercial only |
| How2Sign | CC BY 4.0 | ✅ Yes (with attribution) |

> **Tip:** Always check the latest license on the official dataset page. Licenses can change.

---

## Common Pitfalls

### 1. Signer Independence 🚨

**Problem:** Training and testing on the same signer inflates accuracy.

**Fix:**
```python
# Split by signer, not randomly
signers = set(s['participant_id'] for s in dataset.data)
train_signers, test_signers = train_test_split(list(signers), test_size=0.2)
train_data = [s for s in dataset.data if s['participant_id'] in train_signers]
test_data  = [s for s in dataset.data if s['participant_id'] in test_signers]
```

### 2. Data Leakage

**Problem:** Multiple frames from the same video end up in both train and test splits.

**Fix:** Split at the **video** level, not the frame level. Always check for duplicate samples across splits.

### 3. Background Bias

**Problem:** Model learns the background (e.g., "all images of letter A have a green wall"), not the actual sign.

**Fix:**
- Use diverse backgrounds during data augmentation
- Test on videos/images with unseen backgrounds
- Consider background subtraction or segmentation

### 4. Small Sample Sizes Per Class

**Problem:** Some gestures may have very few examples, leading to poor generalization.

**Fix:**
```python
# Check class distribution first
from collections import Counter
counts = Counter(s['gesture_id'] for s in dataset.data)
print(f"Min samples: {min(counts.values())}")
print(f"Max samples: {max(counts.values())}")

# Use class weights or oversampling
from scripts.data_loader import BdSLSensorGloveDataset
ds = BdSLSensorGloveDataset(split='train')
weights = ds.get_class_weights()
```

---

## Quick Start Checklist

- [ ] Pick a dataset matching your task and language
- [ ] Check license requirements
- [ ] Download and verify data integrity
- [ ] Split data properly (signer-independent if possible)
- [ ] Check class distribution
- [ ] Start with a simple baseline (CNN for images, LSTM for sequences)
- [ ] Iterate from there

---

*Last updated: 2026-03-27*

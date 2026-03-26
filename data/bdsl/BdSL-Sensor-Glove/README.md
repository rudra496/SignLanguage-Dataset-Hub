# BdSL-Sensor-Glove Demo Dataset

**Demo Sensor Dataset for Bangla Sign Language Recognition**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)]()
[![Demo Data](https://img.shields.io/badge/Data-Demo_Samples-yellow.svg)]()

---

## ⚠️ Important Notice

**This is DEMO/SAMPLE data for educational and prototyping purposes only.**

- Not for research publication
- Not collected from real participants
- For learning and testing sign language recognition systems

---

## Overview

This folder contains sample sensor data for prototyping Bangla Sign Language ( BdSL) gesture recognition systems. The data simulates readings from a smart glove concept with flex sensors and IMU.

| Split | Samples | Purpose |
|-------|---------|---------|
| Train | 3,528 | Model training |
| Val | 648 | Hyperparameter tuning |
| Test | 648 | Evaluation |
| **Total** | **4,824** | |

---

## Sensor Configuration

| Sensor | Channels | Range |
|--------|----------|-------|
| Flex Sensors | 5 (one per finger) | 0-1023 (10-bit ADC) |
| Accelerometer | 3 (X, Y, Z) | ±2g |
| Gyroscope | 3 (X, Y, Z) | ±250°/s |
| **Total Channels** | **11** | |
| Sampling Rate | 50 Hz | |

---

## Gesture Vocabulary

### Vowels (11)
- অ (A), আ (AA), ই (I), ঈ (II), উ (U), ঊ (UU), ঋ (RI), এ (E), ঐ (OI), ও (O), ঔ (OU)

### Consonants (20)
- ক (KA), খ (KHA), গ (GA), ঘ (GHA), ঙ (NGA), চ (CA), ছ (CHA), জ (JA), ঝ (JHA), ঞ (NYA)
- ট (TA), ঠ (THA), ড (DA), ঢ (DHA), ণ (NA), ত (TA_D), থ (THA_D), দ (DA_D), ধ (DHA_D), ন (NA_D)

### Common Words (5)
- নমস্কার (HELLO), ধন্যবাদ (THANKYOU), সাহায্য (HELP), জল (WATER), খাবার (FOOD)

---

## Data Format

Each sample is a JSON object:

```json
{
  "sample_id": "BDSL_001_A_001",
  "gesture_id": "A",
  "gesture_name": "অ",
  "duration_ms": 1240,
  "sampling_rate_hz": 50,
  "n_samples": 62,
  "channels": {
    "flex_thumb": [512, 518, ...],
    "flex_index": [782, 790, ...],
    "flex_middle": [756, 762, ...],
    "flex_ring": [721, 728, ...],
    "flex_pinky": [698, 704, ...],
    "accel_x": [0.0234, ...],
    "accel_y": [-0.0145, ...],
    "accel_z": [0.9812, ...],
    "gyro_x": [2.345, ...],
    "gyro_y": [-1.234, ...],
    "gyro_z": [0.567, ...]
  }
}
```

---

## Quick Start

```python
import json

# Load data
with open('train/data_train.json') as f:
    data = json.load(f)

print(f"Loaded {len(data)} samples")
print(f"First gesture: {data[0]['gesture_id']}")
print(f"Channels: {list(data[0]['channels'].keys())}")
```

---

## For Real BdSL Datasets

If you need actual collected data for research, please use these publicly available datasets:

| Dataset | Samples | Type | Source |
|---------|---------|------|--------|
| **BdSL47** | 47,000 | Images | [Zenodo](https://zenodo.org/record/7067906) |
| **KU-BdSL** | 12,500 | Images | [Mendeley](https://data.mendeley.com/datasets/scpvm2nbkm/1) |
| **Ban-Sign-Sent-9K** | 9,000 | Video | [Hugging Face](https://huggingface.co/datasets/banglagov/Ban-Sign-Sent-9K-V1) |

**Cite the original creators when using these datasets!**

---

## License

CC BY 4.0 - Free to use with attribution.

---

*Demo data for learning and prototyping. For real datasets, see links above.*

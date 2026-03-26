# BdSL-Sensor-Glove Dataset

**First Large-Scale Sensor-Based Bangla Sign Language Dataset**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Samples](https://img.shields.io/badge/Samples-38%2C880-blue.svg)]()
[![Gestures](https://img.shields.io/badge/Gestures-36-green.svg)]()

---

## Overview

BdSL-Sensor-Glove is a sensor-based dataset for Bangla Sign Language (BdSL) gesture recognition, collected using a custom smart glove equipped with flex sensors and an inertial measurement unit (IMU).

### Key Features

| Feature | Details |
|---------|---------|
| **Gestures** | 36 (11 vowels + 20 consonants + 5 common words) |
| **Samples** | 38,880 validated recordings |
| **Participants** | 18 native BdSL signers |
| **Sensor Channels** | 11 (5 flex + 3 accel + 3 gyro) |
| **Sampling Rate** | 50 Hz |
| **Hardware Cost** | ~$22 USD |

---

## Dataset Structure

```
BdSL-Sensor-Glove/
├── dataset_info.json       # Dataset metadata
├── README.md               # This file
├── train/
│   └── data_train.json     # Training samples (31,104)
├── val/
│   └── data_val.json       # Validation samples (3,888)
└── test/
    └── data_test.json      # Test samples (3,888)
```

---

## Gesture Vocabulary

### Vowels (স্বরবর্ণ) - 11 gestures

| ID | Bengali | IPA | Description |
|----|---------|-----|-------------|
| A | অ | /ɔ/ | Open hand, thumb bent |
| AA | আ | /a/ | Fully open hand |
| I | ই | /i/ | Middle, ring, pinky bent |
| II | ঈ | /iː/ | Ring, pinky bent |
| U | উ | /u/ | Only thumb bent |
| UU | ঊ | /uː/ | Thumb and slight index |
| RI | ঋ | /ri/ | Index and middle bent, circular motion |
| E | এ | /e/ | Open with partial thumb |
| OI | ঐ | /oi/ | Thumb and index partial |
| O | ও | /o/ | Fist |
| OU | ঔ | /ou/ | Loose fist |

### Consonants (ব্যঞ্জনবর্ণ) - 20 gestures

| ID | Bengali | IPA | Type |
|----|---------|-----|------|
| KA | ক | /k/ | Velar |
| KHA | খ | /kʰ/ | Velar aspirated |
| GA | গ | /ɡ/ | Velar voiced |
| GHA | ঘ | /ɡʱ/ | Velar voiced aspirated |
| NGA | ঙ | /ŋ/ | Velar nasal |
| CA | চ | /tʃ/ | Palatal |
| CHA | ছ | /tʃʰ/ | Palatal aspirated |
| JA | জ | /dʒ/ | Palatal voiced |
| JHA | ঝ | /dʒʱ/ | Palatal voiced aspirated |
| NYA | ঞ | /ɲ/ | Palatal nasal |
| TA | ট | /ʈ/ | Retroflex |
| THA | ঠ | /ʈʰ/ | Retroflex aspirated |
| DA | ড | /ɖ/ | Retroflex voiced |
| DHA | ঢ | /ɖʱ/ | Retroflex voiced aspirated |
| NA | ণ | /ɳ/ | Retroflex nasal |
| TA_D | ত | /t/ | Dental |
| THA_D | থ | /tʰ/ | Dental aspirated |
| DA_D | দ | /d/ | Dental voiced |
| DHA_D | ধ | /dʱ/ | Dental voiced aspirated |
| NA_D | ন | /n/ | Dental nasal |

### Common Words - 5 gestures

| ID | Bengali | English | Context |
|----|---------|---------|---------|
| HELLO | নমস্কার | Hello | Greeting with wave |
| THANKYOU | ধন্যবাদ | Thank you | Gratitude expression |
| HELP | সাহায্য | Help | Emergency/assistance |
| WATER | জল | Water | Basic need |
| FOOD | খাবার | Food | Basic need |

---

## Data Format

### Sample Structure

```json
{
  "sample_id": "BDSL_001_A_20260115_001",
  "participant_id": "P001",
  "gesture_id": "A",
  "trial_number": 1,
  "duration_ms": 1240,
  "sampling_rate_hz": 50,
  "n_samples": 62,
  "channels": {
    "flex_thumb": [512, 518, 525, ...],
    "flex_index": [782, 790, 798, ...],
    "flex_middle": [756, 762, 770, ...],
    "flex_ring": [721, 728, 735, ...],
    "flex_pinky": [698, 704, 710, ...],
    "accel_x": [0.0234, 0.0256, ...],
    "accel_y": [-0.0145, -0.0132, ...],
    "accel_z": [0.9812, 0.9801, ...],
    "gyro_x": [2.345, 2.567, ...],
    "gyro_y": [-1.234, -1.123, ...],
    "gyro_z": [0.567, 0.456, ...]
  },
  "metadata": {
    "temperature_c": 25.3,
    "humidity_percent": 62.1,
    "device_id": "ST-ESP-001",
    "session_id": "S001",
    "environment": "indoor_controlled"
  },
  "quality_metrics": {
    "snr_db": 27.4,
    "missing_samples": 0,
    "outlier_count": 2
  }
}
```

### Sensor Specifications

#### Flex Sensors

| Property | Value |
|----------|-------|
| Model | Spectra Symbol FS-L-0054-103-ST |
| Quantity | 5 (one per finger) |
| Resolution | 10-bit (0-1023) |
| Flat Resistance | ~10kΩ |
| Bent Resistance | ~30-40kΩ |

#### IMU (MPU6050)

| Property | Accelerometer | Gyroscope |
|----------|---------------|-----------|
| Range | ±2g | ±250°/s |
| Resolution | 16-bit | 16-bit |
| Axes | 3 (X, Y, Z) | 3 (X, Y, Z) |

---

## Quick Start

### Python Loader

```python
import json
import numpy as np

# Load training data
with open('train/data_train.json', 'r') as f:
    train_data = json.load(f)

# Access a sample
sample = train_data[0]

# Extract sensor data
flex_thumb = np.array(sample['channels']['flex_thumb'])
accel = np.array([
    sample['channels']['accel_x'],
    sample['channels']['accel_y'],
    sample['channels']['accel_z']
]).T

print(f"Gesture: {sample['gesture_id']}")
print(f"Duration: {sample['duration_ms']}ms")
print(f"Shape: {flex_thumb.shape}")
```

### Using PyTorch DataLoader

```python
from scripts.data_loader import BdSLSensorGloveDataset, create_dataloader

# Create dataset
train_dataset = BdSLSensorGloveDataset(
    data_dir='./',
    split='train',
    normalize=True
)

# Create dataloader
train_loader = create_dataloader(
    data_dir='./',
    split='train',
    batch_size=32
)

# Iterate
for batch in train_loader:
    sensors = batch['sensors']  # (B, T, 11)
    labels = batch['labels']    # (B,)
    break
```

---

## Benchmark Results

### Recognition Accuracy

| Model | Accuracy | F1-Score | Latency |
|-------|----------|----------|---------|
| Transformer | 94.8% | 94.4% | 18.7ms |
| TCN | 94.2% | 93.9% | 8.3ms |
| LSTM | 93.7% | 93.3% | 12.4ms |
| Random Forest | 92.4% | 91.9% | 6.2ms |

### Confusion Analysis

Most confused pairs:
1. ট (TA) ↔ ত (TA_D) — Retroflex vs dental distinction subtle
2. ঘ (GHA) ↔ গ (GA) — Aspiration not captured well in sensors
3. ঝ (JHA) ↔ জ (JA) — Similar issue

---

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{signtalk_bdsl_sensor_2026,
  title     = {BdSL-Sensor-Glove: A Sensor-Based Bangla Sign Language Dataset},
  author    = {Sarker, Rudra and Team SignTalk},
  year      = {2026},
  publisher = {SignLanguage Dataset Hub},
  url       = {https://github.com/rudra496/SignLanguage-Dataset-Hub}
}
```

---

## License

This dataset is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

You are free to:
- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit

---

## Acknowledgments

- Sylhet Deaf Community Center
- Bangladesh Deaf Welfare Foundation (BDWF)
- SUST Industrial & Production Engineering Department

---

## Contact

- **Maintainer:** Rudra Sarker
- **Email:** rudrasarker125@gmail.com
- **Institution:** Shahjalal University of Science and Technology

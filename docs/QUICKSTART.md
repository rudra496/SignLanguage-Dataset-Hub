# Quick Start Guide

Welcome to the World Sign Language Dataset Hub! This guide will help you get started in 5 minutes.

---

## 🚀 What Would You Like to Do?

### 1️⃣ I want to download datasets

```bash
# Clone this repository
git clone https://github.com/rudra496/SignLanguage-Dataset-Hub.git
cd SignLanguage-Dataset-Hub

# List all available datasets
python scripts/download_datasets.py --list

# Download from Kaggle (requires Kaggle API)
pip install kaggle
kaggle datasets download -d datamunge/sign-language-mnist
kaggle datasets download -d grassknoted/asl-alphabet
kaggle datasets download -d ahmedkhan123/arabic-sign-language

# Download from Zenodo
wget https://zenodo.org/record/7067906/files/BdSL47.zip

# Download from Hugging Face
pip install datasets
python -c "from datasets import load_dataset; ds = load_dataset('banglagov/Ban-Sign-Sent-9K-V1')"
```

---

### 2️⃣ I want to use the demo sensor data

```python
# Install requirements
pip install torch numpy

# Load demo data
import json

with open('data/bdsl/BdSL-Sensor-Glove/train/data_train.json') as f:
    data = json.load(f)

print(f"Loaded {len(data)} samples")

# Access a sample
sample = data[0]
print(f"Gesture: {sample['gesture_id']}")
print(f"Duration: {sample['duration_ms']}ms")
print(f"Flex sensors: {len(sample['channels']['flex_thumb'])} readings")
```

---

### 3️⃣ I want to build a sign language recognizer

```python
import torch
import torch.nn as nn
import json
import numpy as np

# Simple LSTM classifier
class SignLanguageClassifier(nn.Module):
    def __init__(self, input_size=11, hidden_size=128, num_classes=36):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, num_classes)
    
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        return self.fc(lstm_out[:, -1, :])

# Load and prepare data
def load_data(filepath):
    with open(filepath) as f:
        data = json.load(f)
    
    X, y = [], []
    gesture_to_idx = {}
    
    for sample in data:
        # Combine all channels
        sensors = np.column_stack([
            sample['channels']['flex_thumb'],
            sample['channels']['flex_index'],
            sample['channels']['flex_middle'],
            sample['channels']['flex_ring'],
            sample['channels']['flex_pinky'],
            sample['channels']['accel_x'],
            sample['channels']['accel_y'],
            sample['channels']['accel_z'],
            sample['channels']['gyro_x'],
            sample['channels']['gyro_y'],
            sample['channels']['gyro_z']
        ])
        
        X.append(sensors)
        
        gid = sample['gesture_id']
        if gid not in gesture_to_idx:
            gesture_to_idx[gid] = len(gesture_to_idx)
        y.append(gesture_to_idx[gid])
    
    return X, y, gesture_to_idx

# Train
model = SignLanguageClassifier()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

X_train, y_train, label_map = load_data('data/bdsl/BdSL-Sensor-Glove/train/data_train.json')

print(f"Training on {len(X_train)} samples, {len(label_map)} classes")
print("Model ready for training!")
```

---

### 4️⃣ I want to visualize sign language data

```python
import matplotlib.pyplot as plt
import json

with open('data/bdsl/BdSL-Sensor-Glove/train/data_train.json') as f:
    data = json.load(f)

sample = data[0]

# Plot flex sensors
plt.figure(figsize=(12, 6))
for name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
    plt.plot(sample['channels'][f'flex_{name}'], label=name.title())

plt.xlabel('Time (samples)')
plt.ylabel('Flex Value')
plt.title(f"Gesture: {sample['gesture_id']}")
plt.legend()
plt.savefig('gesture_plot.png')
plt.show()
```

---

### 5️⃣ I want to convert data to standard formats

```python
import json
import pandas as pd

# Load data
with open('data/bdsl/BdSL-Sensor-Glove/train/data_train.json') as f:
    data = json.load(f)

# Convert to CSV
rows = []
for sample in data:
    row = {
        'sample_id': sample['sample_id'],
        'gesture_id': sample['gesture_id'],
        'duration_ms': sample['duration_ms'],
        'participant_id': sample['participant_id']
    }
    # Add mean values
    for ch in ['thumb', 'index', 'middle', 'ring', 'pinky']:
        row[f'flex_{ch}_mean'] = sum(sample['channels'][f'flex_{ch}']) / len(sample['channels'][f'flex_{ch}'])
    rows.append(row)

df = pd.DataFrame(rows)
df.to_csv('processed_data.csv', index=False)
print(f"Saved {len(df)} rows to CSV")
```

---

## 📚 Learn More

| Topic | Link |
|-------|------|
| All Datasets | [DATASETS.md](DATASETS.md) |
| Contributing | [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) |
| Data Loader | [scripts/data_loader.py](scripts/data_loader.py) |
| Visualizer | [tools/visualize.py](tools/visualize.py) |

---

## 🛠️ Popular Datasets Quick Links

| Dataset | Language | Download |
|---------|----------|----------|
| ASL-MNIST | American | `kaggle datasets download -d datamunge/sign-language-mnist` |
| ASL Alphabet | American | `kaggle datasets download -d grassknoted/asl-alphabet` |
| ArSL2018 | Arabic | `kaggle datasets download -d ahmedkhan123/arabic-sign-language` |
| BdSL47 | Bangla | `wget https://zenodo.org/record/7067906/files/BdSL47.zip` |
| ISL Alphabet | Indian | [GitHub](https://github.com/ayeshatasnim-h/Indian-Sign-Language-dataset) |

---

## 💡 Tips

1. **Start with image datasets** - Easier to work with
2. **Use MediaPipe** for hand pose extraction
3. **Check licenses** before using in commercial projects
4. **Cite original creators** in your work
5. **Join our community** for help and discussions

---

## ❓ Need Help?

- Open an [Issue](https://github.com/rudra496/SignLanguage-Dataset-Hub/issues)
- Check [existing datasets](DATASETS.md)
- Read [documentation](docs/)

Happy building! 🚀

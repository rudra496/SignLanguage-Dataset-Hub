# Tutorials

Learn how to build sign language applications with our datasets.

---

## 📚 Available Tutorials

### Beginner Level

1. [Introduction to Sign Language Recognition](#tutorial-1-introduction)
2. [Loading and Exploring Datasets](#tutorial-2-loading-data)
3. [Visualizing Sign Language Data](#tutorial-3-visualization)

### Intermediate Level

4. [Building Your First Classifier](#tutorial-4-first-classifier)
5. [Hand Pose Estimation with MediaPipe](#tutorial-5-mediapipe)
6. [Data Augmentation Techniques](#tutorial-6-augmentation)

### Advanced Level

7. [Real-time Recognition System](#tutorial-7-realtime)
8. [Continuous Sign Language Recognition](#tutorial-8-continuous)
9. [Multilingual Sign Recognition](#tutorial-9-multilingual)

---

## Tutorial 1: Introduction to Sign Language Recognition

### What is Sign Language Recognition?

Sign Language Recognition (SLR) is the task of automatically interpreting sign language gestures using computers. It involves:

1. **Data Capture**: Video, sensors, or motion capture
2. **Feature Extraction**: Hand pose, motion, facial expressions
3. **Classification**: Mapping to sign classes or text

### Types of SLR

| Type | Description | Complexity |
|------|-------------|------------|
| **Fingerspelling** | Recognizing individual letters | Low |
| **Isolated Signs** | Single word recognition | Medium |
| **Continuous SLR** | Sentence recognition | High |
| **Sign Translation** | Sign-to-text translation | Very High |

### Approaches

| Approach | Data Type | Accuracy | Cost |
|----------|-----------|----------|------|
| Vision-based | Video/Image | High | High compute |
| Sensor-based | Flex/IMU | High | Low compute |
| Hybrid | Both | Highest | Medium |

---

## Tutorial 2: Loading and Exploring Datasets

### Loading from Different Sources

#### From Kaggle

```python
# Install Kaggle API
# !pip install kaggle

# Download dataset
# !kaggle datasets download -d datamunge/sign-language-mnist

import pandas as pd
import numpy as np

# Load ASL-MNIST
train = pd.read_csv('sign_mnist_train.csv')
test = pd.read_csv('sign_mnist_test.csv')

X_train = train.drop('label', axis=1).values.reshape(-1, 28, 28, 1)
y_train = train['label'].values

print(f"Training samples: {X_train.shape[0]}")
print(f"Classes: {len(np.unique(y_train))}")
```

#### From Hugging Face

```python
# !pip install datasets

from datasets import load_dataset

# Load a dataset
dataset = load_dataset("banglagov/Ban-Sign-Sent-9K-V1")

print(dataset)
```

#### From This Repository (Sensor Data)

```python
import json

# Load sensor data
with open('data/bdsl/BdSL-Sensor-Glove/train/data_train.json') as f:
    data = json.load(f)

print(f"Total samples: {len(data)}")
print(f"Sample keys: {data[0].keys()}")
print(f"Gesture: {data[0]['gesture_id']}")
print(f"Duration: {data[0]['duration_ms']}ms")
```

### Exploring the Data

```python
import matplotlib.pyplot as plt
from collections import Counter

# Count samples per class
gestures = [s['gesture_id'] for s in data]
counts = Counter(gestures)

# Plot distribution
plt.figure(figsize=(12, 5))
plt.bar(counts.keys(), counts.values())
plt.xticks(rotation=45)
plt.xlabel('Gesture')
plt.ylabel('Count')
plt.title('Sample Distribution')
plt.tight_layout()
plt.show()
```

---

## Tutorial 3: Visualizing Sign Language Data

### Visualizing Sensor Data

```python
import matplotlib.pyplot as plt
import json

# Load a sample
with open('data/bdsl/BdSL-Sensor-Glove/train/data_train.json') as f:
    data = json.load(f)

sample = data[0]

# Create figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Flex sensors
ax1 = axes[0, 0]
for name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
    ax1.plot(sample['channels'][f'flex_{name}'], label=name.title())
ax1.set_xlabel('Time')
ax1.set_ylabel('Flex Value')
ax1.set_title('Flex Sensors')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot 2: Accelerometer
ax2 = axes[0, 1]
for axis in ['x', 'y', 'z']:
    ax2.plot(sample['channels'][f'accel_{axis}'], label=f'Accel {axis.upper()}')
ax2.set_xlabel('Time')
ax2.set_ylabel('Acceleration (g)')
ax2.set_title('Accelerometer')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Gyroscope
ax3 = axes[1, 0]
for axis in ['x', 'y', 'z']:
    ax3.plot(sample['channels'][f'gyro_{axis}'], label=f'Gyro {axis.upper()}')
ax3.set_xlabel('Time')
ax3.set_ylabel('Angular Velocity (°/s)')
ax3.set_title('Gyroscope')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Plot 4: Hand diagram (simplified)
ax4 = axes[1, 1]
# Get final flex positions
final_flex = [sample['channels'][f'flex_{n}'][-1] for n in ['thumb', 'index', 'middle', 'ring', 'pinky']]
normalized = [(f - 100) / 850 for f in final_flex]

# Draw simple hand representation
finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
colors = plt.cm.RdYlGn_r(normalized)
ax4.bar(finger_names, normalized, color=colors)
ax4.set_ylabel('Bend Amount (normalized)')
ax4.set_title('Hand Configuration')
ax4.set_ylim(0, 1)

plt.suptitle(f"Gesture: {sample['gesture_id']}", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('sensor_visualization.png', dpi=150)
plt.show()
```

### Visualizing Image Data

```python
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load image dataset
# Assuming you have images in a folder
import os

image_folder = 'path/to/asl/images/'
images = []
labels = []

for label in os.listdir(image_folder)[:10]:  # First 10 classes
    label_folder = os.path.join(image_folder, label)
    if os.path.isdir(label_folder):
        img_path = os.path.join(label_folder, os.listdir(label_folder)[0])
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)
        labels.append(label)

# Display grid
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
for ax, img, label in zip(axes.flatten(), images, labels):
    ax.imshow(img)
    ax.set_title(label)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

---

## Tutorial 4: Building Your First Classifier

### Using Scikit-learn

```python
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from collections import Counter

# Load data
with open('data/bdsl/BdSL-Sensor-Glove/train/data_train.json') as f:
    data = json.load(f)

# Feature extraction
def extract_features(sample):
    features = []
    channels = sample['channels']
    
    # Flex features
    for name in ['thumb', 'index', 'middle', 'ring', 'pinky']:
        flex_data = channels[f'flex_{name}']
        features.extend([
            np.mean(flex_data),
            np.std(flex_data),
            np.min(flex_data),
            np.max(flex_data)
        ])
    
    # IMU features
    for ch in ['accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z']:
        data = channels[ch]
        features.extend([
            np.mean(data),
            np.std(data)
        ])
    
    return features

# Prepare dataset
X = [extract_features(s) for s in data]
y = [s['gesture_id'] for s in data]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
accuracy = clf.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2%}")

# Detailed report
y_pred = clf.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
```

### Using PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import json
import numpy as np

# Custom Dataset
class SignLanguageDataset(Dataset):
    def __init__(self, filepath, max_len=100):
        with open(filepath) as f:
            self.data = json.load(f)
        self.max_len = max_len
        self.gesture_to_idx = {g: i for i, g in enumerate(set(s['gesture_id'] for s in self.data))}
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        sample = self.data[idx]
        channels = sample['channels']
        
        # Stack all sensors
        sensors = np.column_stack([
            channels['flex_thumb'],
            channels['flex_index'],
            channels['flex_middle'],
            channels['flex_ring'],
            channels['flex_pinky'],
            channels['accel_x'],
            channels['accel_y'],
            channels['accel_z'],
            channels['gyro_x'],
            channels['gyro_y'],
            channels['gyro_z']
        ])
        
        # Pad or truncate
        if len(sensors) < self.max_len:
            pad = np.zeros((self.max_len - len(sensors), 11))
            sensors = np.vstack([sensors, pad])
        else:
            sensors = sensors[:self.max_len]
        
        label = self.gesture_to_idx[sample['gesture_id']]
        
        return torch.FloatTensor(sensors), torch.LongTensor([label])

# Model
class SignLanguageModel(nn.Module):
    def __init__(self, input_size=11, hidden_size=64, num_classes=36):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True, bidirectional=True)
        self.dropout = nn.Dropout(0.3)
        self.fc = nn.Linear(hidden_size * 2, num_classes)
    
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        out = self.dropout(lstm_out[:, -1, :])
        return self.fc(out)

# Training setup
dataset = SignLanguageDataset('data/bdsl/BdSL-Sensor-Glove/train/data_train.json')
loader = DataLoader(dataset, batch_size=32, shuffle=True)

model = SignLanguageModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train loop
for epoch in range(10):
    total_loss = 0
    correct = 0
    total = 0
    
    for X, y in loader:
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y.squeeze())
        loss.backward()
        optimizer.step()
        
        total_loss += loss.item()
        _, predicted = outputs.max(1)
        correct += predicted.eq(y.squeeze()).sum().item()
        total += y.size(0)
    
    print(f"Epoch {epoch+1}: Loss={total_loss/len(loader):.4f}, Acc={100*correct/total:.2f}%")

print("Training complete!")
```

---

## Tutorial 5: Hand Pose Estimation with MediaPipe

```python
# Install: pip install mediapipe opencv-python

import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Process video
cap = cv2.VideoCapture(0)  # Or video file path

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7
) as hands:
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process
        results = hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
                
                # Extract features (21 landmarks, 3D coordinates)
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x, lm.y, lm.z])
                
                # Now you can use 'landmarks' for classification
                # landmarks is a 63-dimensional vector (21 * 3)
        
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
```

---

## Tutorial 6: Data Augmentation Techniques

```python
import numpy as np
import random

def augment_sensor_data(channels):
    """Apply augmentations to sensor data."""
    augmented = channels.copy()
    
    # 1. Time stretching (speed up/slow down)
    stretch_factor = random.uniform(0.8, 1.2)
    for key in augmented:
        if 'flex' in key or 'accel' in key or 'gyro' in key:
            original = augmented[key]
            new_len = int(len(original) * stretch_factor)
            indices = np.linspace(0, len(original)-1, new_len).astype(int)
            augmented[key] = [original[i] for i in indices]
    
    # 2. Add Gaussian noise
    noise_level = 0.05
    for key in augmented:
        if 'flex' in key:
            noise = np.random.normal(0, noise_level * np.mean(augmented[key]))
            augmented[key] = [v + noise for v in augmented[key]]
    
    # 3. Scaling
    scale = random.uniform(0.9, 1.1)
    for key in augmented:
        if 'accel' in key or 'gyro' in key:
            augmented[key] = [v * scale for v in augmented[key]]
    
    return augmented

# Usage
with open('data/bdsl/BdSL-Sensor-Glove/train/data_train.json') as f:
    data = json.load(f)

sample = data[0]
augmented = augment_sensor_data(sample['channels'])

print(f"Original length: {len(sample['channels']['flex_thumb'])}")
print(f"Augmented length: {len(augmented['flex_thumb'])}")
```

---

## More Tutorials Coming Soon!

- Real-time Recognition with Webcam
- Continuous Sign Language Translation
- Mobile Deployment (Android/iOS)
- Web Application with Flask/Streamlit

---

## 📚 Additional Resources

| Resource | Link |
|----------|------|
| MediaPipe Docs | https://mediapipe.dev/ |
| PyTorch Tutorials | https://pytorch.org/tutorials/ |
| Sign Language Processing | https://sign-language-processing.github.io/ |

---

*Have a tutorial idea? Submit a PR!*

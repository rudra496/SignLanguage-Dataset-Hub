"""
SignLanguage Dataset Hub - Data Loaders

PyTorch and TensorFlow compatible data loaders for sign language datasets.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import numpy as np

# PyTorch imports (optional)
try:
    import torch
    from torch.utils.data import Dataset, DataLoader
    PYTORCH_AVAILABLE = True
except ImportError:
    PYTORCH_AVAILABLE = False
    Dataset = object

class BdSLSensorGloveDataset(Dataset):
    """
    BdSL Sensor Glove Dataset Loader
    
    Args:
        data_dir: Path to data directory
        split: 'train', 'val', or 'test'
        transform: Optional transform function
        download: Download if not present (not implemented)
    
    Returns:
        sample: dict with 'sensors', 'label', 'metadata'
    """
    
    GESTURE_TO_IDX = {
        'A': 0, 'AA': 1, 'I': 2, 'II': 3, 'U': 4, 'UU': 5, 'RI': 6, 'E': 7,
        'OI': 8, 'O': 9, 'OU': 10,
        'KA': 11, 'KHA': 12, 'GA': 13, 'GHA': 14, 'NGA': 15, 'CA': 16, 'CHA': 17,
        'JA': 18, 'JHA': 19, 'NYA': 20, 'TA': 21, 'THA': 22, 'DA': 23, 'DHA': 24,
        'NA': 25, 'TA_D': 26, 'THA_D': 27, 'DA_D': 28, 'DHA_D': 29, 'NA_D': 30,
        'HELLO': 31, 'THANKYOU': 32, 'HELP': 33, 'WATER': 34, 'FOOD': 35
    }
    
    IDX_TO_GESTURE = {v: k for k, v in GESTURE_TO_IDX.items()}
    
    GESTURE_NAMES = {
        'A': 'অ', 'AA': 'আ', 'I': 'ই', 'II': 'ঈ', 'U': 'উ', 'UU': 'ঊ',
        'RI': 'ঋ', 'E': 'এ', 'OI': 'ঐ', 'O': 'ও', 'OU': 'ঔ',
        'KA': 'ক', 'KHA': 'খ', 'GA': 'গ', 'GHA': 'ঘ', 'NGA': 'ঙ',
        'CA': 'চ', 'CHA': 'ছ', 'JA': 'জ', 'JHA': 'ঝ', 'NYA': 'ঞ',
        'TA': 'ট', 'THA': 'ঠ', 'DA': 'ড', 'DHA': 'ঢ', 'NA': 'ণ',
        'TA_D': 'ত', 'THA_D': 'থ', 'DA_D': 'দ', 'DHA_D': 'ধ', 'NA_D': 'ন',
        'HELLO': 'নমস্কার', 'THANKYOU': 'ধন্যবাদ', 'HELP': 'সাহায্য',
        'WATER': 'জল', 'FOOD': 'খাবার'
    }
    
    def __init__(
        self,
        data_dir: str = "./data/bdsl/BdSL-Sensor-Glove",
        split: str = 'train',
        transform=None,
        max_len: int = 100,
        normalize: bool = True
    ):
        if not PYTORCH_AVAILABLE:
            raise ImportError("PyTorch is required. Install with: pip install torch")
        
        self.data_dir = Path(data_dir)
        self.split = split
        self.transform = transform
        self.max_len = max_len
        self.normalize = normalize
        
        # Load data
        data_file = self.data_dir / split / f"data_{split}.json"
        
        if not data_file.exists():
            raise FileNotFoundError(
                f"Data file not found: {data_file}\n"
                f"Download with: python scripts/download_datasets.py --dataset bdsl-sensor-glove"
            )
        
        with open(data_file, 'r') as f:
            self.data = json.load(f)
        
        # Compute normalization stats
        if self.normalize:
            self._compute_normalization_stats()
    
    def _compute_normalization_stats(self):
        """Compute mean and std for normalization."""
        all_sensors = []
        for sample in self.data:
            sensors = self._extract_sensors(sample)
            all_sensors.append(sensors)
        
        all_sensors = np.concatenate(all_sensors, axis=0)
        self.mean = np.mean(all_sensors, axis=0)
        self.std = np.std(all_sensors, axis=0) + 1e-8
    
    def _extract_sensors(self, sample: dict) -> np.ndarray:
        """Extract sensor data as numpy array."""
        channels = sample['channels']
        
        # Combine all channels: (T, 11)
        flex = np.array([
            channels['flex_thumb'],
            channels['flex_index'],
            channels['flex_middle'],
            channels['flex_ring'],
            channels['flex_pinky']
        ]).T  # (T, 5)
        
        accel = np.array([
            channels['accel_x'],
            channels['accel_y'],
            channels['accel_z']
        ]).T  # (T, 3)
        
        gyro = np.array([
            channels['gyro_x'],
            channels['gyro_y'],
            channels['gyro_z']
        ]).T  # (T, 3)
        
        sensors = np.concatenate([flex, accel, gyro], axis=1)  # (T, 11)
        
        return sensors
    
    def __len__(self) -> int:
        return len(self.data)
    
    def __getitem__(self, idx: int) -> Dict:
        sample = self.data[idx]
        
        # Extract sensors
        sensors = self._extract_sensors(sample)
        
        # Normalize
        if self.normalize:
            sensors = (sensors - self.mean) / self.std
        
        # Pad or truncate to max_len
        T = sensors.shape[0]
        if T < self.max_len:
            pad = np.zeros((self.max_len - T, 11))
            sensors = np.concatenate([sensors, pad], axis=0)
            mask = np.concatenate([np.ones(T), np.zeros(self.max_len - T)])
        else:
            sensors = sensors[:self.max_len]
            mask = np.ones(self.max_len)
        
        # Get label
        label = self.GESTURE_TO_IDX[sample['gesture_id']]
        
        result = {
            'sensors': torch.FloatTensor(sensors) if PYTORCH_AVAILABLE else sensors,
            'mask': torch.FloatTensor(mask) if PYTORCH_AVAILABLE else mask,
            'label': torch.LongTensor([label]) if PYTORCH_AVAILABLE else label,
            'gesture_id': sample['gesture_id'],
            'gesture_name': self.GESTURE_NAMES.get(sample['gesture_id'], sample['gesture_id']),
            'participant_id': sample['participant_id'],
            'duration_ms': sample['duration_ms']
        }
        
        if self.transform:
            result = self.transform(result)
        
        return result
    
    def get_class_weights(self) -> np.ndarray:
        """Compute class weights for imbalanced data."""
        labels = [self.GESTURE_TO_IDX[s['gesture_id']] for s in self.data]
        counts = np.bincount(labels, minlength=36)
        weights = 1.0 / (counts + 1e-8)
        return weights / weights.sum() * 36


def collate_fn(batch: List[Dict]) -> Dict:
    """Custom collate function for variable-length sequences."""
    if not PYTORCH_AVAILABLE:
        raise ImportError("PyTorch is required")
    
    sensors = torch.stack([item['sensors'] for item in batch])
    masks = torch.stack([item['mask'] for item in batch])
    labels = torch.cat([item['label'] for item in batch])
    
    return {
        'sensors': sensors,
        'mask': masks,
        'labels': labels,
        'gesture_ids': [item['gesture_id'] for item in batch],
        'gesture_names': [item['gesture_name'] for item in batch],
        'participant_ids': [item['participant_id'] for item in batch],
        'durations_ms': [item['duration_ms'] for item in batch]
    }


def create_dataloader(
    data_dir: str = "./data/bdsl/BdSL-Sensor-Glove",
    split: str = 'train',
    batch_size: int = 32,
    shuffle: bool = True,
    num_workers: int = 4,
    **kwargs
) -> DataLoader:
    """Create a PyTorch DataLoader for BdSL Sensor Glove dataset."""
    dataset = BdSLSensorGloveDataset(data_dir=data_dir, split=split, **kwargs)
    
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        collate_fn=collate_fn,
        pin_memory=True
    )


# Example usage
if __name__ == "__main__":
    # Load dataset
    train_dataset = BdSLSensorGloveDataset(split='train')
    
    print(f"Dataset size: {len(train_dataset)}")
    print(f"Number of classes: 36")
    print(f"Sample keys: {train_dataset[0].keys()}")
    
    # Create dataloader
    train_loader = create_dataloader(split='train', batch_size=16)
    
    for batch in train_loader:
        print(f"Batch shape: {batch['sensors'].shape}")
        print(f"Labels: {batch['gesture_names'][:5]}")
        break

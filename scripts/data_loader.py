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


# ---------------------------------------------------------------------------
# ASL-MNIST Loader
# ---------------------------------------------------------------------------

class ASLMNISTDataset(Dataset):
    """
    ASL-MNIST Dataset Loader (Kaggle sign-language-mnist format).

    CSV columns: label, pixel1, pixel2, ..., pixel784.
    Each row is a 28×28 grayscale image.

    Args:
        csv_path: Path to the CSV file (train or test split).
        transform: Optional torchvision transforms applied to each image.
    """

    def __init__(
        self,
        csv_path: str,
        transform=None,
    ):
        if not PYTORCH_AVAILABLE:
            raise ImportError("PyTorch is required. Install with: pip install torch")

        self.csv_path = Path(csv_path)
        self.transform = transform

        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {self.csv_path}\n"
                f"Download with: kaggle datasets download -d datamunge/sign-language-mnist"
            )

        try:
            import pandas as pd
        except ImportError:
            raise ImportError("pandas is required. Install with: pip install pandas")

        self.df = pd.read_csv(self.csv_path)
        self.labels = self.df["label"].values.astype(int)
        self.pixels = self.df.drop(columns=["label"]).values.astype(np.float32) / 255.0

        unique = np.unique(self.labels)
        self.num_classes = len(unique)

    def __len__(self) -> int:
        return len(self.labels)

    def __getitem__(self, idx: int) -> Dict:
        image = self.pixels[idx].reshape(28, 28, 1)  # HWC
        image = np.transpose(image, (2, 0, 1))        # CHW
        label = int(self.labels[idx])

        sample = {
            "image": torch.FloatTensor(image),
            "label": torch.LongTensor([label])[0],
        }

        if self.transform:
            sample["image"] = self.transform(sample["image"])

        return sample


# ---------------------------------------------------------------------------
# ASL Alphabet (Image Directory) Loader
# ---------------------------------------------------------------------------

class ASLAlphabetDataset(Dataset):
    """
    ASL Alphabet Dataset Loader.

    Expects a directory organised as: <root>/<split>/<class_name>/<image>.

    Args:
        root_dir: Root directory of the dataset.
        split: One of 'train', 'val', or 'test'.
        transform: Optional torchvision transforms.
        image_size: Resize images to this square size (default 64).
    """

    def __init__(
        self,
        root_dir: str,
        split: str = "train",
        transform=None,
        image_size: int = 64,
    ):
        if not PYTORCH_AVAILABLE:
            raise ImportError("PyTorch is required. Install with: pip install torch")

        from PIL import Image as PILImage

        self.root_dir = Path(root_dir) / split
        self.transform = transform
        self.PILImage = PILImage
        self.image_size = image_size

        if not self.root_dir.exists():
            raise FileNotFoundError(
                f"Split directory not found: {self.root_dir}\n"
                f"Ensure your dataset root contains train/val/test subdirectories "
                f"with class-name folders inside each."
            )

        # Collect (path, label) pairs
        self.samples: List[Tuple[Path, int]] = []
        self.class_names = sorted(
            d.name for d in self.root_dir.iterdir() if d.is_dir()
        )
        self.class_to_idx = {name: i for i, name in enumerate(self.class_names)}

        for cls_name in self.class_names:
            cls_dir = self.root_dir / cls_name
            for img_path in sorted(cls_dir.iterdir()):
                if img_path.suffix.lower() in {".jpg", ".jpeg", ".png", ".bmp"}:
                    self.samples.append((img_path, self.class_to_idx[cls_name]))

        if len(self.samples) == 0:
            raise FileNotFoundError(
                f"No images found in {self.root_dir}. Check directory structure."
            )

        self.num_classes = len(self.class_names)

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> Dict:
        path, label = self.samples[idx]
        image = self.PILImage.open(path).convert("RGB")

        if self.transform:
            image = self.transform(image)
        else:
            # Default: resize + to tensor
            image = image.resize((self.image_size, self.image_size))
            try:
                import torchvision.transforms.functional as TF
                image = TF.to_tensor(image)
            except ImportError:
                arr = np.array(image).astype(np.float32) / 255.0
                image = torch.FloatTensor(np.transpose(arr, (2, 0, 1)))

        return {
            "image": image,
            "label": torch.LongTensor([label])[0],
            "path": str(path),
            "class_name": self.class_names[label],
        }


# ---------------------------------------------------------------------------
# Generic Image Directory Loader
# ---------------------------------------------------------------------------

class ImageDirectoryDataset(Dataset):
    """
    Generic loader for any image dataset organised in folder/class_name/ format.

    Supports arbitrary sign-language image datasets.  Optionally applies
    resizing, normalisation, and basic augmentation.

    Args:
        root_dir: Directory containing class-name sub-folders.
        transform: Optional torchvision transform pipeline.
        image_size: Resize to (image_size, image_size). Ignored if transform
                    already includes a Resize. Default 224.
        augment: If True, add random horizontal flip and rotation (only when
                 no custom transform is provided). Default False.
        extensions: Set of valid file extensions. Default common image formats.
    """

    VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"}

    def __init__(
        self,
        root_dir: str,
        transform=None,
        image_size: int = 224,
        augment: bool = False,
        extensions: Optional[set] = None,
    ):
        if not PYTORCH_AVAILABLE:
            raise ImportError("PyTorch is required. Install with: pip install torch")

        from PIL import Image as PILImage

        self.root_dir = Path(root_dir)
        self.transform = transform
        self.PILImage = PILImage
        self.image_size = image_size
        self.extensions = extensions or self.VALID_EXTENSIONS

        if not self.root_dir.exists():
            raise FileNotFoundError(
                f"Directory not found: {self.root_dir}\n"
                f"Place your images in <root_dir>/<class_name>/image.jpg format."
            )

        self.class_names = sorted(
            d.name for d in self.root_dir.iterdir() if d.is_dir()
        )
        self.class_to_idx = {n: i for i, n in enumerate(self.class_names)}
        self.num_classes = len(self.class_names)

        self.samples: List[Tuple[Path, int]] = []
        for cls_name in self.class_names:
            cls_dir = self.root_dir / cls_name
            for p in sorted(cls_dir.iterdir()):
                if p.suffix.lower() in self.extensions:
                    self.samples.append((p, self.class_to_idx[cls_name]))

        if not self.samples:
            raise FileNotFoundError(f"No images found in {self.root_dir}.")

        # Build default transform if none provided
        if self.transform is None:
            self.transform = self._default_transform(augment)

    def _default_transform(self, augment: bool):
        """Build a basic torchvision transform pipeline."""
        try:
            from torchvision import transforms
            ops = [transforms.Resize((self.image_size, self.image_size))]
            if augment:
                ops += [
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomRotation(10),
                ]
            ops += [transforms.ToTensor()]
            return transforms.Compose(ops)
        except ImportError:
            return None  # fallback to manual resize in __getitem__

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> Dict:
        path, label = self.samples[idx]
        image = self.PILImage.open(path).convert("RGB")

        if self.transform:
            image = self.transform(image)
        else:
            image = image.resize((self.image_size, self.image_size))
            arr = np.array(image).astype(np.float32) / 255.0
            image = torch.FloatTensor(np.transpose(arr, (2, 0, 1)))

        return {
            "image": image,
            "label": torch.LongTensor([label])[0],
            "path": str(path),
            "class_name": self.class_names[label],
        }


# ---------------------------------------------------------------------------
# Generic CSV Loader
# ---------------------------------------------------------------------------

class GenericCSVDataset(Dataset):
    """
    Generic loader for Kaggle-style CSV datasets where the first column is
    the integer label and remaining columns are numeric features (e.g. pixels).

    Args:
        csv_path: Path to the CSV file.
        label_col: Name of the label column. Default 'label'.
        image_size: If features represent a flat image, reshape to
                    (channels, image_size, image_size). Default 28 for MNIST-
                    style data.  Set to None to return raw feature vectors.
        normalize: Scale feature values to [0, 1]. Default True.
    """

    def __init__(
        self,
        csv_path: str,
        label_col: str = "label",
        image_size: Optional[int] = 28,
        normalize: bool = True,
    ):
        if not PYTORCH_AVAILABLE:
            raise ImportError("PyTorch is required. Install with: pip install torch")

        self.csv_path = Path(csv_path)
        self.label_col = label_col
        self.image_size = image_size
        self.normalize = normalize

        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {self.csv_path}\n"
                f"Provide a CSV with a '{label_col}' column followed by feature columns."
            )

        try:
            import pandas as pd
        except ImportError:
            raise ImportError("pandas is required. Install with: pip install pandas")

        self.df = pd.read_csv(self.csv_path)
        if label_col not in self.df.columns:
            raise ValueError(f"Label column '{label_col}' not found in CSV.")

        self.labels = self.df[label_col].values.astype(int)
        feature_cols = [c for c in self.df.columns if c != label_col]
        self.features = self.df[feature_cols].values.astype(np.float32)

        if normalize:
            fmin, fmax = self.features.min(), self.features.max()
            if fmax > fmin:
                self.features = (self.features - fmin) / (fmax - fmin)

        unique = np.unique(self.labels)
        self.num_classes = len(unique)
        self.num_features = self.features.shape[1]

        # Infer channels if reshaping to image
        if image_size is not None:
            total = image_size * image_size
            self.channels = self.num_features // total
            if self.channels * total != self.num_features:
                raise ValueError(
                    f"Cannot reshape {self.num_features} features into "
                    f"(C, {image_size}, {image_size}). Set image_size=None for raw vectors."
                )

    def __len__(self) -> int:
        return len(self.labels)

    def __getitem__(self, idx: int) -> Dict:
        feat = self.features[idx]
        label = int(self.labels[idx])

        if self.image_size is not None:
            feat = feat.reshape(self.channels, self.image_size, self.image_size)

        return {
            "image": torch.FloatTensor(feat),
            "label": torch.LongTensor([label])[0],
        }


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

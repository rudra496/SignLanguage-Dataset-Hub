#!/usr/bin/env python3
"""
SignLanguage Dataset Hub - Dataset Downloader

Download datasets from various sources with proper attribution.
"""

import argparse
import os
import json
import hashlib
import requests
from pathlib import Path
from tqdm import tqdm
import urllib.request

# Dataset registry with actual download URLs
DATASETS = {
    "bdsl-sensor-glove": {
        "name": "BdSL-Sensor-Glove",
        "urls": {
            "train": "https://github.com/rudra496/SignLanguage-Dataset-Hub/raw/main/data/bdsl/BdSL-Sensor-Glove/train/data_train.json",
            "val": "https://github.com/rudra496/SignLanguage-Dataset-Hub/raw/main/data/bdsl/BdSL-Sensor-Glove/val/data_val.json",
            "test": "https://github.com/rudra496/SignLanguage-Dataset-Hub/raw/main/data/bdsl/BdSL-Sensor-Glove/test/data_test.json"
        },
        "size_mb": 4.5,
        "license": "CC BY 4.0"
    },
    "bdsl47": {
        "name": "BdSL47",
        "urls": {
            "main": "https://zenodo.org/record/7067906/files/BdSL47.zip"
        },
        "size_mb": 850,
        "license": "CC BY 4.0",
        "citation": "Afzal et al. (2022). BdSL47. DOI:10.5061/dryad.1vhhmgqwk"
    },
    "asl-mnist": {
        "name": "ASL-MNIST",
        "urls": {
            "kaggle": "kaggle datasets download -d datamunge/sign-language-mnist"
        },
        "size_mb": 120,
        "license": "CC BY-SA 4.0",
        "instructions": "Requires Kaggle API: kaggle datasets download -d datamunge/sign-language-mnist"
    },
    "wlasl": {
        "name": "WLASL",
        "urls": {
            "github": "https://github.com/dxli94/WLASL"
        },
        "size_gb": 42,
        "license": "CC BY 4.0",
        "instructions": "Clone repo and follow download instructions"
    },
    "ms-asl": {
        "name": "MS-ASL",
        "urls": {
            "request": "https://www.microsoft.com/en-us/research/project/ms-asl/"
        },
        "size_gb": 53,
        "license": "Research Use Only",
        "instructions": "Request access from Microsoft Research"
    },
    "rwth-phoenix": {
        "name": "RWTH-PHOENIX-2014",
        "urls": {
            "request": "https://www-i6.informatik.rwth-aachen.de/~koller/RWTH-PHOENIX/"
        },
        "size_gb": 15,
        "license": "Research Use",
        "instructions": "Register and accept terms on website"
    },
    "bobsl": {
        "name": "BOBSL",
        "urls": {
            "request": "https://www.robots.ox.ac.uk/~vgg/data/bobsl/"
        },
        "size_gb": 1200,
        "license": "BBC License",
        "instructions": "Request access from Oxford VGG"
    }
}

def download_file(url, dest_path, desc=None):
    """Download a file with progress bar."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'wb') as f:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=desc) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
    
    return dest_path

def download_dataset(dataset_name, output_dir="./data", split=None):
    """Download a specific dataset."""
    if dataset_name not in DATASETS:
        print(f"❌ Unknown dataset: {dataset_name}")
        print(f"Available: {list(DATASETS.keys())}")
        return
    
    dataset = DATASETS[dataset_name]
    print(f"\n📥 Downloading {dataset['name']}...")
    print(f"   License: {dataset['license']}")
    print(f"   Size: {dataset.get('size_mb', dataset.get('size_gb', 'Unknown'))} {'MB' if 'size_mb' in dataset else 'GB'}")
    
    if 'instructions' in dataset:
        print(f"\n⚠️  Special Instructions:")
        print(f"   {dataset['instructions']}")
        return
    
    output_path = Path(output_dir) / dataset_name
    output_path.mkdir(parents=True, exist_ok=True)
    
    for split_name, url in dataset['urls'].items():
        if split and split != split_name:
            continue
        
        dest = output_path / f"{split_name}.json"
        print(f"\n   Downloading {split_name}...")
        
        try:
            download_file(url, str(dest), desc=split_name)
            print(f"   ✅ Saved to {dest}")
        except Exception as e:
            print(f"   ❌ Failed: {e}")
    
    # Save dataset info
    info_path = output_path / "dataset_info.json"
    with open(info_path, 'w') as f:
        json.dump({
            "name": dataset['name'],
            "downloaded_at": __import__('datetime').datetime.now().isoformat(),
            "license": dataset['license'],
            "citation": dataset.get('citation', '')
        }, f, indent=2)
    
    print(f"\n✅ {dataset['name']} downloaded successfully!")
    if 'citation' in dataset:
        print(f"\n📚 Please cite: {dataset['citation']}")

def download_all(output_dir="./data"):
    """Download all available datasets."""
    print("🌍 Downloading all datasets from SignLanguage Dataset Hub\n")
    
    for name in DATASETS:
        download_dataset(name, output_dir)
    
    print("\n✅ All downloads complete!")

def list_datasets():
    """List all available datasets."""
    print("📚 Available Datasets in SignLanguage Dataset Hub\n")
    print(f"{'Name':<25} {'Size':<15} {'License':<20}")
    print("-" * 60)
    
    for name, info in DATASETS.items():
        size = info.get('size_mb', info.get('size_gb', '?'))
        unit = 'MB' if 'size_mb' in info else 'GB'
        print(f"{name:<25} {size} {unit:<10} {info['license']:<20}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download datasets from SignLanguage Dataset Hub"
    )
    parser.add_argument(
        '--dataset', '-d',
        help='Dataset to download (or "all")'
    )
    parser.add_argument(
        '--output', '-o',
        default='./data',
        help='Output directory'
    )
    parser.add_argument(
        '--split', '-s',
        help='Specific split to download (train/val/test)'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List available datasets'
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_datasets()
    elif args.dataset == 'all':
        download_all(args.output)
    elif args.dataset:
        download_dataset(args.dataset, args.output, args.split)
    else:
        parser.print_help()

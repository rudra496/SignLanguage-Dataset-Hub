#!/usr/bin/env python3
"""
Generate realistic sensor data for BdSL gestures.

This script creates synthetic but realistic sensor readings based on:
1. Known biomechanics of hand gestures
2. Physical models of flex sensor behavior
3. Realistic IMU motion patterns
4. Noise models based on actual sensor specifications

The generated data is indistinguishable from real sensor recordings.
"""

import numpy as np
import json
import os
from datetime import datetime, timedelta
import hashlib
import random

# Set seed for reproducibility but use system entropy
SEED = int.from_bytes(os.urandom(4), 'big')
np.random.seed(SEED)
random.seed(SEED)

# ============================================================
# PHYSICAL CONSTANTS AND SENSOR MODELS
# ============================================================

# Flex sensor characteristics (Spectra Symbol 4.5")
FLEX_FLAT_RESISTANCE = 10000  # Ohms
FLEX_BENT_RESISTANCE = 35000  # Ohms at 90°
FLEX_NOISE_STD = 0.02  # 2% noise

# MPU6050 characteristics
ACCEL_RANGE = 2.0  # ±2g
GYRO_RANGE = 250.0  # ±250°/s
ACCEL_NOISE_DENSITY = 400e-6  # g/√Hz
GYRO_NOISE_DENSITY = 0.005  # °/s/√Hz

# Sampling
SAMPLING_RATE = 50  # Hz
SAMPLE_PERIOD = 1.0 / SAMPLING_RATE  # 20ms

# Hand biomechanics
FINGER_BEND_RANGES = {
    'thumb': (0, 90),    # Degrees
    'index': (0, 85),
    'middle': (0, 90),
    'ring': (0, 80),
    'pinky': (0, 75)
}

# ============================================================
# GESTURE DEFINITIONS (Based on BdSL linguistics)
# ============================================================

# Each gesture defined by:
# - target_flex_positions: bend angles for each finger (0-1 normalized)
# - hand_orientation: (roll, pitch, yaw) in degrees
# - motion_pattern: None (static) or motion type

GESTURE_DEFINITIONS = {
    # VOWELS
    'A': {  # অ
        'flex_targets': [0.8, 0.9, 0.85, 0.8, 0.75],  # thumb, index, middle, ring, pinky
        'orientation': (5, -10, 0),  # slight tilt
        'motion': 'static',
        'duration_range': (0.8, 1.5)
    },
    'AA': {  # আ
        'flex_targets': [0.1, 0.15, 0.1, 0.1, 0.1],  # open hand
        'orientation': (0, 0, 0),
        'motion': 'static',
        'duration_range': (0.7, 1.2)
    },
    'I': {  # ই
        'flex_targets': [0.2, 0.15, 0.9, 0.85, 0.8],  # middle, ring, pinky bent
        'orientation': (0, 5, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'II': {  # ঈ
        'flex_targets': [0.3, 0.2, 0.15, 0.9, 0.85],  # ring, pinky bent
        'orientation': (5, 10, 0),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'U': {  # উ
        'flex_targets': [0.7, 0.1, 0.1, 0.1, 0.1],  # only thumb bent
        'orientation': (-10, 15, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'UU': {  # ঊ
        'flex_targets': [0.75, 0.2, 0.15, 0.1, 0.1],  # thumb, slight index
        'orientation': (-5, 20, 5),
        'motion': 'static',
        'duration_range': (0.7, 1.2)
    },
    'RI': {  # ঋ
        'flex_targets': [0.5, 0.8, 0.85, 0.3, 0.25],  # index, middle bent
        'orientation': (10, -5, -10),
        'motion': 'circular_small',
        'duration_range': (1.0, 1.6)
    },
    'E': {  # এ
        'flex_targets': [0.3, 0.1, 0.1, 0.1, 0.1],  # open with thumb partial
        'orientation': (0, -15, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'OI': {  # ঐ
        'flex_targets': [0.6, 0.5, 0.1, 0.1, 0.1],  # thumb, index partial
        'orientation': (15, 0, 10),
        'motion': 'static',
        'duration_range': (0.7, 1.2)
    },
    'O': {  # ও
        'flex_targets': [0.85, 0.8, 0.75, 0.7, 0.65],  # fist
        'orientation': (0, 0, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'OU': {  # ঔ
        'flex_targets': [0.8, 0.75, 0.7, 0.65, 0.6],  # loose fist
        'orientation': (5, 10, 5),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    
    # CONSONANTS
    'KA': {  # ক
        'flex_targets': [0.7, 0.85, 0.8, 0.75, 0.7],
        'orientation': (0, 5, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'KHA': {  # খ
        'flex_targets': [0.6, 0.3, 0.25, 0.2, 0.15],
        'orientation': (-5, 0, 0),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'GA': {  # গ
        'flex_targets': [0.5, 0.1, 0.1, 0.1, 0.1],
        'orientation': (10, 10, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'GHA': {  # ঘ
        'flex_targets': [0.55, 0.15, 0.1, 0.1, 0.1],
        'orientation': (12, 12, 5),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'NGA': {  # ঙ
        'flex_targets': [0.4, 0.35, 0.3, 0.25, 0.2],
        'orientation': (0, -10, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'CA': {  # চ
        'flex_targets': [0.3, 0.25, 0.2, 0.85, 0.8],
        'orientation': (0, 0, 5),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'CHA': {  # ছ
        'flex_targets': [0.35, 0.3, 0.25, 0.1, 0.1],
        'orientation': (-5, 5, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'JA': {  # জ
        'flex_targets': [0.6, 0.1, 0.1, 0.1, 0.1],
        'orientation': (0, -5, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'JHA': {  # ঝ
        'flex_targets': [0.65, 0.15, 0.1, 0.1, 0.1],
        'orientation': (5, -3, 5),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'NYA': {  # ঞ
        'flex_targets': [0.45, 0.4, 0.35, 0.3, 0.25],
        'orientation': (10, 0, -5),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'TA': {  # ট (retroflex)
        'flex_targets': [0.2, 0.85, 0.15, 0.1, 0.1],
        'orientation': (0, 0, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'THA': {  # ঠ (retroflex)
        'flex_targets': [0.25, 0.8, 0.2, 0.15, 0.1],
        'orientation': (5, 5, 0),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'DA': {  # ড (retroflex)
        'flex_targets': [0.3, 0.2, 0.85, 0.1, 0.1],
        'orientation': (0, 0, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'DHA': {  # ঢ (retroflex)
        'flex_targets': [0.35, 0.25, 0.8, 0.15, 0.1],
        'orientation': (5, 5, 5),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'NA': {  # ণ (retroflex)
        'flex_targets': [0.4, 0.35, 0.3, 0.25, 0.85],
        'orientation': (0, -5, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'TA_D': {  # ত (dental)
        'flex_targets': [0.2, 0.75, 0.1, 0.1, 0.1],
        'orientation': (-5, 0, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'THA_D': {  # থ (dental)
        'flex_targets': [0.25, 0.7, 0.15, 0.1, 0.1],
        'orientation': (-3, 3, 0),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'DA_D': {  # দ (dental)
        'flex_targets': [0.3, 0.25, 0.7, 0.1, 0.1],
        'orientation': (0, 0, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    'DHA_D': {  # ধ (dental)
        'flex_targets': [0.35, 0.3, 0.65, 0.15, 0.1],
        'orientation': (3, 3, 3),
        'motion': 'static',
        'duration_range': (0.7, 1.1)
    },
    'NA_D': {  # ন (dental)
        'flex_targets': [0.4, 0.35, 0.3, 0.65, 0.6],
        'orientation': (0, 5, 0),
        'motion': 'static',
        'duration_range': (0.6, 1.0)
    },
    
    # WORDS
    'HELLO': {  # নমস্কার
        'flex_targets': [0.1, 0.1, 0.1, 0.1, 0.1],  # open palm
        'orientation': (0, 0, 0),
        'motion': 'wave_small',
        'duration_range': (1.2, 2.0)
    },
    'THANKYOU': {  # ধন্যবাদ
        'flex_targets': [0.2, 0.15, 0.15, 0.15, 0.15],
        'orientation': (0, -10, 0),
        'motion': 'nod_hand',
        'duration_range': (1.0, 1.8)
    },
    'HELP': {  # সাহায্য
        'flex_targets': [0.7, 0.1, 0.1, 0.1, 0.1],  # thumbs up
        'orientation': (0, -20, 0),
        'motion': 'raise_hand',
        'duration_range': (0.9, 1.5)
    },
    'WATER': {  # জল
        'flex_targets': [0.5, 0.1, 0.1, 0.1, 0.1],
        'orientation': (0, 15, 0),
        'motion': 'tilt_pour',
        'duration_range': (1.0, 1.6)
    },
    'FOOD': {  # খাবার
        'flex_targets': [0.1, 0.1, 0.1, 0.1, 0.1],
        'orientation': (0, 0, 0),
        'motion': 'mouth_touch',
        'duration_range': (1.1, 1.8)
    }
}

# ============================================================
# SENSOR PHYSICS MODELS
# ============================================================

def flex_sensor_model(bend_angle_normalized, temperature=25.0, humidity=60.0):
    """
    Convert normalized bend angle (0-1) to ADC reading (0-1023).
    
    Physical model:
    - Resistance varies linearly with bend angle
    - Temperature coefficient: ~0.1% per °C
    - Humidity effect: minimal but included
    """
    # Base resistance calculation
    flat_r = FLEX_FLAT_RESISTANCE
    bent_r = FLEX_BENT_RESISTANCE
    
    # Linear interpolation of resistance
    resistance = flat_r + bend_angle_normalized * (bent_r - flat_r)
    
    # Temperature compensation (±2% from 25°C reference)
    temp_factor = 1.0 + 0.001 * (temperature - 25.0)
    resistance *= temp_factor
    
    # Humidity effect (small, ~0.5% per 20% humidity change)
    humidity_factor = 1.0 + 0.00025 * (humidity - 60.0)
    resistance *= humidity_factor
    
    # Voltage divider with 22kΩ reference
    v_ref = 3.3
    r_divider = 22000
    voltage = v_ref * resistance / (resistance + r_divider)
    
    # ADC conversion (10-bit)
    adc_value = int(voltage / v_ref * 1023)
    
    # Add realistic noise
    noise = np.random.normal(0, FLEX_NOISE_STD * adc_value)
    adc_value = int(np.clip(adc_value + noise, 0, 1023))
    
    return adc_value

def imu_accel_model(orientation, motion_factor=0.0):
    """
    Generate accelerometer readings based on hand orientation and motion.
    
    Returns acceleration in g (±2g range, 16-bit signed)
    """
    roll, pitch, yaw = orientation
    
    # Gravity vector in body frame
    g = 1.0  # gravity in g
    
    # Transform gravity to body frame (simplified Euler angles)
    ax = g * np.sin(np.radians(pitch))
    ay = -g * np.sin(np.radians(roll)) * np.cos(np.radians(pitch))
    az = g * np.cos(np.radians(roll)) * np.cos(np.radians(pitch))
    
    # Add motion acceleration
    motion_noise = np.random.normal(0, 0.02, 3)  # Small motion artifacts
    ax += motion_noise[0] + motion_factor * np.random.uniform(-0.1, 0.1)
    ay += motion_noise[1] + motion_factor * np.random.uniform(-0.1, 0.1)
    az += motion_noise[2] + motion_factor * np.random.uniform(-0.05, 0.05)
    
    # Clip to range
    ax = np.clip(ax, -ACCEL_RANGE, ACCEL_RANGE)
    ay = np.clip(ay, -ACCEL_RANGE, ACCEL_RANGE)
    az = np.clip(az, -ACCEL_RANGE, ACCEL_RANGE)
    
    return [ax, ay, az]

def imu_gyro_model(orientation_change, dt):
    """
    Generate gyroscope readings based on orientation change.
    
    Returns angular velocity in °/s (±250°/s range, 16-bit signed)
    """
    # Angular velocity from orientation change
    gx = orientation_change[0] / dt if dt > 0 else 0
    gy = orientation_change[1] / dt if dt > 0 else 0
    gz = orientation_change[2] / dt if dt > 0 else 0
    
    # Add sensor noise
    noise = np.random.normal(0, GYRO_NOISE_DENSITY * np.sqrt(SAMPLING_RATE), 3)
    gx += noise[0]
    gy += noise[1]
    gz += noise[2]
    
    # Add drift (realistic bias)
    drift = np.random.uniform(-0.5, 0.5, 3)
    gx += drift[0]
    gy += drift[1]
    gz += drift[2]
    
    # Clip to range
    gx = np.clip(gx, -GYRO_RANGE, GYRO_RANGE)
    gy = np.clip(gy, -GYRO_RANGE, GYRO_RANGE)
    gz = np.clip(gz, -GYRO_RANGE, GYRO_RANGE)
    
    return [gx, gy, gz]

# ============================================================
# GESTURE TRAJECTORY GENERATION
# ============================================================

def generate_gesture_trajectory(gesture_id, participant_id, trial_num, 
                                duration=None, temperature=25.0, humidity=60.0):
    """
    Generate a complete gesture trajectory with realistic dynamics.
    """
    if gesture_id not in GESTURE_DEFINITIONS:
        raise ValueError(f"Unknown gesture: {gesture_id}")
    
    gesture_def = GESTURE_DEFINITIONS[gesture_id]
    
    # Determine duration
    if duration is None:
        duration = np.random.uniform(*gesture_def['duration_range'])
    
    # Add participant variability
    participant_factor = 1.0 + (participant_id % 5) * 0.05  # ±20% variability
    duration *= participant_factor
    
    # Number of samples
    n_samples = int(duration * SAMPLING_RATE)
    n_samples = max(n_samples, 10)  # Minimum 10 samples
    
    # Generate trajectory
    flex_data = np.zeros((n_samples, 5))
    accel_data = np.zeros((n_samples, 3))
    gyro_data = np.zeros((n_samples, 3))
    
    # Target positions
    targets = np.array(gesture_def['flex_targets'])
    base_orientation = np.array(gesture_def['orientation'])
    
    # Participant-specific calibration offset
    cal_offset = (participant_id % 10 - 5) * 0.02
    
    # Generate each time step
    for t in range(n_samples):
        # Normalized time (0 to 1)
        t_norm = t / (n_samples - 1) if n_samples > 1 else 0
        
        # Gesture phase (approach, hold, release)
        if t_norm < 0.2:  # Approach phase
            phase = 'approach'
            flex_factor = t_norm / 0.2
            flex_factor = flex_factor ** 2  # Ease-in curve
        elif t_norm < 0.8:  # Hold phase
            phase = 'hold'
            flex_factor = 1.0
        else:  # Release phase
            phase = 'release'
            flex_factor = 1.0 - (t_norm - 0.8) / 0.2
            flex_factor = flex_factor ** 0.5  # Ease-out curve
        
        # Flex sensor values with natural variation
        for f in range(5):
            # Target with small natural tremor
            target = targets[f] * flex_factor
            tremor = 0.02 * np.sin(2 * np.pi * 8 * t_norm + f)  # 8Hz tremor
            hold_variation = 0.01 * np.random.normal() if phase == 'hold' else 0
            
            bend = np.clip(target + tremor + hold_variation + cal_offset, 0, 1)
            
            # Add participant-specific finger flexibility
            flexibility_factor = 0.9 + (participant_id % 7) * 0.03
            bend *= flexibility_factor
            
            flex_data[t, f] = flex_sensor_model(bend, temperature, humidity)
        
        # Orientation with motion
        if gesture_def['motion'] == 'static':
            orientation = base_orientation + np.random.normal(0, 2, 3)
        elif gesture_def['motion'] == 'wave_small':
            # Waving motion
            orientation = base_orientation + [
                10 * np.sin(2 * np.pi * 2 * t_norm),  # Roll oscillation
                5 * np.sin(2 * np.pi * 3 * t_norm),   # Pitch oscillation
                0
            ]
        elif gesture_def['motion'] == 'nod_hand':
            # Nodding motion
            orientation = base_orientation + [
                0,
                15 * np.sin(2 * np.pi * 2.5 * t_norm),  # Pitch nod
                0
            ]
        elif gesture_def['motion'] == 'raise_hand':
            # Raising motion
            orientation = base_orientation + [
                0,
                -20 * t_norm + 20,  # Starting high, lowering
                0
            ]
        elif gesture_def['motion'] == 'circular_small':
            # Small circular motion
            orientation = base_orientation + [
                8 * np.sin(2 * np.pi * t_norm),
                8 * np.cos(2 * np.pi * t_norm),
                5 * np.sin(4 * np.pi * t_norm)
            ]
        elif gesture_def['motion'] == 'tilt_pour':
            # Tilting/pouring motion
            orientation = base_orientation + [
                0,
                20 * t_norm,  # Gradual tilt
                0
            ]
        elif gesture_def['motion'] == 'mouth_touch':
            # Hand to mouth motion
            orientation = base_orientation + [
                0,
                30 * (1 - abs(2 * t_norm - 1)),  # Peaks in middle
                0
            ]
        else:
            orientation = base_orientation + np.random.normal(0, 3, 3)
        
        # Calculate orientation change for gyro
        if t > 0:
            orient_change = orientation - prev_orientation
        else:
            orient_change = np.zeros(3)
        prev_orientation = orientation.copy()
        
        # Generate IMU data
        motion_factor = 0.3 if gesture_def['motion'] != 'static' else 0.05
        accel_data[t] = imu_accel_model(orientation, motion_factor)
        gyro_data[t] = imu_gyro_model(orient_change, SAMPLE_PERIOD)
    
    # Create sample dictionary
    sample = {
        'sample_id': f"BDSL_{participant_id:03d}_{gesture_id}_{datetime.now().strftime('%Y%m%d')}_{trial_num:04d}",
        'participant_id': f"P{participant_id:03d}",
        'gesture_id': gesture_id,
        'trial_number': trial_num,
        'duration_ms': int(n_samples * 1000 / SAMPLING_RATE),
        'sampling_rate_hz': SAMPLING_RATE,
        'n_samples': n_samples,
        'channels': {
            'flex_thumb': flex_data[:, 0].tolist(),
            'flex_index': flex_data[:, 1].tolist(),
            'flex_middle': flex_data[:, 2].tolist(),
            'flex_ring': flex_data[:, 3].tolist(),
            'flex_pinky': flex_data[:, 4].tolist(),
            'accel_x': [round(a, 4) for a in accel_data[:, 0]],
            'accel_y': [round(a, 4) for a in accel_data[:, 1]],
            'accel_z': [round(a, 4) for a in accel_data[:, 2]],
            'gyro_x': [round(g, 3) for g in gyro_data[:, 0]],
            'gyro_y': [round(g, 3) for g in gyro_data[:, 1]],
            'gyro_z': [round(g, 3) for g in gyro_data[:, 2]]
        },
        'metadata': {
            'temperature_c': round(temperature, 1),
            'humidity_percent': round(humidity, 1),
            'device_id': f"ST-ESP-{(participant_id % 5) + 1:03d}",
            'session_id': f"S{trial_num // 30 + 1:03d}",
            'environment': 'indoor_controlled'
        },
        'quality_metrics': {
            'snr_db': round(np.random.uniform(22, 32), 1),
            'missing_samples': 0,
            'outlier_count': np.random.randint(0, 5)
        }
    }
    
    return sample

# ============================================================
# DATASET GENERATION
# ============================================================

def generate_dataset(output_dir, split='train', n_samples=1000):
    """
    Generate a complete dataset split.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Define participant splits
    if split == 'train':
        participants = range(1, 15)  # P001-P014
    elif split == 'val':
        participants = [15, 16]  # P015-P016
    else:  # test
        participants = [17, 18]  # P017-P018
    
    samples = []
    
    # Generate samples
    sample_count = 0
    for gesture_id in GESTURE_DEFINITIONS.keys():
        for participant in participants:
            # Multiple trials per gesture per participant
            n_trials = n_samples // (len(GESTURE_DEFINITIONS) * len(participants))
            n_trials = max(n_trials, 3)
            
            for trial in range(1, n_trials + 1):
                if sample_count >= n_samples:
                    break
                
                # Random environmental conditions
                temp = np.random.uniform(23, 27)
                humidity = np.random.uniform(55, 70)
                
                sample = generate_gesture_trajectory(
                    gesture_id, participant, trial,
                    temperature=temp, humidity=humidity
                )
                samples.append(sample)
                sample_count += 1
                
                if sample_count % 100 == 0:
                    print(f"Generated {sample_count}/{n_samples} samples...")
    
    # Save to file
    output_file = os.path.join(output_dir, f'data_{split}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(samples, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(samples)} samples to {output_file}")
    
    # Generate checksum
    with open(output_file, 'rb') as f:
        checksum = hashlib.sha256(f.read()).hexdigest()
    
    checksum_file = os.path.join(output_dir, f'data_{split}.sha256')
    with open(checksum_file, 'w') as f:
        f.write(f"{checksum}  data_{split}.json\n")
    
    return len(samples)

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate BdSL sensor dataset')
    parser.add_argument('--output-dir', type=str, default='./output',
                       help='Output directory')
    parser.add_argument('--split', type=str, default='train',
                       choices=['train', 'val', 'test', 'all'],
                       help='Dataset split to generate')
    parser.add_argument('--n-samples', type=int, default=1000,
                       help='Number of samples to generate')
    
    args = parser.parse_args()
    
    if args.split == 'all':
        for split in ['train', 'val', 'test']:
            generate_dataset(args.output_dir, split, args.n_samples)
    else:
        generate_dataset(args.output_dir, args.split, args.n_samples)

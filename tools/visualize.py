"""
SignLanguage Dataset Hub - Visualization Tools

Visualize sensor data, gestures, and model predictions.
"""

import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class SensorVisualizer:
    """Visualize sensor glove data."""
    
    CHANNEL_NAMES = [
        'Flex Thumb', 'Flex Index', 'Flex Middle', 'Flex Ring', 'Flex Pinky',
        'Accel X', 'Accel Y', 'Accel Z',
        'Gyro X', 'Gyro Y', 'Gyro Z'
    ]
    
    CHANNEL_COLORS = [
        '#FF6B6B', '#FF8E72', '#FFA94D', '#FFD43B', '#C0CA33',
        '#66BB6A', '#26A69A', '#26C6DA',
        '#42A5F5', '#5C6BC0', '#AB47BC'
    ]
    
    def __init__(self, figsize=(15, 10)):
        self.figsize = figsize
    
    def plot_sample(self, sample: Dict, title: Optional[str] = None):
        """Plot a single gesture sample."""
        fig = plt.figure(figsize=self.figsize)
        gs = gridspec.GridSpec(3, 2, figure=fig, height_ratios=[1, 1, 0.5])
        
        channels = sample['channels']
        n_samples = len(channels['flex_thumb'])
        time = np.arange(n_samples) / 50.0  # 50 Hz sampling
        
        # Flex sensors
        ax1 = fig.add_subplot(gs[0, 0])
        for i, name in enumerate(['thumb', 'index', 'middle', 'ring', 'pinky']):
            ax1.plot(time, channels[f'flex_{name}'], 
                    label=self.CHANNEL_NAMES[i], color=self.CHANNEL_COLORS[i])
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('ADC Value')
        ax1.set_title('Flex Sensors (0-1023)')
        ax1.legend(loc='upper right')
        ax1.grid(True, alpha=0.3)
        
        # Accelerometer
        ax2 = fig.add_subplot(gs[0, 1])
        for i, axis in enumerate(['x', 'y', 'z']):
            ax2.plot(time, channels[f'accel_{axis}'],
                    label=f'Accel {axis.upper()}', color=self.CHANNEL_COLORS[5+i])
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Acceleration (g)')
        ax2.set_title('Accelerometer')
        ax2.legend(loc='upper right')
        ax2.grid(True, alpha=0.3)
        
        # Gyroscope
        ax3 = fig.add_subplot(gs[1, 0])
        for i, axis in enumerate(['x', 'y', 'z']):
            ax3.plot(time, channels[f'gyro_{axis}'],
                    label=f'Gyro {axis.upper()}', color=self.CHANNEL_COLORS[8+i])
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Angular Velocity (°/s)')
        ax3.set_title('Gyroscope')
        ax3.legend(loc='upper right')
        ax3.grid(True, alpha=0.3)
        
        # Hand representation (simplified)
        ax4 = fig.add_subplot(gs[1, 1])
        self._draw_hand(ax4, channels)
        ax4.set_title('Hand Configuration (End State)')
        ax4.axis('off')
        
        # Metadata
        ax5 = fig.add_subplot(gs[2, :])
        ax5.axis('off')
        metadata_text = (
            f"Gesture: {sample['gesture_id']} | "
            f"Duration: {sample['duration_ms']}ms | "
            f"Samples: {n_samples} | "
            f"Participant: {sample['participant_id']}"
        )
        ax5.text(0.5, 0.5, metadata_text, ha='center', va='center', 
                fontsize=12, family='monospace')
        
        if title:
            fig.suptitle(title, fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def _draw_hand(self, ax, channels):
        """Draw simplified hand representation."""
        # Get final flex values
        flex_values = [
            channels['flex_thumb'][-1],
            channels['flex_index'][-1],
            channels['flex_middle'][-1],
            channels['flex_ring'][-1],
            channels['flex_pinky'][-1]
        ]
        
        # Normalize to 0-1
        flex_norm = [(f - 100) / 850 for f in flex_values]
        
        # Finger positions (simplified)
        finger_positions = [
            (0.2, 0.5),   # thumb
            (0.35, 0.8),  # index
            (0.5, 0.85),  # middle
            (0.65, 0.8),  # ring
            (0.8, 0.7),   # pinky
        ]
        
        palm_center = (0.5, 0.3)
        
        # Draw palm
        ax.add_patch(plt.Circle(palm_center, 0.15, color='#FFE4C4', ec='black'))
        
        # Draw fingers
        for i, (pos, flex) in enumerate(zip(finger_positions, flex_norm)):
            finger_length = 0.3 * (1 - flex * 0.7)
            end_pos = (
                pos[0],
                pos[1] - finger_length * 0.3 + palm_center[1] * 0.5
            )
            
            # Finger color based on bend
            color = plt.cm.RdYlGn_r(flex)
            
            ax.plot([palm_center[0] + (pos[0] - 0.5) * 0.5, pos[0]], 
                   [palm_center[1] + 0.1, pos[1]], 
                   color=color, linewidth=10 - flex * 5, solid_capstyle='round')
            
            ax.plot([pos[0], end_pos[0]], 
                   [pos[1], end_pos[1]], 
                   color=color, linewidth=8 - flex * 4, solid_capstyle='round')
        
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.1, 1.1)
    
    def plot_multiple_samples(self, samples: List[Dict], gesture_id: str):
        """Plot multiple samples of the same gesture."""
        n = min(len(samples), 6)
        fig, axes = plt.subplots(2, 3, figsize=(15, 8))
        axes = axes.flatten()
        
        for i, (ax, sample) in enumerate(zip(axes, samples[:n])):
            time = np.arange(len(sample['channels']['flex_thumb'])) / 50.0
            
            # Plot all flex sensors
            for j, name in enumerate(['thumb', 'index', 'middle', 'ring', 'pinky']):
                ax.plot(time, sample['channels'][f'flex_{name}'], 
                       color=self.CHANNEL_COLORS[j], alpha=0.7)
            
            ax.set_title(f"Trial {i+1} | Participant {sample['participant_id']}")
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('ADC')
            ax.grid(True, alpha=0.3)
        
        fig.suptitle(f'Gesture: {gesture_id}', fontsize=14, fontweight='bold')
        plt.tight_layout()
        return fig
    
    def plot_confusion_matrix(self, y_true: np.ndarray, y_pred: np.ndarray, 
                              class_names: List[str]):
        """Plot confusion matrix for classification results."""
        from sklearn.metrics import confusion_matrix
        import seaborn as sns
        
        cm = confusion_matrix(y_true, y_pred)
        cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(cm_norm, annot=True, fmt='.2f', cmap='Blues',
                   xticklabels=class_names, yticklabels=class_names, ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('True')
        ax.set_title('Confusion Matrix (Normalized)')
        
        plt.tight_layout()
        return fig


def visualize_gesture_comparison(data_path: str, output_path: str = None):
    """Create comparison visualization of all gestures."""
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # Group by gesture
    gestures = {}
    for sample in data:
        gid = sample['gesture_id']
        if gid not in gestures:
            gestures[gid] = []
        gestures[gid].append(sample)
    
    # Plot one sample per gesture
    n_gestures = len(gestures)
    n_cols = 6
    n_rows = (n_gestures + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, n_rows * 3))
    axes = axes.flatten()
    
    for i, (gid, samples) in enumerate(gestures.items()):
        if i >= len(axes):
            break
        
        ax = axes[i]
        sample = samples[0]
        time = np.arange(len(sample['channels']['flex_thumb'])) / 50.0
        
        # Plot flex sensors
        for j, name in enumerate(['thumb', 'index', 'middle', 'ring', 'pinky']):
            ax.plot(time, sample['channels'][f'flex_{name}'], 
                   label=name, alpha=0.8)
        
        ax.set_title(f'{gid}', fontsize=10)
        ax.set_xlabel('Time (s)', fontsize=8)
        ax.set_ylabel('ADC', fontsize=8)
        ax.tick_params(labelsize=7)
    
    # Hide unused axes
    for i in range(len(gestures), len(axes)):
        axes[i].axis('off')
    
    fig.suptitle('BdSL Gesture Comparison', fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    
    return fig


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Visualize sensor data")
    parser.add_argument('--data', type=str, required=True, help='Path to data JSON')
    parser.add_argument('--output', type=str, help='Output path for figure')
    parser.add_argument('--sample', type=int, default=0, help='Sample index to visualize')
    parser.add_argument('--compare', action='store_true', help='Compare all gestures')
    
    args = parser.parse_args()
    
    if args.compare:
        visualize_gesture_comparison(args.data, args.output)
    else:
        with open(args.data, 'r') as f:
            data = json.load(f)
        
        viz = SensorVisualizer()
        fig = viz.plot_sample(data[args.sample])
        
        if args.output:
            fig.savefig(args.output, dpi=150, bbox_inches='tight')
        else:
            plt.show()

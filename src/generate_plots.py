"""
Visualization Script for Quicksort Comparison

Generates plots comparing Randomized vs Deterministic Quicksort
across different input sizes and distributions.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict
import random
import time
from src.quicksort import (
    randomized_quicksort,
    deterministic_quicksort,
    measure_time
)


def generate_random_array(size: int, min_val: int = 1, max_val: int = 1000000) -> List[int]:
    """Generate a random array of given size."""
    return [random.randint(min_val, max_val) for _ in range(size)]


def generate_sorted_array(size: int) -> List[int]:
    """Generate a sorted array."""
    return list(range(1, size + 1))


def generate_reverse_sorted_array(size: int) -> List[int]:
    """Generate a reverse-sorted array."""
    return list(range(size, 0, -1))


def generate_repeated_array(size: int, num_unique: int = 10) -> List[int]:
    """Generate an array with many repeated elements."""
    return [random.randint(1, num_unique) for _ in range(size)]


def compare_algorithms(arr: List[int], num_runs: int = 3) -> Dict:
    """Compare randomized and deterministic quicksort on the same array."""
    # Test deterministic quicksort
    det_times = []
    for _ in range(num_runs):
        test_arr = arr.copy()
        det_time, det_result = measure_time(deterministic_quicksort, test_arr)
        det_times.append(det_time)
    
    det_avg_time = sum(det_times) / len(det_times)
    
    # Test randomized quicksort
    rand_times = []
    for _ in range(num_runs):
        test_arr = arr.copy()
        rand_time, rand_result = measure_time(randomized_quicksort, test_arr)
        rand_times.append(rand_time)
    
    rand_avg_time = sum(rand_times) / len(rand_times)
    
    return {
        'size': len(arr),
        'det_time': det_avg_time,
        'rand_time': rand_avg_time
    }


def generate_plots():
    """Generate comprehensive plots for quicksort comparison."""
    
    # Test sizes
    small_sizes = [100, 500, 1000]
    medium_sizes = [5000, 10000]
    large_sizes = [25000, 50000]
    all_sizes = small_sizes + medium_sizes + large_sizes
    
    # Collect data for each distribution
    distributions = {
        'random': [],
        'sorted': [],
        'reverse_sorted': [],
        'repeated': []
    }
    
    print("Collecting data for plots...")
    print("This may take a few minutes...")
    
    # 1. Random arrays
    print("\n1. Random arrays...")
    for size in all_sizes:
        arr = generate_random_array(size)
        result = compare_algorithms(arr, num_runs=3)
        distributions['random'].append(result)
        print(f"  Size {size}: Det={result['det_time']:.6f}s, Rand={result['rand_time']:.6f}s")
    
    # 2. Sorted arrays
    print("\n2. Sorted arrays...")
    sorted_sizes = small_sizes + medium_sizes + large_sizes[:2]
    for size in sorted_sizes:
        arr = generate_sorted_array(size)
        result = compare_algorithms(arr, num_runs=3)
        distributions['sorted'].append(result)
        print(f"  Size {size}: Det={result['det_time']:.6f}s, Rand={result['rand_time']:.6f}s")
    
    # 3. Reverse-sorted arrays
    print("\n3. Reverse-sorted arrays...")
    reverse_sizes = small_sizes + medium_sizes + large_sizes[:2]
    for size in reverse_sizes:
        arr = generate_reverse_sorted_array(size)
        result = compare_algorithms(arr, num_runs=3)
        distributions['reverse_sorted'].append(result)
        print(f"  Size {size}: Det={result['det_time']:.6f}s, Rand={result['rand_time']:.6f}s")
    
    # 4. Repeated elements
    print("\n4. Repeated elements arrays...")
    for size in all_sizes:
        arr = generate_repeated_array(size, num_unique=min(100, size // 10))
        result = compare_algorithms(arr, num_runs=3)
        distributions['repeated'].append(result)
        print(f"  Size {size}: Det={result['det_time']:.6f}s, Rand={result['rand_time']:.6f}s")
    
    # Create plots
    print("\nGenerating plots...")
    
    # Set up the figure with subplots
    fig = plt.figure(figsize=(16, 12))
    
    # 1. Line plot: Running time vs input size for all distributions
    ax1 = plt.subplot(2, 2, 1)
    for dist_name, dist_data in distributions.items():
        if not dist_data:
            continue
        sizes = [d['size'] for d in dist_data]
        det_times = [d['det_time'] for d in dist_data]
        rand_times = [d['rand_time'] for d in dist_data]
        
        dist_label = dist_name.replace('_', ' ').title()
        ax1.plot(sizes, det_times, 'o--', label=f'Deterministic ({dist_label})', alpha=0.7)
        ax1.plot(sizes, rand_times, 's-', label=f'Randomized ({dist_label})', alpha=0.7)
    
    ax1.set_xlabel('Input Size (n)', fontsize=11)
    ax1.set_ylabel('Running Time (seconds)', fontsize=11)
    ax1.set_title('Running Time Comparison: Randomized vs Deterministic Quicksort', fontsize=12, fontweight='bold')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.legend(loc='best', fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    # 2. Bar chart: Speedup ratio for sorted arrays (worst case)
    ax2 = plt.subplot(2, 2, 2)
    if distributions['sorted']:
        sizes = [d['size'] for d in distributions['sorted']]
        speedups = [d['det_time'] / d['rand_time'] for d in distributions['sorted']]
        colors = ['red' if s > 1 else 'blue' for s in speedups]
        bars = ax2.bar(range(len(sizes)), speedups, color=colors, alpha=0.7)
        ax2.set_xticks(range(len(sizes)))
        ax2.set_xticklabels([f'{s}' for s in sizes])
        ax2.axhline(y=1, color='black', linestyle='--', linewidth=1, label='Equal Performance')
        ax2.set_xlabel('Input Size (n)', fontsize=11)
        ax2.set_ylabel('Speedup Ratio (Det / Rand)', fontsize=11)
        ax2.set_title('Speedup: Randomized vs Deterministic (Sorted Arrays)', fontsize=12, fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for i, (bar, speedup) in enumerate(zip(bars, speedups)):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{speedup:.2f}x', ha='center', va='bottom', fontsize=9)
    
    # 3. Comparison: Random arrays
    ax3 = plt.subplot(2, 2, 3)
    if distributions['random']:
        sizes = [d['size'] for d in distributions['random']]
        det_times = [d['det_time'] for d in distributions['random']]
        rand_times = [d['rand_time'] for d in distributions['random']]
        
        x = np.arange(len(sizes))
        width = 0.35
        
        bars1 = ax3.bar(x - width/2, det_times, width, label='Deterministic', alpha=0.8, color='#ff7f0e')
        bars2 = ax3.bar(x + width/2, rand_times, width, label='Randomized', alpha=0.8, color='#2ca02c')
        
        ax3.set_xlabel('Input Size (n)', fontsize=11)
        ax3.set_ylabel('Running Time (seconds)', fontsize=11)
        ax3.set_title('Random Arrays: Performance Comparison', fontsize=12, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels([f'{s}' for s in sizes])
        ax3.legend()
        ax3.set_yscale('log')
        ax3.grid(True, alpha=0.3, axis='y')
    
    # 4. Comparison: Reverse-sorted arrays (worst case demonstration)
    ax4 = plt.subplot(2, 2, 4)
    if distributions['reverse_sorted']:
        sizes = [d['size'] for d in distributions['reverse_sorted']]
        det_times = [d['det_time'] for d in distributions['reverse_sorted']]
        rand_times = [d['rand_time'] for d in distributions['reverse_sorted']]
        
        x = np.arange(len(sizes))
        width = 0.35
        
        bars1 = ax4.bar(x - width/2, det_times, width, label='Deterministic', alpha=0.8, color='#d62728')
        bars2 = ax4.bar(x + width/2, rand_times, width, label='Randomized', alpha=0.8, color='#2ca02c')
        
        ax4.set_xlabel('Input Size (n)', fontsize=11)
        ax4.set_ylabel('Running Time (seconds)', fontsize=11)
        ax4.set_title('Reverse-Sorted Arrays: Worst Case for Deterministic', fontsize=12, fontweight='bold')
        ax4.set_xticks(x)
        ax4.set_xticklabels([f'{s}' for s in sizes])
        ax4.legend()
        ax4.set_yscale('log')
        ax4.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('quicksort_comparison_plots.png', dpi=300, bbox_inches='tight')
    print("\nPlot saved as 'quicksort_comparison_plots.png'")
    
    # Create a second figure with detailed comparison
    fig2 = plt.figure(figsize=(16, 10))
    
    # 1. Detailed line plot for each distribution
    ax1 = plt.subplot(2, 2, 1)
    if distributions['random']:
        sizes = [d['size'] for d in distributions['random']]
        det_times = [d['det_time'] for d in distributions['random']]
        rand_times = [d['rand_time'] for d in distributions['random']]
        ax1.plot(sizes, det_times, 'o--', label='Deterministic', linewidth=2, markersize=8)
        ax1.plot(sizes, rand_times, 's-', label='Randomized', linewidth=2, markersize=8)
    ax1.set_xlabel('Input Size (n)', fontsize=11)
    ax1.set_ylabel('Running Time (seconds)', fontsize=11)
    ax1.set_title('Random Arrays', fontsize=12, fontweight='bold')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Sorted arrays
    ax2 = plt.subplot(2, 2, 2)
    if distributions['sorted']:
        sizes = [d['size'] for d in distributions['sorted']]
        det_times = [d['det_time'] for d in distributions['sorted']]
        rand_times = [d['rand_time'] for d in distributions['sorted']]
        ax2.plot(sizes, det_times, 'o--', label='Deterministic', linewidth=2, markersize=8, color='red')
        ax2.plot(sizes, rand_times, 's-', label='Randomized', linewidth=2, markersize=8, color='green')
    ax2.set_xlabel('Input Size (n)', fontsize=11)
    ax2.set_ylabel('Running Time (seconds)', fontsize=11)
    ax2.set_title('Sorted Arrays (Worst Case for Deterministic)', fontsize=12, fontweight='bold')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Reverse-sorted arrays
    ax3 = plt.subplot(2, 2, 3)
    if distributions['reverse_sorted']:
        sizes = [d['size'] for d in distributions['reverse_sorted']]
        det_times = [d['det_time'] for d in distributions['reverse_sorted']]
        rand_times = [d['rand_time'] for d in distributions['reverse_sorted']]
        ax3.plot(sizes, det_times, 'o--', label='Deterministic', linewidth=2, markersize=8, color='red')
        ax3.plot(sizes, rand_times, 's-', label='Randomized', linewidth=2, markersize=8, color='green')
    ax3.set_xlabel('Input Size (n)', fontsize=11)
    ax3.set_ylabel('Running Time (seconds)', fontsize=11)
    ax3.set_title('Reverse-Sorted Arrays (Worst Case for Deterministic)', fontsize=12, fontweight='bold')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Repeated elements
    ax4 = plt.subplot(2, 2, 4)
    if distributions['repeated']:
        sizes = [d['size'] for d in distributions['repeated']]
        det_times = [d['det_time'] for d in distributions['repeated']]
        rand_times = [d['rand_time'] for d in distributions['repeated']]
        ax4.plot(sizes, det_times, 'o--', label='Deterministic', linewidth=2, markersize=8)
        ax4.plot(sizes, rand_times, 's-', label='Randomized', linewidth=2, markersize=8)
    ax4.set_xlabel('Input Size (n)', fontsize=11)
    ax4.set_ylabel('Running Time (seconds)', fontsize=11)
    ax4.set_title('Arrays with Repeated Elements', fontsize=12, fontweight='bold')
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('quicksort_comparison_detailed.png', dpi=300, bbox_inches='tight')
    print("Detailed plot saved as 'quicksort_comparison_detailed.png'")
    
    # Create speedup comparison plot
    fig3 = plt.figure(figsize=(14, 8))
    
    # Speedup ratios for all distributions
    distributions_list = ['random', 'sorted', 'reverse_sorted', 'repeated']
    dist_labels = ['Random', 'Sorted', 'Reverse-Sorted', 'Repeated']
    
    for idx, (dist_name, dist_label) in enumerate(zip(distributions_list, dist_labels)):
        ax = plt.subplot(2, 2, idx + 1)
        if distributions[dist_name]:
            sizes = [d['size'] for d in distributions[dist_name]]
            speedups = [d['det_time'] / d['rand_time'] for d in distributions[dist_name]]
            
            colors = ['green' if s > 1 else 'red' for s in speedups]
            bars = ax.bar(range(len(sizes)), speedups, color=colors, alpha=0.7)
            ax.axhline(y=1, color='black', linestyle='--', linewidth=1, label='Equal Performance')
            
            ax.set_xticks(range(len(sizes)))
            ax.set_xticklabels([f'{s}' for s in sizes])
            ax.set_xlabel('Input Size (n)', fontsize=10)
            ax.set_ylabel('Speedup Ratio', fontsize=10)
            ax.set_title(f'{dist_label} Arrays', fontsize=11, fontweight='bold')
            ax.legend(fontsize=8)
            ax.grid(True, alpha=0.3, axis='y')
            
            # Add value labels
            for bar, speedup in zip(bars, speedups):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{speedup:.2f}x', ha='center', va='bottom' if height > 1 else 'top', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('quicksort_speedup_comparison.png', dpi=300, bbox_inches='tight')
    print("Speedup comparison plot saved as 'quicksort_speedup_comparison.png'")
    
    plt.close('all')
    print("\nAll plots generated successfully!")


if __name__ == "__main__":
    try:
        generate_plots()
    except ImportError:
        print("Error: matplotlib is required for plotting.")
        print("Please install it with: pip install matplotlib")
    except Exception as e:
        print(f"Error generating plots: {e}")
        import traceback
        traceback.print_exc()


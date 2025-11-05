"""
Empirical Comparison: Randomized Quicksort vs Deterministic Quicksort

This script performs comprehensive empirical comparison between:
- Randomized Quicksort (random pivot selection)
- Deterministic Quicksort (first element as pivot)

Tests are performed on different input sizes and distributions:
1. Randomly generated arrays
2. Already sorted arrays
3. Reverse-sorted arrays
4. Arrays with repeated elements
"""

import random
import time
from typing import List, Dict, Tuple
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


def compare_algorithms(arr: List[int], num_runs: int = 5) -> Dict:
    """
    Compare randomized and deterministic quicksort on the same array.
    
    Args:
        arr: Array to sort
        num_runs: Number of runs for averaging (for randomized quicksort)
    
    Returns:
        Dictionary with comparison results
    """
    # Test deterministic quicksort
    det_times = []
    for _ in range(num_runs):
        test_arr = arr.copy()
        det_time, det_result = measure_time(deterministic_quicksort, test_arr)
        det_times.append(det_time)
    
    det_avg_time = sum(det_times) / len(det_times)
    det_best_time = min(det_times)
    det_worst_time = max(det_times)
    
    # Test randomized quicksort (multiple runs for averaging)
    rand_times = []
    for _ in range(num_runs):
        test_arr = arr.copy()
        rand_time, rand_result = measure_time(randomized_quicksort, test_arr)
        rand_times.append(rand_time)
    
    rand_avg_time = sum(rand_times) / len(rand_times)
    rand_best_time = min(rand_times)
    rand_worst_time = max(rand_times)
    
    # Verify correctness
    reference = sorted(arr)
    is_det_correct = det_result == reference
    is_rand_correct = rand_result == reference
    
    return {
        'array_length': len(arr),
        'deterministic': {
            'avg_time': det_avg_time,
            'best_time': det_best_time,
            'worst_time': det_worst_time,
            'correct': is_det_correct
        },
        'randomized': {
            'avg_time': rand_avg_time,
            'best_time': rand_best_time,
            'worst_time': rand_worst_time,
            'correct': is_rand_correct
        },
        'speedup': det_avg_time / rand_avg_time if rand_avg_time > 0 else float('inf'),
        'slowdown': rand_avg_time / det_avg_time if det_avg_time > 0 else float('inf')
    }


def run_comprehensive_comparison() -> Dict:
    """
    Run comprehensive comparison across different input sizes and distributions.
    
    Returns:
        Dictionary with all comparison results
    """
    # Test sizes
    small_sizes = [100, 500, 1000]
    medium_sizes = [5000, 10000]
    large_sizes = [25000, 50000]
    
    all_results = {
        'random': [],
        'sorted': [],
        'reverse_sorted': [],
        'repeated': []
    }
    
    print("=" * 80)
    print("Empirical Comparison: Randomized vs Deterministic Quicksort")
    print("=" * 80)
    
    # 1. Random arrays
    print("\n1. RANDOMLY GENERATED ARRAYS")
    print("-" * 80)
    print(f"{'Size':<10} {'Det Avg (s)':<15} {'Rand Avg (s)':<15} {'Speedup':<12} {'Better':<10}")
    print("-" * 80)
    
    for size in small_sizes + medium_sizes + large_sizes:
        arr = generate_random_array(size)
        result = compare_algorithms(arr, num_runs=3)
        all_results['random'].append(result)
        
        better = "Randomized" if result['speedup'] > 1 else "Deterministic"
        print(f"{size:<10} {result['deterministic']['avg_time']:<15.6f} "
              f"{result['randomized']['avg_time']:<15.6f} "
              f"{result['speedup']:<12.2f} {better:<10}")
    
    # 2. Sorted arrays (worst case for deterministic)
    print("\n2. ALREADY SORTED ARRAYS (Worst case for Deterministic)")
    print("-" * 80)
    print(f"{'Size':<10} {'Det Avg (s)':<15} {'Rand Avg (s)':<15} {'Speedup':<12} {'Better':<10}")
    print("-" * 80)
    
    for size in small_sizes + medium_sizes + large_sizes[:2]:  # Skip very large for sorted
        arr = generate_sorted_array(size)
        result = compare_algorithms(arr, num_runs=3)
        all_results['sorted'].append(result)
        
        better = "Randomized" if result['speedup'] > 1 else "Deterministic"
        print(f"{size:<10} {result['deterministic']['avg_time']:<15.6f} "
              f"{result['randomized']['avg_time']:<15.6f} "
              f"{result['speedup']:<12.2f} {better:<10}")
    
    # 3. Reverse-sorted arrays (worst case for deterministic)
    print("\n3. REVERSE-SORTED ARRAYS (Worst case for Deterministic)")
    print("-" * 80)
    print(f"{'Size':<10} {'Det Avg (s)':<15} {'Rand Avg (s)':<15} {'Speedup':<12} {'Better':<10}")
    print("-" * 80)
    
    for size in small_sizes + medium_sizes + large_sizes[:2]:  # Skip very large for reverse sorted
        arr = generate_reverse_sorted_array(size)
        result = compare_algorithms(arr, num_runs=3)
        all_results['reverse_sorted'].append(result)
        
        better = "Randomized" if result['speedup'] > 1 else "Deterministic"
        print(f"{size:<10} {result['deterministic']['avg_time']:<15.6f} "
              f"{result['randomized']['avg_time']:<15.6f} "
              f"{result['speedup']:<12.2f} {better:<10}")
    
    # 4. Arrays with repeated elements
    print("\n4. ARRAYS WITH REPEATED ELEMENTS")
    print("-" * 80)
    print(f"{'Size':<10} {'Det Avg (s)':<15} {'Rand Avg (s)':<15} {'Speedup':<12} {'Better':<10}")
    print("-" * 80)
    
    for size in small_sizes + medium_sizes + large_sizes:
        arr = generate_repeated_array(size, num_unique=min(100, size // 10))
        result = compare_algorithms(arr, num_runs=3)
        all_results['repeated'].append(result)
        
        better = "Randomized" if result['speedup'] > 1 else "Deterministic"
        print(f"{size:<10} {result['deterministic']['avg_time']:<15.6f} "
              f"{result['randomized']['avg_time']:<15.6f} "
              f"{result['speedup']:<12.2f} {better:<10}")
    
    return all_results


def generate_detailed_report(results: Dict) -> str:
    """Generate a detailed markdown report from results."""
    report = []
    report.append("# Empirical Comparison: Randomized vs Deterministic Quicksort\n\n")
    report.append("## Executive Summary\n\n")
    report.append("This document presents empirical comparison results between Randomized Quicksort ")
    report.append("and Deterministic Quicksort (using first element as pivot) across different ")
    report.append("input sizes and distributions.\n\n")
    
    # Summary statistics
    report.append("## Summary Statistics\n\n")
    
    for dist_name, dist_results in results.items():
        if not dist_results:
            continue
        
        dist_title = dist_name.replace('_', ' ').title()
        report.append(f"### {dist_title}\n\n")
        
        report.append("| Size | Det Avg (s) | Det Best (s) | Det Worst (s) | ")
        report.append("Rand Avg (s) | Rand Best (s) | Rand Worst (s) | Speedup | Better |\n")
        report.append("|------|-------------|--------------|---------------|")
        report.append("-------------|---------------|---------------|---------|--------|\n")
        
        for result in dist_results:
            size = result['array_length']
            det = result['deterministic']
            rand = result['randomized']
            speedup = result['speedup']
            better = "Randomized" if speedup > 1 else "Deterministic"
            
            report.append(f"| {size} | {det['avg_time']:.6f} | {det['best_time']:.6f} | ")
            report.append(f"{det['worst_time']:.6f} | {rand['avg_time']:.6f} | ")
            report.append(f"{rand['best_time']:.6f} | {rand['worst_time']:.6f} | ")
            report.append(f"{speedup:.2f}x | {better} |\n")
        
        report.append("\n")
    
    # Key findings
    report.append("## Key Findings\n\n")
    
    # Analyze random arrays
    if results['random']:
        avg_speedup_random = sum(r['speedup'] for r in results['random']) / len(results['random'])
        report.append(f"1. **Random Arrays**: Randomized quicksort is ")
        report.append(f"{'faster' if avg_speedup_random > 1 else 'slower'} on average ")
        report.append(f"(average speedup: {avg_speedup_random:.2f}x)\n\n")
    
    # Analyze sorted arrays
    if results['sorted']:
        avg_speedup_sorted = sum(r['speedup'] for r in results['sorted']) / len(results['sorted'])
        report.append(f"2. **Sorted Arrays**: Randomized quicksort shows ")
        report.append(f"{avg_speedup_sorted:.2f}x speedup over deterministic quicksort ")
        report.append("(deterministic's worst case)\n\n")
    
    # Analyze reverse-sorted arrays
    if results['reverse_sorted']:
        avg_speedup_reverse = sum(r['speedup'] for r in results['reverse_sorted']) / len(results['reverse_sorted'])
        report.append(f"3. **Reverse-Sorted Arrays**: Randomized quicksort shows ")
        report.append(f"{avg_speedup_reverse:.2f}x speedup over deterministic quicksort ")
        report.append("(deterministic's worst case)\n\n")
    
    # Analyze repeated elements
    if results['repeated']:
        avg_speedup_repeated = sum(r['speedup'] for r in results['repeated']) / len(results['repeated'])
        report.append(f"4. **Repeated Elements**: Randomized quicksort is ")
        report.append(f"{'faster' if avg_speedup_repeated > 1 else 'slower'} on average ")
        report.append(f"(average speedup: {avg_speedup_repeated:.2f}x)\n\n")
    
    report.append("## Conclusions\n\n")
    report.append("1. **Randomized Quicksort** performs consistently well across all input types, ")
    report.append("avoiding worst-case O(n²) behavior.\n\n")
    report.append("2. **Deterministic Quicksort** degrades significantly on sorted and reverse-sorted ")
    report.append("arrays, demonstrating O(n²) worst-case performance.\n\n")
    report.append("3. **Randomization** provides significant performance improvement for adversarial ")
    report.append("inputs while maintaining competitive performance on random inputs.\n\n")
    
    return "".join(report)


if __name__ == "__main__":
    # Run comprehensive comparison
    results = run_comprehensive_comparison()
    
    # Generate and save report
    report = generate_detailed_report(results)
    
    # Save to file
    with open("QUICKSORT_COMPARISON.md", "w") as f:
        f.write(report)
    
    print("\n" + "=" * 80)
    print("Comparison complete! Detailed report saved to QUICKSORT_COMPARISON.md")
    print("=" * 80)


"""
Randomized Quicksort Implementation

This module provides a randomized quicksort algorithm implementation
along with utilities for performance analysis and comparison.
"""

import random
from typing import List, Callable, Tuple
import time
import sys


def randomized_quicksort(arr: List[int], low: int = None, high: int = None) -> List[int]:
    """
    Sort an array using randomized quicksort algorithm.
    
    Time Complexity:
        - Average: O(n log n)
        - Worst: O(n²) (rarely occurs due to randomization)
        - Best: O(n log n)
    
    Space Complexity: O(log n) average case due to recursion stack
    
    Args:
        arr: List of integers to sort
        low: Starting index (default: 0)
        high: Ending index (default: len(arr) - 1)
    
    Returns:
        Sorted list of integers
    """
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    # Create a copy to avoid mutating the original array
    arr = arr.copy()
    
    def _quicksort(arr: List[int], low: int, high: int) -> None:
        """Internal recursive quicksort function."""
        if low < high:
            # Partition the array and get pivot index
            pivot_idx = randomized_partition(arr, low, high)
            
            # Recursively sort elements before and after partition
            _quicksort(arr, low, pivot_idx - 1)
            _quicksort(arr, pivot_idx + 1, high)
    
    _quicksort(arr, low, high)
    return arr


def randomized_partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition the array using a random pivot element.
    
    This randomization helps avoid worst-case O(n²) behavior
    that occurs when the pivot is always the smallest or largest element.
    
    Args:
        arr: List to partition
        low: Starting index
        high: Ending index
    
    Returns:
        Final position of pivot element
    """
    # Randomly select a pivot index
    random_idx = random.randint(low, high)
    
    # Swap random element with last element
    arr[random_idx], arr[high] = arr[high], arr[random_idx]
    
    # Use standard partition with pivot at high
    return partition(arr, low, high)


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition the array around a pivot element.
    
    Elements smaller than pivot go to the left,
    elements greater than pivot go to the right.
    
    Args:
        arr: List to partition
        low: Starting index
        high: Ending index (pivot position)
    
    Returns:
        Final position of pivot element
    """
    pivot = arr[high]  # Pivot element
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def measure_time(func: Callable, *args, **kwargs) -> Tuple[float, any]:
    """
    Measure execution time of a function.
    
    Args:
        func: Function to measure
        *args: Positional arguments for function
        **kwargs: Keyword arguments for function
    
    Returns:
        Tuple of (execution_time_in_seconds, function_result)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time, result


def compare_with_builtin(arr: List[int]) -> dict:
    """
    Compare randomized quicksort with Python's built-in sort.
    
    Args:
        arr: List to sort
    
    Returns:
        Dictionary with timing comparison results
    """
    # Test randomized quicksort
    quicksort_time, sorted_quicksort = measure_time(randomized_quicksort, arr)
    
    # Test built-in sort
    builtin_time, sorted_builtin = measure_time(sorted, arr)
    
    # Verify correctness
    is_correct = sorted_quicksort == sorted_builtin
    
    return {
        'quicksort_time': quicksort_time,
        'builtin_time': builtin_time,
        'speedup': quicksort_time / builtin_time if builtin_time > 0 else float('inf'),
        'is_correct': is_correct,
        'array_length': len(arr)
    }


def deterministic_quicksort(arr: List[int], low: int = None, high: int = None) -> List[int]:
    """
    Sort an array using deterministic quicksort algorithm (first element as pivot).
    
    Time Complexity:
        - Average: O(n log n)
        - Worst: O(n²) - occurs when array is sorted or reverse sorted
        - Best: O(n log n)
    
    Space Complexity: O(log n) average case, O(n) worst case due to recursion stack
    
    Args:
        arr: List of integers to sort
        low: Starting index (default: 0)
        high: Ending index (default: len(arr) - 1)
    
    Returns:
        Sorted list of integers
    """
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    
    # Create a copy to avoid mutating the original array
    arr = arr.copy()
    
    # Increase recursion limit for worst-case scenarios
    original_limit = sys.getrecursionlimit()
    max_required = len(arr) * 2 + 1000
    if max_required > original_limit:
        sys.setrecursionlimit(max_required)
    
    try:
        def _quicksort(arr: List[int], low: int, high: int) -> None:
            """Internal recursive quicksort function."""
            if low < high:
                # Partition the array and get pivot index
                pivot_idx = deterministic_partition(arr, low, high)
                
                # Recursively sort elements before and after partition
                _quicksort(arr, low, pivot_idx - 1)
                _quicksort(arr, pivot_idx + 1, high)
        
        _quicksort(arr, low, high)
    finally:
        # Restore original recursion limit
        sys.setrecursionlimit(original_limit)
    
    return arr


def deterministic_partition(arr: List[int], low: int, high: int) -> int:
    """
    Partition the array using the first element as pivot.
    
    This deterministic approach can lead to O(n²) worst-case performance
    when the array is already sorted or reverse sorted.
    
    Args:
        arr: List to partition
        low: Starting index
        high: Ending index
    
    Returns:
        Final position of pivot element
    """
    # Use first element as pivot (swap with last element for partition)
    arr[low], arr[high] = arr[high], arr[low]
    
    # Use standard partition with pivot at high
    return partition(arr, low, high)


def analyze_performance(array_sizes: List[int] = None) -> List[dict]:
    """
    Analyze quicksort performance across different array sizes.
    
    Args:
        array_sizes: List of array sizes to test (default: [100, 1000, 10000, 100000])
    
    Returns:
        List of performance metrics for each array size
    """
    if array_sizes is None:
        array_sizes = [100, 1000, 10000, 100000]
    
    results = []
    
    for size in array_sizes:
        # Generate random array
        test_array = [random.randint(1, 1000000) for _ in range(size)]
        
        # Measure performance
        comparison = compare_with_builtin(test_array)
        results.append(comparison)
    
    return results


"""
Example usage of Randomized Quicksort and Hash Table implementations.

This module demonstrates how to use the algorithms and data structures
implemented in this project.
"""

import random
from src.quicksort import (
    randomized_quicksort,
    compare_with_builtin,
    analyze_performance
)
from src.hash_table import HashTable


def example_quicksort():
    """Demonstrate randomized quicksort usage."""
    print("=" * 60)
    print("Randomized Quicksort Example")
    print("=" * 60)
    
    # Example 1: Basic sorting
    print("\n1. Basic Sorting:")
    arr = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Original array: {arr}")
    sorted_arr = randomized_quicksort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # Example 2: Large random array
    print("\n2. Large Random Array:")
    large_arr = [random.randint(1, 1000) for _ in range(20)]
    print(f"Original array (first 20 elements): {large_arr[:20]}")
    sorted_large = randomized_quicksort(large_arr)
    print(f"Sorted array (first 20 elements): {sorted_large[:20]}")
    
    # Example 3: Performance comparison
    print("\n3. Performance Comparison with Built-in Sort:")
    test_array = [random.randint(1, 100000) for _ in range(10000)]
    comparison = compare_with_builtin(test_array)
    print(f"Array length: {comparison['array_length']}")
    print(f"Quicksort time: {comparison['quicksort_time']:.6f} seconds")
    print(f"Built-in sort time: {comparison['builtin_time']:.6f} seconds")
    print(f"Speedup ratio: {comparison['speedup']:.2f}x")
    print(f"Results match: {comparison['is_correct']}")


def example_hash_table():
    """Demonstrate hash table with chaining usage."""
    print("\n" + "=" * 60)
    print("Hash Table with Chaining Example")
    print("=" * 60)
    
    # Create hash table
    ht = HashTable(initial_size=8)
    
    # Example 1: Insert operations
    print("\n1. Insert Operations:")
    keys_values = [
        (1, "apple"),
        (2, "banana"),
        (3, "cherry"),
        (10, "date"),
        (11, "elderberry"),
        (18, "fig"),
        (19, "grape"),
        (26, "honeydew")
    ]
    
    for key, value in keys_values:
        ht.insert(key, value)
        print(f"Inserted ({key}, {value}) - Load factor: {ht.get_load_factor():.2f}")
    
    print(f"\nHash table size: {ht.size}")
    print(f"Number of elements: {len(ht)}")
    print(f"Load factor: {ht.get_load_factor():.2f}")
    
    # Example 2: Search operations
    print("\n2. Search Operations:")
    search_keys = [1, 3, 11, 99]
    for key in search_keys:
        value = ht.get(key)
        if value:
            print(f"Key {key} found: {value}")
        else:
            print(f"Key {key} not found")
    
    # Example 3: Contains operator
    print("\n3. Using 'in' Operator:")
    test_keys = [2, 5, 18]
    for key in test_keys:
        print(f"{key} in hash table: {key in ht}")
    
    # Example 4: Delete operations
    print("\n4. Delete Operations:")
    delete_key = 3
    print(f"Deleting key {delete_key}...")
    deleted = ht.delete(delete_key)
    print(f"Delete successful: {deleted}")
    print(f"Key {delete_key} still exists: {delete_key in ht}")
    print(f"Updated count: {len(ht)}")
    
    # Example 5: Get all items
    print("\n5. All Items in Hash Table:")
    all_items = ht.get_all_items()
    for key, value in all_items:
        print(f"  Key: {key}, Value: {value}")
    
    # Example 6: Collision demonstration
    print("\n6. Collision Resolution (Chaining):")
    collision_ht = HashTable(initial_size=5)
    # Keys that will likely collide
    collision_keys = [1, 6, 11, 16, 21]
    for key in collision_keys:
        collision_ht.insert(key, f"value_{key}")
    print(f"Hash table with collisions:")
    print(f"  Size: {collision_ht.size}")
    print(f"  Count: {len(collision_ht)}")
    print(f"  Load factor: {collision_ht.get_load_factor():.2f}")
    print(f"  Items: {collision_ht.get_all_items()}")


def example_performance_analysis():
    """Demonstrate performance analysis of quicksort."""
    print("\n" + "=" * 60)
    print("Performance Analysis Example")
    print("=" * 60)
    
    print("\nAnalyzing quicksort performance across different array sizes:")
    results = analyze_performance([100, 1000, 10000])
    
    print("\nResults:")
    print(f"{'Size':<10} {'Quicksort Time':<18} {'Built-in Time':<18} {'Speedup':<10} {'Correct':<10}")
    print("-" * 70)
    for result in results:
        print(f"{result['array_length']:<10} "
              f"{result['quicksort_time']:<18.6f} "
              f"{result['builtin_time']:<18.6f} "
              f"{result['speedup']:<10.2f} "
              f"{str(result['is_correct']):<10}")


if __name__ == "__main__":
    # Run all examples
    example_quicksort()
    example_hash_table()
    example_performance_analysis()


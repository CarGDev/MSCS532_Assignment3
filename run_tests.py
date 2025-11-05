#!/usr/bin/env python3
"""
Test runner for MSCS532 Assignment 3.

Provides various test execution options:
- Quick tests: Essential functionality
- Full suite: All tests including edge cases
- Unit tests: Standard unittest tests only
- Benchmarks: Performance comparison tests
- Stress tests: Large-scale and boundary tests
- Negative tests: Invalid input and error handling
"""

import unittest
import sys
import argparse
import time
from typing import List, Dict


def run_quick_tests():
    """Run essential functionality tests."""
    print("=" * 70)
    print("Running Quick Tests (Essential Functionality)")
    print("=" * 70)
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add basic functional tests
    from tests.test_quicksort import (
        TestRandomizedQuicksort,
        TestPartition
    )
    from tests.test_hash_table import TestHashTable
    
    suite.addTests(loader.loadTestsFromTestCase(TestRandomizedQuicksort))
    suite.addTests(loader.loadTestsFromTestCase(TestPartition))
    suite.addTests(loader.loadTestsFromTestCase(TestHashTable))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


def run_unit_tests():
    """Run standard unittest tests."""
    print("=" * 70)
    print("Running Unit Tests")
    print("=" * 70)
    
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


def run_performance_tests():
    """Run performance benchmark tests."""
    print("=" * 70)
    print("Running Performance Benchmarks")
    print("=" * 70)
    
    try:
        from src.quicksort import analyze_performance, compare_with_builtin
        import random
        
        print("\n1. Quicksort Performance Analysis:")
        print("-" * 70)
        sizes = [100, 1000, 10000]
        results = analyze_performance(sizes)
        
        print(f"\n{'Size':<10} {'Quicksort Time':<18} {'Built-in Time':<18} {'Speedup':<10} {'Correct':<10}")
        print("-" * 70)
        for result in results:
            print(f"{result['array_length']:<10} "
                  f"{result['quicksort_time']:<18.6f} "
                  f"{result['builtin_time']:<18.6f} "
                  f"{result['speedup']:<10.2f} "
                  f"{str(result['is_correct']):<10}")
        
        print("\n2. Hash Table Performance:")
        print("-" * 70)
        from src.hash_table import HashTable
        
        ht = HashTable(initial_size=16)
        num_operations = 10000
        
        start_time = time.perf_counter()
        for i in range(num_operations):
            ht.insert(i, f"value_{i}")
        insert_time = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for i in range(num_operations):
            _ = ht.get(i)
        get_time = time.perf_counter() - start_time
        
        start_time = time.perf_counter()
        for i in range(num_operations):
            ht.delete(i)
        delete_time = time.perf_counter() - start_time
        
        print(f"Insert {num_operations} elements: {insert_time:.6f} seconds")
        print(f"Get {num_operations} elements: {get_time:.6f} seconds")
        print(f"Delete {num_operations} elements: {delete_time:.6f} seconds")
        print(f"Average insert time: {insert_time/num_operations*1000:.4f} ms")
        print(f"Average get time: {get_time/num_operations*1000:.4f} ms")
        print(f"Average delete time: {delete_time/num_operations*1000:.4f} ms")
        
        return True
        
    except Exception as e:
        print(f"Error running performance tests: {e}")
        return False


def run_stress_tests():
    """Run stress tests with large inputs."""
    print("=" * 70)
    print("Running Stress Tests")
    print("=" * 70)
    
    try:
        from src.quicksort import randomized_quicksort
        from src.hash_table import HashTable
        import random
        
        print("\n1. Quicksort Stress Tests:")
        print("-" * 70)
        
        # Test with very large array
        large_size = 50000
        print(f"Testing with array of size {large_size}...")
        large_arr = [random.randint(1, 1000000) for _ in range(large_size)]
        
        start_time = time.perf_counter()
        sorted_arr = randomized_quicksort(large_arr)
        elapsed = time.perf_counter() - start_time
        
        # Verify correctness
        is_correct = sorted_arr == sorted(large_arr)
        print(f"✓ Large array sorted in {elapsed:.4f} seconds")
        print(f"✓ Correctness: {is_correct}")
        
        # Test with worst-case scenario (many duplicates)
        print(f"\nTesting with array of size {large_size} (many duplicates)...")
        dup_arr = [random.randint(1, 100) for _ in range(large_size)]
        
        start_time = time.perf_counter()
        sorted_dup = randomized_quicksort(dup_arr)
        elapsed = time.perf_counter() - start_time
        
        is_correct = sorted_dup == sorted(dup_arr)
        print(f"✓ Duplicate-heavy array sorted in {elapsed:.4f} seconds")
        print(f"✓ Correctness: {is_correct}")
        
        print("\n2. Hash Table Stress Tests:")
        print("-" * 70)
        
        # Test with many insertions
        ht = HashTable(initial_size=16)
        num_inserts = 100000
        
        print(f"Inserting {num_inserts} elements...")
        start_time = time.perf_counter()
        for i in range(num_inserts):
            ht.insert(i, f"value_{i}")
        elapsed = time.perf_counter() - start_time
        
        print(f"✓ Inserted {num_inserts} elements in {elapsed:.4f} seconds")
        print(f"✓ Hash table size: {ht.size}")
        print(f"✓ Load factor: {ht.get_load_factor():.4f}")
        print(f"✓ Count: {len(ht)}")
        
        # Verify all elements are retrievable
        print(f"\nVerifying retrieval of {num_inserts} elements...")
        start_time = time.perf_counter()
        all_found = True
        for i in range(num_inserts):
            if ht.get(i) != f"value_{i}":
                all_found = False
                break
        elapsed = time.perf_counter() - start_time
        
        print(f"✓ Retrieved {num_inserts} elements in {elapsed:.4f} seconds")
        print(f"✓ All elements found: {all_found}")
        
        return True
        
    except Exception as e:
        print(f"Error running stress tests: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_negative_tests():
    """Run negative test cases (invalid inputs, error handling)."""
    print("=" * 70)
    print("Running Negative Test Cases")
    print("=" * 70)
    
    try:
        from src.quicksort import randomized_quicksort
        from src.hash_table import HashTable
        
        print("\n1. Quicksort Negative Tests:")
        print("-" * 70)
        
        # Test with None (should handle gracefully or raise appropriate error)
        try:
            result = randomized_quicksort(None)
            print("✗ Should have raised TypeError for None input")
        except (TypeError, AttributeError):
            print("✓ Correctly handles None input")
        
        # Test with mixed types (should raise TypeError)
        try:
            result = randomized_quicksort([1, 2, "three", 4])
            print("✗ Should have raised TypeError for mixed types")
        except TypeError:
            print("✓ Correctly raises TypeError for mixed types")
        
        print("\n2. Hash Table Negative Tests:")
        print("-" * 70)
        
        # Test with None key
        ht = HashTable()
        try:
            ht.insert(None, "value")
            print("✗ Should have raised TypeError for None key")
        except TypeError:
            print("✓ Correctly handles None key")
        
        # Test with invalid initial size
        try:
            ht = HashTable(initial_size=0)
            print("✗ Should handle invalid initial size")
        except (ValueError, ZeroDivisionError):
            print("✓ Correctly handles invalid initial size")
        
        # Test with negative initial size
        try:
            ht = HashTable(initial_size=-1)
            print("✗ Should handle negative initial size")
        except (ValueError, AssertionError):
            print("✓ Correctly handles negative initial size")
        
        print("\n✓ Negative tests completed")
        return True
        
    except Exception as e:
        print(f"Error running negative tests: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_full_suite():
    """Run all tests."""
    print("=" * 70)
    print("Running Full Test Suite")
    print("=" * 70)
    
    results = []
    
    print("\n[1/4] Running Unit Tests...")
    results.append(("Unit Tests", run_unit_tests()))
    
    print("\n[2/4] Running Performance Benchmarks...")
    results.append(("Performance Tests", run_performance_tests()))
    
    print("\n[3/4] Running Stress Tests...")
    results.append(("Stress Tests", run_stress_tests()))
    
    print("\n[4/4] Running Negative Tests...")
    results.append(("Negative Tests", run_negative_tests()))
    
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    
    for test_name, success in results:
        status = "✓ PASSED" if success else "✗ FAILED"
        print(f"{test_name:<25} {status}")
    
    all_passed = all(result[1] for result in results)
    return all_passed


def main():
    """Main test runner with command-line interface."""
    parser = argparse.ArgumentParser(
        description='Test runner for MSCS532 Assignment 3',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 run_tests.py --quick          # Run quick tests
  python3 run_tests.py                  # Run full suite
  python3 run_tests.py --unit-only      # Run unit tests only
  python3 run_tests.py --benchmark      # Run performance benchmarks
  python3 run_tests.py --stress         # Run stress tests
  python3 run_tests.py --negative       # Run negative test cases
        """
    )
    
    parser.add_argument(
        '--quick',
        action='store_true',
        help='Run quick tests (essential functionality only)'
    )
    parser.add_argument(
        '--unit-only',
        action='store_true',
        help='Run unit tests only'
    )
    parser.add_argument(
        '--benchmark',
        action='store_true',
        help='Run performance benchmarks'
    )
    parser.add_argument(
        '--stress',
        action='store_true',
        help='Run stress tests'
    )
    parser.add_argument(
        '--negative',
        action='store_true',
        help='Run negative test cases'
    )
    
    args = parser.parse_args()
    
    success = False
    
    if args.quick:
        success = run_quick_tests()
    elif args.unit_only:
        success = run_unit_tests()
    elif args.benchmark:
        success = run_performance_tests()
    elif args.stress:
        success = run_stress_tests()
    elif args.negative:
        success = run_negative_tests()
    else:
        # Default: run full suite
        success = run_full_suite()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()


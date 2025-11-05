"""
Unit tests for Randomized and Deterministic Quicksort implementations.
"""

import unittest
import random
from src.quicksort import (
    randomized_quicksort,
    deterministic_quicksort,
    partition,
    randomized_partition,
    deterministic_partition,
    compare_with_builtin,
    analyze_performance
)


class TestRandomizedQuicksort(unittest.TestCase):
    """Test cases for randomized quicksort algorithm."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        arr = []
        result = randomized_quicksort(arr)
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Test sorting an array with a single element."""
        arr = [42]
        result = randomized_quicksort(arr)
        self.assertEqual(result, [42])
    
    def test_sorted_array(self):
        """Test sorting an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = randomized_quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        """Test sorting a reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = randomized_quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_random_array(self):
        """Test sorting a random array."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        result = randomized_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        result = randomized_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        arr = [-5, -2, -8, 1, 3, -1, 0]
        result = randomized_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_large_array(self):
        """Test sorting a large array."""
        arr = [random.randint(1, 10000) for _ in range(1000)]
        result = randomized_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_original_array_not_modified(self):
        """Test that the original array is not modified."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        original = arr.copy()
        randomized_quicksort(arr)
        self.assertEqual(arr, original)
    
    def test_all_same_elements(self):
        """Test sorting an array with all same elements."""
        arr = [5, 5, 5, 5, 5]
        result = randomized_quicksort(arr)
        self.assertEqual(result, [5, 5, 5, 5, 5])


class TestPartition(unittest.TestCase):
    """Test cases for partition function."""
    
    def test_partition(self):
        """Test partition function."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        pivot_idx = partition(arr, 0, len(arr) - 1)
        
        # Check that pivot is in correct position
        pivot_value = arr[pivot_idx]
        # All elements before pivot should be <= pivot
        for i in range(0, pivot_idx):
            self.assertLessEqual(arr[i], pivot_value)
        # All elements after pivot should be >= pivot
        for i in range(pivot_idx + 1, len(arr)):
            self.assertGreaterEqual(arr[i], pivot_value)
    
    def test_randomized_partition(self):
        """Test randomized partition function."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        pivot_idx = randomized_partition(arr, 0, len(arr) - 1)
        
        # Check that pivot is in correct position
        pivot_value = arr[pivot_idx]
        # All elements before pivot should be <= pivot
        for i in range(0, pivot_idx):
            self.assertLessEqual(arr[i], pivot_value)
        # All elements after pivot should be >= pivot
        for i in range(pivot_idx + 1, len(arr)):
            self.assertGreaterEqual(arr[i], pivot_value)
    
    def test_deterministic_partition(self):
        """Test deterministic partition function."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        pivot_idx = deterministic_partition(arr, 0, len(arr) - 1)
        
        # Check that pivot is in correct position
        pivot_value = arr[pivot_idx]
        # All elements before pivot should be <= pivot
        for i in range(0, pivot_idx):
            self.assertLessEqual(arr[i], pivot_value)
        # All elements after pivot should be >= pivot
        for i in range(pivot_idx + 1, len(arr)):
            self.assertGreaterEqual(arr[i], pivot_value)


class TestDeterministicQuicksort(unittest.TestCase):
    """Test cases for deterministic quicksort algorithm."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        arr = []
        result = deterministic_quicksort(arr)
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Test sorting an array with a single element."""
        arr = [42]
        result = deterministic_quicksort(arr)
        self.assertEqual(result, [42])
    
    def test_sorted_array(self):
        """Test sorting an already sorted array (worst case for deterministic)."""
        arr = [1, 2, 3, 4, 5]
        result = deterministic_quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        """Test sorting a reverse sorted array (worst case for deterministic)."""
        arr = [5, 4, 3, 2, 1]
        result = deterministic_quicksort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_random_array(self):
        """Test sorting a random array."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        result = deterministic_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        result = deterministic_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        arr = [-5, -2, -8, 1, 3, -1, 0]
        result = deterministic_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_large_array(self):
        """Test sorting a large array."""
        arr = [random.randint(1, 10000) for _ in range(1000)]
        result = deterministic_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)
    
    def test_original_array_not_modified(self):
        """Test that the original array is not modified."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        original = arr.copy()
        deterministic_quicksort(arr)
        self.assertEqual(arr, original)
    
    def test_all_same_elements(self):
        """Test sorting an array with all same elements."""
        arr = [5, 5, 5, 5, 5]
        result = deterministic_quicksort(arr)
        self.assertEqual(result, [5, 5, 5, 5, 5])


class TestQuicksortComparison(unittest.TestCase):
    """Test cases comparing randomized vs deterministic quicksort."""
    
    def test_both_produce_same_result(self):
        """Test that both algorithms produce identical results."""
        arr = [64, 34, 25, 12, 22, 11, 90, 5]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
        self.assertEqual(rand_result, det_result)
    
    def test_both_handle_empty_array(self):
        """Test both algorithms handle empty arrays."""
        arr = []
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        
        self.assertEqual(rand_result, [])
        self.assertEqual(det_result, [])
    
    def test_both_handle_duplicates(self):
        """Test both algorithms handle duplicate elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
    
    def test_both_handle_sorted_array(self):
        """Test both algorithms handle already sorted arrays."""
        arr = [1, 2, 3, 4, 5]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        
        self.assertEqual(rand_result, arr)
        self.assertEqual(det_result, arr)
    
    def test_both_handle_reverse_sorted_array(self):
        """Test both algorithms handle reverse sorted arrays."""
        arr = [5, 4, 3, 2, 1]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
    
    def test_both_handle_negative_numbers(self):
        """Test both algorithms handle negative numbers."""
        arr = [-5, -2, -8, 1, 3, -1, 0]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
    
    def test_both_handle_large_array(self):
        """Test both algorithms handle large arrays."""
        arr = [random.randint(1, 10000) for _ in range(1000)]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
    
    def test_deterministic_worst_case_performance(self):
        """Test deterministic quicksort on worst-case inputs (sorted arrays)."""
        # Small sorted array - should still work correctly
        arr = list(range(1, 101))  # 100 elements
        result = deterministic_quicksort(arr)
        self.assertEqual(result, arr)
        
        # Medium sorted array
        arr = list(range(1, 501))  # 500 elements
        result = deterministic_quicksort(arr)
        self.assertEqual(result, arr)
    
    def test_randomized_consistent_performance(self):
        """Test randomized quicksort maintains consistent performance."""
        # Test on sorted array (worst case for deterministic)
        arr = list(range(1, 101))
        rand_result = randomized_quicksort(arr)
        self.assertEqual(rand_result, arr)
        
        # Test on reverse sorted array
        arr = list(range(100, 0, -1))
        rand_result = randomized_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(rand_result, expected)
        
        # Test on random array
        arr = [random.randint(1, 1000) for _ in range(100)]
        rand_result = randomized_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(rand_result, expected)


class TestPerformanceComparison(unittest.TestCase):
    """Test cases for performance comparison utilities."""
    
    def test_compare_with_builtin(self):
        """Test comparison with built-in sort."""
        arr = [random.randint(1, 1000) for _ in range(100)]
        comparison = compare_with_builtin(arr)
        
        self.assertIn('quicksort_time', comparison)
        self.assertIn('builtin_time', comparison)
        self.assertIn('speedup', comparison)
        self.assertIn('is_correct', comparison)
        self.assertIn('array_length', comparison)
        
        self.assertTrue(comparison['is_correct'])
        self.assertEqual(comparison['array_length'], 100)
        self.assertGreater(comparison['quicksort_time'], 0)
        self.assertGreater(comparison['builtin_time'], 0)
    
    def test_analyze_performance(self):
        """Test performance analysis."""
        results = analyze_performance([100, 1000])
        
        self.assertEqual(len(results), 2)
        for result in results:
            self.assertIn('quicksort_time', result)
            self.assertIn('builtin_time', result)
            self.assertIn('is_correct', result)
            self.assertTrue(result['is_correct'])


class TestEdgeCases(unittest.TestCase):
    """Test cases for edge cases and boundary conditions."""
    
    def test_zero_elements(self):
        """Test arrays with zero elements."""
        arr = []
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        
        self.assertEqual(rand_result, [])
        self.assertEqual(det_result, [])
    
    def test_single_element(self):
        """Test arrays with single element."""
        arr = [42]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        
        self.assertEqual(rand_result, [42])
        self.assertEqual(det_result, [42])
    
    def test_two_elements(self):
        """Test arrays with two elements."""
        arr = [2, 1]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
    
    def test_all_zeros(self):
        """Test arrays with all zeros."""
        arr = [0, 0, 0, 0, 0]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        
        self.assertEqual(rand_result, arr)
        self.assertEqual(det_result, arr)
    
    def test_mixed_positive_negative(self):
        """Test arrays with mixed positive and negative numbers."""
        arr = [-5, 10, -3, 0, 7, -1, 2]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
    
    def test_large_range(self):
        """Test arrays with large value range."""
        arr = [1, 1000000, 500000, 250000, 750000]
        rand_result = randomized_quicksort(arr)
        det_result = deterministic_quicksort(arr)
        expected = sorted(arr)
        
        self.assertEqual(rand_result, expected)
        self.assertEqual(det_result, expected)
    
    def test_deterministic_worst_case_small(self):
        """Test deterministic quicksort on small worst-case inputs."""
        # Small sorted array
        arr = list(range(1, 51))
        result = deterministic_quicksort(arr)
        self.assertEqual(result, arr)
        
        # Small reverse sorted array
        arr = list(range(50, 0, -1))
        result = deterministic_quicksort(arr)
        expected = sorted(arr)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()


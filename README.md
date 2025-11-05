# Randomized Quicksort & Hash Table with Chaining - Algorithm Efficiency and Scalability

## Overview

This project implements two fundamental algorithms and data structures demonstrating algorithm efficiency and scalability:

1. **Randomized Quicksort Algorithm** - An efficient sorting algorithm with average O(n log n) time complexity
2. **Hash Table with Chaining** - A hash table implementation using chaining for collision resolution

Both implementations provide comprehensive test suites, performance analysis utilities, and detailed documentation for educational purposes.

### Key Features

* ✅ **Randomized Quicksort**: Efficient sorting with randomized pivot selection to avoid worst-case performance
* ✅ **Performance Analysis**: Built-in utilities for comparing and analyzing algorithm performance
* ✅ **Hash Table with Chaining**: Complete hash table implementation with dynamic resizing
* ✅ **Comprehensive Test Suite**: Extensive test coverage including edge cases, stress tests, and performance benchmarks
* ✅ **Well-Documented Code**: Clear comments, docstrings, and educational examples
* ✅ **Production-Ready**: Robust error handling and comprehensive test coverage

## Architecture

### Randomized Quicksort Algorithm Flow

```
Input Array: [64, 34, 25, 12, 22, 11, 90, 5]
             ↓
    ┌─────────────────────────────────────┐
    │   Randomized Quicksort Process      │
    └─────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────────────────┐
    │  Step 1: Randomly select pivot                  │
    │  Pivot: 25 (randomly selected)                  │
    │  Partition: [12, 22, 11, 5] | 25 | [64, 34, 90] │
    └─────────────────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────┐
    │  Step 2: Recursively sort left      │
    │  Array: [12, 22, 11, 5]             │
    │  Pivot: 11 → [5, 11] | [12, 22]     │
    └─────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────┐
    │  Step 3: Recursively sort right     │
    │  Array: [64, 34, 90]                │
    │  Pivot: 64 → [34, 64] | [90]        │
    └─────────────────────────────────────┘
             ↓
Output Array: [5, 11, 12, 22, 25, 34, 64, 90]
```

### Hash Table with Chaining Structure

```
Hash Table (size=8)
┌─────────────────────────────────────────┐
│ Bucket 0: [Key: 8, Value: "eight"]      │
│           [Key: 16, Value: "sixteen"]   │
│ Bucket 1: [Key: 9, Value: "nine"]       │
│ Bucket 2: [Key: 10, Value: "ten"]       │
│           [Key: 18, Value: "eighteen"]  │
│ Bucket 3: [Key: 11, Value: "eleven"]    │
│ Bucket 4: [Key: 12, Value: "twelve"]    │
│ Bucket 5: [Key: 13, Value: "thirteen"]  │
│ Bucket 6: [Key: 14, Value: "fourteen"]  │
│ Bucket 7: [Key: 15, Value: "fifteen"]   │
└─────────────────────────────────────────┘
         ↓
    Collision Resolution via Chaining
    (Multiple keys hash to same bucket)
```

### Core Algorithm Structure

#### Randomized Quicksort

```
┌─────────────────────────────────────────────────────────────┐
│              Randomized Quicksort                           │
├─────────────────────────────────────────────────────────────┤
│  Function: randomized_quicksort(arr)                        │
│  Input: Array of comparable elements                        │
│  Output: Array sorted in ascending order                    │
├─────────────────────────────────────────────────────────────┤
│  Algorithm Steps:                                           │
│  1. If array has ≤ 1 element, return                        │
│  2. Randomly select pivot element                           │
│  3. Partition array around pivot                            │
│  4. Recursively sort left subarray                          │
│  5. Recursively sort right subarray                         │
│  6. Combine results                                         │
└─────────────────────────────────────────────────────────────┘
```

#### Hash Table with Chaining

```
┌─────────────────────────────────────────────────────────────┐
│              Hash Table with Chaining                       │
├─────────────────────────────────────────────────────────────┤
│  Class: HashTable                                           │
│  Operations: insert, get, delete, contains                  │
├─────────────────────────────────────────────────────────────┤
│  Key Operations:                                            │
│  1. Hash function: h(k) = floor(m × (k × A mod 1))          │
│  2. Collision resolution: Chaining (linked lists)           │
│  3. Load factor management: Resize when threshold exceeded  │
│  4. Dynamic resizing: Double size when load > 0.75          │
└─────────────────────────────────────────────────────────────┘
```

## Implementation Details

### Part 1: Randomized Quicksort

#### Core Functions

##### 1. `randomized_quicksort(arr)`

* **Purpose**: Sort array using randomized quicksort algorithm
* **Parameters**: `arr` (list) - Input array to be sorted
* **Returns**: `list` - New array sorted in ascending order
* **Space Complexity**: O(n) - Creates a copy of the input array
* **Time Complexity**: 
  - Average: O(n log n)
  - Worst: O(n²) - rarely occurs due to randomization
  - Best: O(n log n)

##### 2. `randomized_partition(arr, low, high)`

* **Purpose**: Partition array using a randomly selected pivot
* **Parameters**: 
  - `arr` (list) - Array to partition
  - `low` (int) - Starting index
  - `high` (int) - Ending index
* **Returns**: `int` - Final position of pivot element
* **Key Feature**: Random pivot selection prevents worst-case O(n²) performance

##### 3. `compare_with_builtin(arr)`

* **Purpose**: Compare randomized quicksort with Python's built-in sort
* **Returns**: Dictionary with timing metrics and correctness verification

##### 4. `analyze_performance(array_sizes)`

* **Purpose**: Analyze quicksort performance across different array sizes
* **Returns**: List of performance metrics for each array size

##### 5. `deterministic_quicksort(arr)`

* **Purpose**: Sort array using deterministic quicksort (first element as pivot)
* **Parameters**: `arr` (list) - Input array to be sorted
* **Returns**: `list` - New array sorted in ascending order
* **Time Complexity**: 
  - Average: O(n log n)
  - Worst: O(n²) - occurs on sorted/reverse-sorted arrays
* **Note**: Included for empirical comparison with randomized version

#### Algorithm Logic

**Why Randomization?**

Standard quicksort can degrade to O(n²) when:
- Pivot is always the smallest element (worst case)
- Pivot is always the largest element (worst case)
- Array is already sorted or reverse sorted

Randomization ensures:
- Expected O(n log n) performance
- Expected number of comparisons: 2n ln n ≈ 1.39n log₂ n
- Very low probability of worst-case behavior

### Part 2: Hash Table with Chaining

#### Core Operations

##### 1. `insert(key, value)`

* **Purpose**: Insert or update a key-value pair
* **Time Complexity**: O(1) average case, O(n) worst case
* **Features**: 
  - Automatically updates if key exists
  - Triggers resize when load factor exceeds threshold

##### 2. `get(key)`

* **Purpose**: Retrieve value associated with a key
* **Time Complexity**: O(1) average case, O(n) worst case
* **Returns**: Value if key exists, None otherwise

##### 3. `delete(key)`

* **Purpose**: Remove a key-value pair
* **Time Complexity**: O(1) average case, O(n) worst case
* **Returns**: True if key was found and deleted, False otherwise

##### 4. `contains(key)`

* **Purpose**: Check if a key exists in the hash table
* **Time Complexity**: O(1) average case, O(n) worst case
* **Pythonic**: Supports `in` operator

#### Hash Function

**Multiplication Method:**
```
h(k) = floor(m × (k × A mod 1))
```
where:
- `m` = table size
- `A` ≈ (√5 - 1) / 2 ≈ 0.618 (golden ratio)
- Provides good distribution of keys across buckets

#### Collision Resolution

**Chaining Strategy:**
- Each bucket contains a linked list of key-value pairs
- When collision occurs, new element is appended to chain
- Allows multiple elements per bucket
- No clustering issues unlike open addressing

#### Dynamic Resizing

**Load Factor Management:**
- Default threshold: 0.75
- When load factor exceeds threshold, table size doubles
- All elements are rehashed into new table
- Maintains O(1) average performance

## Complexity Analysis

### Randomized Quicksort

| Aspect               | Complexity | Description                                        |
| -------------------- | ---------- | -------------------------------------------------- |
| **Time Complexity**  | O(n log n) | Average case - randomized pivot selection          |
| **Worst Case**       | O(n²)      | Rarely occurs due to randomization                 |
| **Best Case**        | O(n log n) | Already sorted arrays                              |
| **Space Complexity** | O(log n)   | Average case recursion stack depth                 |
| **Stability**        | Not Stable | Equal elements may change relative order           |

### Hash Table with Chaining

| Aspect               | Complexity | Description                                        |
| -------------------- | ---------- | -------------------------------------------------- |
| **Time Complexity**  | O(1)       | Average case for insert, get, delete               |
| **Worst Case**       | O(n)       | All keys hash to same bucket (rare)                |
| **Space Complexity** | O(n + m)   | n elements + m buckets                             |
| **Load Factor**      | 0.75       | Threshold for automatic resizing                   |

## Usage Examples

### Basic Usage - Randomized Quicksort

```python
from src.quicksort import randomized_quicksort, compare_with_builtin

# Example 1: Basic sorting
arr = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_arr = randomized_quicksort(arr)
print(sorted_arr)  # Output: [5, 11, 12, 22, 25, 34, 64, 90]

# Example 2: Performance comparison
comparison = compare_with_builtin(arr)
print(f"Quicksort time: {comparison['quicksort_time']:.6f} seconds")
print(f"Built-in sort time: {comparison['builtin_time']:.6f} seconds")
print(f"Speedup ratio: {comparison['speedup']:.2f}x")
print(f"Results match: {comparison['is_correct']}")
```

### Basic Usage - Hash Table

```python
from src.hash_table import HashTable

# Create hash table
ht = HashTable(initial_size=16)

# Insert key-value pairs
ht.insert(1, "apple")
ht.insert(2, "banana")
ht.insert(3, "cherry")

# Retrieve values
print(ht.get(1))  # "apple"

# Check if key exists
print(2 in ht)  # True

# Delete a key
ht.delete(2)

# Get all items
items = ht.get_all_items()
print(items)  # [(1, "apple"), (3, "cherry")]
```

### Edge Cases Handled

#### Quicksort

```python
# Empty array
empty_arr = []
result = randomized_quicksort(empty_arr)
print(result)  # Output: []

# Single element
single = [42]
result = randomized_quicksort(single)
print(result)  # Output: [42]

# Duplicate elements
duplicates = [3, 3, 3, 3]
result = randomized_quicksort(duplicates)
print(result)  # Output: [3, 3, 3, 3]

# Negative numbers
negatives = [-5, -2, -8, 1, 3, -1, 0]
result = randomized_quicksort(negatives)
print(result)  # Output: [-8, -5, -2, -1, 0, 1, 3]
```

#### Hash Table

```python
# Empty hash table
ht = HashTable()
print(len(ht))  # 0
print(ht.get(1))  # None

# Collision handling
ht = HashTable(initial_size=5)
ht.insert(1, "one")
ht.insert(6, "six")  # May collide with 1
ht.insert(11, "eleven")  # May collide with 1 and 6
# All keys are stored correctly via chaining

# Load factor management
ht = HashTable(initial_size=4, load_factor_threshold=0.75)
ht.insert(1, "a")
ht.insert(2, "b")
ht.insert(3, "c")
ht.insert(4, "d")  # Triggers resize (load factor = 1.0 > 0.75)
print(ht.size)  # 8 (doubled)
```

## Running the Program

### Prerequisites

* Python 3.7 or higher
* No external dependencies required (uses only Python standard library)

### Execution

#### Run Examples

```bash
python3 -m src.examples
```

#### Run Tests

**Quick Tests (Essential functionality):**
```bash
python3 run_tests.py --quick
```

**Full Test Suite:**
```bash
python3 run_tests.py
```

**Unit Tests Only:**
```bash
python3 run_tests.py --unit-only
```

**Performance Benchmarks:**
```bash
python3 run_tests.py --benchmark
```

**Stress Tests:**
```bash
python3 run_tests.py --stress
```

**Negative Test Cases:**
```bash
python3 run_tests.py --negative
```

**Using unittest directly:**
```bash
python3 -m unittest discover tests -v
```

#### Run Empirical Comparison

**Generate Comparison Plots:**
```bash
python3 -m src.generate_plots
```

**Run Comparison Analysis:**
```bash
python3 -m src.quicksort_comparison
```

Both commands will generate detailed performance data and visualizations comparing Randomized vs Deterministic Quicksort.

## Test Cases

### Randomized Quicksort Tests

The test suite includes comprehensive test cases covering:

#### ✅ **Functional Tests**

* Basic sorting functionality
* Already sorted arrays (ascending/descending)
* Empty arrays and single elements
* Duplicate elements
* Negative numbers and zero values
* Large arrays (1000+ elements)

#### ✅ **Behavioral Tests**

* Non-destructive sorting (original array unchanged)
* Correctness verification against built-in sort
* Partition function correctness

#### ✅ **Performance Tests**

* Comparison with built-in sort
* Performance analysis across different array sizes
* Timing measurements

### Deterministic Quicksort Tests

The test suite includes comprehensive test cases covering:

#### ✅ **Functional Tests**

* All same scenarios as randomized quicksort
* Worst-case performance on sorted/reverse-sorted arrays
* Correctness verification

#### ✅ **Comparison Tests**

* Direct comparison between randomized and deterministic quicksort
* Verification that both produce identical results
* Performance consistency tests

#### ✅ **Edge Cases**

* Zero elements, single element, two elements
* All zeros, mixed positive/negative numbers
* Large value ranges
* Worst-case scenarios for deterministic quicksort

### Hash Table Tests

The test suite includes comprehensive test cases covering:

#### ✅ **Functional Tests**

* Basic insert, get, delete operations
* Empty hash table operations
* Collision handling
* Load factor calculation
* Dynamic resizing

#### ✅ **Behavioral Tests**

* Key existence checking (`in` operator)
* Update existing keys
* Delete from chains (middle of chain)
* Get all items

#### ✅ **Edge Cases**

* Empty hash table
* Single element
* All keys hash to same bucket
* Load factor threshold triggering resize

## Empirical Comparison Study

### Randomized vs Deterministic Quicksort

This project includes a comprehensive empirical comparison study comparing Randomized Quicksort with Deterministic Quicksort (using first element as pivot) across different input sizes and distributions.

**Documentation**: See [`QUICKSORT_COMPARISON.md`](QUICKSORT_COMPARISON.md) for detailed analysis and results.

**Visualizations**: Three comprehensive plots are included:
- `quicksort_comparison_plots.png` - Overview comparison across all distributions
- `quicksort_comparison_detailed.png` - Detailed views for each distribution type
- `quicksort_speedup_comparison.png` - Speedup ratios visualization

**Key Findings**:
- **Random Arrays**: Both algorithms perform similarly (~10-15% difference)
- **Sorted Arrays**: Deterministic degrades to O(n²); Randomized maintains O(n log n) - up to **475x speedup**
- **Reverse-Sorted Arrays**: Even worse degradation for deterministic - up to **857x speedup** for randomized
- **Repeated Elements**: Similar performance for both algorithms

**Running the Comparison**:
```bash
# Generate plots and detailed comparison
python3 -m src.generate_plots
python3 -m src.quicksort_comparison
```

## Project Structure

```
MSCS532_Assignment3/
├── src/
│   ├── __init__.py                # Package initialization
│   ├── quicksort.py              # Randomized & Deterministic Quicksort implementations
│   ├── quicksort_comparison.py   # Empirical comparison script
│   ├── generate_plots.py         # Plot generation script
│   ├── hash_table.py             # Hash Table with Chaining implementation
│   └── examples.py               # Example usage demonstrations
├── tests/
│   ├── __init__.py               # Test package initialization
│   ├── test_quicksort.py         # Comprehensive quicksort tests
│   └── test_hash_table.py        # Comprehensive hash table tests
├── run_tests.py                  # Test runner with various options
├── README.md                     # This documentation
├── QUICKSORT_COMPARISON.md       # Empirical comparison documentation
├── quicksort_comparison_plots.png       # Overview comparison plots
├── quicksort_comparison_detailed.png    # Detailed distribution plots
├── quicksort_speedup_comparison.png     # Speedup ratio plots
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore file
└── requirements.txt              # Python dependencies (none required)
```

## Testing

### Test Coverage

The project includes **41+ comprehensive test cases** covering:

#### ✅ **Functional Tests**

* Basic functionality for both algorithms
* Edge cases (empty, single element, duplicates)
* Correctness verification

#### ✅ **Behavioral Tests**

* Non-destructive operations
* In-place modifications
* Collision resolution
* Dynamic resizing

#### ✅ **Performance Tests**

* Timing comparisons
* Performance analysis across different sizes
* Benchmarking utilities

#### ✅ **Stress Tests**

* Large arrays (1000+ elements)
* Many hash table operations
* Boundary conditions

#### ✅ **Negative Test Cases**

* Invalid input types
* Edge cases and boundary conditions
* Error handling

### Running Tests

The project includes a comprehensive test runner (`run_tests.py`) with multiple options:

- **Quick Tests**: Essential functionality tests
- **Full Suite**: All tests including edge cases
- **Unit Tests**: Standard unittest tests only
- **Benchmarks**: Performance comparison tests
- **Stress Tests**: Large-scale and boundary tests
- **Negative Tests**: Invalid input and error handling tests

## Educational Value

This implementation serves as an excellent learning resource for:

* **Algorithm Understanding**: Clear demonstration of quicksort and hash table mechanics
* **Randomization Techniques**: Shows how randomization improves algorithm performance
* **Data Structure Design**: Demonstrates hash table implementation with collision resolution
* **Code Quality**: Demonstrates good practices in Python programming
* **Testing**: Comprehensive test suite showing edge case handling
* **Documentation**: Well-commented code with clear explanations
* **Performance Analysis**: Tools for understanding algorithm efficiency

## Algorithm Analysis

### Randomized Quicksort

**Why Randomization?**
- Standard quicksort can degrade to O(n²) when the pivot is always the smallest or largest element
- Randomization ensures expected O(n log n) performance
- Expected number of comparisons: 2n ln n ≈ 1.39n log₂ n

**Performance Characteristics:**
- Excellent average-case performance
- Non-destructive sorting (creates copy)
- Cache-friendly due to good locality of reference

**Comparison with Other Algorithms:**
- Faster than O(n²) algorithms (bubble, insertion, selection sort)
- Comparable to merge sort but with better space efficiency
- Generally slower than Python's built-in Timsort (optimized hybrid)

### Empirical Comparison Results

**Randomized vs Deterministic Quicksort:**

The project includes comprehensive empirical analysis comparing Randomized Quicksort with Deterministic Quicksort (first element as pivot). Results demonstrate:

1. **On Random Arrays**: Deterministic is ~10-15% faster (minimal overhead from randomization)
2. **On Sorted Arrays**: Randomized is **up to 475x faster** (deterministic shows O(n²) worst-case)
3. **On Reverse-Sorted Arrays**: Randomized is **up to 857x faster** (even worse degradation for deterministic)
4. **On Repeated Elements**: Both perform similarly (~5% difference)

**Visual Evidence**: The included plots (`quicksort_comparison_*.png`) clearly show:
- Exponential degradation curves for deterministic quicksort on worst-case inputs
- Consistent O(n log n) performance for randomized quicksort across all distributions
- Minimal overhead of randomization on random inputs

See [`QUICKSORT_COMPARISON.md`](QUICKSORT_COMPARISON.md) for detailed analysis, tables, and conclusions.

### Hash Table with Chaining

**Chaining vs. Open Addressing:**
- Chaining stores multiple elements in the same bucket using linked lists
- Handles collisions gracefully without clustering
- Load factor threshold prevents performance degradation

**Hash Function:**
- Uses multiplication method: h(k) = floor(m × (k × A mod 1))
- A ≈ (√5 - 1) / 2 ≈ 0.618 (golden ratio)
- Provides good distribution of keys across buckets

**Performance Considerations:**
- O(1) average case performance
- Dynamic resizing maintains efficiency
- Trade-off between space and time efficiency

## Performance Considerations

1. **Quicksort**: 
   - Best for general-purpose sorting
   - Randomization prevents worst-case scenarios
   - Good for medium to large arrays

2. **Hash Table**: 
   - Maintains O(1) average performance through load factor management
   - Resizing doubles table size when threshold is exceeded
   - Trade-off between space and time efficiency

## Contributing

This is an educational project demonstrating algorithm implementations. Feel free to:

* Add more test cases
* Implement additional algorithms
* Improve documentation
* Optimize the implementations
* Add visualization tools

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Carlos Gutierrez**  
Email: cgutierrez44833@ucumberlands.edu

Created for MSCS532 Assignment 3: Understanding Algorithm Efficiency and Scalability

## Acknowledgments

* Based on standard algorithm implementations from Introduction to Algorithms (CLRS)
* Educational project for algorithm analysis and data structures course

"""
Unit tests for Hash Table with Chaining implementation.
"""

import unittest
from src.hash_table import HashTable, HashNode


class TestHashTable(unittest.TestCase):
    """Test cases for hash table with chaining."""
    
    def test_initialization(self):
        """Test hash table initialization."""
        ht = HashTable(initial_size=16)
        self.assertEqual(ht.size, 16)
        self.assertEqual(len(ht), 0)
        self.assertEqual(ht.get_load_factor(), 0.0)
    
    def test_insert_and_get(self):
        """Test basic insert and get operations."""
        ht = HashTable()
        ht.insert(1, "apple")
        ht.insert(2, "banana")
        
        self.assertEqual(ht.get(1), "apple")
        self.assertEqual(ht.get(2), "banana")
        self.assertEqual(len(ht), 2)
    
    def test_insert_update(self):
        """Test that inserting same key updates value."""
        ht = HashTable()
        ht.insert(1, "apple")
        ht.insert(1, "banana")
        
        self.assertEqual(ht.get(1), "banana")
        self.assertEqual(len(ht), 1)
    
    def test_get_nonexistent_key(self):
        """Test getting a key that doesn't exist."""
        ht = HashTable()
        ht.insert(1, "apple")
        
        self.assertIsNone(ht.get(2))
    
    def test_delete_existing_key(self):
        """Test deleting an existing key."""
        ht = HashTable()
        ht.insert(1, "apple")
        ht.insert(2, "banana")
        
        deleted = ht.delete(1)
        self.assertTrue(deleted)
        self.assertIsNone(ht.get(1))
        self.assertEqual(ht.get(2), "banana")
        self.assertEqual(len(ht), 1)
    
    def test_delete_nonexistent_key(self):
        """Test deleting a key that doesn't exist."""
        ht = HashTable()
        ht.insert(1, "apple")
        
        deleted = ht.delete(2)
        self.assertFalse(deleted)
        self.assertEqual(len(ht), 1)
    
    def test_contains(self):
        """Test contains method."""
        ht = HashTable()
        ht.insert(1, "apple")
        
        self.assertTrue(ht.contains(1))
        self.assertFalse(ht.contains(2))
    
    def test_in_operator(self):
        """Test using 'in' operator."""
        ht = HashTable()
        ht.insert(1, "apple")
        
        self.assertIn(1, ht)
        self.assertNotIn(2, ht)
    
    def test_load_factor(self):
        """Test load factor calculation."""
        ht = HashTable(initial_size=4)
        
        # Initially empty
        self.assertEqual(ht.get_load_factor(), 0.0)
        
        # Add elements
        ht.insert(1, "a")
        self.assertEqual(ht.get_load_factor(), 0.25)
        
        ht.insert(2, "b")
        self.assertEqual(ht.get_load_factor(), 0.5)
        
        ht.insert(3, "c")
        self.assertEqual(ht.get_load_factor(), 0.75)
    
    def test_resize(self):
        """Test automatic resizing when load factor threshold is reached."""
        ht = HashTable(initial_size=4, load_factor_threshold=0.75)
        
        # Insert elements to trigger resize
        ht.insert(1, "a")
        ht.insert(2, "b")
        ht.insert(3, "c")
        # This should trigger resize (3/4 = 0.75)
        ht.insert(4, "d")
        
        # Size should have doubled
        self.assertEqual(ht.size, 8)
        
        # All elements should still be accessible
        self.assertEqual(ht.get(1), "a")
        self.assertEqual(ht.get(2), "b")
        self.assertEqual(ht.get(3), "c")
        self.assertEqual(ht.get(4), "d")
        self.assertEqual(len(ht), 4)
    
    def test_get_all_items(self):
        """Test getting all items from hash table."""
        ht = HashTable()
        ht.insert(1, "apple")
        ht.insert(2, "banana")
        ht.insert(3, "cherry")
        
        items = ht.get_all_items()
        self.assertEqual(len(items), 3)
        
        # Check that all items are present
        item_dict = dict(items)
        self.assertEqual(item_dict[1], "apple")
        self.assertEqual(item_dict[2], "banana")
        self.assertEqual(item_dict[3], "cherry")
    
    def test_collision_handling(self):
        """Test that collisions are handled correctly."""
        ht = HashTable(initial_size=5)
        
        # Insert keys that might collide
        keys = [1, 6, 11, 16, 21]
        for key in keys:
            ht.insert(key, f"value_{key}")
        
        # All keys should be retrievable
        for key in keys:
            self.assertEqual(ht.get(key), f"value_{key}")
        
        self.assertEqual(len(ht), len(keys))
    
    def test_delete_from_chain(self):
        """Test deleting an element from the middle of a chain."""
        ht = HashTable(initial_size=5)
        
        # Create a chain by inserting colliding keys
        keys = [1, 6, 11]
        for key in keys:
            ht.insert(key, f"value_{key}")
        
        # Delete middle element
        deleted = ht.delete(6)
        self.assertTrue(deleted)
        
        # Remaining elements should still be accessible
        self.assertEqual(ht.get(1), "value_1")
        self.assertIsNone(ht.get(6))
        self.assertEqual(ht.get(11), "value_11")
        self.assertEqual(len(ht), 2)
    
    def test_len(self):
        """Test __len__ method."""
        ht = HashTable()
        self.assertEqual(len(ht), 0)
        
        ht.insert(1, "a")
        self.assertEqual(len(ht), 1)
        
        ht.insert(2, "b")
        self.assertEqual(len(ht), 2)
        
        ht.delete(1)
        self.assertEqual(len(ht), 1)
    
    def test_multiple_operations(self):
        """Test a sequence of mixed operations."""
        ht = HashTable()
        
        # Insert
        ht.insert(1, "one")
        ht.insert(2, "two")
        ht.insert(3, "three")
        
        # Update
        ht.insert(2, "TWO")
        
        # Delete
        ht.delete(1)
        
        # Verify final state
        self.assertIsNone(ht.get(1))
        self.assertEqual(ht.get(2), "TWO")
        self.assertEqual(ht.get(3), "three")
        self.assertEqual(len(ht), 2)
    
    def test_empty_hash_table(self):
        """Test operations on empty hash table."""
        ht = HashTable()
        
        self.assertIsNone(ht.get(1))
        self.assertFalse(ht.contains(1))
        self.assertFalse(ht.delete(1))
        self.assertEqual(ht.get_all_items(), [])
        self.assertEqual(len(ht), 0)


if __name__ == '__main__':
    unittest.main()


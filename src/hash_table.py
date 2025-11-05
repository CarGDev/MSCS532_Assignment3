"""
Hash Table with Chaining Implementation

This module provides a hash table implementation using chaining
for collision resolution.
"""

from typing import List, Optional, Tuple, Iterator
from dataclasses import dataclass


@dataclass
class HashNode:
    """Node for storing key-value pairs in hash table chains."""
    key: int
    value: any
    next: Optional['HashNode'] = None


class HashTable:
    """
    Hash Table implementation using chaining for collision resolution.
    
    Chaining stores multiple elements in the same bucket using a linked list.
    When a collision occurs, the new element is appended to the chain.
    
    Time Complexity:
        - Average: O(1) for insert, search, delete
        - Worst: O(n) when all keys hash to the same bucket
    
    Space Complexity: O(n + m) where n is number of elements, m is table size
    """
    
    def __init__(self, initial_size: int = 16, load_factor_threshold: float = 0.75):
        """
        Initialize hash table.
        
        Args:
            initial_size: Initial size of the hash table
            load_factor_threshold: Threshold for resizing (default: 0.75)
        """
        self.size = initial_size
        self.load_factor_threshold = load_factor_threshold
        self.count = 0
        self.buckets: List[Optional[HashNode]] = [None] * self.size
    
    def _hash(self, key: int) -> int:
        """
        Hash function using multiplication method.
        
        Args:
            key: Key to hash
        
        Returns:
            Hash value (bucket index)
        """
        # Using multiplication method: h(k) = floor(m * (k * A mod 1))
        # where A ≈ (√5 - 1) / 2 ≈ 0.618
        A = 0.6180339887498949
        return int(self.size * ((key * A) % 1))
    
    def _resize(self) -> None:
        """Resize hash table when load factor exceeds threshold."""
        old_buckets = self.buckets
        old_size = self.size
        
        # Double the size
        self.size *= 2
        self.count = 0
        self.buckets = [None] * self.size
        
        # Rehash all existing elements
        for bucket in old_buckets:
            current = bucket
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next
    
    def insert(self, key: int, value: any) -> None:
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key: Key to insert
            value: Value associated with the key
        """
        # Check if resize is needed
        load_factor = self.count / self.size
        if load_factor >= self.load_factor_threshold:
            self._resize()
        
        bucket_index = self._hash(key)
        
        # Check if key already exists
        current = self.buckets[bucket_index]
        while current is not None:
            if current.key == key:
                current.value = value  # Update existing key
                return
            current = current.next
        
        # Insert new node at the beginning of the chain
        new_node = HashNode(key, value, self.buckets[bucket_index])
        self.buckets[bucket_index] = new_node
        self.count += 1
    
    def get(self, key: int) -> Optional[any]:
        """
        Retrieve value associated with a key.
        
        Args:
            key: Key to search for
        
        Returns:
            Value associated with key, or None if not found
        """
        bucket_index = self._hash(key)
        current = self.buckets[bucket_index]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def delete(self, key: int) -> bool:
        """
        Delete a key-value pair from the hash table.
        
        Args:
            key: Key to delete
        
        Returns:
            True if key was found and deleted, False otherwise
        """
        bucket_index = self._hash(key)
        current = self.buckets[bucket_index]
        prev = None
        
        while current is not None:
            if current.key == key:
                if prev is None:
                    # Node to delete is at the head of chain
                    self.buckets[bucket_index] = current.next
                else:
                    # Node to delete is in the middle or end
                    prev.next = current.next
                self.count -= 1
                return True
            prev = current
            current = current.next
        
        return False
    
    def contains(self, key: int) -> bool:
        """
        Check if a key exists in the hash table.
        
        Args:
            key: Key to check
        
        Returns:
            True if key exists, False otherwise
        """
        return self.get(key) is not None
    
    def get_load_factor(self) -> float:
        """
        Get current load factor of the hash table.
        
        Returns:
            Load factor (count / size)
        """
        return self.count / self.size if self.size > 0 else 0.0
    
    def get_all_items(self) -> List[Tuple[int, any]]:
        """
        Get all key-value pairs in the hash table.
        
        Returns:
            List of (key, value) tuples
        """
        items = []
        for bucket in self.buckets:
            current = bucket
            while current is not None:
                items.append((current.key, current.value))
                current = current.next
        return items
    
    def __len__(self) -> int:
        """Return the number of elements in the hash table."""
        return self.count
    
    def __contains__(self, key: int) -> bool:
        """Check if key exists in hash table using 'in' operator."""
        return self.contains(key)
    
    def __repr__(self) -> str:
        """String representation of the hash table."""
        items = self.get_all_items()
        return f"HashTable(size={self.size}, count={self.count}, load_factor={self.get_load_factor():.2f}, items={items})"


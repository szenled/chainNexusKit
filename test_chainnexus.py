# test_chainnexus.py
"""
Tests for chainNexus module.
"""

import unittest
from chainnexus import chainNexus

class TestchainNexus(unittest.TestCase):
    """Test cases for chainNexus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = chainNexus()
        self.assertIsInstance(instance, chainNexus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = chainNexus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_etherpeak.py
"""
Tests for EtherPeak module.
"""

import unittest
from etherpeak import EtherPeak

class TestEtherPeak(unittest.TestCase):
    """Test cases for EtherPeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherPeak()
        self.assertIsInstance(instance, EtherPeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherPeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

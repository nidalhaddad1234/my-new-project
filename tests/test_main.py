"""
Tests for the main application
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import greet, add_numbers

def test_greet():
    """Test the greet function"""
    result = greet("World")
    assert "Hello, World!" in result
    print("✅ test_greet passed")

def test_add_numbers():
    """Test the add_numbers function"""
    result = add_numbers(2, 3)
    assert result == 5
    print("✅ test_add_numbers passed")

if __name__ == "__main__":
    test_greet()
    test_add_numbers()
    print("🎉 All tests passed!")

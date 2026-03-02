import sys
import os

# This tells Python to look outside the 'tests' folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic import convert_logic

def test_celsius_to_fahrenheit():
    # Test: 0 Celsius should be 32 Fahrenheit
    assert convert_logic(0, "Celsius to Fahrenheit") == 32.0

def test_km_to_miles():
    # Test: 1 Km should be 0.621371 Miles
    result = convert_logic(1, "Km to Miles")
    assert round(result, 6) == 0.621371
# tests/calculations_test.py

import sys
import os

# Asegura que podamos importar desde src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from calculations import area_of_circle, get_nth_fibonacci  # noqa: E402


def test_area_of_circle_positive_radius_r1():
    """π * r^2 con r=1 -> ~3.14159"""
    result = area_of_circle(1)
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_positive_radius_r2():
    """π * r^2 con r=2 -> 12.56637"""
    result = area_of_circle(2)
    assert round(result, 5) == 12.56637


def test_area_of_circle_zero_radius():
    """r = 0"""
    assert area_of_circle(0) == 0


def test_get_nth_fibonacci_zero():
    """n = 0"""
    assert get_nth_fibonacci(0) == 0


def test_get_nth_fibonacci_one():
    """n = 1"""
    assert get_nth_fibonacci(1) == 1


def test_get_nth_fibonacci_ten():
    """n = 10 -> 55"""
    assert get_nth_fibonacci(10) == 55

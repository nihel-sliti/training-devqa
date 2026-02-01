import pytest
from src.calculator import add, divide

def test_add_ok():
    assert add(2, 3) == 5

def test_divide_ok():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError) as exc:
        divide(10, 0)
    assert "division by zero" in str(exc.value)

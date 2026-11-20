import pytest
from num_series import random_series, sine_series, trend_series

def test_random_series_length():
    data = random_series(10)
    assert len(data) == 10

def test_negative_n_error():
    with pytest.raises(ValueError):
        random_series(-5)

def test_sine_series_range():
    data = sine_series(10, amplitude=1.0, noise=0.0)
    # Синус без шума не должен выходить за пределы амплитуды
    assert all(-1.0 <= x <= 1.0 for x in data)
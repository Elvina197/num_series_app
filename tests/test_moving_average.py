import pytest
from num_series import simple_moving_average, exponential_moving_average, centered_moving_average

def test_sma_simple():
    data = [1.0, 2.0, 3.0, 4.0]
    # (1+2+3)/3 = 2.0; (2+3+4)/3 = 3.0
    assert simple_moving_average(data, window=3) == [2.0, 3.0]

def test_sma_window_too_big():
    with pytest.raises(ValueError):
        simple_moving_average([1, 2], window=3)

def test_ema():
    data = [10.0, 20.0]
    # EMA[0] = 10; EMA[1] = 0.5 * 20 + (1-0.5) * 10 = 15
    assert exponential_moving_average(data, alpha=0.5) == [10.0, 15.0]

def test_cma_even_window_error():
    with pytest.raises(ValueError):
        centered_moving_average([1, 2, 3, 4], window=2)
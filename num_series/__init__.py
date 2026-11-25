"""Пакет алгоритмической обработки числовых рядов. 
Публичный API пакета: 
Генерация ряда: 
random_series, sine_series, trend_series 
Статистика: 
mean, median, spread, summarize 
Скользящие средние: 
simple_moving_average, 
centered_moving_average, 
exponential_moving_average 
Пример: 
>>> from num_series import sine_series, summarize, simple_moving_average 
>>> data = sine_series(20, noise=0.5, seed=42) 
>>> stats = summarize(data) 
>>> sma = simple_moving_average(data, 3) 
"""

from .generator import random_series, sine_series, trend_series
from .stats import mean, median, spread, summarize
from .io_json import save_series_json, load_series_json
from .io_file import load_series_txt, load_series_csv, load_series_auto

from .moving_average import (
    simple_moving_average,
    centered_moving_average,
    exponential_moving_average,
    benchmark_moving_average,
)

from .deque_average import (
    simple_moving_average_deque,
    centered_moving_average_deque,
    exponential_moving_average_deque,
)

from .best_window import best_window_by_rmse

__all__ = [
    # генерация
    "random_series", "sine_series", "trend_series",
    # статистика
    "mean", "median", "spread", "summarize",
    # ввод-вывод
    "save_series_json", "load_series_json", "load_series_txt", "load_series_csv", "load_series_auto",
    # скользящие средние (list)
    "simple_moving_average", "centered_moving_average", "exponential_moving_average",
    # скользящие средние (deque)
    "simple_moving_average_deque", "centered_moving_average_deque", "exponential_moving_average_deque",
    # доп. функции
    "benchmark_moving_average",
    "best_window_by_rmse",
]

__version__ = "1.1.0"
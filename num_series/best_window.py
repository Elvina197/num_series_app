from __future__ import annotations
import math
from typing import Sequence, Tuple
from .moving_average import simple_moving_average

def best_window_by_rmse(data: Sequence[float], windows: Sequence[int]) -> Tuple[int, float]:
    """
    Возвращает кортеж (лучшее_окно, минимальное_СКО) между исходным рядом 
    (в зоне i >= k-1) и его SMA.
    """
    if not data:
        raise ValueError("Ряд пуст")
    
    n = len(data)
    valid_windows = []
    
    # Отфильтровываем невалидные окна
    for k in windows:
        if isinstance(k, int) and not isinstance(k, bool) and 1 <= k <= n:
            valid_windows.append(k)
            
    if not valid_windows:
        raise ValueError("Нет валидных окон для расчёта")

    best_k = None
    best_rmse = math.inf
    
    for k in valid_windows:
        sma = simple_moving_average(data, k)
        # sma[j] соответствует data[j + k - 1]
        diffs = [data[j + k - 1] - sma[j] for j in range(len(sma))]
        # Считаем СКО (Root Mean Square Error)
        rmse = math.sqrt(sum(d * d for d in diffs) / len(diffs))
        
        if rmse < best_rmse:
            best_k = k
            best_rmse = rmse
            
    return best_k, best_rmse
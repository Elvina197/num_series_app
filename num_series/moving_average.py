from typing import List, Sequence

import time 
from collections import deque 
from typing import List, Sequence 

def check_window(window: int, n: int) -> None:
    if not isinstance(window, int) or isinstance(window, bool):
        raise ValueError(f"window должен быть целым, получено: {window!r}")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window - целое > 1")
    if window > n:
        raise ValueError("window не может быть больше длины ряда")

def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA через бегущую сумму (О(n))"""
    check_window(window, len(data))
    running = sum(data[:window]) 
    result = [running / window] 
    for i in range(window, len(data)): 
        running += data[i] - data[i - window] 
        result.append(running / window)
    return result

def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центр. скользящая средняя (нечетное окно)"""
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError("Окно для центрированной средней должно быть нечётным")
    half = window // 2
    result = []
    # Идем по ряду так, чтобы окно помещалось целиком
    for i in range(half, len(data) - half):
        current_window = data[i - half : i + half + 1]
        # ВАЖНО: этот append должен быть внутри цикла (с отступом)
        result.append(sum(current_window) / window) 
        
    return result

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """Экспонц. скользящая средняя""" 
    if not data:
        raise ValueError("Ряд пуст: расчет EMA невозможен")
    if not (0 < alpha <= 1):
        raise ValueError("alpha должно быть в диапазоне (0, 1]")
    
    ema = [data[0]]
    for i in range(1, len(data)):
        next_val = alpha * data[i] + (1 - alpha) * ema[i - 1]
        ema.append(next_val)
    return ema 

def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]: 
    """SMA с использованием deque (двусторонней очереди).""" 
    check_window(window, len(data)) 
    result = [] 
    d = deque() 
    running_sum = 0.0 
    for x in data: 
        d.append(x) 
        running_sum += x 
        if len(d) > window: 
            running_sum -= d.popleft() 
        if len(d) == window: 
            result.append(running_sum / window) 
    return result 
def benchmark_moving_average(data: Sequence[float], window: int, repeats: int = 1000) -> dict: 
    """ 
    Замеряет среднее время выполнения SMA для реализаций на list и deque. 
    Возвращает словарь с ключами 'list' и 'deque' (время в секундах). 
    """ 
    # Проверка корректности окна (выбросит ValueError при необходимости) 
    check_window(window, len(data)) 

    # Замер для list-реализации (существующая simple_moving_average) 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average(data, window) 
    t_list = (time.perf_counter() - t0) / repeats 

    # Замер для deque-реализации 
    t0 = time.perf_counter() 
    for _ in range(repeats): 
        simple_moving_average_deque(data, window) 
    t_deque = (time.perf_counter() - t0) / repeats 
    return {"list": t_list, "deque": t_deque} 


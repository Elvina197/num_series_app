from typing import List, Sequence

def check_window(window: int, n: int) -> None:
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
        raise ValueError("Окно для центр. средней должно быть нечетным")
    half = window // 2
    result = []
    # Идем по ряду так, чтобы окно помещалось целиком
    for i in range(half, len(data) - half):
            current_window = data[i - half : i + half + 1]
    result.append(sum(current_window) / window)
    return result

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """Экспонц. скользящая средняя""" 
    if not (0 < alpha <= 1):
        raise ValueError("alpha должно быть в диапазоне (0, 1]")
    if not data:
        return []
    ema = [data[0]]
    for i in range(1, len(data)):
        next_val = alpha * data[i] + (1 - alpha) * ema[i - 1]
        ema.append(next_val)
    return ema 


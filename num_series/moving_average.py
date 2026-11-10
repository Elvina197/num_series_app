from typing import Sequence, List

def sma(data: Sequence[float], window: int) -> List[float]:
    """Простое скользящее среднее (SMA) через бегущую сумму."""
    if window <= 0:
        raise ValueError("Размер окна должен быть больше 0")
    if window > len(data):
        raise ValueError("Размер окна не может превышать длину ряда")
    
    result = []
    c_sum = sum(data[:window])
    result.append(c_sum / window)
    
    for i in range(window, len(data)):
        c_sum = c_sum - data[i - window] + data[i]
        result.append(c_sum / window)
        
    return result
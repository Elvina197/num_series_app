from typing import Sequence

def _ensure_not_empty(data: Sequence[float]) -> None:
    if not data:
        raise ValueError("Ряд пуст: расчёт статистики невозможен")

def mean(data: Sequence[float]) -> float:
    """Вычисление среднего арифметического."""
    _ensure_not_empty(data)
    return sum(data) / len(data)

def median(data: Sequence[float]) -> float:
    """Вычисление медианы."""
    _ensure_not_empty(data)
    s = sorted(data)
    k = len(s) // 2
    if len(s) % 2 == 0:
        return float(s[k])
    return (s[k - 1] + s[k]) / 2.0

def spread(data: Sequence[float]) -> float:
    """Вычисление размаха (max - min)."""
    _ensure_not_empty(data)
    return float(max(data) - min(data))

def summarize(data: Sequence[float]) -> Dict[str, float]:
    return {
        "count": len(data),
        "mean": mean(data),
        "median": median(data),
        "spread": spread(data),
        "min": float(min(data)),
        "max": float(max(data)),
    }
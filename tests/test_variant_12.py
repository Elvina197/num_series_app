"""Тесты для индивидуального варианта 12."""
import pytest
from num_series.generator import random_series
from num_series.best_window import best_window_by_rmse
from num_series.moving_average import simple_moving_average
from num_series.deque_average import simple_moving_average_deque
from main import main # Импортируем main для CLI-теста

class TestVariant12Generator:
    def test_generator_length_and_bounds(self):
        # Генерируем 500 чисел от 0 до 100 с фиксированным seed
        data = random_series(500, low=0, high=100, seed=42)
        assert len(data) == 500
        assert all(0 <= x < 100 for x in data)
        
    def test_generator_reproducible(self):
        # Проверка воспроизводимости
        data1 = random_series(500, low=0, high=100, seed=42)
        data2 = random_series(500, low=0, high=100, seed=42)
        assert data1 == data2

    def test_best_window_known_values(self):
            # Для константного ряда СКО = 0 для любого окна.
            # Программа выберет первое окно из списка, которое даст 0.
            data = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
            best_k, best_rmse = best_window_by_rmse(data, [2, 5])
            assert best_k == 2
            assert best_rmse == 0.0

    def test_best_window_edge_cases(self):
            # Краевой кейс: окна невалидны (<= 0 или > n)
            data = [1.0, 2.0, 3.0]
            with pytest.raises(ValueError, match="Нет валидных окон"):
                best_window_by_rmse(data, [0, -1, 5])
                
    def test_best_window_ignores_invalid(self):
            # Если есть хоть одно валидное, невалидные просто игнорируются
            data = [1.0, 2.0, 3.0, 4.0]
            # Передаем плохие (0, 10) и хорошее (2) окно. Лучшим должно стать 2.
            best_k, best_rmse = best_window_by_rmse(data, [0, 10, 2])
            assert best_k == 2

class TestVariant12MovingAverages:
    def test_sma_matches_deque(self):
        # Проверяем, что SMA list и SMA deque дают одинаковый результат
        data = [10.0, 20.0, 30.0, 40.0, 50.0]
        w = 3
        sma_list = simple_moving_average(data, w)
        sma_deque = simple_moving_average_deque(data, w)
        assert sma_list == sma_deque

class TestVariant12CLI:
    def test_cli_multiple_windows(self):
        # Проверяем, что CLI принимает несколько окон и выводит результат
        # Строка 1 - успешное выполнение, передаем окна 5 и 10
        exit_code = main(["--kind", "random", "--n", "50", "--window", "5", "10"])
        assert exit_code == 0
        
    def test_cli_drops_invalid_windows(self):
        # Передаем плохие окна (0 и 100), программа не должна падать, 
        # если есть хотя бы одно хорошее (5)
        exit_code = main(["--kind", "random", "--n", "50", "--window", "0", "-5", "100", "5"])
        assert exit_code == 0
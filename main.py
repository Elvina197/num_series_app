import argparse
import sys
from typing import List
from num_series import (
    random_series, sine_series, 
trend_series, 
    get_all_stats, summarize,
    simple_moving_average, centered_moving_average, exponential_moving_average,
)

def main():
    parser = argparse.ArgumentParser(description="Алгоритмическая обработка числовых рядов")
    
    # Аргументы для генерации
    parser.add_argument("--type", choices=["random", "sine", "trend"], default="random", help="Тип генерируемого ряда")
    parser.add_argument("--n", type=int, default=10, help="Количество элементов")
    parser.add_argument("--seed", type=int, default=42, help="Нач. значение для генератора случайных чисел")
    
    # Аргумент для скользящей средней
    parser.add_argument("--window", type=int, default=3, help="Размер окна для скользящей средней")

    args = build_parser().parse_args(argv)

    try:
        # 1. Генерация
        if args.type == "random":
            data = random_series(args.n, seed=args.seed)
        elif args.type == "sine":
            data = sinc_series(args.n, seed=args.seed, noise=0.1)
        elif args.type == "trend":
            data = trend_series(args.n, seed=args.seed, noise=0.5)

        print(f"Сгенерированный ряд ({args.type}):")
        print([round(x, 2) for x in data])
        print("-" * 30)

        # 2. Статистика
        stats = get_all_stats(data)
        print("Статистика:")
        print(f"Среднее: {stats['mean']:.2f}")
        print(f"Медиана: {stats['median']:.2f}")
        print(f"Размах:  {stats['range']:.2f}")
        print("-" * 30)

        # 3. Скользящая средняя
        if args.window <= args.n:
            ma_data = sma(data, args.window)
            print(f"Скользящая средняя (окно {args.window}):")
            print([round(x, 2) for x in ma_data])
        else:
            print("Окно скользящей средней больше длины ряда. Пропуск.")

    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
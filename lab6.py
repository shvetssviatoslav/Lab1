# Автор: Швець Святослав
# Лабораторна №6 — декоратор, що вимірює використання CPU функцією

import time
from functools import wraps


def cpu_usage(func):
    """
    Декоратор вимірює CPU time,
    який витратила функція під час виконання.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_cpu = time.process_time()      # CPU час до виконання
        result = func(*args, **kwargs)       # викликаємо функцію
        end_cpu = time.process_time()        # CPU час після виконання

        cpu_time = end_cpu - start_cpu
        print(f"[{func.__name__}] CPU time: {cpu_time:.6f} секунд")

        return result

    return wrapper


@cpu_usage
def heavy_calculation(n: int):
    """Функція, яка створює навантаження для вимірювання CPU."""
    total = 0
    for i in range(n):
        total += i ** 2
    return total


if __name__ == "__main__":
    number = 1_000_00  # змінюй для більшого навантаження
    result = heavy_calculation(number)
    print(f"Результат: {result}")

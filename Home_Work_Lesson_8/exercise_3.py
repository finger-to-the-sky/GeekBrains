from functools import wraps


# Создаем функцию с аргументом функции
def check_negative(func):
    # Скрываем работу декоратора
    @wraps(func)
    # СОздаем функцию-обертку с разным количеством аргументов
    def wrapper(*args):
        # Чтобы каждое число выводилось с нужными значениями
        for i in args:
            print(i, ':', type(i), end=', ')

    return wrapper


# Вызываем декоратор и оборачиваем функцию ниже
@check_negative
# Создаем функцию а после вызываем ее
def calc_cube(*args):
    for num in args:
        return num ** 3


calc_cube(5, 6)


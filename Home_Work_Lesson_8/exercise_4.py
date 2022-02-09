from functools import wraps


# Cоздаем функцию с параметром для декоратора
def val_checker(*args):
    # Далее функцию с аргументом функции
    def wr(func):
        # Маскировка декоратора и создание самого декоратора
        @wraps(func)
        def wrapper(*args):
            func(*args)
            # Цикл по значениям и если значения больше нуля возвращать работу декоратора
            for i in args:
                if i > 0:
                    return wrapper
            else:
                raise ValueError

        return wrapper

    return wr


# Обертываем функцию ниже с заданым параметром
@val_checker(lambda x: x > 0)
# Создаем функцию для работы с числами
def calc_cube(*args):
    for num in args:
        if num > 0:

            print(num ** 3)
        else:
            return num ** 3


calc_cube(-5)

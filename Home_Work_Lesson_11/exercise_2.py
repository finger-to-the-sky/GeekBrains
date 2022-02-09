# Решение задачи №2:

# Создаем класс обрабатывающий деление на ноль
class ZeroDivisionError:

    # В целях улучшения читабельности кода, используем статический метод и вместо обработки ошибок, зададим правильно условия внутри метода
    @staticmethod
    def Er(num1, num2):

        if num2 == 0:
            return "Деление на ноль невозможно!!!"
        else:
            return f'Результат: {num1 // num2}'


# Создаем экзмепляр нашего класса и выводим результаты на экран
result = ZeroDivisionError.Er(10, 2)
result_error = ZeroDivisionError.Er(10, 0)
print(result)
print(result_error)

# Решение задачи №1

# Создаем класс дата, который принимает в себя значение даты
class Data:
    def __init__(self, data):
        self.data = data

    # Создаем декоратор класса и обрабатываем метод внутри, которого получаем список чисел из даты а затем выводим тип каждого числа пользователю
    @classmethod
    def one_method(cls, data):

        res = [int(i) for i in data.split(".")]
        return f'day: {type(res[0])}, month: {type(res[1])}, year: {type(res[2])}'

    # Обрабатываем второй метод статическим декоратором и проверям валидность значений и в случае их неверности выводим сообщения пользователю
    @staticmethod
    def two_method(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'число: {day} месяц: {month} год: {year}'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


# Далее выводим результаты нашего класса используя два метода
print(Data.one_method('17.05.1999'))
print(Data.two_method(17, 5, 1999))
print(Data.two_method(17, 13, 1999))





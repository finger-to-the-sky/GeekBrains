# Решение задачи №7:

class Complex:

    # Создаем конструктор
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    # Создаем метод сложения

    def __add__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        # Складываем числа и возвращаем числа
        complex_ = self.__complex + other
        return Complex(complex_.real, int(complex_.imag))

    # Создаем метод умножения
    def __mul__(self, other):
        if isinstance(other, Complex):
            other = other.__complex

        complex_ = self.__complex * other
        return Complex(complex_.real, int(complex_.imag))

    # Выводим сообщение пользователю
    def __str__(self):
        return self.__complex.__str__()


c1 = Complex(5, -7)
c2 = Complex(2)

print(c1 + c2, complex(5, -7) + complex(2))
print(c1 * c2, complex(5, -7) * complex(2))
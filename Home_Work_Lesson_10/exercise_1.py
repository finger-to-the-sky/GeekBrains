# Решение задачи №1
# Импортируем модуль для копирования матрицы
import copy


class Matrix:

    # Сощдаем метод-конструктор для хранения данных в классе
    def __init__(self, matrix):
        self.matrix = matrix

    # Затем конструктор строки и в него записываем логику воспроизведения полученных чисел в виде матрицы
    def __str__(self):
        s = ''

        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'

        return s

    # Конструктор который добавит новую матрицу
    def __add__(self, other):

        if len(self.matrix) != len(other.matrix):
            return None

        # Создаем копию матрицы
        matrix_copy = copy.deepcopy(self.matrix)

        # Проходим циклами по спискам списков и складываем их получая новый список
        for i in range(len(self.matrix)):

            for k in range(len(self.matrix[i])):
                matrix_copy[i][k] = self.matrix[i][k] + other.matrix[i][k]

        return Matrix(matrix_copy)


# Создаем списки списков
one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
two = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

a = Matrix(one)
print(a)
b = Matrix(two)
print(b)
# Складываем две матрицы и получаем результат

c = a + b
print(c)


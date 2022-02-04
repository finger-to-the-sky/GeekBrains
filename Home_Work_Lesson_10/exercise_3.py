# Решение задачи №3

class Cell:
    # Создаем конструктор с выозовом и звездочкой
    def __init__(self, cell):
        self.cell = cell
        self.star = '*'

    # Далле конструктор строки и сообщение пользователю
    def __str__(self):

        return str(f'Количество ячеек: {self.cell}')

    # Зтем создаем методы арифметических операций согласно условию задания
    def __sub__(self, other):

        return Cell(abs(self.cell - other.cell))

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    # Создаем метод, который будет выводить нам число звездочек согласно заданому параметру
    def make_order(self, count):
        num = self.cell

        while num > 0:
            for n in range(1, count + 1):
                print(self.star, end='')
                num -= 1
                if num <= 0:
                    break
            print('\n', end='')


# Создаем экземпляры класса и проверяем работу методов
a = Cell(10)
b = Cell(15)
c = Cell(20)
d = Cell(25)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(5)
b.make_order(5)

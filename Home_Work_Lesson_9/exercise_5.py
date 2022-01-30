# Решение задачи №5

# Создаем класс
class Stationery:

    # Определяем аргумент как название
    title = str

    # Просписываем метод с сообщением
    def draw(self):
        message = "Запуск отрисовки..."
        print(message)

# Создаем дочерние классы согласно заднию
class Pen(Stationery):

    # Переопределяем методы draw и указываем название инструмента, а затем выводим сообщение пользователю
    def draw(self):

        instr = self.title = 'Ручка'
        print(f'{instr} - инструмент для записи текста!')


class Pencil(Stationery):

    def draw(self):

        instr = self.title = 'Карандаш'
        print(f'{instr} - Отличный инструмент для визуализации обьектов на бумаге!')


class Handle(Stationery):

    def draw(self):
        instr = self.title = 'Маркер'

        print(f'{instr} - инструмент для обозначения нужных деталей в документации')

# Создаем экземпляр родительского класса и вызываем метод draw
s = Stationery()
s.draw()

# Создаем экземпляр дочернего класса Pen и вызываем метод draw
p = Pen()
p.draw()

# Создаем экземпляр дочернего класса Pencil и вызываем метод draw
pncl = Pencil()
pncl.draw()

# Создаем экземпляр дочернего класса Handle и вызываем метод draw
h = Handle()
h.draw()
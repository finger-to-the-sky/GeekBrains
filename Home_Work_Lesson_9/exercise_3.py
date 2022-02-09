# Решение задачи №3

# Создаем класс Рабочий
class Worker:

    # Определяем аргументы
    name = 'John'
    surname = 'Smith'
    position = 'General Manager'
    # Определяем аргумент как защищенный
    _income = {'wage': 10000, 'bonus': 5000}

# Создаем дочерний класс
class Position(Worker):

    # Определяем метод
    def pos(self):

        # Переопределяем аргументы согласно заданию и выводим результат
        get_full_name = f'Full Name: {self.name} {self.surname} \nPosition: {self.position}'
        print(get_full_name)

        # Переопределяем аргументы и вычисляем общую зарплату рабочего
        income = self._income.values()
        get_total_income = f'Total income: {sum(income)}$'
        print(get_total_income)

# Создаем экземпляр дочернего класса
p = Position()

# Выводим на консоль все аргументы родительского класса
print('Данные в классе Worker: ', p.name, p.surname, p.position, p._income)

# Вызываем метод дочернего класса
p.pos()
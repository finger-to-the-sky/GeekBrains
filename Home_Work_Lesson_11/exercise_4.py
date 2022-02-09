# Решение задач № 4,5,6:

# Создаем класс Уведомленийб который будет выводит сообщение пользователю о передаче товаров и их получении
class Notification:

    # Создаем конструктор с именем складов и самими складами в качестве словарей
    def __init__(self, title):
        self.title = title
        self.equipment = {}
        self.other_equipment = {}

    # Добавляем каждый товар в словарь и выводим сообщение пользователю об этом
    def add_equipment(self, equip):
        self.equipment.update({equip.ser_num: [equip.title]})

        print(f"На склад {self.title} получено оборудование {equip.title}, серийный номер - {str(equip.ser_num)}")

    # Метод для передачи товаров и сообщения пользователю
    def add_other_equipment(self, equip, other):
        self.other_equipment.update({equip.ser_num: [equip.title, other]})

        print(f'Передано оборудование {equip.title},  серийсный номер - {str(equip.ser_num)}')
        other.add_equipment(equip)

    # Сообщения пользователю о списках оборудования и их манипуляций
    def list_equipments(self):
        print(f'На склад {self.title} получено оборудование: ')
        print(self.equipment)
        print(f'Общее количество: {int(len(self.equipment))}')
        print(f'Со склада {self.title} выдано оборудование: ')
        print(self.other_equipment)
        print(f'Общее количество: {int(len(self.other_equipment))}')


# Создаем класс офисное оборудование и конструктор с значениями назввания и серийного номера
class Office_equipment:

    def __init__(self, title, ser_num):
        self.title = title
        self.ser_num = ser_num

    # Возвращаем название модели
    def __str__(self):
        return str(self.title)


# Дочерний класс Принтер
class Printer(Office_equipment):

    # Конструктор, который хранит данный родительского класса и значение скорости печати
    def __init__(self, title, ser_num, speed):
        Office_equipment.__init__(self, title, ser_num)
        self.speed = speed

    # Сообщение пользователю о модели
    def __str__(self):
        return f'Название модели: {Office_equipment.__str__(self)} Параметры: {str(self.speed)}'


# Дочерний класс Сканер
class Scanner(Office_equipment):

    # Коннструктор с значениями родительского класса а так же с значение решительности
    def __init__(self, title, ser_num, resolution):
        Office_equipment.__init__(self, title, ser_num)
        self.resolution = resolution

    def __str__(self):
        return f'Название модели: {Office_equipment.__str__(self)} Параметры: {str(self.resolution)}'


# Дочерний класс Ксерокс
class Copier(Office_equipment):

    # Создаем констурктор с значениями родительского класса а так же с параметрами добавления копий
    def __init__(self, title, ser_num, add):
        Office_equipment.__init__(self, title, ser_num)
        self.add = add

    def __str__(self):
        return f'Название модели: {Office_equipment.__str__(self)} Параметры: {str(self.add)}'


# Создаем два склада и присваиваем им названия
basket_one = Notification('Main')
basket_two = Notification('Small')

# Затем создаем оргтехнику с ее именами и уникальными значениями
model1 = Printer('Lenovo', 345678, 100)
model2 = Scanner('Samsung', 123456, 4000)
model3 = Copier('CopyBoost', 987654, 50)
model4 = Printer('Asus', 245678, 200)

# Выводим ее на консоль

print(model1)
print(model2)
print(model3)

# Далее доббавляем на главный склад наше оборудование
basket_one.add_equipment(model1)
basket_one.add_equipment(model2)
basket_one.add_equipment(model3)
basket_one.add_equipment(model4)

# Передаем оборудование на другой склад
basket_one.add_other_equipment(model1, basket_two)

# Смотрим количество оборудования на двух складах
basket_one.list_equipments()
basket_two.list_equipments()


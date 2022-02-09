# Решение задачи №2
class Road:

    # Определяем аргументы длины и ширины дороги
    _length = 5000
    _width = 20

    # Создаем метод
    def create_road(self):
        # Указываем массу асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1см
        mass_road_kg_1cm = 25

        # Указываем кол-во см толщины полотна
        thickness_sm = 5

        # Делаем рассчет дороги согласно нашим данным и выводим результат
        result = self._length * self._width * mass_road_kg_1cm * thickness_sm
        print(f'{str(result)[:-3]} т.')

# Создаем экземпляр и вызываем метод
a = Road()
a.create_road()
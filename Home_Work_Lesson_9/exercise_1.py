# Решение задачи №1
import time
import os

# Создаем класс
class TrafficLight:

    # Создаем приватный атрибут в качестве списка с цветами светофора
    __color = ['red', 'yellow', 'green']

    # Создаем Метод и Циклом проходим по атрибуту
    def running(self):

        for i in self.__color:

            # Прописываем условия согласно задаче обращайся к каждому элементу списка
            if i == self.__color[0]:
                print(i)
                time.sleep(7)
                os.system('clear')
                print(self.__color[1])
                time.sleep(2)
                os.system('clear')
                print(self.__color[2])

# Создаем экземпляр класса и запускаем светофор
a = TrafficLight()
a.running()


# Решение задачи №3:

# Создаем класс проверки списка
class CheckList:
    # Создаем приватный аргумент - пустой список куда будем заносить наши цифры
    __my_list = []

    # Далее метод добавления
    def app(self):

        # Проверка на наличие ошибок
        try:

            # Бесконечный цикл с условие его остановки
            while True:
                num = int(input("Введите число: "))
                self.__my_list.append(num)
                print(self.__my_list)

            # Обрабатываем ошибки и выводим сообщения пользователю
        except:
            print(f'Вводите только числа! \n{self.__my_list}')
            tr = input(f'Продолжаем? go / stop ')

            # Условие если пользователь хочет остановится то пишет stop и программа завершается
            if tr == 'go':
                my_list = CheckList().app()
                my_list.append(self.__my_list)
                print(my_list)

            elif tr == 'stop':

                print(f'Работа программы завершена! {self.__my_list}')
            else:

                return f'Вы вышли'


# Создаем экземпляры и запускаем метод класса
c = CheckList()
nu = c.app()
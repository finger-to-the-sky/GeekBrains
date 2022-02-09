# Решение задачи №4
import os

# Указываем название папки или же путь к ней если она является подпапкой
#  '/home/runner/TriangularMiniNetworks/1/2'
folder = '/home/runner/TriangularMiniNetworks/1/2'
# Создаем цикл из трех итераторов которые делять папку на составляющие

for root, dirs, files in os.walk(folder):
    # Создаем генератор внутри которого мы получим обьем памяти каждого из файлов зададим ему условие которое будет отбражать файлы нужно длины
    size_100 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 100]

    size_300 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 300]

    size_500 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 500]
    # Выводим в консоль словарь в котором ключи это ограничения и длину каждого списка
    print({100: len(size_100), 300: len(size_300), 500: len(size_500)})

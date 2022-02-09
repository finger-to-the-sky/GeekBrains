# Решение задачи №3
import os
import shutil

# Аргумент функции
n = str
# Название главной директории
main_dir = 'my_project'


# Функция создающая папки а ее аргумент их название
def mkdr(n):
    # Проверка на наличие папки в файловой системе
    if not os.path.exists(n):
        os.mkdir(n)

    # Если папка уже существует
    else:
        print(f"Папка с таким именем {n} уже существует!")


# Обработка исключений
try:
    mkdr(main_dir)
    os.chdir(main_dir)

    # Полный путь к главной директории на случай возврата
    full_path = str(os.getcwd())

    # Создаем список названий подпапок и затем генератор который создает папки с этими названиями
    list_dirs_1 = ['settings', 'adminapp', 'templates']
    path_create = [i == mkdr(i) for i in list_dirs_1]

    # Переходим в нужную директорию и создаем еще две подпапки
    os.chdir('templates')
    mkdr('mainapp')
    mkdr('authapp')

    # Переходим в нужную директорию и создаем два html файла
    os.chdir('mainapp')
    file_1 = open('base.html', 'a', encoding='utf-8')
    file_2 = open('index.html', 'a', encoding='utf-8')

    # Копируем файлы в соседнюю директорию используя ее путь
    shutil.copy2('base.html', '/home/runner/TriangularMiniNetworks/my_project/templates/authapp', follow_symlinks=True)
    shutil.copy2('index.html', '/home/runner/TriangularMiniNetworks/my_project/templates/authapp', follow_symlinks=True)

# На случай когда необходимо вернутся в предыдущую директорию а система выдает ошибку
except FileNotFoundError as e:

    # Сообщение пользователю
    print(f' Обьект {e}, был не найден в текущей дериктории. Вы будете отправленны в: ' + main_dir)

    # Переход в главную директорию
    os.chdir(full_path)
    print(os.getcwd())

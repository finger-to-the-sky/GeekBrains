# Решение задачи №1
import os
# Создаем переменную с название папки
general_path_name = 'my_project'
# Если папки нет в файловой системе то создаем ее
if not os.path.exists(general_path_name):
    os.mkdir(general_path_name)

# Переходим в нашу папку
os.chdir(general_path_name)
# Проверяем текущую директорию
print(os.getcwd())
# Создаем список подпапок
name_list = ['settings','mainapp','adminapp','authapp']
# Далее перебор в цикле списка и создание подпапок с соответствующим названием
for i in name_list:
    if not os.path.exists(i):
        i = os.mkdir(i)


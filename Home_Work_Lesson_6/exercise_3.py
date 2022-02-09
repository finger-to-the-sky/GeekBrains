# Создаем файлы с именами и хобби

with open("users.csv", 'w',encoding='utf-8') as file_1:
    file_1.write('Иванов Иван Иванович'+ '\n')
    file_1.write('Петров Петр Петрович')
    file_1.write('\n'+ 'Максим' + '\n')

with open("hobby.csv", 'w',encoding='utf-8') as file_2:
    file_2.write('Скалолазание, охота' + '\n')
    file_2.write('Горные лыжи' + '\n')

    # Добавление хобби для теста кода
    #file_2.write('бодибилдинг' + '\n')
    #file_2.write('плаванье' + '\n')

# Открываем файлы и заносим их текст в переменные
file_3 = open("users.csv", 'r',encoding='utf-8')
names = file_3.readlines()

file_4 = open ('hobby.csv', 'r',encoding='utf-8')
hobbies = file_4.readlines()

# Создаем пустой словарь
slov = {}
# В результате вывода программа выводит /n чтобы избавится от него сделаем генератор с срезом строки
names = [str[:-1] for str in names]
hobbies = [str[:-1] for str in hobbies]

# Далее цикл в котором мы будем добавлять ключи и значения по условиям согласно заданию
for i in range(0,len(names)):

    if len(names)< len(hobbies):
        slov == int
        slov = 1

    elif len(names) == len(hobbies):
        slov[names[i]] = hobbies[i]
    elif len(names) > len(hobbies):
        hobbies.append(None)
        slov[names[i]] = hobbies[i]

print(slov)
# Далее создаем файл и заносим в него готовый словарь
if slov != 1:
    with open ('slovar.csv', 'w',encoding= 'Utf-8') as f:

         f.write(str(slov))
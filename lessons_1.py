# Решения задачи №1:
duration = 940000

# Создаем переменные с рассчетами полученных чисел
minutes = (duration // 60) % 60
second = duration % 60
hours = ((duration // 60) // 60) % 24
days = (((duration // 60) // 60) // 24) % 24

# Передаем значения переменных под определенные условия
if duration < 60:
    print(duration, 'сек')

elif duration >= 60 and duration < 3600:
    print(minutes, 'мин', second, 'cек')

elif duration >= 3600 and duration < 86400:
    print(hours, 'ч', minutes, 'мин', second, 'сек')

elif duration >= 86400:
    print(days, 'дн', hours, 'ч', minutes, 'мин', second, 'сек')

# Решение  задачи №2:
# Cоздаем список чисел из нечетных кубов
coub = [i ** 3 for i in list(range(1, 1001, 2))]

result = 0  # сюда мы поместим результат первого списка
result_two = 0  # сюда второго
# создаем счетчик чисел и делим их на 7, затем добавляем результат в result
for i in coub:
    number = 0  # хранилище для счетчика

    for digit in str(i):
        number += int(digit)

    if number % 7 == 0:
        result += i
print(result)

# cоздаем аналогию предыдущего счетчика добавив к элементам списка число 17 и делим их на 7
for i in coub:
    i += 17
    number_update = 0

    for dig_update in str(i):
        number_update += int(dig_update)

        if number_update % 7 == 0:
            result_two += i

print(result_two)


# Решение задачи №3:
# Создаем функцию с агруметом который будет обращаться к числу

def declination(number):
    # список склонений
    dec_list = ['', 'а', 'ов']
    # диапазон чисел
    number = number % 100
    # условия для правильного склонения к каждому числу
    if number >= 11 and number <= 19:
        dec = dec_list[2]
    else:
        i = number % 10
        if i == 1:
            dec = dec_list[0]
        elif i in [2, 3, 4]:
            dec = dec_list[1]
        else:
            dec = dec_list[2]
    return dec


for i in range(1, 101):
    print('{} процент{}'.format(i, declination(i)))

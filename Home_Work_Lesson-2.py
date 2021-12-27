# Рeшение задачи №1:
number_one = 15 * 3
# Определяем тип результата выражений c помощью type
print(type(number_one))

number_two = 15 / 3
print(type(number_two))

number_three =15 // 2
print(type(number_three))

number_four = 15 ** 2
print(type(number_four))
# Решение задачи №2:

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была','+5','градусов']

# Создаем новый список для добавления туда элементов старого списка с новыми значениями
my_new_list = []

# Перебираем элементы старого списка и добавляем их в новый с улучшением значений согласно заданию
for i in my_list:

    if i.isdigit():

        my_new_list.append('"{:02d}"'.format(int(i)))

    elif i.startswith('-'):
        my_new_list.append('"{}{:02d}"'.format(i[0], int(i[1])))

    elif i.startswith('+'):
        my_new_list.append('"{}{:02d}"'.format(i[0], int(i)))

    else:
        my_new_list.append(i)

# Далее полученный результат преобразовываем в строку с соблюдением отступа
print(' '.join(my_new_list))

# Решение задачи №4:
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Перебираем значения в списке и разобьем их на части методом split, после чего обращаемся к индексу каждого элемента
for ind in my_list:
    name = ind.split()
    # Оформим вывод согласно заданию
    print('Привет, {}!'.format(name[-1].lower().title()))

# Решение задачи №5:
prices = [45.04, 97.62, 13.01, 29, 55.5, 87.36, 63.91, 71.45, 30.78, 7.82]

# Для доказательства работы с одним и тем же списком, выведем адрес нашего списка на экран
print(id(prices), '<- id до сортировки')

# Отсортируем список по возрастанию
prices.sort()

# Создаем строку с заданными условиями согласно заданию
for i in prices:
    rub = int(i)
    kop = round((i - rub) * 100)
    string = f'{rub} руб {kop:02.0f} коп'
    print(string, end=', ')
# Выводим на экран адрес списка после сортировки
print(id(prices), '<- id после сортировки')

# Cоздаем список покупок отсортированный в обратном порядке
reverse_prices = []
reverse_prices.extend(prices)
reverse_prices.sort(reverse=True)
for price in reverse_prices:
    rub = int(price)
    kop = round((price - rub) * 100)
    string = f'{rub} руб {kop:02.0f} коп'
    print(string, end=', ')

# Создаем список 5 самых дорогих покупок
max_prices = sorted(reverse_prices)[-5:]

# В цикле отсортируем полученный список по убыванию, для удобного чтения полученного результата
for m in sorted(max_prices, reverse=True):
    rub = int(m)
    kop = round((m - rub) * 100)
    string = f'{rub} руб {kop:02.0f} коп'
    # Для того, чтобы эти значения не сливались с верхними списками, сделаем перенос строки и изменим окончание итерации
    print('\n' + string, end=' - Одна из самых дорогих покупок')

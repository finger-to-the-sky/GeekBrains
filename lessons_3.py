# Решение задачи №1 и №2:

# Создаем словарь с числительными
dict_list = {'One': 'Один', 'one': 'один', 'Two': 'Два', 'two': 'два', 'Three': 'Три', 'three': 'три', 'Four': 'Четыре',
             'four': 'четыре', 'Five': 'Пять', 'five': 'пять', 'Six': 'Шесть', 'six': 'шесть', 'Seven': 'Семь',
             'seven': 'семь', 'Eighth': 'Восемь', 'eighth': 'восемь', 'Nine': 'Девять', 'nine': 'девять',
             'Ten': 'Десять', 'ten': 'десять'}


# Создаем функцию с аргументом, который будет в качестве указанного ключа в словаре
def num_translate_adv(s):
    # Выводим в консоль значение по указанному ключу
    print(dict_list.get(s))


# Вызываем функцию и указываем числительное, которое нужно перевести
num_translate_adv('One')

# Решение задачи №3:
# Создаем пустой список, который будет аргументом нашей функции.
names = []
# Создаем словарь в который будем добавлять первые буквы имен и их списки
albums = dict()
# Создаем функцию
def thesaurus(names):
    for name in names:
        # Переменная которая является первой буквой каждого нашего имени в списке
        first_letter = name[0].upper()
        # Заносим буквы и имена в словарь
        albums[first_letter] = albums.setdefault(first_letter, []) + [name.capitalize()]

    print(albums, sep= '/n')

thesaurus(("Иван", "Мария", "Петр", "Илья"))

# Решение задачи №5:
# импортируем модуль рандом для получения случайных значений
import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Далее создаем пустой список в который будут заносится три рандомных слова из трех списков
joke = []
# Создаем функцию с аргументами согласно заданию
def get_jokes(n,flag = False):
    for i in range(n):
    # Получаем рандомное слово из каждого списка
        element_1 = random.choice(nouns)
        element_2 = random.choice(adverbs)
        element_3 = random.choice(adjectives)
    # Далее формируем все три слова в одну строку
        jok = (f'{element_1} {element_2} {element_3}')
    # Добавляем полученный результат в список
        joke.append(jok)
        # Затем создаем список который будет список в случае разрешения повтора слов
        list_one = []
        if flag == True:
            list_one = jok.split()
        # Организовываем цикл к каждому списку слов и если они равны слову которое уже есть в повторе то заменяем его
            for noun in nouns:
                for fun in list_one:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in list_one:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjectiv in adjectives:
                for fun in list_one:
                    if fun == adjectiv:
                        adjectives.remove(adjectiv)

# Выводим на консоль результат
    print(joke)
print(get_jokes(3,flag = True))






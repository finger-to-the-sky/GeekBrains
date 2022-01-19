import sys

if __name__ == '__main__':
    # Создаем список и с помощью метода map указываем преобразование к числу и аргумент(ы) скрипта
    i = list(map(int, sys.argv[1:]))
    # Далее открываем файл и в переменную заносим линию текста
    with open('bakery.csv') as f:
        text = f.readlines()
        # Согласно условиям задачи указываем что если аргумента два то выводить от начала первого до конца второго
        # c помощью указания индекса в списке
        if len(i) == 2:
            for j in text[i[0] - 1: i[1]]:
                print(j.strip())
        # Если аргумент один то он так же равняется индексу и выводить число под этим индексом
        elif len(i) == 1:
            for j in text[i[0] - 1:]:
                print(j.strip())
        else:
            for j in text:
                print(j.strip())
    exit()
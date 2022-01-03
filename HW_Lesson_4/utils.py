# Решение задачи №2:

import requests

# через API получает ответ от сервера
responce = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
# далее разбиваем полученный текст на список
my_params = responce.split()
# преобразовываем его в тип данных строка
string_my_params = str(my_params)

# далее срезом выводим курсы доллара и евро по отношению к рублю
string_USD = string_my_params[1815:1822]

# для того, чтобы преобразовать результат функции в float необходимо заменить результат с 74,2926 на 74.2926
replace_USD = string_USD.replace(',', '.')

# преобразовываем string в тип float
course_USD = float(replace_USD)

# все тоже самое с евро
string_EUR = string_my_params[1952:1959]
replace_EUR = string_EUR.replace(',', '.')
course_EUR = float(replace_EUR)

# аргументы для функции
one = None
two = None


def currenry_rates(one, two):
    # для того чтобы функция работала только с USD и EUR аргументы будут равны строке с названием валюты
    if one == "USD":
        print(course_USD)

    # для различного порядка аргументов сделаем следующее
    elif one == "EUR":
        print(course_EUR)

    # если аргументы функции не соответствует USD вовращать None
    elif one != "USD":
        print(None)

    if two == "USD":
        print(course_USD)
    elif two == "EUR":
        print(course_EUR)

    # если аргументы функции не соответствует EUR возвращать None
    elif two != 'EUR':
        print(None)

if __name__ == "__main__":
    currenry_rates("USD", "EUR")



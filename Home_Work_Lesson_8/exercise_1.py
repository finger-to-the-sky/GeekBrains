import re


# Создаем функцию с аргуметом нашего адрес
def email_parse(email):
    # Пишем регулярное выражение адреса
    valid_email_regex = '^(\w|.|_|-)+[@](\w|_|-|.)+[.]\w{2,3}$'
    # Проверяем на наличие всех значений наш адрес
    if not re.search(valid_email_regex, email):
        raise ValueError
        # Далее делим полученный адрес
    sp_email = re.split(r'[@]', email)
    # СОздаем словарь и выводим его пользователю
    result = {'username': sp_email[0], 'domain': sp_email[1]}
    print(result)


email_parse('someone@geekbrains.com')



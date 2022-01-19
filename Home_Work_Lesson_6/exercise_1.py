import requests
# Используем отправку запроса серверу для получения текста
url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
responce = requests.get(url).text
# Указываем название файла
name = 'nginx_logs.txt'
# Создаем файл и вносим в него полученный текст в ответе от сервера
with open(name,'w') as f:
    f.write(responce)



# Открываем файл и полученную строку делим на элементы строки и заносим в список
with open(name, "r") as f:
    for i in f:
        line = f.readline()
        pri = line.split()
        # Указываем индекс нужной нам строки из списка
        result = pri[0],pri[5],pri[6]
        print(result)

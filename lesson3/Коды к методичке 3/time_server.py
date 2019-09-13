# Программа сервера времени
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind(('', 8888))                # Присваивает порт 8888
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # одновременно обслуживает не более
                                  # 5 запросов.
while True:
    client, addr = s.accept()     # Принять запрос на соединение
    print("Получен запрос на соединение от %s" % str(addr))
    timestr = time.ctime(time.time()) + "\n"

    # Обратите внимание, дальнейшая работа ведётся с сокетом клиента
    client.send(timestr.encode('utf-8'))   # <- По сети должны передаваться байты,
                                           # поэтому выполняется кодирование строки
    client.close()


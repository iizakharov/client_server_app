# 1) Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность
# сетевых узлов. Аргументом функции является список, в котором каждый сетевой узел должен быть
# представлен именем хоста или ip-адресом. В функции необходимо перебирать ip-адреса и проверять
# их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
import os
from subprocess import Popen, PIPE, call, check_call, CalledProcessError
import sys


def host_ping(arr):
    i = 0
    for n in arr:
        args = ['ping', n]
        try:
            process = check_call(args, stdout=PIPE, universal_newlines=True)
            print(n + ' Доступен!')
        except CalledProcessError:
            print(n +' не пингуется!')



array = ['yandex.ru', 'google.com', 'mail.ru', 'geekbrains.ru', '10.0.1.23']
host_ping(array)

# args = ["ping", "www.google.ru"]
# process = Popen(args, stdout=PIPE)
#
# # communicate - связь с созданным процессом
# # None – это результат stderr, а это значит, что ошибок не найдено
# data = process.communicate()
# for line in data:
#     print(line.decode("cp866"))




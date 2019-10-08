# Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний
# октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.


import subprocess
import os


# def host_range_ping(host, min, max):
#     with open(os.devnull, "wb") as limbo:
#         ip_split = host.split('.')
#         new_ip = '{}.{}.{}.'.format(ip_split[0], ip_split[1], ip_split[2])
#
#         for n in range(min, max):
#             ip = "{}{}".format(new_ip, n)
#             result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
#                                   stdout=limbo, stderr=limbo).wait()
#             print(result)
#             if result:
#                 print(ip, "inactive")
#             else:
#                 print(ip, "active")
#
#
# host_range_ping('192.168.0.0', 10, 15)


for n in range(1, 10):
    ip = "192.168.0.{0}".format(n)
    result = subprocess.Popen(["ping", ip])
    if result:
        print(ip, "inactive")
    else:
        print(ip, "active")
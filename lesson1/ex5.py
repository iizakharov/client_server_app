# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.

import subprocess
import chardet

print(' Ping yandex.ru..........')
site1 = ['ping', 'yandex.ru']
ping_ya = subprocess.Popen(site1, stdout=subprocess.PIPE)
for i in ping_ya.stdout:
    result = chardet.detect(i)
    i = i.decode(result['encoding']).encode('utf-8')
    print(i.decode('utf-8'))

print(' Ping youtube.com..........')
site2 = ['ping', 'youtube.com']
ping_you = subprocess.Popen(site2, stdout=subprocess.PIPE)
for i in ping_you.stdout:
    result = chardet.detect(i)
    i = i.decode(result['encoding']).encode('utf-8')
    print(i.decode('utf-8'))


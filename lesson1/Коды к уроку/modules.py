import subprocess
import chardet

args = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in ya_ping.stdout:
    result = chardet.detect(line)
    print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

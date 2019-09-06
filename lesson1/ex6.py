# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл
# в формате Unicode и вывести его содержимое.

import locale

str_ru = 'сетевое программирование, сокет, декоратор'
f_n = open('test_file.txt', 'w', encoding='utf-8')
f_n.write(str_ru)
f_n.close()
print(type(f_n))  # <class '_io.TextIOWrapper'>
a = locale.getpreferredencoding(f_n)
print(a)  # cp1251

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')



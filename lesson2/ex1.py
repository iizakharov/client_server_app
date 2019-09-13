# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных
# данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл
# в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью
# регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
# «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка
# и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
# получение данных через вызов функции get_data(), а также сохранение подготовленных данных
# в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv
import re


os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = [{
    'Изготовитель системы': os_prod_list,
    'Название ОС': os_name_list,
    'Код продукта': os_code_list,
    'Тип системы': os_type_list,
}]


def get_data(file):
    with open(file) as f_n:
        f_n_reader = csv.reader(f_n)
        for row in f_n_reader:
            myString = ''.join(row)
            new_row = re.sub(r'\s{2,}', ' ', myString)
            if 'Изготовитель системы' in new_row:
                list_row = new_row.split(':')
                os_prod_list.append(list_row[1])
            elif 'Название ОС' in new_row:
                list_row = new_row.split(':')
                os_name_list.append(list_row[1])
            elif 'Код продукта' in new_row:
                list_row = new_row.split(':')
                os_code_list.append(list_row[1])
            elif 'Тип системы' in new_row:
                list_row = new_row.split(':')
                os_type_list.append(list_row[1])

get_data('info_1.txt')
get_data('info_2.txt')
get_data('info_3.txt')

# print(list(main_data.keys()))


def write_to_csv(file_csv, data):
    with open(file_csv, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.DictWriter(f_n, fieldnames=list(data[0].keys()))
        f_n_writer.writeheader()
        for d in data:
            f_n_writer.writerow(d)

write_to_csv('file_1.csv', main_data)

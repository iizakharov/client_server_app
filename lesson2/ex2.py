# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров
# — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений
# каждого параметра.

import json


def write_order_to_json():
    it = str(input('Введите название товара: '))
    qua = input('Введите количество товара: ')
    pr = input('Введите цену товара: ')
    bu = input('Введите имя покупателя: ')
    da = input('Введите дату покупки: ')

    dict_1 = {
        "item": it,
        "quantity": qua,
        "price": pr,
        "buyer": bu,
        "date": da,
    }

    dict_new = {"orders": dict_1}

    return dict_new


dict_to_json = write_order_to_json()


with open('orders.json', 'w', encoding='utf-8') as f_n:
    json.dump(dict_to_json, f_n, sort_keys=True, indent=4)

with open('orders.json', encoding='utf-8') as f_n:
    print(f_n.read())




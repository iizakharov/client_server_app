from config.dict import *
import json


# Утилита приёма и декодирования сообщения
# принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):  # являются ли полученые 2048 байт информации Байтами
        json_response = encoded_response.decode(ENCODING)  # Перевод в UTF-8
        response = json.loads(json_response)  # принимает строку байтов UTF-8 и переводит в json объект
        if isinstance(response, dict):  # являются ли полученый json объектом
            return response
        else:
            raise ValueError
    else:
        raise ValueError


# Утилита кодирования и отправки сообщения
# принимает словарь и отправляет его
def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)

import argparse
import sys
import json
import socket
import time
import logging
import log.client_log_config
from config.utils import *
from config.dict import *
from errors import ReqFieldMissingError
from decos import log


# Инициализация клиентского логера
client_logger = logging.getLogger('client')


# запрос о подключении клиента
@log
def create_presence(account_name='User'):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    client_logger.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return out


# Функция разбирает ответ сервера
@log
def process_answer(message):
    client_logger.debug(f'Разбор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        elif message[RESPONSE] == 400:
            return f'400 : {message[ERROR]}'
    raise ReqFieldMissingError(RESPONSE)


# Создаём парсер аргументов коммандной строки
@log
def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    # parser.add_argument('port', default=1022, type=int, nargs='?')
    return parser


def main():
    # Загружаем параметы коммандной строки
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port

    # проверим подходящий номер порта
    if not 1023 < server_port < 65536:
        client_logger.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}. '
            f'Допустимы адреса с 1024 до 65535. Клиент завершается.')
        exit(1)

    client_logger.info(f'Запущен клиент с парамертами: адрес сервера: {server_address} , порт: {server_port}')

    # Инициализация сокета и обмен
    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
        answer = process_answer(get_message(transport))
        client_logger.info(f'Принят ответ от сервера {answer}')
        print(answer)
    except json.JSONDecodeError:
        client_logger.error('Не удалось декодировать полученную Json строку.')
    except ReqFieldMissingError as missing_error:
        client_logger.error(f'В ответе сервера отсутствует необходимое поле {missing_error.missing_field}')
    except ConnectionRefusedError:
        client_logger.critical(
            f'Не удалось подключиться к серверу {server_address}:{server_port}, '
            f'конечный компьютер отверг запрос на подключение.')


if __name__ == '__main__':
    main()

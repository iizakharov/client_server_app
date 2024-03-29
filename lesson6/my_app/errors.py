# Исключение  - некорректные данные получены от сокета
class IncorrectDataRecivedError(Exception):
    def __str__(self):
        return 'Принято некорректное сообщение от удалённого компьютера.'


# исключение - аргумент функции не словарь.
class NonDictInputError(Exception):
    def __str__(self):
        return 'Аргумент функции должен быть словарём.'


# Ошибка - отсутствует обязательное поле в принятом словаре.
class ReqFieldMissingError(Exception):
    def __init__(self, missing_field):
        self.missing_field = missing_field

    def __str__(self):
        return f'В принятом словаре отсутствует обязательное поле {self.missing_field}.'

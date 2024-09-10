class Car:
    @classmethod
    def __is_valid_vin(cls, vin_number):
        if isinstance(vin_number, int):
            if vin_number in range (1000000, 10000000):
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    @classmethod
    def __is_valid_numbers(cls, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

    def __init__(self, model, vin, numbers):
        self.model = model
        if Car.__is_valid_vin(vin):
            self.__vin = vin
            if Car.__is_valid_numbers(numbers):
                self.__numbers = numbers

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

try:   #Дополнительная проверка на тип данных для vip номеров
    fourth = Car('Model4', '500000', 'k234lt')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)

try: #Дополнительная проверка на тип данных для номеров
   fifth = Car('Model5', 5000000, 123456)
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
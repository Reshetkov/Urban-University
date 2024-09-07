def add_everything_up(a,b):
    try:
        return a + b
    except TypeError:
        return str(a)+str(b)
def devide_everthing(a,b):
    try:
        print(int(a)/int(b))
    except ValueError:
        print('Ошибка типа данных')
    except ZeroDivisionError:
        print('Деление на ноль')
    try:
        print(int(a) / int(c))
    except NameError:
        print('Ошибка обращения')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
devide_everthing(10,5)
devide_everthing(10, 'Hello')
devide_everthing(10, 0)
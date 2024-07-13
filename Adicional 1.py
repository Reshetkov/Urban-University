number = float(input('Введите число: '))
condition = True
while condition:
    if number > 100:
        print('Отлично!')
        condition = False
    else:
        number = float(input('Введите число: '))

first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')
if first == second and first == third:
    print('3')
elif first != second and first != third and second != third:
    print('0')
else:
    print('2')
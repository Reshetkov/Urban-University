def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) < 2:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))

n = int(input('Введите число: '))
result = get_multiplied_digits(n)
print(result)
#fake_math.py

def divide(first, second):
    global quotient
    if second != 0:
        quotient = first / second
        return quotient
    else:
        return 'Ошибка'
#fake_math.py
quotient = 0

def divide(first, second):
    global quotient
    if second != 0:
        quotient = first / second
        return quotient
    else:
        return 'Ошибка'
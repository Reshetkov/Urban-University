#true_math.py
from math import inf

def divide(first, second):
    global quotient
    if second != 0:
        quotient = first / second
        return quotient
    else:
        return inf
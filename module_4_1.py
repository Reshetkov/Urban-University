#module_4_1.py
from fake_math import divide as divide_falso
from true_math import divide as divide_verdadero
resultado_1 = divide_falso(10, 2)
resultado_2 = divide_falso(10, 0)
resultado_3 = divide_verdadero(15, 5)
resultado_4 = divide_verdadero(10, 0)
print(resultado_1)
print(resultado_2)
print(resultado_3)
print(resultado_4)
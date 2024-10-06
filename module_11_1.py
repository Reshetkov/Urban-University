import numpy as np
# Работа с векторами, матрицами, системами линейных уравнений

a = np.array([3,4,5,1])
b = np.array([8,1,2,3])

print(a[0])

matrix_1 = a.reshape(2,2)       # Две матрицы 2х2
matrix_2 = b.reshape(2,2)

matrix_product = np.matmul(matrix_1, matrix_2)          # Произведение матриц
print(matrix_product)

c = np.array([1,2,3])       # Два вектора
d = np.array([4,5,6])

summa = c + d               # Сложение векторов
print(summa)

product = 2 * c             # Умножение вектора на число
print(product)

dot_product_1 = np.dot(c, d)    # Три способа найти скалярное произведение векторов
print(dot_product_1)

dot_product_2 = np.inner(c, d)
print(dot_product_2)

dot_product_3 = c @ d
print(dot_product_3)

magnitude = np.linalg.norm(c)          # Модуль вектора
print(magnitude)

unit_vector = c / magnitude             # Единичный вектор
print(unit_vector)

cross_product = np.cross(c, d)     #Векторное произведение векторов
print(cross_product)

matrix_3 = np.array([[5,3,-2], [3,2,-3], [4,2,-1]])   # Решение системы линейных уравнений
matrix_4 = np.array([2,0,1])
solution_1 = np.linalg.solve(matrix_3, matrix_4)
print(solution_1)

print(np.linalg.matrix_rank(matrix_3))          # Ранг матрицы
inverse_matrix = np.linalg.inv(matrix_3)        # Обратная матрица
print(inverse_matrix)

unit_matrix = np.matmul(matrix_3, inverse_matrix)  # Умножение матрицы на обратную матрицу
print(unit_matrix)

solution_2 = np.matmul(inverse_matrix, matrix_4)        # Решение системы линейных уравнений (2-ой способ)
print(solution_2)

determinant = np.linalg.det(matrix_3)               # Определитель матрицы
print(determinant)
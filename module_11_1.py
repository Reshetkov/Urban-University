import numpy as np
# Работа с векторами, матрицами, системами линейных уравнений

a = np.array([3,4,5,1])
b = np.array([8,1,2,3])

print(a[0])

matrix_1 = a.reshape(2,2)       #Две матрицы 2х2
matrix_2 = b.reshape(2,2)

matrix_product = np.matmul(matrix_1, matrix_2)
print(matrix_product)

c = np.array([1,2,3])       #Два вектора
d = np.array([4,5,6])

dot_product_1 = np.dot(c, d)    #Три способа найти скалярное произведение векторов
print(dot_product_1)

dot_product_2 = np.inner(c, d)
print(dot_product_2)

dot_product_3 = c @ d
print(dot_product_3)


cross_product = np.cross(c, d)     #Векторное произведение векторов
print(cross_product)
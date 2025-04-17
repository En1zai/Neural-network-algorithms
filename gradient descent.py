from numpy import arange
from numpy import asarray
from numpy.random import rand
import numpy as np
import matplotlib.pyplot as plt

#Функция y=x^2
def f(x):
    return x**2
#Функция для вычисления производной
def derivative(x):
    return 2.0*x

array = np.array([[-10, 10]]) # Границы весов функции

#Массивы с множеством значений для X и Y для последующей визуализации
x_arr = []
y_arr = []
for i in range(2000):
    x = array[:, 0] + rand(len(array)) * (array[:, 1] - array[:, 0])
    y = f(x)
    x_arr.append(x)
    y_arr.append(y)

#Выбираем случайный вес функции
x = array[:, 0] + rand(len(array)) * (array[:, 1] - array[:, 0])

#Массивы для визуализации работы алгоритма
s = []
d = []

for i in range(30):
    s.append(x) # Текущей вес
    y_s = f(x)
    d.append(y_s) # Текущая ошибка

    gradient = derivative(x)
    new_x = x - 0.1*gradient # Вычисление нового веса
    x = new_x
    print(i+1, x, y_s) # Вывод текущего шага, веса и ошибки

#Визуализация работы алгоритма
plt.scatter(x_arr, y_arr)
plt.scatter(s, d, color="red")
plt.xlabel("ВЕС", fontsize = 15)
plt.ylabel("ОШИБКА", fontsize =  15)
plt.show()
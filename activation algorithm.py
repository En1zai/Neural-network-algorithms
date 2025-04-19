import numpy as np

#Функция Rectified Linear Unit
def RELU(x):
    return max(x, 0)

#Функция Сигмоиды
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Фунция Гиперболического тангенса
def hyp_tan(x):
    return np.tanh(x)

x = -5
print(RELU(x))

arr = np.array([-5, 1, 5])
print(sigmoid(arr))
print(hyp_tan(arr))
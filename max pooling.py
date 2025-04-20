import numpy as np


def max_pooling(array, window_size=2, stride=2):
    """
    Параметры:
    input_data - передаваемый 2D-массив
    window_size - размер окна (2х2)
    stride - размер шага окна (2)
    """

    # Вычисляем размеры выходного изображения и создаем пустой массив для результата
    h = (array.shape[0] - window_size) // stride + 1
    w = (array.shape[1] - window_size) // stride + 1
    output = np.zeros((h, w), dtype=int)

    # Используем Max_Pooling
    for i in range(h):
        for j in range(w):
            # Выделяем текущее окно
            window = array[
                     i * stride: i * stride + window_size,
                     j * stride: j * stride + window_size
                     ]
            # Получаем максимум в текущем окне и записываем в массив
            output[i, j] = np.max(window)

    return output


# Черно-белое изображение, каждое число массива - интенсивность пикселя
image_pixel = np.array([
    [1, 2, 3, 5],
    [5, 6, 7, 5],
    [9, 10, 11, 4],
    [13, 14, 15, 2]
])

#Вывод результата алгоритма
output_image = max_pooling(image_pixel)
print("Изначальные данные:\n", image_pixel)
print("Результат работы:\n", output_image)

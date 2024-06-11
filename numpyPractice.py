import numpy as np

#https://pythonist.ru/python-numpy-tutorial/

#Создание массива
arr = np.array([1, 2, 3, 4, 5])
arr = np.array((1, 2, 3, 4, 5))

#numpy.empty() создает неинициализированный массив заданной формы и dtype
arr = np.empty([3, 2], dtype=int)

#numpy.zeros возвращает новый массив заполненный нулями
arr = np.zeros(5)
arr = np.ones(5)

#Нульмерный массив
arr = np.array(36)

#Массив, элементами которого являются нульмерные массивы,
#является одномерным или 1-D массивом
arr = np.array([1, 2, 3, 4, 5])

#Двумерный массив
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

#Трехмерный массив из двух двухмерных
arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#Использование ndarray.ndim
ndim = arr1.ndim

#Объекты типа данных dtype
dt = np.dtype(np.int32)
dt = np.dtype('i4')
dt = np.dtype('>i4')

#Структурированные типы данных
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)

#Использование ndarray.shape
a = np.array([[1, 2, 3], [4, 5, 6]])
sh = a.shape

a.shape = (3, 2)

#Использование ndarray.itemsize
#возвращает длину каждого элемента массива в байтах
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
size = x.itemsize

#Объект ndarray имеет флаги numpy.flags
x = np.array([1, 2, 3, 4, 5])
flags = x.flags

#Срезы (представляют view данных)
a = np.arange(10)
s = slice(2, 7, 2)
slice_res = a[s]
b = a[2:7:2]
b = a[5]
b = a[2:]
b = a[2:5]

#Расширенное целочисленное индексирование
#индекс строки содержит все номера строк,
#а индекс столбца указывает на элемент,
#который нужно выбрать
#Расширенная индексация приводит к созданию копии
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]

#Булевая расширенная индексация
x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9, 10, 11]])
new_x = x[x > 5]

#Использование broadcasting в numpy
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b

#Итерация по массивам c помощью nditer
array = np.arange(12).reshape(3, 4)

#for element in np.nditer(array):
    #print(element, end=' ')

#Изменение формы массива
array = np.arange(12).reshape(3, 4)

#for element in array.flat:
    #print(element, end=' ')

array_flatten = array.flatten() #делает копию
array_ravel = array.ravel() #делает view

#Операции транспонирования
array = np.arange(12).reshape(3, 4)
array_transposed = array.transpose()
array_transposed = array.T
array_transposed = np.rollaxis(array, 1) #крутить матрицу по оси

array_swappedaxes = np.swapaxes(array, 0, 1)

#Изменение размеров
array = np.arange(3)
array_reshaped = np.broadcast_to(array, (3, 3)) #копирует строки
array_expanded = np.expand_dims(array, axis=0)
array_start = np.squeeze(array_expanded)



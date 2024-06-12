import matplotlib.pyplot as plt
import numpy as np

#Использование plot
plt.plot([1, 2, -6, 0, 4]) #y - указанные значения, x - индексы элементов
plt.show()

x = np.array([1, 3, 7, 9])
y = np.array([2, 5, 9, 3])
plt.plot(x, y)
plt.grid()
plt.show()

#Рисование нескольких графиков
x1 = [1, 2, 3, 4, 5]
y1 = [i + 1 for i in x1]

x2 = [i + 2 for i in x1]
y2 = [i * i for i in x2]

x3 = [i + 3 for i in x1]
y3 = [i - 4 for i in x2]

plt.plot(x1, y1, 'o-', x2, y2, markerfacecolor='g')
plt.plot(x3, y3, '--r')
plt.grid()
plt.show()

#Изменение свойств линий
x = np.array([1, 3, 7, 9])
y = np.array([2, 5, 9, 3])
lines = plt.plot(x, y)
plt.setp(lines, linestyle='-.', linewidth=4)
plt.grid()
plt.show()

#Функция fill_between
plt.plot(x, y)
plt.fill_between(x, y, 0.5, color='r', where=(y > 0))
plt.grid()
plt.show()
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import (NullLocator, LinearLocator, MultipleLocator, IndexLocator,
                               FixedLocator, LogLocator, MaxNLocator)

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

#Функция subplot
ax1 = plt.subplot(1, 3, 1)
plt.plot(np.random.random(10))
ax2 = plt.subplot(1, 3, 2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(1, 3, 3)
plt.plot(np.random.random(10))
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()

ax1 = plt.subplot(2, 3, 1)
plt.plot(np.random.random(10))
ax2 = plt.subplot(2, 3, 2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(2, 3, 3)
plt.plot(np.random.random(10))
ax4 = plt.subplot(2, 1, 2)
plt.plot(np.random.random(10))
ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
plt.show()

#Разделяем секцию на графике каждый раз по новой
ax1 = plt.subplot(2, 3, 1)
plt.plot(np.random.random(10))
ax2 = plt.subplot(2, 3, 2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(2, 3, (4, 5))
plt.plot(np.random.random(10))
ax4 = plt.subplot(1, 3, 3)
plt.plot(np.random.random(10))
ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
plt.show()

#Функция subplots
f, ax = plt.subplots(2, 2)

f.set_size_inches(7, 4)
f.set_facecolor('#eee')

ax[0, 0].plot(np.arange(0, 5, 0.2))
ax[0, 0].grid()
ax[0, 1].plot(np.arange(5, 0, -0.2))
ax[0, 1].grid()
plt.show()

#Использование figure
fig = plt.figure(figsize=(7, 4))
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(np.arange(0, 5, 0.2))
plt.show()

#Использование GridSpec
ws = [1, 2, 5]
hs = [2, 0.5]

fig = plt.figure(figsize=(7, 4))
gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs)

ax1 = plt.subplot(gs[0, 0])
ax1.plot(np.arange(0, 5, 0.2))
ax2 = fig.add_subplot(gs[1, 0:2])
ax2.plot(np.random.random(10))
ax3 = fig.add_subplot(gs[:,2])
ax3.plot(np.random.random(10))

plt.show()

#Граничные значения
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))
ax.set(xlim=(-5, 30), ylim=(-1, 6))

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))
ax.set_xlim(xmin=-5, xmax=10)
ax.set_ylim(-1, 6)

plt.show()

#Управление метками
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

lc = NullLocator()

ax.grid()
ax.yaxis.set_major_locator(lc)

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

ax.grid()
ax.yaxis.set_major_locator(LinearLocator(5))

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

ax.grid()
ax.yaxis.set_major_locator(MultipleLocator(2))

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.grid()
ax.yaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57))

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

ax.grid()
ax.yaxis.set_major_locator(FixedLocator([1, 4, 9, 12]))

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

ax.grid()
ax.yaxis.set_major_locator(LogLocator(base=2))

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

ax.minorticks_on()
ax.grid(which='major', lw=2)
ax.grid(which='minor')

ax.yaxis.set_major_locator(MaxNLocator(3))

plt.show()

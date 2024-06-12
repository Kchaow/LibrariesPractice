import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (NullFormatter, FormatStrFormatter, FuncFormatter,
                               ScalarFormatter, FixedFormatter)

#Убрать метки осей
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)

ax.plot(x, np.sin(x))

ax.set_xticklabels([])
ax.set_yticklabels([])

ax.grid()
plt.show()

#Использование форматтеров
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)

ax.plot(x, np.sin(x))

ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())

ax.grid()
plt.show()

#Отображение в вещественных числах
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)

ax.plot(x, np.sin(x))

ax.xaxis.set_major_formatter(FormatStrFormatter("x = %.2f"))
ax.yaxis.set_major_formatter(FormatStrFormatter("y = %.2f"))

ax.grid()
plt.show()


def format_oy(x, pos):
    return f"[{x}]" if x < 0 else f"({x})"


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)

ax.plot(x, np.sin(x))

ax.xaxis.set_major_formatter(FuncFormatter(format_oy))
ax.yaxis.set_major_formatter(FuncFormatter(format_oy))

ax.grid()
plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)

ax.plot(x, np.sin(x) * 1e5)

sf = ScalarFormatter()
sf.set_powerlimits((-4, 4))
ax.yaxis.set_major_formatter(sf)

ax.grid()
plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)

ax.plot(x, np.sin(x) * 1e5)

ax.yaxis.set_major_formatter(FixedFormatter(['a', 'b', 'c', 'd', 'e', 'f', 'g']))

ax.grid()
plt.show()

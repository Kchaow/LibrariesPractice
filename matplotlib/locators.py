import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import (NullLocator, LinearLocator, MultipleLocator, IndexLocator,
                               FixedLocator, LogLocator, MaxNLocator)

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
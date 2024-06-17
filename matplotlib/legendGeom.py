import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import *

#Легенда
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(0, 5, 0.25), label='line 1')
ax.plot(np.arange(0, 10, 0.5), label='line 2')
ax.legend(['1', '2'])
plt.show()

#Ломаная
l1 = Line2D([1, 2, 3], [1, 2, 4])

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(0, 5, 0.25), label='line 1')
ax.plot(np.arange(0, 10, 0.5), label='line 2')
ax.legend(['1', '2'])
ax.add_line(l1)
plt.show()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
cos = Line2D(x, np.cos(x))
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.add_line(cos)
ax.set(xlim=(-2*np.pi, 2*np.pi), ylim=(-1, 1))
plt.show()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
cos = Line2D(x, np.cos(x))
rect = Rectangle((0, 0), 2.5, 0.5, facecolor='g')
cos = Line2D(x, np.cos(x))
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.add_line(cos)
ax.add_patch(rect)
ax.set(xlim=(-2*np.pi, 2*np.pi), ylim=(-1, 1))
plt.show()

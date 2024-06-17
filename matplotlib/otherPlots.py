import numpy as np
import matplotlib.pyplot as plt

#Step
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(0, 10)
ax.step(x, x, '-go')
ax.grid()

plt.show()

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(0, 10)
ax.step(x, x, '-go', where='post')
ax.grid()

plt.show()

#Stack
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(-2, 2, 0.1)
y1 = np.array([-y**2 for y in x]) + 8
y2 = np.array([-y**2 for y in x]) + 8
y3 = np.array([-y**2 for y in x]) + 8
ax.stackplot(x, y1, y2, y3)

ax.grid()

plt.show()

#Stem
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi, np.pi, 0.3)
ax.stem(x, np.cos(x), '--r', bottom=0.5)
ax.grid()
plt.show()

#Scatter
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)

ax.scatter(x, y)
ax.grid()
plt.show()

#Hist
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

y = np.random.normal(0, 2, 500)
ax.hist(y, 50)
ax.grid()
plt.show()

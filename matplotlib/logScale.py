import matplotlib.pyplot as plt
import numpy as np

#Использование semilog
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi, 10*np.pi, 0.5)
ax.semilogy(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax.grid()

plt.show()

#Использование set_scale
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi, 10*np.pi, 0.5)
ax.plot(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax.set_yscale('log', base=2)
ax.grid()

plt.show()

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi, 10*np.pi, 0.5)
ax.plot(x, np.sinc(x) * np.exp(-np.abs(x/10)))
ax.set_yscale('symlog', base=2, linthresh=2)
ax.grid()

plt.show()

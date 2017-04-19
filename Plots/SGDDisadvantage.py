import matplotlib.pyplot as plot
import numpy as np


def func(x, y):
    return x ** 2 / 20 + y ** 2


fig = plot.figure()
ax = fig.add_subplot(111, projection="3d")
x = np.arange(-5.0, 5.0, 0.1)
y = np.arange(-5.0, 5.0, 0.1)

ax.plot_wireframe(x, y, func(x, y), rstride=10, cstride=10)
plot.show()

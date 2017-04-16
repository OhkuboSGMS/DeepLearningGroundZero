import os
import sys

sys.path.append(os.pardir)
import Differentiation as df
import numpy as np
import matplotlib.pylab as plt


def function_l(x):
    return 0.01 * x ** 2 + 0.1 * x


def function_2(x):
    return x[0] ** 2 + x[1] ** 2


def plot_f1():
    x = np.arange(0.0, 20.0, 0.1)
    y = function_l(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)
    # plt.plot(x,df.numerical_diff(function_l,x))
    print(df.numerical_diff(function_l, 5))
    print(df.numerical_diff(function_l, 10))
    plt.show()


def plot_f2():
    x1 = x2 = np.arange(0.0, 20.0, 0.1)
    xx = np.array([x1, x2])
    print(xx)
    y = function_2(xx)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(xx, y)
    # plt.plot(x,df.numerical_diff(function_l,x))
    plt.show()


plot_f2()

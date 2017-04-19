import os
import sys

sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from TwoLayerNet import TwoLayersNet

# データの読み込み
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

network = TwoLayersNet(input_size=784, hidden_size=50, output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

print(x_batch)
grad_numerical = network.numerical_gradient(x_batch, t_batch)
grad_backprop = network.gradient(x_batch, t_batch)
import numpy as np

# 各重みの絶対誤差の平均を求める
for key in grad_numerical.keys():
    diff = np.average(np.abs(grad_backprop[key] - grad_numerical[key]))
    print(key + ":" + str(diff))

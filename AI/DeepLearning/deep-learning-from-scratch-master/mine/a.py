import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import numpy as np
from PIL import Image


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

def show(img):
    img = Image.fromarray(np.uint8(img))
    img.show()

img = x_train[0]
label = t_train[0]
print(label)
print(img.shape)
img = img.reshape(28,28)
print(img.shape)

show(img)

"""
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
"""
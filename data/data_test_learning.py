import numpy as np

class BaseTransform:
    def __init__(self, size, mean):
        self.size = size
        self.mean = np.array(mean, dtype=np.float32)
        print(size, mean)

    def __call__(self, image, boxes=None, labels=None):
        print(image, boxes, labels)

if __name__ == '__main__':
    dataset = BaseTransform(1, [[2, 3, 2]])

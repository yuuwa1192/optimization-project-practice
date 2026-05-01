import numpy as np

def objective(x, y):
    valley1 = -3.0 * np.exp(-((x - 2) ** 2 + (y + 3) ** 2) / 2.0)
    valley2 = -2.5 * np.exp(-((x + 3) ** 2 + (y - 1) ** 2) / 1.5)

    base = 0.05 * (x ** 2 + y ** 2)

    return base + valley1 + valley2
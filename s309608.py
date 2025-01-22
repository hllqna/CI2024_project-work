import numpy as np

def f1(x: np.ndarray) -> np.ndarray:
    # MSE: 7.12594e-34
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    # MSE: 1.7784e+13
    return np.multiply(3108956.2730975375, np.arctan(x[0]))

def f3(x: np.ndarray) -> np.ndarray:
    # MSE: 172.397
    return np.subtract(np.cosh(x[0]), np.multiply(x[1], np.square(x[1])))

def f4(x: np.ndarray) -> np.ndarray:
    # MSE: 0.659456
    return np.multiply(np.cos(np.add(5, np.cos(x[1]))), np.add(np.add(np.add( \
        np.add(np.add(6, np.cos(6)), np.cos(x[1])), np.cos(x[1])), np.cos(x[1])), np.cos(np.cos(6))))

def f5(x: np.ndarray) -> np.ndarray:
    # MSE: 5.57281e-18
    return 0

def f6(x: np.ndarray) -> np.ndarray:
    # MSE: 1.59972
    return np.subtract(x[1], np.subtract(x[0], x[1]))

def f7(x: np.ndarray) -> np.ndarray:
    # MSE: 348.783
    return np.power(np.power(np.log(84.83571317218195), x[0]), x[1])

def f8(x: np.ndarray) -> np.ndarray:
    # MSE: 734176.046
    return np.multiply(np.subtract(x[5], np.sinh(x[5])), np.subtract(x[5], 224.6429079932195))
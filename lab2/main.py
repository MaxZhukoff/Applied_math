import math
import numpy as np
from sympy import diff, symbols, false

x, y = symbols('x y')
variables = (x, y)
f = lambda variables: 3 / 2 * (x - y) ** 2 + 1 / 3 * (x + y) ** 2 + 1


def value(values):
    if len(values) != len(variables) or len(values) < 1:
        return false
    funcValue = f(values)
    replacements = []
    for i in range(len(values)):
        replacements += [(variables[i], values[i])]
    return funcValue.subs(replacements)


def differentiation(var, point):
    if len(point) != len(variables) or len(point) < 1:
        return false
    dv = diff(f(variables), var)
    replacements = []
    for i in range(len(point)):
        replacements += [(variables[i], point[i])]
    return dv.subs(replacements)


def gradient(point):
    size = int((len(point)))
    if len(point) != len(variables) or size < 1:
        return false
    grad = np.array([])
    for i in range(size):
        grad = np.append(grad, np.array([differentiation(variables[i], point)]))
    return grad


def gradientDescent(xPrev):
    xNew = np.array([])
    e = 0.01
    a = 0.1
    it = 0
    while True:
        it += 1
        xNew = xPrev - a * gradient(xPrev)
        # if math.fabs(value(xNew) - value(xPrev)) <= e or all(np.absolute(xNew - xPrev) <= e):
        if all(np.absolute(xNew - xPrev) <= e):
            break
        xPrev = xNew
    print(value(xNew), it)


# point1 = np.array([2, 3])
# print(gradient(point1))
# val = np.array([2, 3])
# print(value(val))

x0 = np.array([1.7, 2.5])
gradientDescent(x0)

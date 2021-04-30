import math
import numpy as np
from one_dimensional_methods import *
from sympy import diff, symbols, false
import random

variables = symbols('x y')
f = lambda variables: 3 / 2 * (variables[0] - variables[1]) ** 2 + 1 / 3 * (variables[0] + variables[1]) ** 2 + 1


def init():
    x0 = np.array([], dtype=int)
    for i in range(0, len(variables)):
        x0 = np.append(x0, [random.randint(-3, 3)])
    return x0


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


def length_grad(grad):
    length = 0
    for i in range(len(x0)):
        length += grad[i] ** 2
    return length


def gradientDescent(xPrev):
    xNew = np.array([])
    epsilon = 0.01
    alpha = 0.1
    it = 0
    while True:
        it += 1
        xNew = xPrev - alpha * gradient(xPrev)
        # alpha /= 1.5
        # if math.fabs(value(xNew) - value(xPrev)) <= e or all(np.absolute(xNew - xPrev) <= e):
        if math.fabs(value(xNew) - value(xPrev)) <= epsilon:
            break
        xPrev = xNew
    print(value(xNew), it)


def next_step(curr_x, alpha):
    return curr_x - alpha * gradient(curr_x)


def steepest_descent(point, epsilon):
    curr_x = point
    it = 0
    while True:
        it += 1
        alpha = golden_ratio_method(lambda alp: f(next_step(curr_x, alp)), -1, 1, 0.001)
        next_x = next_step(curr_x, alpha)
        if (math.sqrt(np.absolute(length_grad(next_x) - length_grad(curr_x)))) <= epsilon:
            break
        curr_x = next_x
    return next_x, f(next_x)




x0 = init()
gradientDescent(x0)
print(steepest_descent(x0, 0.001))

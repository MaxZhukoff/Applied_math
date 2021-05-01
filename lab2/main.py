import math
import numpy as np
from one_dimensional_methods import *
from sympy import diff, symbols, false
import random

variables = symbols('x y')
f = lambda variables: 3 / 2 * (variables[0] - variables[1]) ** 2 + 1 / 3 * (variables[0] + variables[1]) ** 2 + 1
epsilon = 0.01

def init():
    x0 = np.array([], dtype=int)
    for i in range(0, len(variables)):
        x0 = np.append(x0, [random.randint(-30, 30)])
    return x0


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


def gradientDescent(curr_x):
    alpha = 0.1
    it = 0
    while True:
        it += 1
        next_x = curr_x - alpha * gradient(curr_x)
        # if math.fabs(value(next_x) - value(curr_x)) <= e or all(np.absolute(next_x - curr_x) <= e):
        if math.fabs(f(next_x) - f(curr_x)) <= epsilon:
            break
        curr_x = next_x
    return f(next_x), it


def step_split_gradient_descent(curr_x):
    alpha = 1
    delta = 0.5
    it = 0
    while True:
        it += 1
        next_x = curr_x - alpha * gradient(curr_x)
        if f(curr_x - alpha * gradient(curr_x)) <= f(curr_x) - epsilon * alpha * math.fabs(length_grad(curr_x)):
            if math.fabs(f(next_x) - f(curr_x)) <= epsilon:
                break
            curr_x = next_x
        else:
            while f(curr_x - alpha * gradient(curr_x)) > f(curr_x):
                alpha *= delta
    return f(next_x), it


def next_step(curr_x, alpha):
    return curr_x - alpha * gradient(curr_x)


def steepest_descent(point):
    curr_x = point
    it = 0
    while True:
        it += 1
        alpha = golden_ratio_method(lambda alp: f(next_step(curr_x, alp)), -1, 1, 0.001)
        next_x = next_step(curr_x, alpha)
        if (math.sqrt(np.absolute(length_grad(next_x) - length_grad(curr_x)))) <= epsilon:
            break
        curr_x = next_x
    return f(next_x), it


point1 = np.array([2, 3])
x0 = init()
print(x0)
print("Gradient descent:", gradientDescent(x0))
print("Steepest descent:", steepest_descent(x0))
print(step_split_gradient_descent(x0))

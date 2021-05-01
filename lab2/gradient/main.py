import math
import numpy as np
from one_dimensional_methods import *
from sympy import *
import random

variables = symbols('x y')
f = lambda variables: 3 / 2 * (variables[0] - variables[1]) ** 2 + 1 / 3 * (variables[0] + variables[1]) ** 2 + 1
# f = lambda variables: 4*(variables[0] - 5) ** 2 + (variables[1] - 6) ** 2
epsilon = 0.1

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

def conjugent_gradient(point):
    it = 0
    k = 0
    beta = 0
    curr_x = point
    p = -1 * gradient(curr_x)
    while True:
        it += 1
        if k == 0:
            p = -1 * gradient(curr_x)
        alpha = golden_ratio_method(lambda alp: f(next_step(curr_x, alp)), -1, 1, 0.001)
        next_x = curr_x + alpha * p
        # print(np.absolute(gradient(next_x)))
        if math.sqrt(np.absolute(length_grad(gradient(next_x)))) < epsilon:
            return next_x, f(next_x), it
        elif k + 1 == len(point):
            k = 0
            curr_x = next_x
            continue
        else:
            beta = (math.sqrt(np.absolute(length_grad(gradient(next_x)))) ** 2) / (math.sqrt(np.absolute(length_grad(gradient(curr_x)))) ** 2)
            p = -1 * gradient(next_x) + beta * p
        k += 1

def conjugent_directions(point):
    it = 0
    curr_x = point
    p = np.zeros((len(point), len(point)))

    for i in range(len(point)):
        for j in range(len(point)):
            if i == j:
                p[i][j] = 1

    # while math.sqrt(np.absolute(length_grad(gradient(curr_x)))) > epsilon:
    it += 1
    # h = symbols('h')
    # funct1 = f([point[0] + h * p[1][0], point[1] + h * p[1][1]])
    # print(f([point[0] + h * p[1][0], point[1] + h * p[1][1]]))
    # funct1 = lambda f: eval(f([point[0] + h * p[1][0], point[1] + h * p[1][1]]))
    # print(funct1(f([1, 1])))
    # print(type(f([point[0] + h * p[1][0], point[1] + h * p[1][1]])))
    # min1 = golden_ratio_method(f([h, h]), -1, 1, 0.001)
    # print(min1)
    # x1 = np.array([point[0] + min1 * p[1][0], point[1] + min1 * p[1][1]])

    # funct2 = f([x1[0] + h * p[0][0], x1[1] + h * p[0][1], -1, 1, 0.001])
    # x2 = np.array([x1[0] + min2 * p[0][0], x1[1] + m1])
    # min2 = golden_ratio_method(lambda funct2: funct2 * p[0][1], -1, 1, 0.001)

    # funct3 = f([x2[0] + h * p[1][0], x2[1] + h * p[1][1]])
    # min3 = golden_ratio_method(lambda funct3: funct3, -1, 1, 0.001)
    # x3 = np.array([point[0] + min3 * p[1][0], point[1] + min3 * p[1][1]])
    
    # print(funct1, funct2, funct3)

    # p[1] = x3 - x1
    
    # print(min1, min2, min3)
    # print(x3, x2, x1)

point1 = np.array([2, 3])
x0 = init()
# x0 = [8, 9]
print(x0)
print("Gradient descent first:", gradientDescent(x0))
print("Steepest descent:", steepest_descent(x0))
print("Gradient descent second: ", step_split_gradient_descent(x0))
print("Conjugent gradient method: ", conjugent_gradient(x0))
# print("Conjugent directions method: ", conjugent_directions(x0))
# print("Newton method:", newton_method(x0))
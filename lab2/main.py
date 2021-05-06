import numpy as np
from one_dimensional_methods import *
from sympy import diff, symbols, false, nsolve, sin, cos
import random

variables = symbols('x y')

f = lambda variables: variables[0] ** 2 / 5 + variables[1] ** 2 / 5 - sin(variables[0]) + sin(variables[1])
# variables[0] ** 2 / 5 + variables[1] ** 2 / 5 - sin(variables[0]) + sin(variables[1])
# 3 / 2 * (variables[0] - variables[1]) ** 2 + 1 / 3 * (variables[0] + variables[1]) ** 2 + 1
# 3/2*(x-y)^2 + 1/3*(x+y)^2+1
epsilon = 0.01


def init():
    x0 = np.array([], dtype=int)
    for i in range(0, len(variables)):
        x0 = np.append(x0, [random.randint(-10, 10)])
    return x0


def differentiation(var, point):
    if len(point) != len(variables) or len(point) < 1:
        return false
    dv = diff(f(variables), var)
    replacements = []
    for i in range(len(point)):
        replacements += [(variables[i], point[i])]
    return dv.subs(replacements).evalf()


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


def gradient_descent(curr_x):
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
            if math.fabs(f(next_x) - f(curr_x)) <= epsilon:
                break
    return f(next_x), it


def next_step(curr_x, alpha):
    return curr_x - alpha * gradient(curr_x)


def steepest_descent(point):
    curr_x = point
    it = 0
    while True:
        it += 1
        alpha = golden_ratio_method(lambda alp: f(next_step(curr_x, alp)), -1, 1, 0.1)
        next_x = next_step(curr_x, alpha)
        if (math.sqrt(np.absolute(length_grad(next_x) - length_grad(curr_x)))) <= epsilon:
            break
        curr_x = next_x
    return f(next_x), it


def conjugate_gradient(point):
    it = 0
    k = 0
    curr_x = point
    p = -1 * gradient(curr_x)
    while True:
        it += 1
        if k == 0:
            p = -1 * gradient(curr_x)
        alpha = golden_ratio_method(lambda alp: f(next_step(curr_x, alp)), -1, 1, 0.1)
        next_x = curr_x + alpha * p
        if math.sqrt(np.absolute(length_grad(gradient(next_x)))) < epsilon:
            return f(next_x), it
        elif k + 1 == len(point):
            k = 0
            curr_x = next_x
            continue
        else:
            beta = (math.sqrt(np.absolute(length_grad(gradient(next_x)))) ** 2) / (
                    math.sqrt(np.absolute(length_grad(gradient(curr_x)))) ** 2)
            p = -1 * gradient(next_x) + beta * p
        k += 1


def grad_to_matrix(grad):
    matrix_grad = np.zeros((len(grad), 1))
    for i in range(len(grad)):
        matrix_grad[i][0] = grad[i]
    return matrix_grad


def conjugate_directions(point):  # Powell's method
    p1 = np.array([1, 0])
    p2 = np.array([0, 1])
    x0 = point
    h = symbols('h')
    it = 0
    while True:
        it += 1
        x1 = x0 + h * p2
        hr = nsolve(diff(f(x1), h), 0)
        x1 = x0 + hr * p2
        x2 = x1 + h * p1
        hr = nsolve(diff(f(x2), h), 0)
        x2 = x1 + hr * p1
        x3 = x2 + h * p2
        hr = nsolve(diff(f(x3), h), 0)
        x3 = x2 + hr * p2
        p2 = x3 - x1
        x0 = x3
        if math.sqrt(np.absolute(length_grad(gradient(x3)))) < epsilon:
            return f(x3), it


def hessian(point):
    size = (len(variables))
    matrix = np.eye(size)
    for i in range(size):
        for j in range(size):
            dx1 = lambda variables: diff(f(variables), variables[i])
            dx2 = diff(dx1(variables), variables[j])
            dx2 = dx2.subs([(variables[0], point[0]), (variables[1], point[1])]).evalf()
            matrix[i][j] = dx2
    return matrix


def newton(point):
    curr_x = point
    it = 0
    while True:
        it += 1
        next_x = curr_x.reshape(-1, 1) - np.dot(np.linalg.inv(hessian(curr_x)), gradient(curr_x).reshape(-1, 1))
        vec_length = 0
        for i in range(len(next_x)):
            vec_length += next_x[i] ** 2
        if math.sqrt(vec_length) < epsilon:
            break
        temp = next_x
        next_x = np.array([])
        for i in range(len(temp)):
            next_x = np.append(next_x, temp[i])
        if math.fabs(f(next_x) - f(curr_x)) <= epsilon:
            break
        curr_x = next_x
    return f(next_x), it


# x0 = init()
x0 = np.array([-1, 0])
print(x0)
print("Gradient descent:", gradient_descent(x0))
print("Steepest descent:", steepest_descent(x0))
print("Gradient descent second: ", step_split_gradient_descent(x0))
print("Conjugate gradient method: ", conjugate_gradient(x0))
print("Conjugate directions method: ", conjugate_directions(x0))
print("Newton method: ", newton(x0))

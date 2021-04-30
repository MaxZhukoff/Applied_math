import sympy as sm
import numpy as np
import random

from one_dimensional_methods import *

variables = sm.symbols('x y')
f = lambda variables: 4 * variables[0] ** 2 + variables[1] ** 2 - variables[0] + 2 * variables[1]
a = -7
b = -4
epsilon = 0.1

def init(f):
    x = np.array([], dtype=int)

    for i in range(0, len(variables)):
        x = np.append(x, [random.randint(-3, 3)])
    return x

x = init(f)

def gradient(f):
    buf = np.array([])
    for i in range(len(variables)):
        dif = sm.diff(f(variables), variables[i])
        buf = np.append(buf, [dif])
    return buf

def grad_in_point(grad, x):
    buf = np.array([])
    for i in range(len(grad)):
        buf = np.append(buf, [grad[i].subs(variables[i], x[i])])
    return buf

def length_grad(grad):
    length = 0
    for i in range(len(x)):
        length += grad[i]**2
    return length
    






print(f(variables))
print(x)

# print(x * gradient(f))

grad = gradient(f)

print(grad)

print(grad_in_point(grad, x))

def next_step(x, alpha):
    return (x - alpha * grad_in_point(grad, x))

def steepest_descent(f, a, b, epsilon):
    curr_x = x
    grad = gradient(f)
    iter = 0
    next_x = np.array([])
    while True:
        iter += 1
        alpha = golden_ratio_method(lambda alp: f(next_step(curr_x, alp)), -1, 1, 0.001)
        # print(next_step(x, alpha))
        next_x = next_step(curr_x, alpha)
        if (math.sqrt(np.absolute(length_grad(next_x) - length_grad(curr_x)))) <= epsilon:
            print(next_x, iter)
            break
        print(next_x)
        curr_x = next_x
    return next_x , f(next_x)


print(steepest_descent(f, a, b, epsilon))




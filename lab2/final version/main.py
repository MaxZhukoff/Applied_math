import numpy as np
from one_dimensional_methods import *
from sympy import diff, symbols, false, nsolve, sin, cos
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

variables = symbols('x y')

epsilon = 0.1

f = lambda variables: variables[0] ** 2 / 2 + variables[1] ** 2 / 3

# epsilon = 0.01

# f = lambda variables: variables[0] ** 2 / 5 - sin(variables[0]) + variables[1] ** 2 / 5 + sin(variables[1])

png = 1


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


def plot_function():
    xlist = np.linspace(x0[0] - 1, x0[1] + 1, 1000)
    ylist = np.linspace(x0[0] - 1, x0[1] + 1, 1000)
    X, Y = np.meshgrid(xlist, ylist)
    # f = lambda variables: variables[0] ** 2 / 5 - np.sin(variables[0]) + variables[1] ** 2 / 5 + np.sin(variables[1])
    Z = f([X, Y])
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, Z, cmap='viridis', antialiased=False)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')
    plt.savefig('figure.png')
    plt.show()


def plot_moving(array_x, text):
    xlist = np.linspace(x0[0] - 1, x0[1] + 1, 1000)
    ylist = np.linspace(x0[0] - 1, x0[1] + 1, 1000)
    X, Y = np.meshgrid(xlist, ylist)
    # f = lambda variables: variables[0] ** 2 / 5 - np.sin(variables[0]) + variables[1] ** 2 / 5 + np.sin(variables[1])
    Z = f([X, Y])
    fig, ax = plt.subplots()
    cp = ax.contourf(X, Y, Z)
    title = "Сходимость " + text
    ax.set_title(title)
    # print("++++++++++++++++++++++++X1++++++++++++++++++++++++")
    # for i in range(len(array_x)):
    #     print(array_x[i][0])
    # print("++++++++++++++++++++++++X2++++++++++++++++++++++++")
    # for i in range(len(array_x)):
    #     print(array_x[i][1])
    for i in range(0, len(array_x) - 1):
        plt.plot([array_x[i][0], array_x[i + 1][0]], [array_x[i][1], array_x[i + 1][1]], 'o-', color="Red")
    global png
    name = f"{png}.png"
    plt.savefig(name)
    png += 1
    plt.show()


def gradient_descent_constant_step(point):
    curr_x = point
    alpha = 0.1
    it = 0
    array_x = np.empty((0, 2))
    while True:
        array_x = np.append(array_x, np.array([[curr_x[0], curr_x[1]]]), axis=0)
        it += 1
        next_x = curr_x - alpha * gradient(curr_x)
        if (math.sqrt(np.absolute(length_grad(next_x) - length_grad(curr_x)))) <= epsilon:
            array_x = np.append(array_x, np.array([[next_x[0], next_x[1]]]), axis=0)
            plot_moving(array_x, "метода градиентного спуска (постоянный шаг)")
            return f(next_x), it
        curr_x = next_x


def gradient_descent_step_splitting(curr_x):
    alpha = 0.2
    delta = 0.95
    it = 0
    array_x = np.empty((0, 2))
    while True:
        array_x = np.append(array_x, np.array([[curr_x[0], curr_x[1]]]), axis=0)
        it += 1
        next_x = curr_x - alpha * gradient(curr_x)
        if f(next_x) > f(curr_x) - epsilon * alpha * ((math.sqrt(np.absolute(length_grad(gradient(curr_x))))) ** 2):
            alpha *= delta
            continue
        if (math.sqrt(np.absolute(length_grad(next_x) - length_grad(curr_x)))) <= epsilon:
            array_x = np.append(array_x, np.array([[next_x[0], next_x[1]]]), axis=0)
            plot_moving(array_x, "градиентного спуска (дробление шага)")
            return f(next_x), it
        curr_x = next_x


def steepest_descent(point):
    curr_x = point
    it = 0
    array_x = np.empty((0, 2))
    while True:
        array_x = np.append(array_x, np.array([[curr_x[0], curr_x[1]]]), axis=0)
        it += 1
        alpha = fibonacci_method(lambda alpha_min: f(curr_x - alpha_min * gradient(curr_x)), -1, 1, 0.1)
        next_x = curr_x - alpha * gradient(curr_x)
        if (math.sqrt(np.absolute(length_grad(next_x) - length_grad(curr_x)))) <= epsilon:
            array_x = np.append(array_x, np.array([[next_x[0], next_x[1]]]), axis=0)
            plot_moving(array_x, "метода наискорейшего спуска")
            return f(next_x), it
        curr_x = next_x


def conjugate_gradient(point):
    it = 0
    k = 0
    curr_x = point
    p = gradient(curr_x)
    array_x = np.empty((0, 2))
    while True:
        array_x = np.append(array_x, np.array([[curr_x[0], curr_x[1]]]), axis=0)
        it += 1
        alpha = fibonacci_method(lambda alp: f(curr_x - alp * p), -1, 1, 0.1)
        next_x = curr_x - alpha * p
        if math.sqrt(np.absolute(length_grad(gradient(next_x)))) < epsilon:
            array_x = np.append(array_x, np.array([[next_x[0], next_x[1]]]), axis=0)
            plot_moving(array_x, "метода сопряженных градиентов")
            return f(next_x), it
        elif k + 1 == len(point):
            curr_x = next_x
            k = 0
            p = gradient(curr_x)
            continue
        else:
            beta = (sqrt(np.absolute(length_grad(gradient(next_x)))) ** 2) / (
                        sqrt(np.absolute(length_grad(gradient(curr_x)))) ** 2)
            curr_x = next_x
            p = gradient(next_x) + beta * p
            k += 1


def grad_to_matrix(grad):
    matrix_grad = np.zeros((len(grad), 1))
    for i in range(len(grad)):
        matrix_grad[i][0] = grad[i]
    return matrix_grad


def conjugate_directions(point):
    p1 = np.array([1, 0])
    p2 = np.array([0, 1])
    x0 = point
    h = symbols('h')
    it = 0
    array_x = np.empty((0, 2))
    while True:
        array_x = np.append(array_x, np.array([[x0[0], x0[1]]]), axis=0)
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
            array_x = np.append(array_x, np.array([[x0[0], x0[1]]]), axis=0)
            plot_moving(array_x, "метода сопряженных направлений")
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
    array_x = np.empty((0, 2))
    while True:
        array_x = np.append(array_x, np.array([[curr_x[0], curr_x[1]]]), axis=0)
        it += 1
        next_x = curr_x.reshape(-1, 1) - np.dot(np.linalg.inv(hessian(curr_x)), gradient(curr_x).reshape(-1, 1))
        vec_length = 0
        for i in range(len(next_x)):
            vec_length += next_x[i] ** 2
        if math.sqrt(vec_length) < epsilon:
            array_x = np.append(array_x, np.array([[float(next_x[0]), float(next_x[1])]]), axis=0)
            plot_moving(array_x, "метода Ньютона")
            return f(array_x[len(array_x) - 1]), it
        temp = next_x
        next_x = np.array([])
        for i in range(len(temp)):
            next_x = np.append(next_x, temp[i])
        if math.fabs(f(next_x) - f(curr_x)) <= epsilon:
            array_x = np.append(array_x, np.array([[float(next_x[0]), float(next_x[1])]]), axis=0)
            plot_moving(array_x, "метода Ньютона")
            return f(array_x[len(array_x) - 1]), it
        curr_x = next_x


# x0 = init()
x0 = np.array([-10, 10])
# x0 = np.array([-1, 1])
print(x0)
plot_function()
print("Constant step gradient descent method:", gradient_descent_constant_step(x0))
print("Gradient descent with step split method: ", gradient_descent_step_splitting(x0))
print("Steepest descent:", steepest_descent(x0))
print("Conjugate gradient method: ", conjugate_gradient(x0))
print("Conjugate directions method: ", conjugate_directions(x0))
print("Newton method: ", newton(x0))
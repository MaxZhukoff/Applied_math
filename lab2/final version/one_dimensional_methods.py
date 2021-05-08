import math
from sympy import *

def golden_ratio_method(function, a, b, epsilon):
    x1 = a + ((3 - math.sqrt(5)) / 2) * (b - a)
    x2 = a + ((math.sqrt(5) - 1) / 2) * (b - a)
    fx1 = function(x1)
    fx2 = function(x2)
    while (b - a) / 2 >= epsilon:
        if fx1 > fx2:
            a = x1
            x1 = x2
            x2 = a + ((math.sqrt(5) - 1) / 2) * (b - a)
            fx1 = fx2
            fx2 = function(x2)
        elif fx1 < fx2:
            b = x2
            x2 = x1
            x1 = a + ((3 - math.sqrt(5)) / 2) * (b - a)
            fx2 = fx1
            fx1 = function(x1)
    return (a + b) / 2


def fibonacci_default(number):
    return (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** number - ((1 - math.sqrt(5)) / 2) ** number)


def fibonacci_method(f, a, b, epsilon):
    iterations = 0
    while ((b - a) / epsilon) > fibonacci_default(iterations + 2):
        iterations += 1
    fibonacci_def_n = fibonacci_default(iterations)
    fibonacci_def_plus_n = fibonacci_default(iterations + 1)
    fibonacci_def_plus_2n = fibonacci_default(iterations + 2)
    k = 0
    x1 = a + (fibonacci_def_n / fibonacci_def_plus_2n) * (b - a)
    x2 = a + (fibonacci_def_plus_n / fibonacci_def_plus_2n) * (b - a)
    fx1 = f(x1)
    fx2 = f(x2)
    i = 0
    while (b - a) / 2 >= epsilon:
        i += 1
        k += 1
        if fx1 > fx2:
            a = x1
            x1 = x2
            x2 = a + (fibonacci_default(iterations - k + 2) / fibonacci_default(iterations - k + 3)) * (b - a)
            fx1 = fx2
            fx2 = f(x2)
        elif fx1 < fx2:
            b = x2
            x2 = x1
            x1 = a + (fibonacci_default(iterations - k + 1) / fibonacci_default(iterations - k + 3)) * (b - a)
            fx2 = fx1
            fx1 = f(x1)
    return (a + b) / 2
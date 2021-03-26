import math

func = lambda x: math.sin(x) * x ** 3

epsilon = 0.01


def dichotomy_method(a0, b0):
    iterations = math.log((b0 - a0) / epsilon) / math.log(2)
    delta = epsilon / 2 - 0.001
    while iterations >= 1:
        x = (a0 + b0) / 2
        x1 = x - delta
        x2 = x + delta
        if func(x1) > func(x2):
            a0 = x1
        else:
            b0 = x2
        iterations -= 1
    return a0, func(a0)


print(dichotomy_method(-7, -3))

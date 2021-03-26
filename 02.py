import math

func = lambda x: math.sin(x) * x ** 3

epsilon = 0.01


def golden_ratio_method(a0, b0):
    x1 = a0 + ((3 - math.sqrt(5)) / 2) * (b0 - a0)
    x2 = b0 - ((3 - math.sqrt(5)) / 2) * (b0 - a0)
    while ((b0 - a0) / 2) >= epsilon:
        if func(x1) > func(x2):
            a0 = x1
            x1 = x2
            x2 = b0 - (x1 - a0)
        elif func(x1) < func(x2):
            b0 = x2
            x2 = x1
            x1 = a0 + (b0 - x2)
    return (a0 + b0) / 2, func((a0 + b0) / 2)


print(golden_ratio_method(-7, -3))

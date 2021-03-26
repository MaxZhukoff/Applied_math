import math

func = lambda x: math.sin(x) * x ** 3

epsilon = 0.001


def dichotomy_method(a0, b0):
    iterations = math.log((b0 - a0) / epsilon) / math.log(2)
    delta = (epsilon / 2) - 0.0001
    while iterations >= 1:
        x = (a0 + b0) / 2
        x1 = x - delta
        x2 = x + delta
        if func(x1) > func(x2):
            a0 = x1
        else:
            b0 = x2
        iterations -= 1
    return ((a0 + b0) / 2), func((a0 + b0) / 2)


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


def fibonacci_default(number):
    return (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** number - ((1 - math.sqrt(5)) / 2) ** number)


def fibonacci_main(a0, b0):
    iterations = 0
    while ((b0 - a0) / epsilon) >= fibonacci_default(iterations + 2):
        iterations += 1
    fibonacci_def_n = fibonacci_default(iterations)
    fibonacci_def_plus_n = fibonacci_default(iterations + 1)
    fibonacci_def_plus_2n = fibonacci_default(iterations + 2)
    while (iterations > 0):
        iterations -= 1
        x1 = a0 + (fibonacci_def_n / fibonacci_def_plus_2n)*(b0 - a0)
        x2 = a0 + (fibonacci_def_plus_n / fibonacci_def_plus_2n)*(b0 - a0)
        if func(x1) > func(x2):
            a0 = x1
            x2 = b0
        elif func(x1) < func(x2):
            b0 = x2
            x1 = a0
    return (a0 + b0) / 2, func((a0 + b0) / 2)



print(dichotomy_method(-13, -1))
print(golden_ratio_method(-13, -1))
print(fibonacci_main(-13, -1))
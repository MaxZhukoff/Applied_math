import math

def dichotomy(f, a, b, epsilon):
    iterations = math.log((b - a) / epsilon) / math.log(2)
    delta = 0.1 * (epsilon / 2)
    while (b - a) / 2 >= epsilon:
        x = (a + b) / 2
        x1 = x - delta
        x2 = x + delta
        if f(x1) > f(x2):
            a = x1
        elif f(x1) < f(x2):
            b = x2
    return (a + b) / 2

def golden_ratio_method(f, a, b, epsilon):
    x1 = a + ((3 - math.sqrt(5)) / 2) * (b - a)
    x2 = a + ((math.sqrt(5) - 1) / 2) * (b - a)
    fx1 = f(x1)
    fx2 = f(x2)
    while (b - a) / 2 >= epsilon:
        if fx1 > fx2:
            # print(fx1, "      ", fx2)
            a = x1
            x1 = x2
            x2 = a + ((math.sqrt(5) - 1) / 2) * (b - a)
            fx1 = fx2
            fx2 = f(x2)
        elif fx1 < fx2:
            b = x2
            x2 = x1
            x1 = a + ((3 - math.sqrt(5)) / 2) * (b - a)
            fx2 = fx1
            fx1 = f(x1)
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
    # prev = b - a
    while (b - a) / 2 >= epsilon:
        k += 1
        if fx1 > fx2:
            a = x1
            x1 = x2
            x2 = a + (fibonacci_default(iterations - k + 2) / fibonacci_default(iterations - k + 3)) * (b - a)
            fx1 = fx2
            fx2 = f(x2)
            x1 = a + (fibonacci_default(iterations - k + 1) / fibonacci_default(iterations - k + 3)) * (b - a)
            fx2 = fx1
            fx1 = f(x1)
            # print(k, fibonacci_default(iterations - k + 2), fibonacci_default(iterations - k + 3),
            #       fibonacci_default(iterations - k + 2) / fibonacci_default(iterations - k + 3))
            # print(prev / (b - a))
        elif fx1 < fx2:
            b = x2
            x2 = x1
            # print(k, fibonacci_default(iterations - k + 1), fibonacci_default(iterations - k + 3),
            #       fibonacci_default(iterations - k + 1) / fibonacci_default(iterations - k + 3))
            # print(prev / (b - a))
        # prev = b - a
    return (a + b) / 2
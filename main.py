import math

f = lambda x: math.sin(x) * x ** 3

a, b = -8, -3

epsilon = 0.001


def dichotomy(a, b):
    iterations = math.log((b - a) / epsilon) / math.log(2)
    print(iterations)
    iterations = 0
    delta = 0.1 * (epsilon / 2)
    while (b - a) / 2 >= epsilon:
        x = (a + b) / 2
        x1 = x - delta
        x2 = x + delta
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
        iterations += 1
    print(iterations)
    return (a + b) / 2, f((a + b) / 2)


def golden_ratio_method(a, b):
    x1 = a + ((3 - math.sqrt(5)) / 2) * (b - a)
    x2 = b - ((3 - math.sqrt(5)) / 2) * (b - a)
    iterations = 0
    while (b - a) / 2 >= epsilon:
        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
        elif f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + (b - x2)
        iterations += 1
    print(iterations)
    return (a + b) / 2, f((a + b) / 2)


def fibonacci_default(number):
    return (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** number - ((1 - math.sqrt(5)) / 2) ** number)


def fibonacci_method(a, b):
    iterations = 0
    while ((b - a) / epsilon) >= fibonacci_default(iterations + 2):
        iterations += 1
    fibonacci_def_n = fibonacci_default(iterations)
    fibonacci_def_plus_n = fibonacci_default(iterations + 1)
    fibonacci_def_plus_2n = fibonacci_default(iterations + 2)
    while (b - a) / 2 >= epsilon:
        x1 = a + (fibonacci_def_n / fibonacci_def_plus_2n) * (b - a)
        x2 = a + (fibonacci_def_plus_n / fibonacci_def_plus_2n) * (b - a)
        if f(x1) > f(x2):
            a = x1
        elif f(x1) < f(x2):
            b = x2
    return (a + b) / 2, f((a + b) / 2)


def parabola_method(a, b):
    x1 = a
    x3 = b
    f1 = f(x1)
    f3 = f(x3)
    iterations = 0
    while x3 - x1 > epsilon:
        x2 = (x1 + x3) / 2
        f2 = f(x2)
        u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f3 - f1)) / (
                2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        fu = f(u)
        if u < x2:
            left, fl = u, fu
            right, fr = x2, f2
        else:
            left, fl = x2, f2
            right, fr = u, fu
        if fl < fr:
            x3, f3 = right, fr
        elif fl > fr:
            x1, f1 = left, fl
        iterations += 1
    return (x1 + x3) / 2, f((x1 + x3) / 2)


def combined_brent_method(a, c):
    iterations = 0
    k = (math.sqrt(5) - 1) / 2
    u = 0
    x = w = v = (a + c) / 2
    fx = fw = fv = f(x)
    d = e = (c - a)
    while math.fabs(c - a) >= epsilon:
        iterations += 1
        g = e
        e = d
        if x != w and x != v and v != w and fx != fw and fx != fv and fw != fv:
            arr = sorted([x, v, w])
            x1 = arr[0]
            x2 = arr[1]
            x3 = arr[2]
            f1, f2, f3 = f(x1), f(x2), f(x3)
            u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f3 - f1)) \
                / (2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        if u >= a + epsilon and u <= c - epsilon and math.fabs(u - x) < g / 2:
            d = math.fabs(u - x)
        else:
            if x < a + (c - a) / 2:
                u = x + k * (c - x)
                d = c - x
            else:
                u = x - k * (x - a)
                d = x - a
        fu = f(u)
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw or w == x:
                v = w
                w = u
                fv = fw
                fw = u
            elif fu <= fv or x == v or w == v:
                v = u
                fv = fu
    return x, fx


print("Dichotomy (x;y): ", dichotomy(a, b))
print("Golden ratio method (x;y): ", golden_ratio_method(a, b))
print("Fibonacci method (x;y): ", fibonacci_method(a, b))
print("Parabola_method (x;y): ", parabola_method(a, b))
print("Combined Brent method (x;y): ", combined_brent_method(a, b))

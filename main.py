import math

f = lambda x: math.sin(x) * x ** 3

a, b = -8, -3

epsilon = 0.001


def dichotomy(a, b):
    iterations = math.log((b - a) / epsilon) / math.log(2)
    delta = 0.1 * (epsilon / 2)
    en = 0
    while (b - a) / 2 >= epsilon:
        x = (a + b) / 2
        x1 = x - delta
        x2 = x + delta
        en += 2
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
    print(en)
    return (a + b) / 2, f((a + b) / 2)


def golden_ratio_method(a, b):
    x1 = a + ((3 - math.sqrt(5)) / 2) * (b - a)
    x2 = b - ((3 - math.sqrt(5)) / 2) * (b - a)
    fx1 = f(x1)
    fx2 = f(x2)
    en = 2
    while (b - a) / 2 >= epsilon:
        if fx1 > fx2:
            a = x1
            x1 = x2
            x2 = a + ((math.sqrt(5) - 1) / 2) * (b - a)
            fx1 = fx2
            fx2 = f(x2)
            en += 1
        elif fx1 < fx2:
            b = x2
            x2 = x1
            x1 = a + (1 - ((math.sqrt(5) - 1) / 2)) * (b - a)
            fx2 = fx1
            fx1 = f(x1)
            en += 1
        # print(en, a, b, math.fabs(b - a), (a + b) / 2, f((a + b) / 2))
    print(en)
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
    x1 = a + (fibonacci_def_n / fibonacci_def_plus_2n) * (b - a)
    x2 = a + (fibonacci_def_plus_n / fibonacci_def_plus_2n) * (b - a)
    fx1 = f(x1)
    fx2 = f(x2)
    en = 2
    while (b - a) / 2 >= epsilon:
        if fx1 > fx2:
            a = x1
            x1 = x2
            x2 = a + (fibonacci_def_plus_n / fibonacci_def_plus_2n) * (b - a)
            fx1 = fx2
            fx2 = f(x2)
            en += 1
        elif fx1 < fx2:
            b = x2
            x2 = x1
            x1 = a + (fibonacci_def_n / fibonacci_def_plus_2n) * (b - a)
            fx2 = fx1
            fx1 = f(x1)
            en += 1
    print(en)
    return (a + b) / 2, f((a + b) / 2)

def parabola_method(a, b):
    x1 = a
    x3 = b
    f1 = f(x1)
    f3 = f(x3)
    en = 2
    while x3 - x1 > epsilon:
        x2 = (x1 + x3) / 2
        f2 = f(x2)
        en += 1
        u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f3 - f1)) / (
                2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        fu = f(u)
        en += 1
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
    print(en)
    return (x1 + x3) / 2, f((x1 + x3) / 2)


def combined_brent_method(a, c):
    k = (math.sqrt(5) - 1) / 2
    u = 0
    x = w = v = (a + c) / 2
    fx = fw = fv = f(x)
    en = 1
    d = e = (c - a)
    while math.fabs(c - a) >= epsilon:
        g = e
        e = d
        if x != w and x != v and v != w and fx != fw and fx != fv and fw != fv:
            x1 = x
            f1 = fx
            x2 = w
            f2 = fw
            x3 = v
            f3 = fv
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
        en += 1
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
    print(en)
    return x, f(x)


print("Dichotomy (x;y): ", dichotomy(a, b))
print("Golden ratio method (x;y): ", golden_ratio_method(a, b))
print("Fibonacci method (x;y): ", fibonacci_method(a, b))
print("Parabola_method (x;y): ", parabola_method(a, b))
print("Combined Brent method (x;y): ", combined_brent_method(a, b))

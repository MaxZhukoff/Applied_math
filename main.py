import math

f = lambda x: math.sin(x) * x ** 3

a0, b0 = -7, -4

e = 0.001

def dichotomy(a0, b0):
    en = math.log((b0 - a0) / e) / math.log(2)
    print(en)
    en = 0
    d = 0.1 * (e / 2)
    while (b0 - a0) / 2 >= e:
        x = (a0 + b0) / 2
        x1 = x - d
        x2 = x + d
        if f(x1) > f(x2):
            a0 = x1
        else:
            b0 = x2
        en += 1
    print(en)
    return (a0 + b0) / 2, f((a0 + b0) / 2)


def parabola_method(a0, b0):
    x1 = a0
    x3 = b0
    f1 = f(x1)
    f3 = f(x3)
    en = 0
    while x3 - x1 > e:
        x2 = (x1 + x3) / 2
        f2 = f(x2)
        u = x2 - ((x2-x1)**2 * (f2-f3) - (x2-x3)**2 * (f3-f1)) / (2 * ((x2-x1) * (f2-f3) - (x2-x3) * (f2-f1)))
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
        en += 1
    print(en)
    return (x1 + x3) / 2, f((x1 + x3) / 2)

def golden_ratio_method(a0, b0):
    x1 = a0 + ((3 - math.sqrt(5)) / 2) * (b0 - a0)
    x2 = b0 - ((3 - math.sqrt(5)) / 2) * (b0 - a0)
    en = 0
    while (b0 - a0) / 2 >= e:
        if f(x1) > f(x2):
            a0 = x1
            x1 = x2
            x2 = b0 - (x1 - a0)
        elif f(x1) < f(x2):
            b0 = x2
            x2 = x1
            x1 = a0 + (b0 - x2)
        en += 1
    print(en)
    return (a0 + b0) / 2, f((a0 + b0) / 2)

def fibonacci_default(number):
    return (1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** number - ((1 - math.sqrt(5)) / 2) ** number)


def fibonacci_method(a0, b0):
    iterations = 0
    while ((b0 - a0) / e) >= fibonacci_default(iterations + 2):
        iterations += 1
    fibonacci_def_n = fibonacci_default(iterations)
    fibonacci_def_plus_n = fibonacci_default(iterations + 1)
    fibonacci_def_plus_2n = fibonacci_default(iterations + 2)
    while (iterations > 0):
        iterations -= 1
        x1 = a0 + (fibonacci_def_n / fibonacci_def_plus_2n)*(b0 - a0)
        x2 = a0 + (fibonacci_def_plus_n / fibonacci_def_plus_2n)*(b0 - a0)
        if f(x1) > f(x2):
            a0 = x1
            x2 = b0
        elif f(x1) < f(x2):
            b0 = x2
            x1 = a0
    return (a0 + b0) / 2, f((a0 + b0) / 2)

def combined_brent_method(a0, b0):
    a, c, x, w, v, u = 1, 1, 1, 1, 1, 1
    a, c = a0, b0


print('dichotomy (x;y): %s %s' % dichotomy(a0, b0))
print('parabola_method (x;y): %s %s' % parabola_method(a0, b0))
print('golden_ratio_method (x;y): %s %s' % golden_ratio_method(a0, b0))
print('fibonacci_method (x;y): %s %s' % fibonacci_method(a0, b0))

import math

func = lambda x: math.sin(x) * x ** 3

a0, b0 = -7, -3

e = 0.01

def dichotomy(a0, b0, f):
    en = math.log((b0 - a0) / e) / math.log(2)
    print(en)
    d = (e / 2) - 0.0001
    while en >= 1:
        x = (a0 + b0) / 2
        x1 = x - d
        x2 = x + d
        if f(x1) > f(x2):
            a0 = x1
        else:
            b0 = x2
        en -= 1
    return f((a0 + b0) / 2)

def parabola_method(a0, b0, f):
    x1 = a0
    x3 = b0
    f1 = f(x1)
    f3 = f(x3)

    un = 3
    while (un >= 1):
        x2 = (x1 + x3) / 2
        f2 = f(x2)
        u = x2 - ((x2-x1)**2 * (f2-f3) - (x2-x3)**2 * (f3-f1)) / (2 * ((x2-x1) * (f2-f3) - (x2-x3) * (f2-f1)))
        print(x1, x2, x3, f1, f2, f3, u, f(u))
        if f2 < f1 and f2 < f3:
            if x2 < u:
                x1 = x2
                x3 = u
                f1 = f(x1)
                f3 = f(x3)
            else:
                x1 = u
                x3 = x1
                f1 = f(x3)
                f3 = f(x1)
        un -= 1

print ('dichotomy: %s' % dichotomy(a0, b0, func))
parabola_method(a0, b0, func)

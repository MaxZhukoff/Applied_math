import math

func = lambda x: math.sin(x) * x ** 3

a0, b0 = -7, -4

e = 0.0001

def parabola_method(a0, b0, f):
    x1 = a0
    x3 = b0
    f1 = f(x1)
    f3 = f(x3)

    en = 0
    while x3 - x1 > e:
        x2 = (x1 + x3) / 2
        f2 = f(x2)
        u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f3 - f1)) / (
                    2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))
        # print(x1, x2, x3, f1, f2, f3, u, f(u))
        left = min(u, x2)  # u
        right = max(u, x2)  # x
        if left == u:
            fl = f(u)
            fr = f2
        else:
            fl = f2
            fr = f(u)
        if f(left) < f(right):
            x3 = right
            f3 = fr
        elif f(left) > f(right):
            x1 = left
            f1 = fl
        else:
            x3 = right
            f3 = fr
            x1 = left
            f1 = fl
    return f((x1 + x3) / 2)

print('parabola_method: %s' % parabola_method(a0, b0, func))

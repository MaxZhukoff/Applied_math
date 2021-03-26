import math

func = lambda x: math.sin(x) * x ** 3

a0, b0 = -7, -4

e = 0.001

def parabola_method(a0, b0):
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
        fu = f(u)
        if u < x2:
            left = u
            fl = fu
            right = x2
            fr = f2
        else:
            left = x2
            fl = f2
            right = u
            fr = fu
        if fl < fr:
            x3 = right
            f3 = fr
        elif fl > fr:
            x1 = left
            f1 = fl
        en += 1
    print(en)
    return (x1 + x3) / 2, f((x1 + x3) / 2)

print('parabola_method (x;y): %s %s' % parabola_method(a0, b0))

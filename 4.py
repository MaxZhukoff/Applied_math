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

print('parabola_method (x;y): %s %s' % parabola_method(a0, b0))
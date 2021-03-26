import math

f = lambda x: math.sin(x) * x ** 3

a0, b0 = -13, -1

e = 0.001

def dichotomy(a0, b0):
    en = math.log((b0 - a0) / e) / math.log(2)
    print(en)
    d = 0.1 * (e / 2)
    while en >= 1:
        x = (a0 + b0) / 2
        x1 = x - d
        x2 = x + d
        if f(x1) > f(x2):
            a0 = x1
        else:
            b0 = x2
        en -= 1
    return (a0 + b0) / 2, f((a0 + b0) / 2)

print('dichotomy (x;y): %s %s' % dichotomy(a0, b0))

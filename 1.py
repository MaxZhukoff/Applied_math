import math

func = lambda x: math.sin(x) * x ** 3

a0, b0 = -3, -3

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

print ('dichotomy: %s' % dichotomy(a0, b0, func))

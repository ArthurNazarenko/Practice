import math
#lab3
# MPD
EPS = 0.001


def f(x):
    return x**2 - 3 #1 2
    #return 3 * x ** 4 - 8 * x ** 3 - 18 * x ** 2 + 2
    #return x**3 - 2*x + 1
    #return 16 - x * x + 0.7

def bisection(a, b, c, eps):
    i = 1
    while ((b-a) > eps):
        c = (a + b) / 2
        if (f(c) == 0):
            break
        if (f(a) * f(c) < 0):
            b = c
        else:
            a = c
    print("x {} = {}".format(i + 1, c))
    return i

print(f(2))

def main():
    Z, Y = 0, 1
    c = None
    print('intervals [a,b]: ')
    a = int(input())
    b = int(input())
    print('intervals [a,b]: [{},{}] '.format(a, b))

    if (a > b):
        tmp = a
        a, b = b, tmp

        #buffer = a
        #a = b
        #b = buffer

    n = (math.fabs(a) + math.fabs(b)) / 0.01
    print(n)
    for i in range(int(n)):

        a = a + 0.1

        if (f(a) > 0):
            Z = 1
        else:
            if (f(a) < 0 and Z == 1 and Y == 1):
                bisection(a - 0.1, a, c, EPS)
                Z = 0
        if (f(a) < 0):
            Y = 0
        else:
            if (f(a) > 0 and Y == 0 and Z == 1):
                bisection(a - 0.1, a, c, EPS)
                Y = 1
    return 0

main()


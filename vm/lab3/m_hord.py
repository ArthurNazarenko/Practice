import math
EPS = 0.001

def func(x):
    return x ** 2 - 3
    #return 3 * x ** 4 - 8 * x ** 3 - 18 * x ** 2 + 2
    #return x**3 - x + 1

def m_hord(a, b, eps):
    i = 1
    while (math.fabs(b - a) > eps):
        a = b - (b - a) * func(b) / (func(b) - func(a))
        b = a - (a - b) * func(a) / (func(a) - func(b))
    print("x = {}".format(b))
    return i

def main():
    Z, Y = 0, 1
    print('intervals:')
    a = int(input())
    b = int(input())
    print('intervals [a,b]: [{},{}] '.format(a, b))

    if (a > b):
        tmp = a
        a,b = b,tmp
    n = (math.fabs(a) + math.fabs(b)) / 0.01
    print(n)
    for i in range(int(n)):
        a = a + 0.1
        if (0 < func(a)):
            Z = 1
        else:
            if (func(a) < 0 and Z == 1 and Y == 1):
                m_hord(a - 0.1, a, EPS)
                Z = 0
        if (0 > func(a)):
            Y = 0
        else:
            if (func(a) > 0 and Y == 0 and Z == 1):
                m_hord(a - 0.1, a, EPS)
                Y = 1

main()


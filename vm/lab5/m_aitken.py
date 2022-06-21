import numpy as np
import matplotlib.pyplot as plt
# 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0
# 2.7182 3.0041 3.3201 3.6692 4.0552 4.816 4.9530 5.4739 6.0496 6.6858 7.3890
x = [] # 1.5 1.52 1.54 1.56 1.58
y = [] # 4.4817 4.5722 4.6646 4.7588 4.855
with open('in.txt', 'rt') as f:
    for line in f:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()  # забираем \n справа
            if (ln != ''):
                num = float(ln)
                lst = lst + [num]
        x = x + [lst]
y = x[-1]
x = x.pop(0)

x = np.array(x, dtype = float)
y = np.array(y, dtype = float)

def Aitken_scheme(x, y, xp, n):
    p = np.zeros((n, n), dtype="float")
    eps = np.ones((n, n))
    for j in range(n):
        p[j, j] = y[j]
        for i in range(j - 1, 0, -1):
            p[i, j] = 1 / (x[j] - x[i]) * ((xp - x[i]) * p[i + 1, j] - (xp - x[j]) * p[i, j - 1])

            eps[i, j] = abs(p[i, j] - p[i - 1, j - 1])

            if (abs(p[i, j] - p[i - 1, j - 1]) < 0.001):
                return p[i, j].round(4)

    return p[np.where(eps == eps.min())][0].round(4)

def Print_Graphs():
    print('Введите точку, в которой нужно найти решение:')
    point = float(input())
    Aitken = Aitken_scheme(x, y, point, 10)
    print(f'В точке {point} значение функции: {Aitken}')
    new_x = np.linspace(np.min(x), np.max(x), 100)
    new_y = [Aitken_scheme(x, y, i, 10) for i in new_x]
    plt.plot(x, y, 'o', new_x, new_y)
    plt.ylabel(r'$Y$')
    plt.xlabel(r'$X$')
    plt.grid(True)
    plt.show()

Print_Graphs()

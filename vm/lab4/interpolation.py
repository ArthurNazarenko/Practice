import numpy as np
import matplotlib.pyplot as plt
# 0.4 0.5 0.6 0.7 0.8
# -0.9163 -0.6931 -0.5108 -0.3567 -0.2231
# read from 'in'
x = [] # 0 0.16 0.5
y = [] # 0 0.5 1
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

def lagrange(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1; p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1; p2 = p2 * 1
            else:
                p1 = p1*(t - x[i])
                p2 = p2 *(x[j] - x[i])
        z = z + y[j] * p1/p2
    return z

def Print_Graphs():
    print('Введите число: ')
    t = float(input())
    print(lagrange(x,y, t)) # 0.54
    new_x = np.linspace(np.min(x), np.max(x), 100)
    new_y = [lagrange(x,y,i) for i in new_x]
    plt.plot(x, y, 'o', new_x, new_y)
    plt.ylabel(r'$Y$')
    plt.xlabel(r'$X$')
    plt.grid(True)
    plt.show()

Print_Graphs()
f = open('vm/lab1/in.txt', 'rt')
mA = []
mB = []
i = 0
for line in f:
    lines = line.split(' ')
    lst = []
    blist = []  ###
    for ln in lines:
        ln = ln.rstrip()  # забираем \n справа
        if (ln != ''):
            num = float(ln)
            lst = lst + [num]
            print(lst)
            blst = lst[-1]
    lst = lst[:-1]  # удаляем последний элемент и ставим его в другой список
    mA = mA + [lst]
    mB = mB + [blst]
# print(mA)
# print(mB)

f.close()

x = []
y = []
with open('in.txt', 'rt') as f:
    for line in f:
        lines = line.split(' ')
        #print(lines)
        lst = []
        for ln in lines:
            ln = ln.rstrip()  # забираем \n справа
            if (ln != ''):
                num = float(ln)
                lst = lst + [num]
        #print(lst)
        x = x + [lst]
        #print(x)
    y = x[-1]
    #print(y)
    x = x.pop(0)
print(x)
print(y)

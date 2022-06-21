# X = A^-1 * B

# чтение матрицы с файла
f = open('in.txt', 'rt')
mA = []
mB = []
i = 0
for line in f:
    lines = line.split(' ')
    lst = []
    blist = []  ###
    for ln in lines:
        ln = ln.rstrip()    #забираем \n справа
        if (ln != ''):
            num = float(ln)
            lst = lst + [num]
            #print(lst)
            blst = lst[-1]
    lst = lst[:-1] #удаляем последний элемент и ставим его в другой список
    mA = mA + [lst]
    mB = mB + [blst]
f.close()


#   перемена двух сторк местами
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]

#   деление строки системы на число
def RowDivision(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider

#   сложение строки с другой, умноженной на число
def RowAddition(A, B, row, source_row, w):
    A[row] = [(a + k * w) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * w

def PrintMatrix(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("\t{1:10.6f}{0}".format(" " if (selected is None
or selected != (row, col)) else "*", A[row][col]), end="")
        print("\t) * (\tX{0}) = (\t{1:10.6f})".format(row + 1, B[row]))

def Gauss(A, B):
    column = 0
    while (column < len(B)):
        print("Находим максимальный по модулю элемент в {0} колонке:".format(column + 1))
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            print("нет решений")
            return None
        PrintMatrix(A, B, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом выше:")
            SwapRows(A, B, current_row, column)
            PrintMatrix(A, B, (column, column))
        print("нормализируем строку с найденным элементом:")
        RowDivision(A, B, column, A[column][column])
        PrintMatrix(A, B, (column, column))
        print("работаем с нижележащими строками:")
        for r in range(column + 1, len(A)):
            RowAddition(A, B, r, column, -A[r][column])
        PrintMatrix(A, B, (column, column))
        column += 1
    print("Матрица приведена к треугольному виду, решаем ее:")
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("получили ответ:")

    sourceFile = open('out.txt', 'w')
    print("\n".join("X{0} =\t{1:10.6f}".format(i + 1, x) for i, x in enumerate(X)), file=sourceFile)
    sourceFile.close()
    return X

#print("Исходная система:")
PrintMatrix(mA, mB, None)
#print("Решаем:")
Gauss(mA, mB)

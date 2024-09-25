d = [1, 2, 3, 4, 5]

for x in d:             #как использовать оператор for
    print(x)
                        #для for есть функция range(start,stop,step)
                        #формирование идет с 0 и ДО stop, stop же не включается в последовательность
                        #все остальное по аналогии со строками или массивами
for i in range(5):
    d[i] = 0
print(d)
                        #пример исползования for на примере факториала

# n = int(input("Enter a number: "))
#
# if n<0 or n>100:
#     print("NO")
# else:
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#     print(p)

#ВЛОЖЕННЫЕ ЦИКЛЫ

for i in range(1,4):
    for j in range (1,6):
        print(f"i = {i}, j = {j}", end = ' ')
    print()

a = [[1, 2, 3 , 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[1, 2, 3 , 4], [2, 3, 4, 5], [3, 4, 5, 6]]
c = []
                                        #пример вложенных циклов
for i in a:
    for x in i:
        print(x, type(x), end = ' ')
    print()

for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])
    c.append(r)
print(c)

#пример с транспонированием матрицы

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        matrix[i][j]= matrix[j][i]

for r in matrix:
    for x in r:
        print(x, end= '\t')
    print()

#Pascal triangle

N = 7
P = []

for i in range(N): #функция range не включает граничное значение, поэтому испольузется i+1, чтобы граничное значние вкл
    row = [1]*(i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1]+P[i-1][j]

    P.append(row)

for r in P:
    print(r)

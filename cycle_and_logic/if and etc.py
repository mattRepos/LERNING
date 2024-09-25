# ------ОПЕРАТОР IF И СВЯЗАННЫЕ С НИМ (WHILE ЕЩЕ)
x = -4
if x < 0:                   #если то, а иначе (принцип работы), в Python важна табуляция (отступы)
    x = -x
    print(x)
else:
    print(x)

# y = int(input("Введите число: ")) #input всегда вовзращает строку, поэтому нужны приведения типов
# if 4 <= y <=10:                   #можно записать и с помощью and или or
#     print("NORMAS")
# else:
#     print("NE NORMAS")

if x %2 ==0:
    if 0 <= x <=9:
        print("x - цифра")
    else:
        print("x - число")
                                #вместо конструкции if else if  можно испольховать if elif
aa = 12
bb = 7
res = aa if aa>bb else bb           #тернарный оператор работает так:
                                #присваиваем а если а больше б иначе присваиваем б
                                #нет внут блоков вместо а и б можно прописывать 1 конструкцию языка Py
                                #некоторое значение или работу операторов (напрм, арифметических)

i = 0
# while True:
#     i += 1
#     break                      #завершает цикл как только встречается этот оператор
# print("end")
#еще один пример использования break
d = [1, 5, 3, 6, 0, -4]
flFind = False
while flFind == False:
    flFind = d[i]%2 == 0
    if flFind == True:
        break
    i += 1
print(flFind)
                                #оператор continue
s = 0
d = 1
while d!=0:
    d = int(input("Введите целое число: "))
    if d % 2 ==0:
        continue
    s +=d
    print("s = "+ str(s))
                                #оператор else также есть и для while, который будет работать после ШТАТНОГО завершения
S = 0
i= - 10

while i<100:
    if i == 0:
        break
    S += 1/i
    i+= 1
else:
    print("NORMA CORRECTNO")
print(S)
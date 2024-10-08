# -------------------------------------------------list comprehensions--------------------------------------------------
sqrt = [n ** 2 for n in range(1, 21) if n % 2 == 0]
print(sqrt)

lst = ["Apple", "Banana", "Pear", "Peach", "Orange"]

a = [lst.lower() for lst in lst]
print(a)

b = [2 * n for n in range(1, 11)]
print(b)

lst2 = ["Anna", "Bob", "Clara", "Derek", "Eve"]
c = [i for i in lst2 if len(i) > 3]  # для адекватной работы функции len() необходимо было передать туда i, а не lst2
print(c)

lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [num if num % 3 != 0  # здесь логика такая, что если число не кратно 3, то оно печатается станл-о, если нет, то
     else "FIZZ"  # выводится строка, которая приведена в коде
     for num in lst3]
print(d)

lst4_1 = [1, 2, 3]
lst4_2 = ['a', 'b', 'c']
e = [(i, j) for i, j in zip(lst4_1, lst4_2)]  # функция zip получается на вход 2 итер.объекта для одновременного
print(e)  # итерирования по двум объектам. Длина итерирования равна длине самого меньшего итер элемента

lst5 = [n for n in range(1, 11)]
f = [(i, "even" if i % 2 == 0 else "odd") for i in lst5]  # здесь прописывается условное выражение в кортеже
print(f)  # иначе просто python не поймет куда и как работать с этим выржением, так получается, что это часть выраж-я

lst6 = ['apple', '', 'banana', '', 'cherry']
g = [j if j != '' else 'empty' for j in lst6]  # j если j не равна "", иначе выводится "empty" для j в lst6
print(g)

lst7_1 = [1, 2, 3]
lst7_2 = [4, 5, 6]
l = [i + j for i, j in zip(lst7_1, lst7_2)]
print(l)
# --------------------------------------------next nested list comprehensions-------------------------------------------

print() # создание пробелов в выводе
a1 = [[x * row for x in range(1,11)] for row in range(1,11)]
for row in a1:
     print(row)
print() # создание пробелов в выводе
b2 = [[0 for x in range(3)] for j in range(3)]
for j in b2:
     print(j)

numbers = [i for i in range(1, 31)]
c2 = [i ** 2 for i in numbers if i % 2 == 0 and i % 3 == 0]
print(c2)

с3 = [[(i,j) for i in range(1, 4)] for j in range(1, 4)]
print(с3)

nested_list = [[1, 2], [3, 4], [5, 6]]
d4 = [item
      for sublist in nested_list        # это внешний цикл
      for item in sublist]              # это внутренний цикл
print(d4)
# здесь логика такая, что берется сначала 1-й элемент исходного списка и из него извлекаеются уже вложенные элементы
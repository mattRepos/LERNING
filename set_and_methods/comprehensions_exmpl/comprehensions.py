a = {x ** 2 for x in range(1, 5)}   # генератор множества
print(a)
d = [1, 2, '1', '2', -4, 3, 4]
d1 = {int(x) for x in d}    # преобразование списка и строк в нем в числа и потом перебирание всего списка в множество
print(d1)
a = {int(x) for x in d if int(x) > 0}   # здесь можно использовать также условия и так далее
print(a)
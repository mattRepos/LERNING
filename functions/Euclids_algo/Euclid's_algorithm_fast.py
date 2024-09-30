def get_nod(a,b):
    """
        Вычисляет НОД для натруальных чисел a и b
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if a<b:
        a ,b = b, a
    while b != 0:
        a, b = a % b
    return a

res =get_nod(18,24)
print(res)
help(get_nod)   # вывод описание, которое было написано

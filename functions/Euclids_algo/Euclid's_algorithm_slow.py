def get_nod(a,b):
    """
        Вычисляет НОД для натруальных чисел a и b
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a !=b:
        if a > b:
            a -= b
        else:
            b -=a
    return a

res =get_nod(18,24)
print(res)
help(get_nod)   # вывод описание, которое было написано

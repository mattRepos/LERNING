def recursive(value):
    print(value)
    recursive(value + 1)


# recursive(1)
# так работает рекурсия, но нет базового случая, который заканчивает рекурсию и раскручивает спираль реку-и


def recurs(value):  # вот здесь есть условие базового случая
    print(value)
    if value < 4:
        recurs(value + 1)
    print(value)  # здесь идет раскручивание рекурсивной спирали и "разгрузка" стека, как бы "назад" по стеку


recurs(1)


def factorial(n):       # это лишь пример и не более, на деле факториал вычисляют с помощью цикла
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

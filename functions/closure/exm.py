import math as m
import random as rd
import time


def cos_func_counter():
    counter = 0

    def increment():
        nonlocal counter
        res_cos = m.cos(m.pi / rd.randrange(1, 6))
        counter += 1
        return res_cos, counter

    return increment


my_cos_and_count = cos_func_counter()
for i in range(1, 3):
    print(my_cos_and_count())


def min_filter(min_value):
    def cond(data):
        nonlocal min_value
        res = list(filter(lambda x: x > min_value, data))
        return res

    return cond


print()
# тут стоит сказать, что функция filter принимает в себя только итерируемые объекты в качестве второго аргумента
# поэтому тут в качестве второго арга идет список. Помимо этого мы также отдаем итерируемвый объект
my_filter = min_filter(5)
d = [4, 5, 6, 7, 8, 9]
print(my_filter(d))
print()


def sum_accumulator():
    res = 0

    def accumulator(value):
        nonlocal res
        res += value
        return res

    return accumulator


my_acc = sum_accumulator()
print(my_acc(10))
print(my_acc(20))
print(my_acc(100))
print()


def multiplier(n):
    def mech_multi(value):
        nonlocal n
        res = n * value
        return res

    return mech_multi


times3 = multiplier(3)
print(times3(5))
print(times3(10))
print()


def delay_execution(sec):  # стоит обратить внимание на этот пример. Тут не надо делать доп переменных, просто
    def sleep():  # возврщаем функцию sleep только, инициализируем и замыкание (внешнюю функцию)
        nonlocal sec
        time.sleep(sec)

    return sleep


delay_2_sec = delay_execution(2)
delay_2_sec()
print("kolbasa")

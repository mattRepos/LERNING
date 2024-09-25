a = {x: x ** 2 for x in range(1, 5)}   # генератор словаря
m = {'неуд': 2, 'удовл.': 3, 'хорошо': '4', 'отл': '5'}
a = {key.upper(): int(value) for key, value in m.items()}
print(a)

mm = {"безнадежно": 0, "убого": 1, "неудовлет": 2, "удовлет": 3, "хорошо": "4","отлично": "5"}
aa = {int(value): key for key, value in mm.items() if 2 <= int(value)<= 5}
print(aa)
from math import ceil


def square(x):
    s = x**2
    return ceil(s)


x = float(input("Введите число: "))
print(f"Округленная в большую сторону площадь - {square(x)}")

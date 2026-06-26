def is_year_leap(year):
    return True if year % 4 == 0 else False


num = int(input("Введите год: "))
result = is_year_leap(num)
print(f"Год {num}: {result}")

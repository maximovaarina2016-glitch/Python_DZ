def month_to_season(season):
    if season in [12, 1, 2]:
        return "Зима"
    elif season in [3, 4, 5]:
        return "Весна"
    elif season in [6, 7, 8]:
        return "Лето"
    elif season in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"


try:
    season = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(season))
except ValueError:
    print("Введите целое число от 1 до 12")

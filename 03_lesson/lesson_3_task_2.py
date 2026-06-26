from smartphone import Smartphone

catalog = [
    Smartphone("Apple", " iPhone 16", +79021481953),
    Smartphone("Xiaomi", "14 / 15", +79994445656),
    Smartphone("Honor", "Magic", +79116546546),
    Smartphone("Huawei", "Pura", +79004564545),
    Smartphone("Vivo", "V40", +79021489898),
]

for smartphone in catalog:
    print(
        f"Марка: {smartphone.brand}, Модель: {smartphone.model}, Телефон: {smartphone.phone}"
    )

class Address:
    def __init__(self, индекс, город, улица, дом, квартира):
        self.index = индекс
        self.country = город
        self.street = улица
        self.house = дом
        self.apartmet = квартира

    def format_address(self):
        return (
            f"{self.index}, {self.country}, "
            f"{self.street},{self.house} - {self.apartmet}"
        )

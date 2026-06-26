class Address:
    def __init__(self, index, country, street, house, apartmet):
        self.index = index
        self.country = country
        self.street = street
        self.house = house
        self.apartmet = apartmet

    def format_address(self):
        return (
        f"{self.index}, {self.country}, "
        f"{self.street},{self.house} - {self.apartmet}"
        )
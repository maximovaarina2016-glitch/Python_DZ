from address import Address


class Mailing:
    def __init__(
        self, to_address: Address, from_address: Address, track: str, cost
    ):
        self.to_address = to_address
        self.from_address = from_address
        self.track = track
        self.cost = cost

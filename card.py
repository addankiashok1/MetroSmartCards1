class MetroCard:
    def __init__(self, default_amount):
        self.balance = default_amount
        self.entered = False
        self.station_count = 0

    def purchase_card(self, amount):
        if self.balance == 0:
            self.balance += amount
            return True
        else:
            raise ValueError("Card purchase failed. Only one card can be purchased.")

    def top_up_card(self, amount):
        if amount <= 0:
            raise ValueError("Invalid top-up amount. Please enter a positive value.")
        self.balance += amount

    def calculate_fare(self, station_count):
        if station_count <= 0:
            raise ValueError("Invalid station count. Please enter a positive value.")
        if station_count <= 3:
            fare = 15
        else:
            fare = 15 + (station_count - 3) * 5
        return fare

    def deduct_fare(self, fare):
        if self.balance >= fare:
            self.balance -= fare
            return True
        else:
            raise ValueError("Insufficient balance. Please top up your card.")

    def enter_station(self):
        if self.balance >= 15:
            self.entered = True
            return True
        else:
            raise ValueError("Insufficient balance. Please top up your card.")

    def exit_station(self):
        if self.entered:
            self.entered = False
            return True
        else:
            raise ValueError("You haven't entered any station.")

    def apply_discount(self):
        if self.station_count % 5 == 0:
            discount = self.calculate_fare(self.station_count) * 0.05
            self.balance -= discount
class Plugboard:
    wiring = None

    def __init__(self, wiring):
        self.wiring = wiring

    def __str__(self):
        return self.wiring
from .ETW import ETW

class EtwPassthrough(ETW):
    wiring = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
         super().__init__(self.wiring)
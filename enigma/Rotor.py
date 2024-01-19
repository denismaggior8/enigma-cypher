
from string import ascii_lowercase

class Rotor:
    wiring = None
    position = 0
    alphabet = list(ascii_lowercase)
    
    def increment_position(self):
        self.position = (self.position + 1) % len(self.wiring)

    def scramble(self, char):
        scrambled_letter_index_from_rotor = self.wiring.index(self.wiring[(self.position + self.alphabet.index(char)) % len(self.wiring)]); 
        return self.wiring[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position):
        self.wiring = wiring
        self.position = position % len(wiring)

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
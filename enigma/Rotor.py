
from string import ascii_lowercase

class Rotor:
    wiring = None
    position = 0
    alphabet = list(ascii_lowercase)
    
    def increment_position(self):
        self.position = (self.position + 1) % len(self.wiring)

    def set_position(self,position):
        self.position = position % len(self.wiring)

    def scramble_letter_index(self, letter_index):
        scrambled_letter_index_from_rotor = self.wiring.index(self.wiring[(self.position + letter_index) % len(self.wiring)])
        return self.wiring[scrambled_letter_index_from_rotor]
    
    def scramble_letter_index_reverse(self, alphabet, letter_index):
        scrambled_letter_index_from_rotor = alphabet.index(alphabet[(self.position + letter_index) % len(alphabet)])
        return alphabet[scrambled_letter_index_from_rotor]

    def __init__(self, wiring, position):
        self.wiring = wiring
        self.position = position % len(wiring)

    def __str__(self):
        pointer = ' ' * self.position + '^'
        return self.wiring + '\n' + pointer 
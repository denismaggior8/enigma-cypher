class Enigma:
    
    plugboard = None
    rotors = None
    reflector = None

    def __init__(self, plugboard, rotors, reflector):
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector

    def input_char(self,char):
        return self.process_char(char)

    def process_char(self, char):
        scrabled_char = char
        for rotor in self.rotors:
            scrabled_char = rotor.scramble(scrabled_char)
        self.reflector.scramble(scrabled_char)
        return scrabled_char

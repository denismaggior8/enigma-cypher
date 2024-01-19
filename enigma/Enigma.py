class Enigma:
    
    plugboard = None
    rotors = None
    reflector = None

    def __init__(self, plugboard, rotors, reflector):
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector

    def input_char(self,char):
        print("Input char: "+ char)
        return self.process_char(char)

    def process_char(self, char):
        scrabled_char = char
        rotor_nr = 0
        for rotor in self.rotors:
            scrabled_char = rotor.scramble(scrabled_char)
            rotor_nr += 1
            print("Scrambled letter from rotor "+ str(rotor_nr)+ ": "+scrabled_char)
        scrabled_char = self.reflector.scramble(scrabled_char)
        print("Scrambled letter from reflector: "+scrabled_char)
        return scrabled_char

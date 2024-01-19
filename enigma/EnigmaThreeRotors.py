from .Enigma import Enigma

class EnigmaThreeRotors(Enigma):
   
    def __init__(self,plugboard,rotor1, rotor2, rotor3,reflector):
         rotors = [rotor1, rotor2, rotor3]
         super().__init__(self.plugboard,rotors,self.reflector)
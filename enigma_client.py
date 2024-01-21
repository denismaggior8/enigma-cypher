from enigma.RotorWiringI import RotorWiringI
from enigma.RotorWiringII import RotorWiringII
from enigma.RotorWiringIII import RotorWiringIII
from enigma.PlugboardPassthrough import PlugboardPassthrough
from enigma.ReflectorUKWB import ReflectorUKWB
from enigma.EnigmaThreeRotors import EnigmaThreeRotors
from enigma.EtwPassthrough import EtwPassthrough

plugboard = PlugboardPassthrough()
rotor1 = RotorWiringI(1)
rotor2 = RotorWiringII(0)
rotor3 = RotorWiringIII(0)
reflector = ReflectorUKWB()
etw = EtwPassthrough()

enigma = EnigmaThreeRotors(plugboard,rotor1,rotor2,rotor3,reflector,etw)

print(enigma.input_char("a"))

# print(plugboard)
#print(rotor1)
#print(rotor2)
#print(rotor3)
# print(reflector)

#rotor2.increment_position()



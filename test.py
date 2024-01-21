from enigma.RotorWiringI import RotorWiringI
from enigma.RotorWiringII import RotorWiringII
from enigma.RotorWiringIII import RotorWiringIII
from enigma.PlugboardPassthrough import PlugboardPassthrough
from enigma.ReflectorUKWB import ReflectorUKWB
from enigma.EnigmaThreeRotors import EnigmaThreeRotors

plugboard = PlugboardPassthrough()
rotor1 = RotorWiringI(0)
rotor2 = RotorWiringII(0)
rotor3 = RotorWiringIII(0)
reflector = ReflectorUKWB()

enigma = EnigmaThreeRotors(plugboard,rotor1,rotor2,rotor3,reflector)

if enigma.input_char("a") != 'l':
    print("Error")

rotor1.set_position(1)

if enigma.input_char("a") != 'h':
    print("Error")

rotor2.set_position(1)

if enigma.input_char("a") != 'j':
    print("Error")
    
rotor3.set_position(1)

if enigma.input_char("a") != 'c':
    print("Error")

rotor3.set_position(25)

if enigma.input_char("a") != 'c':
    print("Error")

# print(plugboard)
#print(rotor1)
#print(rotor2)
#print(rotor3)
# print(reflector)

#rotor2.increment_position()



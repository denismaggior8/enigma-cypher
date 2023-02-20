from string import ascii_lowercase
import sys

alphabet = list(ascii_lowercase)

rotor_1 = list('ekmflgdqvzntowyhxuspaibrcj') 	# Rotor wiring I
rotor_1_length = len(rotor_1)

rotor_2 = list('ajdksiruxblhwtmcqgznpyfvoe') 	# Rotor wiring II
rotor_2_length = len(rotor_2)

rotor_3 = list('bdfhjlcprtxvznyeiwgakmusqo')	# Rotor wiring III
rotor_3_length = len(rotor_3)

reflector = list('yruhqsldpxngokmiebfzcwvjat')	# Reflector model UKW-B
reflector_length = len(reflector)

def scramble(rotor, shift, letter_index):
	scrambled_letter_index_from_rotor = rotor.index(rotor[(shift + letter_index) % len(rotor)]); 
	return rotor[scrambled_letter_index_from_rotor]; 

def shift_letter(letter,shift):
	return alphabet[(alphabet.index(letter)+shift) % len(alphabet)]

def process(input_letter, counter_rotor_1, counter_rotor_2, counter_rotor_3):

    print('Input letter: {}'.format(input_letter))

    input_letter_index = alphabet.index(input_letter)
    print('Input letter index: {}'.format(input_letter_index))


    print('Counter rotor 1: {}'.format(counter_rotor_1))
    print('Counter rotor 2: {}'.format(counter_rotor_2))
    print('Counter rotor 3: {}'.format(counter_rotor_3))

    shift_rotor_1 = counter_rotor_1 % rotor_1_length
    shift_rotor_2 = counter_rotor_2 % rotor_2_length
    shift_rotor_3 = counter_rotor_3 % rotor_3_length

    print('Shift rotor 1: {}'.format(shift_rotor_1))
    print('Shift rotor 2: {}'.format(shift_rotor_2))
    print('Shift rotor 3: {}'.format(shift_rotor_3))

    letter_rotor_1 = alphabet[shift_rotor_1]
    letter_rotor_2 = alphabet[shift_rotor_2]
    letter_rotor_3 = alphabet[shift_rotor_3]

    print('Letter rotor 1: {}'.format(letter_rotor_1))
    print('Letter rotor 2: {}'.format(letter_rotor_2))
    print('Letter rotor 3: {}'.format(letter_rotor_3))

    scrambled_letter_from_rotor_1 = scramble(rotor_1,shift_rotor_1,input_letter_index)
    print('Scrambled letter from rotor 1: {}'.format(scrambled_letter_from_rotor_1))

    scrambled_letter_from_rotor_2 = scramble(rotor_2,shift_rotor_2,(alphabet.index(scrambled_letter_from_rotor_1)-shift_rotor_1) % rotor_2_length)
    print('Scrambled letter from rotor 2: {}'.format(scrambled_letter_from_rotor_2))

    scrambled_letter_from_rotor_3 = scramble(rotor_3,shift_rotor_3,(alphabet.index(scrambled_letter_from_rotor_2)-shift_rotor_2) % rotor_3_length)
    print('Scrambled letter from rotor 3: {}'.format(scrambled_letter_from_rotor_3))

    scrambled_letter_from_reflector = scramble(reflector,0,(alphabet.index(scrambled_letter_from_rotor_3)-shift_rotor_3) % reflector_length)
    print('Scrambled letter from reflector: {}'.format(scrambled_letter_from_reflector))

    scrambled_letter_from_rotor_3 = scramble(alphabet,shift_rotor_3,(rotor_3.index(shift_letter(scrambled_letter_from_reflector,shift_rotor_3))-shift_rotor_3) % rotor_3_length)
    print('Scrambled letter from rotor 3: {}'.format(scrambled_letter_from_rotor_3))

    scrambled_letter_from_rotor_2 = scramble(alphabet,shift_rotor_2,(rotor_2.index(shift_letter(scrambled_letter_from_rotor_3, (shift_rotor_2 - shift_rotor_3))) - shift_rotor_2) % rotor_2_length)
    print('Scrambled letter from rotor 2: {}'.format(scrambled_letter_from_rotor_2))

    scrambled_letter_from_rotor_1 = scramble(alphabet,shift_rotor_1,(rotor_1.index(shift_letter(scrambled_letter_from_rotor_2, (shift_rotor_1 - shift_rotor_2))) - shift_rotor_1) % rotor_1_length)
    print('Scrambled letter from rotor 1: {}'.format(scrambled_letter_from_rotor_1))

    scrambled_letter_from_etw = alphabet[(alphabet.index(scrambled_letter_from_rotor_1)-shift_rotor_1) % rotor_1_length]
    print('Scrambled letter from etw to lamp: {}'.format(scrambled_letter_from_etw))

def usage():
    print('Usage:\n\t# python enigma.py <input_letter> <rotor_1_counter> <rotor_2_counter> <rotor_3_counter>')
    print('i.e.:\n\t# python enigma.py z 1 0 0')

def main(input_letter,counter_rotor_1,counter_rotor_2,counter_rotor_3):
    if input_letter.lower() not in alphabet:
        exit('{} is not a valid letter'.format(input_letter))
    else:
        process(input_letter.lower(),counter_rotor_1,counter_rotor_2,counter_rotor_3)

if __name__ == "__main__":
    if len(sys.argv) < 5 :
        usage()
        exit()
    else:
        main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
    
# Enigma Cypher

This repo contains sample code to reproduce the Enigma cyper machine in Python. It resamble the Enigma M3 model (3 rotors) with the following configurations:

- Rotor 1 wiring I
- Rotor 2 wiring II
- Rotor 3 wiring III
- Reflector model UKW-B
- No steckerboard has been implemented so far

To run:

```console
$ python3 enigma.py <input_letter> <rotor_1_counter> <rotor_2_counter> <rotor_3_counter>
```

Rotor counters are a mechanism to shift each rotor by N positions. They can be any integer you want since they are translated to 0 up to 25 (0=a, 25=z).

For example:

```console
$ python3 enigma.py t 1 0 0
Input letter: t
Input letter index: 19
Counter rotor 1: 1
Counter rotor 2: 0
Counter rotor 3: 0
Shift rotor 1: 1
Shift rotor 2: 0
Shift rotor 3: 0
Letter rotor 1: b
Letter rotor 2: a
Letter rotor 3: a
Scrambled letter from rotor 1: a
Scrambled letter from rotor 2: e
Scrambled letter from rotor 3: j
Scrambled letter from reflector: x
Scrambled letter from rotor 3: k
Scrambled letter from rotor 2: d
Scrambled letter from rotor 1: a
Scrambled letter from etw: z
```

Reference: https://piotte13.github.io/enigma-cipher/

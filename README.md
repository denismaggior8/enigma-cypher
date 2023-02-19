# Enigma Cypher

This repo contains sample code to reproduce the Enigma cyper machine in Python.

To run:

```console
$ python3 enigma.py <input letter> <rotor 1 counter> <rotor 2 counter> <rotor 3 counter>
```

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

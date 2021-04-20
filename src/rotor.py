"""Holds the rotor class

Each object represents one rotor
Within the enigma machine the rotor would also scramble each letter similar to the plugboard
The rotors could not be configured similar to the plugboard and the connections are permanent
A letter would be switched to a different letter for each rotor it traveled through
Similarly to the plugboard a letter would not be mapped to itself
The rotors would increment for each letter pressed changing mapping during the process
Each rotor had a rollover point which could be set
Once the point was reached the next rotor would begin incrementing until its rollover point
Once the final rotor's rollover point was reached the cycle began again
After passing through each rotor the final encrypted character was shown on the lamp board"""

class rotor:
    def __init__():
        pass

    def convert_char():
        raise NotImplementedError()
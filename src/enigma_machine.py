"""This file hold the enigma class which represents the machine as a whole

It is capable of encrypting and decrypting messages"""
import plugboard
import spindle


class EnigmaMachine:
    def __init__(spindle: spindle.Spindle, plugboard: plugboard.Plugboard):
        this.spindle = spindle
        this.plugboard = plugboard

    def encrypt_message(plaintext: str) -> str:
        raise NotImplementedError()

    def decrypt_message(ciphertext: str) -> str:
        raise NotImplementedError()

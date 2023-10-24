import pyaes
from hashlib import sha256

## This class simplifies key derivation and keeping track of counters
class AES:
    ## 256-bit key derivation for AES using SHA256
    def __init__(self, key):
        self.key = sha256(bytes(str(key), 'ascii')).digest()
        self.encrypt_counter = self.decrypt_counter = 0

    def encrypt(self, plaintext):
        counter = pyaes.Counter(initial_value = self.encrypt_counter)
        aes = pyaes.AESModeOfOperationCTR(self.key, counter = counter)
        self.encrypt_counter += len(plaintext)
        return aes.encrypt(plaintext)

    def decrypt(self, ciphertext):
        counter = pyaes.Counter(initial_value = self.decrypt_counter)
        aes = pyaes.AESModeOfOperationCTR(self.key, counter = counter)
        self.decrypt_counter += len(ciphertext)
        return aes.decrypt(ciphertext).decode()

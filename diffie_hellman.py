## We should use "secrets" instead of "random" for
## cryptographically secure randomness, but DICE is spartan
from random import randrange

## Public parameters
g = 2 # generator
p = int('FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A6'
        '7CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A'
        '6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0'
        'BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE4'
        '5B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D2'
        '3DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1'
        '746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A'
        '28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D22618'
        '98FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF', 16) # group size

class DH:
    msg_length = len(str(p - 1))

    @staticmethod
    def generate_local_secret():
        return randrange(0, p - 1)

    @staticmethod
    def get_public_share(a):
        return pow(g, a, p)

    @staticmethod
    def get_shared_key(y, a):
        return pow(y, a, p)

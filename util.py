from diffie_hellman import DH

MAX_MSG_LENGTH = 10

def pad(msg, length):
    return bytes(str(msg).ljust(length), 'ascii')

def do_Diffie_Hellman(socket):
    local_secret = DH.generate_local_secret()
    our_public_share = DH.get_public_share(local_secret)
    socket.send(pad(our_public_share, DH.msg_length))
    remote_public_share = int(socket.recv(DH.msg_length))
    return DH.get_shared_key(remote_public_share, local_secret)

def encrypt_and_send(plaintext, aes, socket):
    ## We can only send messages of up to 16**MAX_MSG_LENGTH chars
    assert(len(plaintext) <= 16**MAX_MSG_LENGTH)
    length = aes.encrypt(pad(hex(len(plaintext)), len('0x') + MAX_MSG_LENGTH))
    socket.send(length)
    ciphertext = aes.encrypt(plaintext)
    socket.send(ciphertext)

def receive_and_decrypt(aes, socket):
    encrypted_len = socket.recv(len('0x') + MAX_MSG_LENGTH)
    decrypted_len_str = aes.decrypt(encrypted_len)
    decrypted_len = int(decrypted_len_str, 16)
    encrypted_msg = socket.recv(decrypted_len)
    return aes.decrypt(encrypted_msg)

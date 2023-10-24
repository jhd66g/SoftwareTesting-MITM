from dialog import Dialog
from simple_sockets import Socket
from symmetric import AES
from util import *

def setup(player, buffer_dir, buffer_file_name):
    assert player in set(('alice', 'bob'))
    dialog = Dialog('print')
    dialog.welcome('Hi {}! Welcome to SuperSecureChat!'.format(player.capitalize()))
    socket = Socket(player, buffer_dir, buffer_file_name)
    dialog.info('Establishing secure channel with your better half...')
    shared_key = do_Diffie_Hellman(socket)
    dialog.info('Established secure channel!')
    aes = AES(shared_key)
    return socket, aes

def tear_down(socket, buffer_dir, buffer_file_name):
    dialog = Dialog('print')
    dialog.info('Closing socket...')
    socket.close(buffer_dir, buffer_file_name)
    dialog.info('Socket closed! Bye-bye!')

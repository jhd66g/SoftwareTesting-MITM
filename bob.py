import sys
import os

from common import *
from const import *

dialog = Dialog('print')
player = os.path.basename(sys.argv[0]).split('.', 1)[0]
socket, aes = setup(player, BUFFER_DIR, BUFFER_FILE_NAME)

if CUSTOM_CHAT:
    dialog.prompt('Please input message...')
    to_send = input()
else:
    to_send = NICE_MSG[player]
encrypt_and_send(to_send, aes, socket)
dialog.info('Message sent! Waiting for reply...')
received = receive_and_decrypt(aes, socket)
dialog.chat('Alice said: "{}"'.format(received))

tear_down(socket, BUFFER_DIR, BUFFER_FILE_NAME)

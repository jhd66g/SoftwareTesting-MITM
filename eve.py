import sys
import os
import time

from common import *
from const import *

dialog = Dialog('print')

def relay():
    # Impersonate Alice to intercept Bob's message
    socket1, aes1 = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + "AE")

    # Impersonate Bob to intercept Alice's reply
    socket2, aes2 = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)
    bobs_message = receive_and_decrypt(aes2, socket2) 
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + "EB")
    os.rename(BUFFER_DIR + "AE", BUFFER_DIR + BUFFER_FILE_NAME)

    # Send Bob's original message to Alice
    encrypt_and_send(bobs_message, aes1, socket1)
    alices_message = receive_and_decrypt(aes1, socket1)
    tear_down(socket1, BUFFER_DIR, BUFFER_FILE_NAME)

    # Send Alice's reply to Bob
    os.rename(BUFFER_DIR + "EB", BUFFER_DIR + BUFFER_FILE_NAME)
    encrypt_and_send(alices_message, aes2, socket2) 
    tear_down(socket2, BUFFER_DIR, BUFFER_FILE_NAME)

def breakheart():
    # Impersonate Alice to intercept Bob's message
    socket1, aes1 = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + "AE")

    # Impersonate Bob to intercept Alice's reply
    socket2, aes2 = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)
    receive_and_decrypt(aes2, socket2)
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + "EB")
    os.rename(BUFFER_DIR + "AE", BUFFER_DIR + BUFFER_FILE_NAME)

    # Send altered message to Alice
    encrypt_and_send("I hate you!", aes1, socket1)
    receive_and_decrypt(aes1, socket1)
    tear_down(socket1, BUFFER_DIR, BUFFER_FILE_NAME)

    # Send altered message to Bob
    os.rename(BUFFER_DIR + "EB", BUFFER_DIR + BUFFER_FILE_NAME)
    encrypt_and_send("You broke my heart...", aes2, socket2)
    tear_down(socket2, BUFFER_DIR, BUFFER_FILE_NAME)

def custom():
    # Impersonate Alice to intercept Bob's message
    socket1, aes1 = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + "AE")

    # Impersonate Bob to intercept Alice's reply
    socket2, aes2 = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)
    receive_and_decrypt(aes2, socket2)
    os.rename(BUFFER_DIR + BUFFER_FILE_NAME, BUFFER_DIR + "EB")
    os.rename(BUFFER_DIR + "AE", BUFFER_DIR + BUFFER_FILE_NAME)

    # Send custom message to Alice
    dialog.prompt('Input a custom message to send to Alice: ')
    custom_to_alice = input()
    encrypt_and_send(custom_to_alice, aes1, socket1)
    receive_and_decrypt(aes1, socket1)
    tear_down(socket1, BUFFER_DIR, BUFFER_FILE_NAME)

    # Send altered message to Bob
    os.rename(BUFFER_DIR + "EB", BUFFER_DIR + BUFFER_FILE_NAME)
    dialog.prompt('Input a custom message to send to Bob: ')
    custom_to_bob = input()
    encrypt_and_send(custom_to_bob, aes2, socket2)
    tear_down(socket2, BUFFER_DIR, BUFFER_FILE_NAME)

# Main
if __name__ == "__main__":
    if len(sys.argv) < 2:
        dialog.error("Please provide a mode (--relay or --break-heart)")
        sys.exit(1)
    
    mode = sys.argv[1]

    if mode == "--relay":
        relay()
    elif mode == "--break-heart":
        breakheart()
    elif mode == "--custom":
        custom()
    else:
        dialog.error("Unknown mode. Please use either --relay, --break-heart, or --custom")

## Accept message from standard input or use defaults?
from string import Template
import getpass

CUSTOM_CHAT = False

## buffer for socket
# The slash here is important...
BUFFER_DIR = Template('/tmp/$usr/').substitute(usr = getpass.getuser())
BUFFER_FILE_NAME = 'buffer'

## Secret messages
NICE_MSG = {
    'alice': 'I love you too!',
    'bob': 'I love you!'
}
BAD_MSG = {
    'alice': 'You broke my heart...',
    'bob': 'I hate you!'
}

## Coloured output
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

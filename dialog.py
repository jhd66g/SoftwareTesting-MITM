from const import HEADER, BOLD, WARNING, FAIL, OKGREEN, ENDC

class Dialog:
    def __init__(self, print_mode):
        #  True for print, False for string
        self.print_mode = print_mode

    def output(self, formatted_msg):
        if self.print_mode == 'print':
            print(formatted_msg)
        elif self.print_mode == 'string':
            return formatted_msg
        else:
            raise

    def welcome(self, msg):
        return self.output(BOLD + msg + ENDC)

    def info(self, msg):
        return self.output(WARNING + msg + ENDC)

    def prompt(self, msg):
        return self.output(FAIL + msg + ENDC)

    def chat(self, msg):
        return self.output(OKGREEN + msg + ENDC)

    def think(self, msg):
        return self.output(HEADER + msg + ENDC)

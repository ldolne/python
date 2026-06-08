# from subprocess import call
import os
import time 

class Tools:
    @staticmethod
    def clear_console():
        os.system('clear' if os.name == 'posix' else 'cls')
        # _ = call('clear' if os.name == 'posix' else 'cls')

    @staticmethod
    def pause(second):
        time.sleep(second)
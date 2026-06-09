import os
import time

class Outils:
    
    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear') 
    
    @staticmethod
    def pause(seconde):
        time.sleep(seconde)
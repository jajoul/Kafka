import time
import os
import sounds
from colorama import Fore,Style
import sys

def starting_wizard():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    sounds.background_sound()
    print(f" Welcome to {Fore.RED} Kafka.{Style.RESET_ALL}")
    time.sleep(4)
    accept_age=input(f'this game is for adults only which has not violence graphics but it has violence sound effects.\nto accept your age please type 18 and press enter.\n{Fore.CYAN}')
    Style.RESET_ALL
    if accept_age=='18':
        print(f"{Fore.GREEN}Accepted{Style.RESET_ALL}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        quote=f'“And what I really intended to say in the end remains unsaid.\nSo I am still and I am silent, because if I open my mouth,I may never stop{Fore.RED} screaming{Style.RESET_ALL}.”'
        for char in quote:

            time.sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        sounds.scream_sound()
        time.sleep(4)
    else:
        print(f'{Fore.RED}Rejected{Style.RESET_ALL}')
    time.sleep(3)


starting_wizard()
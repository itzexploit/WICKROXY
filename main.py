from requests import get
from os import system , name , getpid
from colorama import Fore , init
from pystyle import Colors , Colorate
from os import kill as killx

init()
system('cls' if name == 'nt' else 'clear')

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

bann = f'''
             █████   ███   █████ █████   █████████  █████   ████ ███████████      ███████    █████ █████ █████ █████
            ░░███   ░███  ░░███ ░░███   ███░░░░░███░░███   ███░ ░░███░░░░░███   ███░░░░░███ ░░███ ░░███ ░░███ ░░███ 
             ░███   ░███   ░███  ░███  ███     ░░░  ░███  ███    ░███    ░███  ███     ░░███ ░░███ ███   ░░███ ███  
             ░███   ░███   ░███  ░███ ░███          ░███████     ░██████████  ░███      ░███  ░░█████     ░░█████   
             ░░███  █████  ███   ░███ ░███          ░███░░███    ░███░░░░░███ ░███      ░███   ███░███     ░░███    
              ░░░█████░█████░    ░███ ░░███     ███ ░███ ░░███   ░███    ░███ ░░███     ███   ███ ░░███     ░███    
                ░░███ ░░███      █████ ░░█████████  █████ ░░████ █████   █████ ░░░███████░   █████ █████    █████   
                  ░░░   ░░░      ░░░░░   ░░░░░░░░░  ░░░░░   ░░░░ ░░░░░   ░░░░░    ░░░░░░░    ░░░░░ ░░░░░    ░░░░░'''

print(Colorate.Horizontal(Colors.red_to_blue, bann, 1))
print(Colorate.Horizontal(Colors.red_to_yellow, '                                              Created By John Wick', 1))
print(Colorate.Horizontal(Colors.green_to_cyan, '                                                Team Pytho Learn', 1))
print(f'{green}\n  METHODS {red}: {yellow}socks5 {red}, {yellow}socks4 {red},{yellow} http {green}| {red}exit {yellow}, {cyan}clear')

while True:
    c = input(Colorate.Horizontal(Colors.red_to_blue,'\n  root@select-method#~$ ',1))

    def socks5():
        pr = get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
        file = open('socks5.txt', 'w')
        for p in pr:
            file.write(p)
        print(Colorate.Horizontal(Colors.green_to_cyan, '\n  <3 OK SUCESSFUL xD',1))

    def socks4():
        pr = get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text
        file = open('socks4.txt', 'w')
        for p in pr:
            file.write(p)
        print(Colorate.Horizontal(Colors.green_to_cyan, '\n  <3 OK SUCESSFUL xD',1))

    def http():
        pr = get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
        file = open('http.txt', 'w')
        for p in pr:
            file.write(p)
        print(Colorate.Horizontal(Colors.green_to_cyan, '\n  <3 OK SUCESSFUL xD',1))

    def exitt():
        killx(getpid(), 9)
    
    def clear():
        system('cls' if name == 'nt' else 'clear')

    if c == 'socks5':
        socks5()
    elif c == 'socks4':
        socks4()
    elif c == 'http':
        http()
    elif c == 'exit':
        exitt()
    elif c == 'clear':
        clear()
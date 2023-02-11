
import time
import os
import sys
from dhooks import Webhook, Embed
embed = Embed(
    description='Passwords.',
    color=0x38482,
    Timestamp='now',
    )
import colorama
from colorama import Fore
colorama.init()
def add():
    used = input("What program or site would this login info be for >> ")
    brah = input("Username for account: ")
    ah = input("Password for account: ")
    with open ('passwords.txt','a') as f:
        f.write(f"Username for {used} account:{brah}\n")
        f.write(f"Password for {used} account is: {ah}\n\n")
        "\n"
def view():
    with open ('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())
def exile():
    time.sleep(1)
    quit()
print(Fore.GREEN)
while True:
    pwed = input("Enter the master password >> ")
    if pwed == "hamood":
        print("correct.")
        time.sleep(1)
        os.system("cls")
        break
    else:
        print("incorrect.")
        time.sleep(1)
        os.system("cls")
        continue
while True:
    banner = (Fore.GREEN +"""
                                                    __
                                    ____  ____ ____________      ______  _________/ /
                                / __ \/ __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
                                / /_/ / /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
                                / .___/\__,_/____/____/ |__/|__/\____/_/   \__,_/   
                                /_/                                                  
                                                                            
                                ____ ___  ____ _____  ____ _____ ____  _____
                                / __ `__ \/ __ `/ __ \/ __ `/ __ `/ _ \/ ___/
                                / / / / / / /_/ / / / / /_/ / /_/ /  __/ /    
                                /_/ /_/ /_/\__,_/_/ /_/\__,_/\__, /\___/_/     
                                                            /____/             
                                made by ibzzy#0001
                                
    """)
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.00000000)
    menu = (Fore.LIGHTGREEN_EX +"""
[1] to add a password
[2] to View your existing passwords
[3] to Toggle Webhook
[4] to send Available passwords to Webhook
[5] to exit
    """)
    for char in menu:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
    option = int(input("> "))
    if option <= 0:
        print(Fore.RED +"exiting..")
        exile()
    elif option >= 6:
        exile()
    elif option == 5:
        exile()
    elif option == 1:
        add()
        print(Fore.GREEN +"added password succesfully")
        time.sleep(1)
        os.system('cls')
        continue
    elif option == 2:  
        view()
        print(f"{Fore.GREEN}[1] to return to the main menu\n[2] to exit""\n")
        select = int(input("> "))
        if select <= 0:
            exile()
        elif select >= 3:
            exile()
        elif select == 2:
            exile()
        elif select == 1:
            print(Fore.GREEN +"returning...")
            time.sleep(1)
            os.system('cls')
            continue
    elif option == 3:
        wabhook = input("Enter your webhook URL here: ")
        hook = Webhook(wabhook)
        time.sleep(1)
        print(Fore.GREEN +"Succesfully toggled webhook.")
        time.sleep(1)
        os.system('cls')
        continue
    elif option == 4:
        decis = int(input(f"[1] to send password to a webhook\n[2] to return to main menu\n[3] to exit >> "))
        if decis <= 0:
            exile()
        elif decis >= 4:
            exile()
        elif decis == 3:
            exile()
        elif decis == 2:
            while True:
                chars = input("What brand or program is your login info for?: ")
                charsa = input("Username for that account: ")
                hamda = input("Password for that account: ")
                embed.set_author(name='Passmang')
                embed.add_field(name=f"{chars} account info", value=f"username: {charsa}\nPassword: {hamda}")
                embed.set_footer(text='Powered by Passmang')
                hook.send(embed=embed)
                os.system('cls')
                time.sleep(1)
                break
        elif decis == 3:
            os.system('cls')
            continue

            
    
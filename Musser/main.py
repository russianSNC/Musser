# ok, Musser is a joke
# Fake Hack tool by Ferne

from colorama import init
from termcolor import colored
from os import system as s
from random import randint
from time import sleep
import sys
import os
from bl import *
import random as r

init()

print(colored("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ """, "white"))

print(colored('ENTER[enter]', 'green'))
print(colored('\nEXIT[exit]', 'green'))

choice = input("?: ")

if choice.lower() == "exit":
	quit()

if choice.lower() == "enter":
    s('cls')

s('cls')

print(colored("""

███╗   ███╗██╗   ██╗ ██████╗ ██████╗███████╗██████╗ 
████╗ ████║██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗
██╔████╔██║██║   ██║╚█████╗ ╚█████╗ █████╗  ██████╔╝
██║╚██╔╝██║██║   ██║ ╚═══██╗ ╚═══██╗██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██████╔╝██████╔╝███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝""", "green"))
print(colored("""█▀█ ▄▀█ ▀█▀ █▀█ █▀█ █
█▀▄ █▀█  █  █▄█ █▄█ █▄▄ by Ferne""", "red"))

choice = input("password: ")

while choice.lower() != "localhost":
  print(colored("access denied", "red"))
  choice = input("password: ")

s('cls')

beautifulPrint(text="Loading....")

s('cls')

print(colored('successful', "green"))

s('cls')

print(colored("""
█▀▄▀█ █ █ █▀ █▀ █▀▀ █▀█
█ ▀ █ █▄█ ▄█ ▄█ ██▄ █▀▄""", "green"))

print(colored('Welcome', 'red' ))

choice = input("Target: ")

sleep(3.50)
beautifulPrint(text="searching....")

sleep(3.50)
beautifulPrint(text="\ninjecting bypass")

sleep(3.50)
print(colored('\n2fa bypassed!!', 'green' ))

beautifulPrint(text="\nsearching IP address")

sleep(3.50)
print(colored(f"\n IP Found!!! {r.randint(0, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}.{r.randint(0, 255)}", "green"))


sleep(5.00)
s('cls')

print(colored("""
██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║██║░░╚═╝█████═╝░█████╗░░██║░░██║
██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██║░░██║
██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░""", "red"))

choice = input("force login?: ")
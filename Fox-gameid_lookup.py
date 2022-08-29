from os import closerange
from textwrap import indent
import requests , json , time
from pyfiglet import Figlet
import colorama
from rainbowtext import text
rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
mag = colorama.Fore.MAGENTA
bl = colorama.Fore.BLUE
yl = colorama.Fore.YELLOW
gn = colorama.Fore.GREEN
cy = colorama.Fore.CYAN


def xbox(id):
    req = requests.get(f"https://playerdb.co/api/player/xbox/{id}").json()
    return json.dumps(req , indent=4)

def minecraft(id):
    req = requests.get(f"https://playerdb.co/api/player/minecraft/{id}").json()
    return json.dumps(req , indent=4)

def steam(id):
    req = requests.get(f"https://playerdb.co/api/player/steam/{id}").json()
    return json.dumps(req , indent=4)


def banner():
    return text(Figlet(font="script").renderText("Black Fox"))

print (banner())
print (rd + "[-] Coded By ~> Maximum Radikal")
mode = input(bl + "[$] steam\n[$] xbox\n[$] minecraft\n\n[-] Please Enter An Option ~> : ")
username = input(yl + "[^] Please Enter your Username ~> ")
if mode == "steam":
    print (gn + steam(username) + cv)
if mode == "xbox":
    print (gn + xbox(username) + cv)
if mode == "minecraft":
    print (gn + minecraft(username) + cv)
else:
    print (rd + "You selected wrong Option ! ")

print (cy + "Channel : @BlackFoxSecurityTeam" + cv)

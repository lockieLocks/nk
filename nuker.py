import discord
import socket
from colorama import Fore, init, Style
from pystyle import Colorate, Colors
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
hostname = socket.gethostname()

root = (Fore.LIGHTMAGENTA_EX+f"""
┌──({hostname}&)-[~Menu -]│
└─$> """)

ascii_ = '''
SSSSS       .sSSSSs.    .sSSS  SSSSS                   .sSSSSSSs.  
SSSSS       SSSSSSSSSs. SSSSS  SSSSS                   `SSSS SSSSs 
S SSS       S SSS SSSSS S SSS SSSSS                          S SSS 
S  SS       S  SS SSSS' S  SS SSSSS         .sS          .sS S  SS 
S..SS       S..SS       S..SSsSSSSS        SSSSsssssss  SSSSsS..SS 
S:::S       S:::S SSSSS S:::S SSSSS         `:;          `:; S:::S 
S;;;S       S;;;S SSSSS S;;;S  SSSSS                         S;;;S 
S%%%S SSSSS S%%%S SSSSS S%%%S  SSSSS                   .SSSS S%%%S 
SSSSSsSS;:' SSSSSsSSSSS SSSSS   SSSSS                  `:;SSsSSSSS 
                                                                                                                                
┌─────────────────┐                        ┌─────────┐                          ┌───────────┐            
├──── Osint-Tools ┤────────────┬───────────┤ Discord ├────────────┬─────────────┤ Utilities ├────────────┤
└─────────────────┘            │           └─────────┘            │             └───────────┘            │
├ [01] OSINT Recon Menu        ├ [02] Discord-Tools Menu          ├ [03] Utilities Tool Menu             │
│────────────────────────────────────────────────────────────────────────────────────────────────────────│
│ [N] Next Page  |  [B] Back  |  [C] Credits | [Q] Quit                                                  │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

'''

def main():
    clear()
    COLS = Colorate.Diagonal(Colors.white_to_red, ascii_, 1) # pyright: ignore[reportAttributeAccessIssue] <- I couldnt figure out why Pylance kept flagging this.
    print(COLS)
    opt = input(root).lower().strip()
    if opt == "1" or opt == "01":
        print("Wont be added for a while, sorry.")
    elif opt == "2" or opt == "02":
        discord_menu()

def discord_menu():
    clear()
    root = f'''
┌──({hostname}&)-[~Menu -]│
└─$>'''
    ascii_ = """
    .sSSSSs.                                                                                       .sSSSSSSs.  
    SSSSSSSSSs. SSSSS .sSSSSSSSs. .sSSSSs.    .sSSSSs.    .sSSSSSSSs. .sSSSSs.                     `SSSS SSSSs 
    S SSS SSSSS S SSS S SSS SSSS' S SSSSSSSs. S SSSSSSSs. S SSS SSSSS S SSSSSSSs.                        S SSS 
    S  SS SSSSS S  SS S  SS       S  SS SSSS' S  SS SSSSS S  SS SSSS' S  SS SSSSS       .sS          .sS S  SS 
    S..SS SSSSS S..SS `SSSSsSSSa. S..SS       S..SS SSSSS S..SSsSSSa. S..SS SSSSS      SSSSsssssss  SSSSsS..SS 
    S:::S SSSSS S:::S .sSSS SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS       `:;          `:; S:::S 
    S;;;S SSSSS S;;;S S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS                        S;;;S 
    S%%%S SSSS' S%%%S S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSS'                  .SSSS S%%%S 
    SSSSSsS;:'  SSSSS SSSSSsSSSSS SSSSSsSSSSS SSSSSsSSSSS SSSSS SSSSS SSSSSsS;:'                   `:;SSsSSSSS         
        ---[INFO]---                                                                                     --[INFO]--
    [1] Discord Token Checker
    [2] Discord Webhook Checker
    [3] Discord Guild ID Checker
    """
    opt = input(root).lower().strip()
    if opt == "1" or opt == "01":
        print("Wont be added for a while, sorry.")
    elif opt == "2" or opt == "02":
        print("Wont be added for a while, sorry.")
    elif opt == "3" or opt == "03":
        print("Wont be added for a while, sorry.")

class Destruction:
    def __init__(self):
        pass

while True:
    main()
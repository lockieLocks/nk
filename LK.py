import discord
import socket
from colorama import Fore, init, Style
from pystyle import Colorate, Colors
from cogs.token_checker import check_discord_token
from cogs.webhook_checker import check_webhook
from cogs.guild_checker import get_info
from cogs.webhook_spammer import webhook_spammer
import os
import sys

init(autoreset=True)

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
hostname = socket.gethostname()

def root(discord: bool, MM: bool):
    if MM:
        iu = Fore.RED+f"""
┌──({hostname}#LK)-[~Menu ~]│
└─$> """
    elif discord:
        iu = Fore.RED+f"""
┌──({hostname}#LK)-[~Discord ~]│
└─$> """
    else:
        iu = Fore.RED+f"""
┌──({hostname}#LK)-[~]│
└─$> """
    return iu
ascii_ = r'''
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
    opt = input(root(MM=True, discord=False)).lower().strip()
    if opt == "1" or opt == "01":
        print("Wont be added for a while, sorry.")
    elif opt == "2" or opt == "02":
        discord_menu()

def discord_menu():
    clear()
    ascii_ = r"""

    .sSSSSs.                                                                                       .sSSSSSSs.  
    SSSSSSSSSs. SSSSS .sSSSSSSSs. .sSSSSs.    .sSSSSs.    .sSSSSSSSs. .sSSSSs.                     `SSSS SSSSs 
    S SSS SSSSS S SSS S SSS SSSS' S SSSSSSSs. S SSSSSSSs. S SSS SSSSS S SSSSSSSs.                        S SSS 
    S  SS SSSSS S  SS S  SS       S  SS SSSS' S  SS SSSSS S  SS SSSS' S  SS SSSSS       .sS          .sS S  SS 
    S..SS SSSSS S..SS `SSSSsSSSa. S..SS       S..SS SSSSS S..SSsSSSa. S..SS SSSSS      SSSSsssssss  SSSSsS..SS 
    S:::S SSSSS S:::S .sSSS SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS S:::S SSSSS       `:;          `:; S:::S 
    S;;;S SSSSS S;;;S S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS S;;;S SSSSS                        S;;;S 
    S%%%S SSSS' S%%%S S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSS'                  .SSSS S%%%S 
    SSSSSsS;:'  SSSSS SSSSSsSSSSS SSSSSsSSSSS SSSSSsSSSSS SSSSS SSSSS SSSSSsS;:'                   `:;SSsSSSSS       


        ---[INFO]---                    ---[WEBHOOK]---
    [1] Discord Token Checker         [4] Webhook Spammer
    [2] Discord Webhook Checker       [5] Webhook Change Name
    [3] Discord Guild INFO Checker    [6] Webhook Delete
                                      [7] Webhook Change PFP
    """
    proc = Colorate.Diagonal(Colors.white_to_red, ascii_, 1) # pyright: ignore[reportAttributeAccessIssue] <- I couldnt figure out why Pylance kept flagging this.
    print(proc)
    opt = input(root(MM=False, discord=True)).lower().strip()
    if opt == "1" or opt == "01":
        istxt = input("Are you using the token.txt file? (y/n): ").lower().strip()
        if istxt == "y" or istxt == "yes":
            txt_list = True
            result = check_discord_token(token="None", txt_list=txt_list)
        else:
            txt_list = False
            token = input("Enter a Discord token: ")
            result = check_discord_token(token, txt_list)
        print(result)
        input("Press Enter to continue...")
    elif opt == "2" or opt == "02":
        webhook = input("Enter a Discord webhook: ")
        result = check_webhook(webhook)
        print(result)
        input("Press Enter to continue...")
    elif opt == "3" or opt == "03":
        code = input("Enter Invite Code >> ")
        print(get_info(code))
        input("Press Enter to Return...")
    elif opt == '4':
        webhook = input("Enter Webhook: ")
        amount = int(input("Enter Amount of Messages >> "))
        context = input("Enter Message to spam >> ")
        print(webhook_spammer(webhook, amount, context))
        input("Press Enter to Continue...")
    elif opt == "n" or opt == "next":
        print("Wont be added for a while, sorry.")
        input("Press Enter to Return...")
    elif opt == "q" or opt == "quit":
        sys.exit()
    else:
        print("Invalid option")
        input("Press Enter to continue...")

try:
    while True:
        main()
except KeyboardInterrupt:
    print("\n" + Fore.LIGHTMAGENTA_EX + "Goodbye!" + Style.RESET_ALL)
    sys.exit()

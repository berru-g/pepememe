import ctypes
import pyautogui
import time
import winsound
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialiser Colorama
init()

# Afficher le titre avec pyfiglet
fig = Figlet(font='slant')
print(Fore.WHITE + fig.renderText('AutoClic V2') + Style.RESET_ALL)
print(Fore.WHITE + "AutoClic non stop")
print("Autoclick for - Tap To Earn 🪙 by https://pepememe.io/?code=h7krhhgt" + Style.RESET_ALL)
print(Fore.CYAN + "⚙️ Dev by https://github.com/berru-g/pepememe")


# Cacher la fenêtre de la console
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 1
hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)

# Début du programme
for i in range(10, 0, -1):
    print(Fore.YELLOW + f"\rLancement dans {i} secondes... " + Style.RESET_ALL, end="")
    time.sleep(1)

print(Fore.WHITE + "\n🪙 🐸 Autoclick faster than my grandMa who has Parkinson 🐸 🪙" + Style.RESET_ALL)

while True:
    for session in range(7):
        print(Fore.LIGHTCYAN_EX + f"\r🐸 Session {session + 1}/7 en cours... " + Style.RESET_ALL, end="")
        
        for click in range(1, 101):
            pyautogui.click(319, 813)  # Utilise les coordonnées
            time.sleep(0.1)
            if click % 10 == 0:
                print(Fore.YELLOW + f"\r⚙️ Session {session + 1}/7 | Clic {click}/100" + Style.RESET_ALL, end="")
        
        print(Fore.GREEN + f"\r✅ Session {session + 1}/7 terminée." + Style.RESET_ALL)
        
        # Pause de 4 minutes entre les sessions
        if session < 6:  # Pas de pause après la dernière session
            print(Fore.LIGHTBLUE_EX + "\r⏸️ Rechargement" + Style.RESET_ALL, end="")
            for remaining in range(7, 0, -1):  # 240 secondes = 4 minutes
                print(Fore.LIGHTBLUE_EX + f"\r⏸️ Pause : {remaining} secondes... " + Style.RESET_ALL, end="")
                time.sleep(1)
    
    # Alerte sonore avant la boucle suivante
    print(Fore.WHITE + "\r🔁 Nouvelle boucle" + Style.RESET_ALL)
    winsound.Beep(1000, 200)
    print(Fore.CYAN + "\rℹ️ Si tu utilise mon outil et que tu le souhaite, tu peut me faire un don 🤷‍♂️ " + Style.RESET_ALL)
    winsound.Beep(1200, 200)
    print(Fore.YELLOW + "\r ℹ️   - USDC / BTC / Paypal - " + Style.RESET_ALL)
    winsound.Beep(1000, 200)
    print(Fore.LIGHTBLUE_EX + "\r ➡️ https://fiboscope.netlify.app/donation" + Style.RESET_ALL)
    
    # Pause de 5 minutes avant la prochaine boucle
    print(Fore.WHITE + "\rRechargement...", end="" + Style.RESET_ALL)
    for remaining in range(300, 0, -1):  # 300 secondes = 5 minutes
        print(Fore.LIGHTCYAN_EX + f"\r🔄 Nouvelle boucle dans {remaining} secondes... " + Style.RESET_ALL, end="")
        time.sleep(1)
    winsound.Beep(1200, 200)
    winsound.Beep(1000, 200)

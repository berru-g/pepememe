import ctypes
import pyautogui
import time
import winsound
#
# Dev  by github.com/berru-g/
# Autoclic-V2

# Cacher la fenêtre de la console
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 1
hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)

# Début du programme
print("Tap To 🪙 Autoclick for pepememe.io")
for i in range(10, 0, -1):
    print(f"\rLancement dans {i} secondes... ", end="")
    time.sleep(1)

print("\nAutoclick faster than my grandMa who has Parkinson !")

while True:
    for session in range(7):
        print(f"\r🐸 Session {session + 1}/7 en cours... ", end="")
        
        for click in range(1, 101):
            pyautogui.click(319, 813)  # Utilise les coordonnées
            time.sleep(0.1)
            if click % 10 == 0:
                print(f"\r⚙️ Session {session + 1}/7 | Clic {click}/100", end="")
        
        print(f"\r✅ Session {session + 1}/7 terminée.")
        
        # Pause de 4 minutes entre les sessions
        if session < 6:  # Pas de pause après la dernière session
            print("\r⏸️ Pause de 30 secondes", end="")
            for remaining in range(10, 0, -1):  # 240 secondes = 4 minutes
                print(f"\r⏸️ Pause : {remaining} ", end="")
                time.sleep(1)
    
    # Alerte sonore avant la boucle suivante
    print("\r🔁 Nouvelle boucle")
    winsound.Beep(200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(1200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(440, 200)
    
    # Pause de 5 minutes avant la prochaine boucle
    print("\rRechargement... Nouvelle boucle dans ", end="")
    for remaining in range(300, 0, -1):  # 300 secondes = 5 minutes
        print(f"\r🔄 Nouvelle boucle dans {remaining} secondes... ", end="")
        time.sleep(1)

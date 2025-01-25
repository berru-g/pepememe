import ctypes
import pyautogui
import time
import winsound

# Minimise la fenêtre de la console
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 1  # 0 Cache la console
hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)

# Décompte avant le lancement
print("Tap To Earn Autoclick for pepememe.io")
for i in range(10, 0, -1):
    print(f"d {i} ...")
    time.sleep(1)

print("Début du programme.")

# Boucle infinie
while True:
   # print(f"Boucle  {session + 1}")

    # Répète 6 sessions de clics
    for session in range(7):
        print(f"--- Session {session + 1} ---")
        
        # 200 clics dans cette session
        for click in range(1, 101):
            pyautogui.click(319, 813)# use coordonate
            time.sleep(0.1)  # Pause de 0.1 seconde entre les clics
            if click % 10 == 0:  # Afficher la progression tous les 10 clics
                print(f"Clic {click}/100")
        
        print(f"Session {session + 1} terminée.")
        
        # Pause de 4 minutes entre les sessions
        if session < 2:  # Pas de pause après la dernière session
            print("Pause ")
            for remaining in range(30, 0, -1):
                if remaining % 10 == 0 or remaining <= 5:  # Afficher toutes les 10 secondes et les 5 dernières secondes
                    print(f" {remaining} s")
                time.sleep(1)
    print("Préparation...")
    winsound.Beep(200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(1200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(440, 200)
    print("Boucle FINITO")
     
    # Pause de 5 minutes après les 3 sessions avant de recommencer
    print("Pause de 300s")
    for remaining in range(300, 0, -1):  # 5 minutes = 300 secondes
        if remaining % 10 == 0 or remaining <= 5:  # Afficher toutes les 10 secondes et les 5 dernières secondes
            print(f" {remaining} ...")
        time.sleep(1)

print("Programme terminé.")  # Ne sera jamais atteint sauf si interrompu manuellement

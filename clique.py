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
print("Lancement du programme dans 10 secondes...")
for i in range(10, 0, -1):
    print(f"Début dans {i} seconde(s)...")
    time.sleep(1)

print("Début du programme.")

# Boucle infinie
while True:
    print("--- Nouvelle boucle ---")

    # Répète 6 sessions de clics
    for session in range(6):
        print(f"--- Début de la session {session + 1} ---")
        
        # 200 clics dans cette session
        for click in range(1, 101):
            pyautogui.click(1000, 800)
            time.sleep(0.1)  # Pause de 0.1 seconde entre les clics
            if click % 10 == 0:  # Afficher la progression tous les 10 clics
                print(f"Clic {click}/100 effectué.")
        
        print(f"Session {session + 1} terminée. 100 clics effectués.")
        
        # Pause de 4 minutes entre les sessions
        if session < 2:  # Pas de pause après la dernière session
            print("Pause ")
            for remaining in range(30, 0, -1):
                if remaining % 10 == 0 or remaining <= 5:  # Afficher toutes les 10 secondes et les 5 dernières secondes
                    print(f"Reprise dans {remaining} seconde(s)...")
                time.sleep(1)
    print("Préparation pour une nouvelle boucle. Son d'alerte...")
    winsound.Beep(200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(1200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(440, 200)
    # Pause de 5 minutes après les 3 sessions avant de recommencer
    print("Pause de 5 minutes avant de relancer les 4 sessions...")
    for remaining in range(300, 0, -1):  # 5 minutes = 300 secondes
        if remaining % 10 == 0 or remaining <= 5:  # Afficher toutes les 10 secondes et les 5 dernières secondes
            print(f"Redémarrage dans {remaining} seconde(s)...")
        time.sleep(1)

print("Programme terminé.")  # Ne sera jamais atteint sauf si interrompu manuellement

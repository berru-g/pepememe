import ctypes
import pyautogui
import time
import winsound


kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 1 
hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)

print("Tap To 🪙 Autoclick for pepememe.io")
for i in range(10, 0, -1):
    print(f" {i} ")
    time.sleep(1)

print("Autoclick faster than my grandMa who has Parkinson ! ")

while True:

    for session in range(7):
        print(f"🐸 Session {session + 1} ")
        
        for click in range(1, 101):
            pyautogui.click(319, 813)# use coordonate
            time.sleep(0.1)  
            if click % 10 == 0: 
                print(f"Clic {click}/100")
        
        print(f"✅ {session + 1} ")
        
        # Pause de 4 minutes entre les sessions
        if session < 2:  # Pas de pause après la dernière session
            print("⏸️ ")
            for remaining in range(30, 0, -1):
                if remaining % 10 == 0 or remaining <= 5:  
                    print(f" {remaining} ")
                time.sleep(1)
    print("⚙️ 🔁")
    winsound.Beep(200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(1200, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(440, 200)
     
    print("Rechargement...")
    for remaining in range(300, 0, -1):  # 5 minutes = 300 secondes
        if remaining % 10 == 0 or remaining <= 5:  # Afficher toutes les 10 secondes et les 5 dernières secondes
            print(f" {remaining} ")
        time.sleep(1)

print("Programme terminé.")  # Ne sera jamais atteint sauf si interrompu manuellement

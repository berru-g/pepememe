import pyautogui

# Afficher les coordonnées X et Y de la souris en temps réel
def display_mouse_coordinates():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Coordonnées X : {x}, Coordonnées Y : {y}", end="\r")
    except KeyboardInterrupt:
        print("\nArrêt de l'affichage des coordonnées de la souris.")

# Exécution du script
if __name__ == "__main__":
    display_mouse_coordinates()

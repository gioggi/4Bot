import pyautogui
import time
from config import TASTO_ABILITA, TASTO_CURA

def attacca():
    """Esegue una sequenza di attacchi."""
    for tasto in TASTO_ABILITA:
        pyautogui.press(tasto)
        time.sleep(0.5)

def cura():
    """Usa una pozione se necessario."""
    pyautogui.press(TASTO_CURA)

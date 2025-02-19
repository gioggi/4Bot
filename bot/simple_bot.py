import pydirectinput  # Alternativa a PyAutoGUI per DirectX
import time
import threading
import tkinter as tk
import mss
import numpy as np
import cv2

running = False  # Variabile per controllare lo stato del bot

def cattura_schermo():
    """Cattura lo schermo anche con giochi DirectX."""
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Se hai più monitor, scegli quello giusto
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)  # Converti in scala di grigi

def bot_loop():
    global running
    last_f7_time = time.time()

    while running:
        pydirectinput.press("tab")  # Cambia target
        time.sleep(0.2)
        pydirectinput.press("2")  # Attacco

        if time.time() - last_f7_time >= 18:
            pydirectinput.press("f7")
            print("F7 premuto!")
            pydirectinput.press("9")
            print("9 premuto!")
            last_f7_time = time.time()

        time.sleep(2)

def start_bot():
    global running
    if not running:
        running = True
        threading.Thread(target=bot_loop, daemon=True).start()
        status_label.config(text="Bot ATTIVO", fg="green")

def stop_bot():
    global running
    running = False
    status_label.config(text="Bot FERMO", fg="red")

# Creiamo la finestra GUI
root = tk.Tk()
root.title("Bot 4Story")
root.geometry("250x150")

status_label = tk.Label(root, text="Bot FERMO", fg="red", font=("Arial", 12))
status_label.pack(pady=10)

start_button = tk.Button(root, text="Avvia Bot", command=start_bot, font=("Arial", 12))
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Ferma Bot", command=stop_bot, font=("Arial", 12))
stop_button.pack(pady=5)

root.mainloop()

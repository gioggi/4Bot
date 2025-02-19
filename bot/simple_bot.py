import pyautogui
import time
import threading
import tkinter as tk

running = False  # Variabile per controllare lo stato del bot

def bot_loop():
    global running
    last_f7_time = time.time()

    while running:
        pyautogui.press("tab")
        time.sleep(0.2)
        pyautogui.press("2")

        if time.time() - last_f7_time >= 18:
            pyautogui.press("f7")
            print("F7 premuto!")
            pyautogui.press("7")
            print("7 premuto!")
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

# Creiamo la finestra
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

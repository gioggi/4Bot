import time
import threading
import tkinter as tk
import keyboard  # Migliore per DirectX 12 rispetto a PyDirectInput

running = False

def bot_loop():
    global running
    last_f7_time = time.time()

    while running:
        keyboard.press_and_release("tab")  # Cambia target
        time.sleep(0.2)
        keyboard.press_and_release("2")  # Attacco

        if time.time() - last_f7_time >= 18:
            keyboard.press_and_release("f7")
            print("F7 premuto!")
            keyboard.press_and_release("7")
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

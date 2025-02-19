import time
from actions import attacca, cura
from vision import find_enemy, life_check

def main():
    while True:
        if find_enemy():
            print("Nemico trovato! Attacco in corso...")
            attacca()
            life_check()
        else:
            print("Nessun nemico, riprovo...")
        time.sleep(2)

if __name__ == "__main__":
    print("Avvio del bot...")
    time.sleep(3)
    main()

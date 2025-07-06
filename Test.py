# ordner_logic.py

Zahlen = []
Woerter = []

def sortiere_text(eingabe):
    teile = eingabe.strip().split()
    
    for teil in teile:
        if teil.isdigit():
            Zahlen.append(int(teil))
        else:
            Woerter.append(teil)

def get_ergebnisse():
    return Zahlen, Woerter

def reset():
    Zahlen.clear()
    Woerter.clear()



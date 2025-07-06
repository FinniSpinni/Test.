Zahlen = []
Woerter = []

def main():
    while True:
        eingabe = input("Gib Wörter und/oder Zahlen ein (oder 'exit' zum Beenden): ").strip()

        if eingabe.lower() == "exit":
            print("\nZahlen:", Zahlen)
            print("Wörter:", Woerter)
            break  # Beende die Schleife

        # Teile die Eingabe in einzelne Wörter/Zahlen
        teile = eingabe.split()

        for teil in teile:
            if teil.isdigit():
                Zahlen.append(int(teil))
            else:
                Woerter.append(teil)

        print("✅ Aktueller Stand:")
        print("Zahlen:", Zahlen)
        print("Wörter:", Woerter)

main()

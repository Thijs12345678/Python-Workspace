import random

def toon_lucifers(aantal):
    print("\nLucifers over: " + str(aantal))
    print("|" * aantal)
    print()

def computer_keuze(aantal):
    # Slimme strategie: probeer de tegenstander in een verliezende positie te brengen
    # Als (aantal - keuze) % 4 == 0, verliest de tegenstander
    for k in [1, 2, 3]:
        if (aantal - k) % 4 == 0:
            return k
    return random.randint(1, min(3, aantal))

def speel_spel():
    print("=" * 40)
    print("   LUCIFERSPEL")
    print("=" * 40)
    print("Regels:")
    print("- Er liggen 21 lucifers op tafel.")
    print("- Jij en de computer spelen om de beurt.")
    print("- Je mag 1, 2 of 3 lucifers pakken.")
    print("- Wie de LAATSTE lucifer pakt, VERLIEST.")
    print("=" * 40)

    lucifers = 21
    speler_aan_beurt = True  # True = jij, False = computer

    while lucifers > 0:
        toon_lucifers(lucifers)

        if speler_aan_beurt:
            # Speler is aan de beurt
            while True:
                try:
                    keuze = int(input("Hoeveel lucifers pak jij? (1, 2 of 3): "))
                    if keuze < 1 or keuze > 3:
                        print("Kies 1, 2 of 3!")
                    elif keuze > lucifers:
                        print("Er liggen maar " + str(lucifers) + " lucifers!")
                    else:
                        break
                except ValueError:
                    print("Voer een getal in.")

            lucifers -= keuze
            print("Jij pakt " + str(keuze) + " lucifer(s).")

            if lucifers == 0:
                print("\nJij pakte de laatste lucifer. Jij verliest!")
                print("De computer wint. Volgende keer beter!")
                return

        else:
            # Computer is aan de beurt
            keuze = computer_keuze(lucifers)
            lucifers -= keuze
            print("De computer pakt " + str(keuze) + " lucifer(s).")

            if lucifers == 0:
                print("\nDe computer pakte de laatste lucifer.")
                print("Jij wint! Gefeliciteerd!")
                return

        speler_aan_beurt = not speler_aan_beurt

# Start het spel
while True:
    speel_spel()
    print()
    opnieuw = input("Nog een keer spelen? (ja/nee): ").strip().lower()
    if opnieuw != "ja":
        print("Tot de volgende keer!")
        break

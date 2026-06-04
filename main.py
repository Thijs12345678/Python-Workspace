import random

lucifers = random.randint(20, 45)

def Speler():
    global lucifers
    print("Er zijn nog", lucifers, "lucifers over")
    pakken = int(input("Hoeveel lucifers wil je pakken? "))
    if pakken > 0 and pakken <= 3:
        print("Je hebt", pakken, "lucifers gepakt")
        lucifers = lucifers - pakken
        print("Er zijn nog", lucifers, "lucifers over")
        if lucifers <= 0:
            print("Jij pakte de laatste lucifer. Jij verliest!")
        else:
            Anderespeler()
    else:
        print("Kies 1, 2 of 3!")
        Speler()

def Anderespeler():
    global lucifers
    print("Er zijn nog", lucifers, "lucifers over")
    pakken = random.randint(1, min(3, lucifers))
    print("De computer heeft", pakken, "lucifers gepakt")
    lucifers = lucifers - pakken
    print("Er zijn nog", lucifers, "lucifers over")
    if lucifers <= 0:
        print("De computer pakte de laatste lucifer. Jij wint!")
    else:
        Speler()

Speler()

import random

lucifers = random.randint(20, 25)

def Speler():
    global lucifers
    while lucifers > 0:
        print("Er zijn nog", lucifers, "lucifers over")
        pakken = int(input("Hoeveel lucifers wil je pakken? "))
        if pakken > 0 and pakken <= 3:
            print("Je hebt", pakken, "lucifers gepakt")
            lucifers = lucifers - pakken
            print("Er zijn nog", lucifers, "lucifers over")
            if lucifers <= 0:
                print("Jij pakte de laatste lucifer. Jij verliest!")
            else:
                computer()
            return
        else:
            print("Kies 1, 2 of 3!")

def computer():
    global lucifers
    print("Er zijn nog", lucifers, "lucifers over")
    if lucifers > 4:
        pakken = random.randint(1, 3)
    elif lucifers == 4:
        pakken = 3
    elif lucifers == 3:
        pakken = 2
    elif lucifers == 2:
        pakken = 1
    elif lucifers == 1:
        pakken = 1
    print("De computer heeft", pakken, "lucifers gepakt")
    lucifers = lucifers - pakken
    print("Er zijn nog", lucifers, "lucifers over")
    if lucifers <= 0:
        print("De computer pakte de laatste lucifer. Jij wint!")
    else:
        Speler()

Speler()

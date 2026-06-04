def Speler
  lucifers = random(25) + 20

while lucifers > 0:
  print("Er zijn nog", lucifers, "lucifers over")
  pakken = str(input( "Hoeveel lucifers wil je pakken"))
  if pakken >0 and pakken <= 3:
    print("Je hebt" pakken "lucifers gepakt")
  lucifers = lucifers - pakken
    print("Er zijn nog" lucifers "lucifers over")
    beurt = computer

def computer
  print("Er zijn nog" lucifers "lucifers over")
  pakken = random(3) + 1
  print("De computer heeft" pakken "lucifers gepakt")
  lucifers = lucifers - pakken
  print("Er zijn nog" lucifers "lucifers over")
  if lucifers <= 0:
    print("De Speler heeft gewonnen")
  else : 
     beurt = Speler
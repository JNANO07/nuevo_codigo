contrincante_pikachu=input("contra quien quieres peliar?(charma/squir/bulba)")

charma=("charma")
squir=("squir")
bulba=("bulba")
vida_pokemon=0
ataque_poquemon=0

if contrincante_pikachu== charma:
    vida_pokemon=120
    ataque_poquemon= 10
    vida_picachu=100

elif contrincante_pikachu== squir:
    vida_pokemon=100
    ataque_poquemon= 12
    vida_picachu = 100

elif contrincante_pikachu== bulba:
    vida_pokemon=95
    ataque_poquemon= 11
    vida_picachu = 100

while vida_pokemon >0 and vida_picachu>0:

    ataque_picachu=input("que ataque quieres hacer (impact / mirada furiosa)")
    if ataque_picachu==("impact"):
        vida_pokemon-=15
        print("el enemigo perdio 15 de salud")

    elif ataque_picachu==("mirada furiosa"):
        vida_pokemon-=20
        print("el enemigo perdio 20 de salud")

    if contrincante_pikachu == charma:
        vida_picachu-=10

    elif contrincante_pikachu == squir:
        vida_picachu -= 10

    elif contrincante_pikachu == bulba:
        vida_picachu -= 11

    print("el enemigo ahora tiene {} de vida".format(vida_pokemon))

    print("resiciviste un ataque de {} de daño".format(ataque_poquemon))
    print("ahora tu vida es de {}". format(vida_picachu -ataque_poquemon))

if vida_picachu>0:
    print("felicidades ganaste")
elif vida_pokemon>0:
   print("perdiste")
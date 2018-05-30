numero_ganador =7
advina_el_numero = int(input("adivine un numero del 1 al 10"))
if numero_ganador==advina_el_numero:
    print("¡ganaste!")
else:
    advina_el_numero = int(input("adivine un numero del 1 al 10"))
    if numero_ganador == advina_el_numero:
        print("¡ganaste!")
    else:
        advina_el_numero = int(input("adivine un numero del 1 al 10"))
        if numero_ganador == advina_el_numero:
            print("¡ganaste!")
        else:
            advina_el_numero = int(input("adivine un numero del 1 al 10"))
            if numero_ganador == advina_el_numero:
                print("¡ganaste!")
            else:
                advina_el_numero = int(input("adivine un numero del 1 al 10"))
                if numero_ganador == advina_el_numero:
                    print("¡ganaste!")
                else:
                    print("perdiste")
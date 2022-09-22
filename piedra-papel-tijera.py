import random

juegos = int(input("Ingrese la cantidad de veces que desea jugar:\n"))

ganador1 = 0
ganador2 = 0

for i in range(juegos):
    usuario = input("Ingresa tu jugada: 'piedra', 'papel' o 'tijera'\n").lower()
    computador = random.choice(["piedra","papel","tijera"])
    print(f"El computador escogió '{computador}'")
    if usuario == computador:
        print("No hay punto")
    elif ((usuario == "piedra" and computador == "tijera")
        or (usuario == "tijera" and computador == "papel")
        or (usuario == "papel" and computador == "piedra")):
        print("Punto para ti")
        ganador1 += 1
    else:
        print("Punto para el computador")
        ganador2 += 1

if ganador1 == ganador2:
    print("Es un empate. Ronda a muerte súbita:")
    while ganador1 == ganador2:
        usuario = input("Ingresa tu jugada: 'piedra', 'papel' o 'tijera'\n").lower()
        computador = random.choice(["piedra","papel","tijera"])
        print(f"El computador escogió '{computador}'")
        if usuario == computador:
            print("No hay punto")
        elif ((usuario == "piedra" and computador == "tijera")
            or (usuario == "tijera" and computador == "papel")
            or (usuario == "papel" and computador == "piedra")):
            print("Punto para ti")
            ganador1 += 1
        else:
            print("Punto para el computador")
            ganador2 += 1

if ganador1 > ganador2:
    print(f"¡Ganaste! Marcador final: {ganador1} a {ganador2}")

else:
    print(f"¡Perdiste! Marcador final: {ganador2} a {ganador1}")

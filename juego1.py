#funcion spock
def spock(item_enemigo):
    if item_enemigo == 'tijera':
        print('Spock destruye tijera')
        print('Ganaste!')
    elif item_enemigo == 'papel':
        print('Papel desaprueba a Spock')
        print('Perdiste')
    elif item_enemigo == 'piedra':
        print('Spock vaporiza piedra')
        print('Ganaste!')
    elif item_enemigo == 'lagarto':
        print('Lagarto envenena a Spock')
        print('Perdiste')

def tijera(item_enemigo):
    if item_enemigo == 'spock':
        print('Spock destruye tijera')
        print('Perdiste')
    elif item_enemigo == 'papel':
        print('Tijera corta papel')
        print('Ganaste!')
    elif item_enemigo == 'piedra':
        print('Piedra rompe tijera')
        print('Perdiste')
    elif item_enemigo == 'lagarto':
        print('Tijera decapita lagarto')
        print('Ganaste!')


# funciones flo 
# aclaración para mi: item_enemigo es el del compu, no el input!

def lagarto(item_enemigo):
    if item_enemigo == "piedra":
        print("Piedra aplasta lagarto")
        print("Perdiste")

    elif item_enemigo == "papel":
        print("Lagarto come papel")
        print("Ganaste!")

    elif item_enemigo == "tijera":
        print("Tijera decapita lagarto")
        print("Perdiste")

    elif item_enemigo == "spock":
        print("Lagarto envenena a spock")
        print("Ganaste!")


def piedra(item_enemigo):
    if item_enemigo == "tijera":
        print("Piedra rompe tijera")
        print("Ganaste!")

    elif item_enemigo == "papel":
        print("Papel cubre piedra")
        print("Perdiste")

    elif item_enemigo == "spock":
        print("Spock vaporiza piedra")
        print("Perdiste")

    elif item_enemigo == "lagarto":
        print("Piedra aplasta lagarto")
        print("Ganaste!")

def papel(item_enemigo):
    if item_enemigo == "piedra":
        print("Papel cubre piedra")
        print("Ganaste!")

    elif item_enemigo == "tijera":
        print("Tijera corta papel")
        print("Perdiste")

    elif item_enemigo == "spock":
        print('Papel desaprueba a Spock')
        print("Ganaste!")

    elif item_enemigo == "lagarto":
        print("Lagarto come papel")
        print("Perdiste")

import random as r

print('Inicia Juego!!')

mano_jugador = input('Escoge: piedra, papel, tijera, lagarto o spock: ')

opciones = ['piedra', 'papel', 'tijera', 'lagarto','spock']

while mano_jugador.lower() not in opciones:
    mano_jugador = input('Escoge: piedra, papel, tijera, lagarto o spock')

mano_jugador = mano_jugador.lower()

enemigo = r.choice(opciones)

if enemigo == mano_jugador:
    print('Empate!')
elif mano_jugador == 'piedra':
    piedra(enemigo)
elif mano_jugador == 'papel':
    papel(enemigo)
elif mano_jugador == 'tijera':
    tijera(enemigo)
elif mano_jugador == 'lagarto':
    lagarto(enemigo)
else:
    spock(enemigo)
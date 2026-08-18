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

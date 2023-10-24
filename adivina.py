# Se importa rendit desde la biblioteca random
from random import randint

# Se crea la variable que guardara el nombre del usuario
nombre = input('- Ingresa tu nombre: ')
# El número elegido será de manera aleatoria entre 1 y 10
numero = randint(1,10)
# Determinamos si el número aleatorio que ha salido es par o impar
if(numero % 2 == 0):
    pista = "par"
else:
    pista = 'impar'
# Cuenta con una cantidad definida de intentos para adivinar
intentos = 3

# Le preguntamos al usuario si quiere comenzar el juego
jugar = input(f"""- Hola {nombre}.
- Estoy pensando en un número entre el 1 y el 10
- ¿Te animas a jugar? si/no: """).strip().lower()
# Se crea un bucle en caso de que el usuario responda algo distinto a si/no
while jugar not in ["si", "no"]:
    print("- Necesito que respondas SI quieres jugar o NO")
    jugar = input(f"- {nombre}, Quieres jugar? si/no ")

if(jugar == "si"):
    print(numero)
    while intentos > 0:
        # Se le pide al jugador que adivine el número
        numero_jugador = int(input('- Entre los números 1 y 10. Cuál crees que tengo?: '))
        # Se crea una condicional en caso de que el usuario escoja un número distinto a los solicitados
        if(numero_jugador > 10 or numero_jugador < 1):
            print(f"- {nombre}, solo se permite un número entre 1 y 10")
        # En caso de ser mayor o menor al número de la computadora, nos proporciona pistas
        elif(numero_jugador < numero):
            intentos -= 1
            print(f"""- Incorrecto!!, intenta una vez más!
- (pista 1): El número que has escogido es menor.
- (Pista 2): El número que tengo es {pista}
- Intentos restantes: {intentos}""")
        elif(numero_jugador > numero):
            intentos -= 1
            print(f"""- Incorrecto!!, intenta una vez más!
- (Pista 1): El número que has escogido es mayor. 
- (Pista 2): El número que tengo es {pista}
- Intentos restantes: {intentos}""")
        # En caso de acertar, nos felicita
        else:
            print(f"- Felicitaciones {nombre}!!, has acertado el número!!!")
            break
    # En caso de quedar sin intentos nos da un aviso y nos revela el número que tenía
    if(intentos == 0):
        print(f"""- {nombre}, te has quedado sin intentos!
- El número que tenía era el {numero}""")
    # Si aún quedan intentos, despues de contestar nos avisa cuantos nos quedan
    else:
        print(f"---> Tus intentos restantes: {intentos - 1} <---")
# En caso de no querer jugar, el programa termina
else:
    print("- Qué pena, vuelve luego")
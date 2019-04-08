import colorsys
tabla = ["-","-","-",
        "-","-","-",
        "-","-","-"]

juego_activo = True
ganador = None
jugador_activo = "X"
xi = input("Ingrese el nombre del jugador 1: \n")
yi = input("Ingrese el nombre del jugador 2: \n")

def mostratrabla():
    print(tabla[0] + " | " + tabla[1] + " | " + tabla[2])
    print(tabla[3] + " | " + tabla[4] + " | " + tabla[5])
    print(tabla[6] + " | " + tabla[7] + " | " + tabla[8])

def jugar():
    #mostrar la tabla
    mostratrabla()
    global x
    global y 

    while juego_activo:
        turnos(jugador_activo)

        revision_game_over()

        cambio_turno()
        
        
    if ganador == 'X' or ganador == 'O':
        print(ganador + " ganó")
    elif ganador == None:
        print("Empate")

def jugar_misere():
    #mostrar la tabla
    mostratrabla()

    while juego_activo:
        turnos(jugador_activo)

        revision_game_over()

        cambio_turno()
        
    
    if ganador == 'X' or ganador == 'O':
        print(ganador + "perdió, el oponente logró que juntara 3")
    elif ganador == None:
        print("Empate")
        
        








    
def turnos(jugador):
    print(jugador + " turno")
    pos = input(" eliga una posicion de 1 - 9: ")
    # le resto 1 a la posicion porque va de 0 a 8 pero para que sea más facil de visualizar va de 1 a 9
    valid = False
    #este while verifica si el input está en rango, verifica si el espacio está vacio y si lo está, cambia a true y sale del loop 
    while not valid:

        while pos not in ["1" , "2", "3" , "4", "5" , "6", "7" , "8", "9"]:
            pos = input("Input inválido, ingrese un número (1-9)")


        pos = int(pos) - 1

        if tabla[pos] == "-":
            valid = True
        else:
            print("El espacio ya está ocupado, intente de nuevo")
            

    tabla[pos]= jugador

    mostratrabla()


def revision_game_over():
    check_if_ganador()
    check_if_empate()

def check_if_ganador():

    global ganador
    #chequear filas
    ganadorfila = revisar_filas()
    #chequear columnas
    ganadorcolumna = revisar_columnas()
    #chequear diagonales 
    ganadordiagonal = revisar_diagonales()

    if ganadorfila:
        ganador = ganadorfila

    elif ganadorcolumna:
        ganador = ganadorcolumna

    elif ganadordiagonal:
        ganador = ganadordiagonal

    else:
        ganador = None
    

        

    return

def revisar_filas():
    global juego_activo

    fila_1 = tabla[0] == tabla[1] == tabla[2] != "-"
    fila_2 = tabla[3] == tabla[4] == tabla[5] != "-"
    fila_3 = tabla[6] == tabla[7] == tabla[8] != "-"
    if fila_1 or fila_2 or fila_3:
        juego_activo = False
    if fila_1:
        return tabla[0]
    elif fila_2:
        return tabla[3]
    elif fila_3:
        return tabla[6]



    return

def revisar_columnas():
    global juego_activo

    columna_1 = tabla[0] == tabla[3] == tabla[6] != "-"
    columna_2 = tabla[1] == tabla[4] == tabla[7] != "-"
    columna_3 = tabla[2] == tabla[5] == tabla[8] != "-"
    if columna_1 or columna_2 or columna_3:
        juego_activo = False
    if columna_1:
        return tabla[0]
    elif columna_2:
        return tabla[1]
    elif columna_3:
        return tabla[2]



    return

def revisar_diagonales():
    global juego_activo
    diagonal_1 = tabla[0] == tabla[4] == tabla[8] != "-"
    diagonal_2 = tabla[6] == tabla[4] == tabla[2] != "-"
    if diagonal_1 or diagonal_2:
        juego_activo = False
    if diagonal_1:
        return tabla[0]
    elif diagonal_2:
        return tabla[6]

   
    
    
    return




def check_if_empate():
    global juego_activo
    #revisa si hay un "-" en el tablero y si lo hay significa que aun no está la tabla llena y no puede haber empate
    if "-" not in tabla:
        juego_activo = False

    return

def cambio_turno():

    global jugador_activo
    #verifiacion si son iguales '=='
    #asignacion '='
    if jugador_activo == 'X':
        jugador_activo = 'O'

    elif jugador_activo == 'O':
        jugador_activo = 'X'
    
    
    return


print("Bienvenido a Totito!")
x = int(input("Qué modo de juego desea jugar? \n(1)Modo jugador vs jugador: \n(2) Modo jugador vs jugador misere:  \n(3)Modo jugador vs computadora: \n"))

if x == 1:
   
    print(xi + " será X")
    print(yi + " será O")
    jugar()

elif x == 2:
    print("El objetivo de este modo de juego es lograr que el oponente junte 3 en fila,columna o en diagonal, suerte ;) !")
    jugar_misere()
    

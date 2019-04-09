import colorama
from colorama import Fore,Back , Style
from colorama import init
import random

import os
init()
os.system("color 05")

tabla = ["-","-","-",
        "-","-","-",
        "-","-","-"]

#lista de nombres para la computadora, se asignan de manera aleatoria con un random
compu_nombre1 = "Perry el ornitorrinco"
compu_nombre2 = "Aquiles Brinco"
compu_nombre3 = "Nori Navas"
compu_nombre4 = "Aquiles Pinto"
compu_nombre5 = "Alan Brito"
compu_nombre6 = "Elvis Cocho"
compu_nombre7 = "Elsa Pito"
compu_nombre8 = "Bad Bunny"
compu_nombre9 = "Soila Lechuga de la Torre"
compu_nombre10 = "Esvin Disel"

#cuando lo cambio a false se acaba el juego
juego_activo = True
ganador = None
#El jugador 1 siempre será X
jugador_activo = "X"

x = random.randint(1,10)
if x == 1 :
    compu_nombre = compu_nombre1
elif x == 2:
    compu_nombre = compu_nombre2
elif x == 3:
    compu_nombre = compu_nombre3
elif x == 4:
    compu_nombre = compu_nombre4
elif x == 5:
    compu_nombre = compu_nombre5
elif x == 6:
    compu_nombre = compu_nombre6
elif x == 7:
    compu_nombre = compu_nombre7
elif x == 8:
    compu_nombre = compu_nombre8
elif x == 9:
    compu_nombre = compu_nombre9
elif x == 10:
    compu_nombre = compu_nombre10


def mostratrabla():
    print(tabla[0] + " | " + tabla[1] + " | " + tabla[2])
    print(tabla[3] + " | " + tabla[4] + " | " + tabla[5])
    print(tabla[6] + " | " + tabla[7] + " | " + tabla[8])

def jugar():
    #mostrar la tabla
    mostratrabla()
    global xi
    global yi 

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
    #aqui hago el algoritmo para jugar vs la computadora, va a revisar los espacios vacios y despues que X juegue se colocará O  en el primer lugar que encuentre
    if jugador == 'O' and x == 3:
        for i in range(1, len(tabla)-1):
            if tabla[i] == "-":
                tabla[i] = 'O'
                break
    else:            
        pos = input(Fore.LIGHTBLUE_EX +  " eliga una posicion de 1 - 9: ")
        # le resto 1 a la posicion porque va de 0 a 8 pero para que sea más facil de visualizar va de 1 a 9
        valid = False
        #este while verifica si el input está en rango, verifica si el espacio está vacio y si lo está, cambia a true y sale del loop 
        while not valid:

            while pos not in ["1" , "2", "3" , "4", "5" , "6", "7" , "8", "9"]:
                pos = input("Input inválido, ingrese un número (1-9)")


            pos = int(pos) - 1

            if tabla[pos] == "-":
                valid = True
                tabla[pos] = jugador
            else:
                print("El espacio ya está ocupado, intente de nuevo")
            

    mostratrabla()

def jugar_compu():
    mostratrabla()
    global xi
    global yi


    while juego_activo:
        jugador_activo = 'X'
        turnos(jugador_activo)
        jugador_activo = 'O'
        turnos(jugador_activo)
      #  cambio_turno_compu(tabla)

        revision_game_over()

              
    if ganador == 'X' or ganador == 'O':
        print(ganador + " ganó")
    elif ganador == None:
        print("Empate")


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


print(Fore.LIGHTGREEN_EX + "Bienvenido a Totito!")
print(Fore.LIGHTGREEN_EX + "Tres modos de juego")
print()
print()
x = int(input( Fore.CYAN + "Qué modo de juego desea jugar? \n(1)Modo jugador vs jugador: \n(2) Modo jugador vs jugador misere:  \n(3)Modo jugador vs computadora: \n"))

if x == 1:
    xi = input(Fore.MAGENTA +  "Ingrese el nombre del jugador 1: \n")
    yi = input(Fore.YELLOW  + "Ingrese el nombre del jugador 2: \n")
   
    print(xi +   " será X")
    print(yi +  " será O")
    jugar()

elif x == 2:
    xi = input(Fore.MAGENTA +  "Ingrese el nombre del jugador 1: \n")
    yi = input(Fore.YELLOW  + "Ingrese el nombre del jugador 2: \n")
    print("El objetivo de este modo de juego es lograr que el oponente junte 3 en fila,columna o en diagonal, suerte ;) !")
    print(xi + " será X")
    print(yi + " será O")
    jugar_misere()

elif x == 3:
    xi = input(Fore.MAGENTA +  "Ingrese el nombre del jugador 1: \n")
    print(xi + " será X")
    print(Fore.WHITE +  compu_nombre + " Será O")
    jugar_compu()
   
    

    




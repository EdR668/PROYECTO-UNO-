import random as rd
import copy as cp
import os

arreglo_guardado = []

def inicializar_arguar():
    if len(arreglo_guardado)!=0:
        for i in range(0,len(arreglo_guardado)):
            arreglo_guardado.pop(0)

def gen_baraja_base ():
    baraja_base = []
    for i in range(0,14):
        if i<=9: baraja_base.append('N'+chr(i+48))
        elif i==10: baraja_base.append("EB")
        elif i==11: baraja_base.append("S2")
        elif i ==12: baraja_base.append("S4")
        elif i == 13: baraja_base.append("CC")
    return baraja_base

def matriz_baraja(baraja_base):
    matriz = [[] for i in range (0,4)]
    for i in range(0,4):
        for j in range(len(baraja_base)):
            if j>11: matriz[i].append('C'+baraja_base[j])
            else:
                if i==0: matriz[i].append('R'+baraja_base[j])
                elif i==1: matriz[i].append('G'+baraja_base[j])
                elif i==2: matriz[i].append('B'+baraja_base[j])
                elif i==3: matriz[i].append('Y'+baraja_base[j])
    return matriz

def imprimir_barajamatriz(matriz):
    print('\n')
    for i in range(len(matriz)):
        line = ''
        for j in matriz[i]:
            line+=(j+' ')
        print(line)


def verificar_repetidas(carta):
    contadormas4 = 4
    contadorcc=4
    for i in arreglo_guardado:
        if i==carta and carta=='CS4' and contadormas4!=0: contadormas4-=1
        if i==carta and carta=='CCC'and contadorcc!=0: contadorcc-=1
        if contadorcc==0 or contadormas4==0: return False
        if i==carta: return False
    return True

def ingresar_repeticiones(carta,verificador):
    if verificador: arreglo_guardado.append(carta)

def gen_mazo():
    mazo = []
    i=0
    while i<=6:
        j = rd.randrange(0,14)
        m = rd.randrange(0,4)
        if verificar_repetidas(baraja_completa[m][j]):
            ingresar_repeticiones(baraja_completa[m][j], verificar_repetidas(baraja_completa[m][j]))
            mazo.append(baraja_completa[m][j])
            i+=1
    return mazo

def actualizar_mazo(mazo,carta):
    if len(carta)==3:
        for i in mazo:
            if i==carta:
                mazo.remove(i)
                break
        return mazo
    else:
        for i in mazo:
            if i==carta[0]:
                mazo.remove(i)
                break
        return mazo

def imprimir_mazo(mazo):
    string = ''
    for i in range(len(mazo)):
        string+=('Carta '+str(i+1)+' = '+mazo[i]+'      ')
    return string

def primera_carta():
    while True:
        j = rd.randrange(0,10)
        m = rd.randrange(0,4)
        if verificar_repetidas(baraja_completa[m][j]):
            ingresar_repeticiones(baraja_completa[m][j], verificar_repetidas(baraja_completa[m][j]))
            return baraja_completa[m][j]

def verificar_juego(carta_poner, carta_juego):
    if len(carta_juego)==3:
        if carta_poner[0]=='C' or (carta_juego[2]==carta_poner[2] and carta_juego[1]==carta_poner[1])or carta_juego[0]==carta_poner[0]: return True
    else:
        if carta_poner[0]=='C' or carta_poner[0]==carta_juego[1]: return True
    return False

def juego_jugador(mazo_jugador, cartas_en_juego):
    print('Tus cartas: ',imprimir_mazo(mazo_jugador))
    k = input('Ingrese la carta que desea jugar (Si no pude jugar ninguna y desea pescar ingrese P): ')
    if k=='P': return 'NHPJ'
    n = int(k)
    if n>=1 and n<=len(mazo_jugador):
        carta=mazo_jugador[n-1]
        if verificar_juego(carta, cartas_en_juego[len(cartas_en_juego)-1]):
            if carta[0]=='C':
                cc=str(input('Ingrese el color al que desea cambiar (Rojo = R // Verde = G // Azul = B // Amarillo = Y): '))
                if cc=='R' or cc=='G' or cc=='B' or cc=='Y': return carta,cc
            else:
                return carta
    print('Elección incorrecta o jugada inválida')
    return juego_jugador(mazo_jugador, cartas_en_juego)
            
def juego_maquina (mazo_maquina, cartas_en_juego):
    for i in mazo_maquina:
        if verificar_juego(i, cartas_en_juego[len(cartas_en_juego)-1]):
            carta = i
            colores = [0,0,0,0]
            for j in mazo_maquina:
                if j[0]=='R': colores[0]+=1
                if j[0]=='G': colores[1]+=1
                if j[0]=='B': colores[2]+=1
                if j[0]=='Y': colores[3]+=1
            if colores[0] == max(colores): color='R'
            if colores[1] == max(colores): color='G'
            if colores[2] == max(colores): color='B'
            if colores[3] == max(colores): color='Y'
            if carta[0]=='C': return carta,color
            return carta
    return 'NHPJ'

def pesca_mazo (mazo,cantidad_cartas):
    i=0
    while i<cantidad_cartas:
        j = rd.randrange(0,14)
        m = rd.randrange(0,4)
        if verificar_repetidas(baraja_completa[m][j]):
            ingresar_repeticiones(baraja_completa[m][j], verificar_repetidas(baraja_completa[m][j]))
            mazo.append(baraja_completa[m][j])
            i+=1
    return mazo

def carta_abs(carta):
    if len(carta)>=3:
        return carta
    return carta[0]

def reiniciar_tamano():
    if len(arreglo_guardado)==56:
        inicializar_arguar()

def juego(mazo_jugador, mazo_maquina, cartas_en_juego):
    carta_maquina = '...'
    carta_jugador = '...'
    k=1
    while len(mazo_jugador)!=0 and len(mazo_maquina)!=0:
        print('\n-----------ROUND',k,'--------------')
        #turno jugador
        reiniciar_tamano()
        print('Cantidad cartas de maquina: ', len(mazo_maquina))
        print('Carta en juego: ',cartas_en_juego[len(cartas_en_juego)-1])
        if carta_abs(cartas_en_juego[len(cartas_en_juego)-1])==carta_abs(carta_maquina) and (carta_abs(carta_maquina)[1]=='S' or carta_abs(carta_maquina)[1]=='E'):
            if carta_abs(carta_maquina)[2]!='B':
                pesca_mazo(mazo_jugador,ord(carta_abs(carta_maquina)[2])-48)
        else:
            carta_jugador = cp.copy(juego_jugador(mazo_jugador,cartas_en_juego))
            if carta_jugador!='NHPJ':
                cartas_en_juego.append(carta_jugador)
                actualizar_mazo(mazo_jugador, carta_jugador)
            else:
                pesca_mazo(mazo_jugador,1)
        #turno maquina
        reiniciar_tamano()
        if carta_abs(cartas_en_juego[len(cartas_en_juego)-1])==carta_abs(carta_jugador) and (carta_abs(carta_jugador)[1]=='S' or carta_abs(carta_jugador)[1]=='E'):
            if carta_abs(carta_jugador)[2]!='B':
                pesca_mazo(mazo_maquina,ord(carta_abs(carta_jugador)[2])-48)
        else:
            carta_maquina = cp.copy(juego_maquina(mazo_maquina,cartas_en_juego))
            if carta_maquina!='NHPJ':
                cartas_en_juego.append(carta_maquina)
                actualizar_mazo(mazo_maquina, carta_maquina)
            else:
                pesca_mazo(mazo_maquina,1)
        k+=1
    if len(mazo_jugador)==0: print('\nHas ganado la partida')
    else: print('\nHas pérdido la partida')

baraja_completa = matriz_baraja(gen_baraja_base())

def menu():
    print('\tBIENVENIDO A SU UNO PERSONAL\n\n1. Ver toda la baraja\n2. Ver las reglas de juego\n3. Jugar\n')
    inicializar_arguar()
    while True:
        n = int(input('Ingrese la opción a la que desea entrar: '))
        if n==1: 
            imprimir_barajamatriz(baraja_completa)
            break
        elif n==2:
            reglasjuego()
            break
        elif n==3:
            mazo_jugador = gen_mazo()
            mazo_maquina = gen_mazo()
            cartas_en_juego = [primera_carta()]
            juego(mazo_jugador,mazo_maquina,cartas_en_juego)
            break
        else:
            print('Opción incorrecta. Intentelo de nuevo: ')
    x=int(input('\n\nEl programa ha terminado. Ingrese 1 si quiere iniciarlo de nuevo o ingrese cualquier otro número para finalizar: '))
    if x==1:
        os.system('cls')
        menu()

def reglasjuego():
    print('\n\tREGLAS DE JUEGO\n\n')
    print('1. El juego inicia con la generación de un mazo inicial de 7 cartas tanto para la máquina (Tú oponente), como para el jugador')
    ejemplo = gen_mazo()
    print('\n',imprimir_mazo(ejemplo),'\n')
    print('2. De los string de cada carta. Estos representan el color, tipo de carta y representación en la baraja')
    print('\n\t Letra 1: R=Rojo / G=Verde / B=Azul / Y=Amarillo / C=Cambio de Color')
    print('\t Letra 2: N=Número / C=Cambio / S=Suma')
    print('\t Letra 3: 0 a 9 = Número / C=Cambio\n')
    print('3. Se siguen las reglas de juego del UNO tradicional')

def main():
    menu()
    
main()
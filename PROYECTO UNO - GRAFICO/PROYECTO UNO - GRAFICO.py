import tkinter
from tkinter.constants import LEFT
from PIL import ImageTk
from PIL import Image
import random as rd
import copy as cp
import webbrowser as web

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


def cartaboton(posicion,ventana):
    ventana.destroy()
    if posicion=='P': return posicion
    else: return posicion+1

def color(carta_juego):
    inicial =[]
    if(carta_abs(carta_juego)[0]=='C'): inicial.append(carta_juego[1])
    else: inicial.append(carta_juego[0])
    if inicial[0]=='R': return '#FF3F3F'
    elif inicial[0]=='Y': return '#FFBB00'
    elif inicial[0]=='G': return '#039921'
    elif inicial[0]=='B': return '#004CFF'

def imprimir_mazo(k,mazo_jugador,mazo_maquina,cartas_en_juego):
    variable = []
    ventanaregla=tkinter.Tk()
    consa = (len(mazo_jugador)*100)+150
    if consa>1600: consa=1600
    consb = 400
    size = str(consa)+'x'+str(consb)
    ventanaregla.geometry(size)
    ventanaregla.title("Juego - Turno Jugador")
    ventanaregla.iconbitmap("1200px-UNO_Logo.svg (1).ico")
    titulojuego= tkinter.Label(ventanaregla, text="ROUND "+str(k)+"    Cartas maquina="+str(len(mazo_maquina)), font= "Helviatica 10 bold")
    titulojuego['bg'] =color(cartas_en_juego[len(cartas_en_juego)-1])
    carta = cp.copy(carta_abs(cartas_en_juego[len(cartas_en_juego)-1]))
    imagencarta=ImageTk.PhotoImage(Image.open(carta+".png").resize((100,150)))
    labelcarta=tkinter.Label(ventanaregla, image=imagencarta).pack()
    titulojuego.pack(fill=tkinter.X)
    Ipesca = ImageTk.PhotoImage(Image.open("Pesca.png").resize((100,150)))
    pesca = tkinter.Button(image=Ipesca,command=lambda: variable.append(cartaboton('P',ventanaregla))).pack(side=LEFT)
    a = []
    b = []
    for j in range(len(mazo_jugador)):
     a.append(None)
     b.append(None)
    for i in range(len(mazo_jugador)):
        a[i]=ImageTk.PhotoImage(Image.open(mazo_jugador[i]+".png").resize((100,150)))
        if verificar_juego(mazo_jugador[i],cartas_en_juego[len(cartas_en_juego)-1]):
            b[i]=tkinter.Button(image=a[i],command=lambda n = i: variable.append(cartaboton(n,ventanaregla))).pack(side=LEFT)
        else:
            b[i]=tkinter.Label(image=a[i]).pack(side=LEFT)
    ventanaregla.mainloop()
    return cp.copy(variable[0])


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

def ccret(letra,ventana):
    ventana.destroy()
    return letra

def cambiocolor():
    color=[]
    ventanacc=tkinter.Tk()
    ventanacc.geometry("300x150")
    ventanacc.title("Cambio de color")
    ventanacc.iconbitmap("1200px-UNO_Logo.svg (1).ico")
    titulojuego= tkinter.Label(ventanacc, text="Cambio de color: Elija el color de su elección", font= "Helviatica 10 bold")
    titulojuego['bg'] ='#00f2ff'
    titulojuego.pack(fill=tkinter.X)
    Rojo = tkinter.Button(text="Color Rojo",command=lambda: color.append(ccret('R',ventanacc))).pack()
    Azul = tkinter.Button(text="Color Azul",command=lambda: color.append(ccret('B',ventanacc))).pack()
    Verde = tkinter.Button(text="Color Verde",command=lambda: color.append(ccret('G',ventanacc))).pack()
    Amarillo = tkinter.Button(text="Color Amarillo",command=lambda: color.append(ccret('Y',ventanacc))).pack()
    ventanacc.mainloop()
    return cp.copy(color[0])


def juego_jugador(k,mazo_jugador,mazo_maquina, cartas_en_juego):
    l=imprimir_mazo(k,mazo_jugador,mazo_maquina,cartas_en_juego)
    if l=='P': return 'NHPJ'
    n = int(l)
    if n>=1 and n<=len(mazo_jugador):
        carta=mazo_jugador[n-1]
        if verificar_juego(carta, cartas_en_juego[len(cartas_en_juego)-1]):
            if carta[0]=='C':
                cc = cambiocolor()
                if cc=='R' or cc=='G' or cc=='B' or cc=='Y': return carta,cc
            else:
                return carta
    return juego_jugador(k,mazo_jugador,mazo_maquina, cartas_en_juego)

def destroy(ventana):
    ventana.destroy()

def mostrar_carta(carta,k):
    ventanam=tkinter.Tk()
    ventanam.geometry("500x200")
    ventanam.title("Juego - Turno Maquina")
    ventanam.iconbitmap("1200px-UNO_Logo.svg (1).ico")
    titulojuego= tkinter.Label(ventanam, text="ROUND "+str(k), font= "Helviatica 10 bold")
    titulojuego['bg'] =color(carta)
    titulojuego.pack(fill=tkinter.X)
    Imagedecard = ImageTk.PhotoImage(Image.open(carta_abs(carta)+".png").resize((100,150)))
    card = tkinter.Label(ventanam, image=Imagedecard).pack()
    continuar = tkinter.Button(text="Continuar",command=lambda: destroy(ventanam)).pack()
    ventanam.mainloop()

def juego_maquina (mazo_maquina, cartas_en_juego,k):
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
            if carta[0]=='C':
                mostrar_carta([carta,color],k) 
                return carta,color
            mostrar_carta(carta,k)
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

def retorno(ventana):
    ventana.destroy()
    menu()

def final_juego(booleano):
    ventanam=tkinter.Tk()
    ventanam.geometry("1000x580")
    ventanam.title("UNO By: Omar y Eder")
    ventanam.iconbitmap("1200px-UNO_Logo.svg (1).ico")
    if booleano: Imagedecard = ImageTk.PhotoImage(Image.open("Ganador.png").resize((1000,562)))
    else:  Imagedecard = ImageTk.PhotoImage(Image.open("Perdedor.png").resize((1000,562)))
    card = tkinter.Label(ventanam, image=Imagedecard).pack()
    continuar = tkinter.Button(text="Volver al menu principal",command=lambda: retorno(ventanam)).pack()
    ventanam.mainloop()


def juego(mazo_jugador, mazo_maquina, cartas_en_juego):
    carta_maquina = '...'
    carta_jugador = '...'
    k=1
    while len(mazo_jugador)!=0 and len(mazo_maquina)!=0:
        reiniciar_tamano()
        if carta_abs(cartas_en_juego[len(cartas_en_juego)-1])==carta_abs(carta_maquina) and (carta_abs(carta_maquina)[1]=='S' or carta_abs(carta_maquina)[1]=='E'):
            if carta_abs(carta_maquina)[2]!='B':
                pesca_mazo(mazo_jugador,ord(carta_abs(carta_maquina)[2])-48)
        else:
            carta_jugador = cp.copy(juego_jugador(k,mazo_jugador,mazo_maquina, cartas_en_juego))
            if carta_jugador!='NHPJ':
                cartas_en_juego.append(carta_jugador)
                actualizar_mazo(mazo_jugador, carta_jugador)
            else:
                pesca_mazo(mazo_jugador,1)
        #turno maquina
        if len(mazo_jugador)==0: break
        reiniciar_tamano()
        if carta_abs(cartas_en_juego[len(cartas_en_juego)-1])==carta_abs(carta_jugador) and (carta_abs(carta_jugador)[1]=='S' or carta_abs(carta_jugador)[1]=='E'):
            if carta_abs(carta_jugador)[2]!='B':
                pesca_mazo(mazo_maquina,ord(carta_abs(carta_jugador)[2])-48)
        else:
            carta_maquina = cp.copy(juego_maquina(mazo_maquina,cartas_en_juego,k))
            if carta_maquina!='NHPJ':
                cartas_en_juego.append(carta_maquina)
                actualizar_mazo(mazo_maquina, carta_maquina)
            else:
                pesca_mazo(mazo_maquina,1)
        k+=1
    if len(mazo_jugador)==0: final_juego(True)
    else: final_juego(False)

baraja_completa = matriz_baraja(gen_baraja_base())
def prepa_juego(ventana):
    ventana.destroy()
    mazo_jugador = gen_mazo()
    mazo_maquina = gen_mazo()
    cartas_en_juego = [primera_carta()]
    juego(mazo_jugador,mazo_maquina,cartas_en_juego)

def matriz(ventana):
    ventana.destroy()
    ventanamm=tkinter.Tk()
    ventanamm.geometry("1600x600")
    ventanamm.title("UNO By: Omar y Eder")
    ventanamm.iconbitmap("1200px-UNO_Logo.svg (1).ico")
    Imagedecard = ImageTk.PhotoImage(Image.open("Bf.png").resize((1500,560)))
    card = tkinter.Label(ventanamm, image=Imagedecard).pack()
    volver = tkinter.Button(text="Volver al Menú Principal",command=lambda: retorno(ventanamm)).pack()
    ventanamm.mainloop()

def menu():
    ventana = tkinter.Tk()
    ventana.geometry("600x400")
    ventana.title("UNO By: Omar y Eder")
    ventana.iconbitmap("1200px-UNO_Logo.svg (1).ico")
    ventana['bg'] = '#f1f0f1'
    colorp='#f1f0f1'
    titulo= tkinter.Label(ventana, text="Bienvenido al UNO-V, una versión completamente virtual de UNO.", font= "Helviatica 10 bold")
    titulo['bg'] ='#FF3F3F'
    reglas=tkinter.Button(text="Reglas del Juego", command=reglasjuego)
    baraja=tkinter.Button(text="Mostrar baraja",command=lambda:matriz(ventana))
    juego=tkinter.Button(text="¡A jugar!", command=lambda:prepa_juego(ventana))
    salir=tkinter.Button(text="Salir", command=ventana.destroy)
    imagen=ImageTk.PhotoImage(Image.open("logox.png").resize((200,100)))
    label=tkinter.Label(image=imagen)
    vacio=tkinter.Label(ventana)
    vacio['bg']=colorp
    vacio2=tkinter.Label(ventana)
    vacio2['bg']=colorp
    vacio3=tkinter.Label(ventana)
    vacio3['bg']=colorp
    vacio4=tkinter.Label(ventana)
    vacio4['bg']=colorp
    vacio5=tkinter.Label(ventana)
    vacio5['bg']=colorp
    vacio6=tkinter.Label(ventana)
    vacio6['bg']=colorp
    #Ordenamiento
    titulo.pack(fill=tkinter.X)
    vacio2.pack()
    reglas.pack()
    vacio3.pack()
    baraja.pack()
    vacio4.pack()
    juego.pack()
    vacio5.pack()
    salir.pack()
    vacio6.pack()
    label.pack()
    ventana.mainloop()

def reglasjuego():
    web.open("https://drive.google.com/file/d/1m6MlOy9BQ5pWHzXLxKE-LbqbhgGe7jMV/view?usp=sharing")

def main():
    menu()
    
main()
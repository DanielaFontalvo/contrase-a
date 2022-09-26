from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ntpath import join
from random import *
import pandas as pd

ventana=Tk()
ventana.title('GENERADOR DE CONTRASEÑAS')
ventana.iconbitmap('C:/Users/equipo/OneDrive/Escritorio/contraseña/logocandado.ico.ico')
ventana.geometry('500x500')
ventana.config(bg="#CDC4D3")

imagen=Image.open('fondo de contraseñas 1.jpg')
imagen= imagen.resize((500,500), Image.ANTIALIAS)
imagen1=ImageTk.PhotoImage(imagen)
Labelimagen=Label (ventana, image= imagen1)
Labelimagen.pack()

barrita= Canvas (width = 500, height= 10, bg= '#CDC4D3', highlightthickness= 0) 
barrita.place(x =0, y=55)

titulo = Label (ventana, text= 'Generador de Contaseñas', font= ('Arial, 22'), bg="#CDC4D3")
titulo.place(x=80 , y=10)

primerp= Label (ventana, text= 'Nivel de Seguridad:', font= ('Calibri, 17'), bg="#CDC4D3")
primerp.place(x= 20 , y=  90)

def facil():
    global password
    lista=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0','1','2','3','4','5','6','7','8','9']
    clave=[]

    for x in range(8):
        y=choice(lista)
        clave.append(y)

    f=''.join(clave) 
  
    password=f

    print(f)

boton=ttk.Button(text="FACIL",command= facil)
boton.place(x=30, y=150, width = 100, height= 35)

def media():
    global password
    lista2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0','1','2','3','4','5','6','7','8','9']
    clave2=[]

    for x in range(10):
        y2=choice(lista2)
        clave2.append(y2)

    f2=''.join(clave2) 

    print(f2)
 
    password=f2

boton2= ttk.Button(text="MEDIA", command=media)
boton2.place(x=150, y=150, width = 100, height= 35)

def dificil():
    global password
    lista3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    clave3=[]

    for x in range(15):
        y3=choice(lista3)
        clave3.append(y3)

    f3=''.join(clave3) 

    print(f3)
    
    password=f3

boton3= ttk.Button(text="DIFICIL", command=dificil)
boton3.place(x=270, y=150, width = 100, height= 35)

def muydificil():
    global password
    lista4=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','*','#']
    clave4=[]

    for x in range(20):
        y4=choice(lista4)
        clave4.append(y4)

    f4=''.join(clave4) 

    print(f4)
      
    password=f4

boton4= ttk.Button(text="MUY DIFICIL", command= muydificil)
boton4.place(x=390, y=150, width = 100, height= 35)

texto=Entry (ventana, bg='#CDC4D3', font= ('Arial, 20'))
texto.place(x=100, y= 270, width = 300, height= 50)

def generador():
    texto.delete(0, END)
    texto.insert(0, password)

boton5= ttk.Button(text="GENERAR", command=generador)
boton5.place(x=200, y=375, width = 100, height= 35)

def copiar_al_portapapeles():
    ventana.clipboard_clear()
    ventana.clipboard_append(texto.get())

boton6= ttk.Button(text="COPIAR", command=copiar_al_portapapeles)
boton6.place(x= 200, y=420, width = 100, height= 35)


#df_datos= pd.DataFrame('texto')
#df_datos.to_csv(r'C:\Users\equipo\OneDrive\Escritorio\contraseña\Claves proyecto.csv')
ventana.mainloop()
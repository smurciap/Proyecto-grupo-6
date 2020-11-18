# -*- coding: utf-8 -*-

"""Librerias"""

import tkinter as tk
import cv2
     

"""Funciones"""

def anima_ciones():
    
    ventana_animaciones=tk.Tk()
    ventana_animaciones.title("Animaciones")
    ventana_animaciones.geometry("430x70")
    ventana_animaciones.configure(background="light cyan") 
    
    anima_teo = tk.Button(ventana_animaciones,text="Animacion teorica", fg="black",command=animacion_teorica)
    anima_teo.place(x=10,y=10,width=200, height=20)

    anima_exp = tk.Button(ventana_animaciones, text="Animacion experimental", fg="black",command=animacion_experimental)
    anima_exp.place(x=220,y=10,width=200, height=20)

    quit = tk.Button( ventana_animaciones, text="volver", fg="black",command=ventana_animaciones.destroy)
    quit.place(x=165,y=40,width=100, height=20)
 
def gra_ficas():

    ventana_graficas=tk.Tk()
    ventana_graficas.title("Graficas")
    ventana_graficas.geometry("660x500")
    ventana_graficas.configure(background="white")
    
    graf_exp = tk.PhotoImage (file='imagen_exp.gif', master=ventana_graficas)
    
    graf_exp_label= tk.Label(ventana_graficas, image=graf_exp)
    graf_exp_label.place(x=0,y=0,width=300,height=300)
    
  
    quit = tk.Button( ventana_graficas, text="volver", fg="black",command=ventana_graficas.destroy)
    quit.place(x=550,y=470,width=100, height=20)

def tabla_datos():
    
    return 0 

def animacion_teorica():
        
        while (video_teo.isOpened()):
          ret, imagen = video_teo.read()
          if ret == True:
            cv2.imshow('video', imagen)
            if cv2.waitKey(30) == ord('s'):
              break
          else: break
        video_1=video_teo.release()
        return video_1      
    
def animacion_experimental():
        
        while (video_exp.isOpened()):
          ret, imagen = video_exp.read()
          if ret == True:
            cv2.imshow('video', imagen)
            if cv2.waitKey(30) == ord('s'):
              break
          else: break
        video_2=video_exp.release()
        return video_2 

"""Lectura de videos"""

video_teo = cv2.VideoCapture('C:/Users/Sergio Murcia P/animation_teo.mp4')
video_exp = cv2.VideoCapture('C:/Users/Sergio Murcia P/animation_exp.mp4')


"""interfaces"""

ventana=tk.Tk()
ventana.title("Pendulo simple")
ventana.geometry("660x500")
ventana.configure(background="white")


"""Lectura de imagenes """

logo= tk.PhotoImage (file='pendulosimple.gif')


"""Botones"""

anima = tk.Button(text="Animaciones", fg="black",command=anima_ciones)
anima.place(x=500,y=215,width=150, height=20)

graf = tk.Button(text="Graficas", fg="black",command=gra_ficas)
graf.place(x=500,y=240,width=150, height=20)

tab_datos = tk.Button(text="Tablas de datos", fg="black",command=tabla_datos)
tab_datos.place(x=500,y=265,width=150, height=20)

quit = tk.Button(text="Salir", fg="black",command=ventana.destroy)
quit.place(x=555,y=475,width=100, height=20)

""" Label´s"""

logotipo = tk.Label(ventana, image=logo)
logotipo.place(x=0,y=0,width=500,height=500)


ventana.mainloop()
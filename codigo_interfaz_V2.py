# -*- coding: utf-8 -*-
import tkinter as tk
import cv2
from tkinter.filedialog import askopenfile
import webbrowser as wb 

video_teo = cv2.VideoCapture('C:/Users/Sergio Murcia P/animation_teo.mp4')
video_exp = cv2.VideoCapture('C:/Users/Sergio Murcia P/animation_exp.mp4')
video_teo_hooke = cv2.VideoCapture('C:/Users/Sergio Murcia P/animation_hooke_teo.mp4')
video_exp_hooke = cv2.VideoCapture('C:/Users/Sergio Murcia P/animation_exp_hooke.mp4')

         
class root_principal: 
    def __init__(self):
        self.interfaz()
        self.label1()
        self.botones()
        self.principal.mainloop() 
        
    def interfaz(self):
        self.principal=tk.Tk()
        self.principal.title("Experimentos")
        self.principal.geometry("400x300")
        self.principal.configure(background="white") 
        
    def label1(self):
        label2 = tk.Label(self.principal)
        label2.configure(bg="white")
        label2.place(x=0,y=0,relwidth=1, relheight=1)
        
        label1 = tk.Label(self.principal, text='Elige el experiemto')
        label1.configure(bg="white", fg="black", font=("Courier", 20, "italic"))
        label1.place(x=40,y=50,width=320,height=30)
        
    def botones(self):
        pendulo = tk.Button(text="Pendulo simple", fg="black", font=("Courier", 8, "italic"),command=self.class_pendulo)
        pendulo.place(x=140,y=120,width=120, height=20)
        
        hooke= tk.Button(text="Ley de Hooke", fg="black", font=("Courier", 8, "italic"), command=self.class_hooke)
        hooke.place(x=140,y=145,width=120, height=20)
        
        quit = tk.Button(text="Salir", fg="black",font=("Courier", 8, "italic"), command=self.principal.destroy)
        quit.place(x=290,y=270,width=100, height=20)
    
    def class_pendulo(self):
        Dialogo1=pendulo(self.principal)
    def class_hooke(self):
        Dialogo2=hooke(self.principal)

class hooke:
    def __init__(self, ventanaprincipal_hooke):
        
        self.ventana_hooke=tk.Toplevel(ventanaprincipal_hooke)
        self.interfaz()
        self.labels()
        self.botones()
        self.ventana_hooke.mainloop() 
        
    def interfaz(self):
        self.ventana_hooke.title("Ley de Hooke")
        self.ventana_hooke.geometry("660x500")
        self.ventana_hooke.configure(background="white")    
    def botones(self):
        self.anima = tk.Button(self.ventana_hooke, text='Animaciones',fg='black',font=("Courier", 8, "italic"),command=self.class_animapendulo_hooke)
        self.anima.place(x=480,y=215,width=170,height=20)
        self.graf = tk.Button(self.ventana_hooke, text='Graficas',fg='black',font=("Courier", 8, "italic"), command=self.class_graficapendulo_hooke)
        self.graf.place(x=480,y=240,width=170,height=20)
        self.tab_datos = tk.Button(self.ventana_hooke, text='Tablas de datos',fg='black',font=("Courier", 8, "italic"),command=self.class_datospendulo_hooke)
        self.tab_datos.place(x=480,y=265,width=170,height=20)
        self.ecu = tk.Button(self.ventana_hooke, text='Ecuacion de movimiento',fg='black',font=("Courier", 8, "italic"),command=self.class_ecuacionpendulo_hooke)
        self.ecu.place(x=480,y=190,width=170,height=20)
        self.car_vid = tk.Button(self.ventana_hooke, text='Subir video',fg='black',font=("Courier", 8, "italic"),command=self.open_video_hooke)
        self.car_vid.place(x=480,y=165,width=170,height=20)
        self.quit = tk.Button(self.ventana_hooke, text="Volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_hooke.destroy)
        self.quit.place(x=555,y=475,width=100, height=20)
    def labels(self):
        self.logo= tk.PhotoImage (file='logo_hooke.png')
        logotipo = tk.Label(self.ventana_hooke,image=self.logo)
        logotipo.place(x=0,y=0,width=500,height=480)
    def class_animapendulo_hooke(self):
        Dialogo2=pendulo_animaciones_hooke(self.ventana_hooke)
    def class_graficapendulo_hooke(self):
        Dialogo3=pendulo_graficas_hooke(self.ventana_hooke)
    def class_datospendulo_hooke(self):
        Dialogo3=pendulo_datos_hooke(self.ventana_hooke)
    def class_ecuacionpendulo_hooke(self):
        Dialogo4=ecuacion_pendulo_hooke(self.ventana_hooke)
    def open_video_hooke(self): 
        file = askopenfile(mode ='r', filetypes =[('Python Files', '*.mp4')]) 
        if file is not None: 
            content = file.read() 
            print(content) 
            
            
class pendulo_animaciones_hooke:
    def __init__(self,ventanahooke):
        self.ventana_animaciones=tk.Toplevel(ventanahooke)
        self.interfaz()
        self.botones()
        self.ventana_animaciones.mainloop()

    def interfaz(self):
        self.ventana_animaciones.title("Animaciones")
        self.ventana_animaciones.geometry("430x70")
        self.ventana_animaciones.configure(background="white")      
    def botones (self):
        self.anima_teo = tk.Button(self.ventana_animaciones,text="Animacion teorica", fg="black",font=("Courier", 8, "italic"),command=self.animacion_teorica)
        self.anima_teo.place(x=10,y=10,width=200, height=20)
    
        self.anima_exp = tk.Button(self.ventana_animaciones, text="Animacion experimental", fg="black",font=("Courier", 8, "italic"),command=self.animacion_experimental)
        self.anima_exp.place(x=220,y=10,width=200, height=20)
    
        self.quit = tk.Button( self.ventana_animaciones, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_animaciones.destroy)
        self.quit.place(x=165,y=40,width=100, height=20)
    
    def animacion_teorica(self):
        while (video_teo_hooke.isOpened()):
          ret, imagen = video_teo_hooke.read()
          if ret == True:
            cv2.imshow('video', imagen)
            if cv2.waitKey(30) == ord('s'):
              break
          else: break
        video_1=video_teo_hooke.release()
        return video_1      
        
    def animacion_experimental(self):
             
        while (video_exp_hooke.isOpened()):
          ret, imagen = video_exp_hooke.read()
          if ret == True:
            cv2.imshow('video', imagen)
            if cv2.waitKey(30) == ord('s'):
              break
          else: break
        video_2=video_exp_hooke.release()
        return video_2 
    
    
class pendulo_graficas_hooke:
    def __init__(self,ventanahooke):
        self.ventana_graficas=tk.Toplevel(ventanahooke)
        self.ventana_graficas.title("Graficas")
        self.ventana_graficas.geometry("1000x410")
        self.ventana_graficas.configure(background="white") 
        
        self.gr_teo= tk.PhotoImage (file='Imagen_teo.png')
        self.gr_teo1 = tk.Label(self.ventana_graficas,image=self.gr_teo,bg="white")
        self.gr_teo1.place(x=0,y=30,width=500,height=350)
        
        self.gr_exp= tk.PhotoImage (file='Imagen_exp_hooke.png')
        self.gr_exp1 = tk.Label(self.ventana_graficas,image=self.gr_exp,bg="white")
        self.gr_exp1.place(x=500,y=30,width=500,height=350)
        
        self.label1 = tk.Label(self.ventana_graficas, text='Grafica teorica')
        self.label1.configure(bg="white", fg="black", font=("Courier", 20, "italic"))
        self.label1.place(x=90,y=0,width=320,height=30)
        
        self.label2 = tk.Label(self.ventana_graficas, text='Grafica experimental')
        self.label2.configure(bg="white", fg="black", font=("Courier", 20, "italic"))
        self.label2.place(x=590,y=0,width=320,height=30)
        
        self.quit = tk.Button( self.ventana_graficas, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_graficas.destroy)
        self.quit.place(x=890,y=380,width=100, height=20)
        
        self.ventana_graficas.mainloop() 
            
     
class pendulo_datos_hooke:
    def __init__(self,ventanahooke):
        self.ventana_datos=tk.Toplevel(ventanahooke)
        self.ventana_datos.title("Tablas de datos")
        self.ventana_datos.geometry("450x70")
        self.ventana_datos.configure(background="white") 
        
        self.datos_teo = tk.Button(self.ventana_datos,text="Tabla de datos teoricos", fg="black",font=("Courier", 8, "italic"), command=self.open_teo)
        self.datos_teo.place(x=10,y=10,width=210, height=20)
    
        self.datos_exp = tk.Button(self.ventana_datos, text="Tabla de datos experimentales", fg="black",font=("Courier", 8, "italic"),command=self.open_exp)
        self.datos_exp.place(x=230,y=10,width=210, height=20)
    
        self.quit = tk.Button( self.ventana_datos, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_datos.destroy)
        self.quit.place(x=175,y=40,width=100, height=20)
        
        self.ventana_datos.mainloop()
        
    def open_exp(self):
        
        wb.open_new(r'C:\Users\Sergio Murcia P\datos_exp_hooke.txt')
        
    def open_teo(self):
        
        wb.open_new(r'C:\Users\Sergio Murcia P\datos_teo.txt')
    
    
class ecuacion_pendulo_hooke:
    def __init__(self,ventanahooke):
        self.ventana_ecuacion=tk.Toplevel(ventanahooke)
        self.ventana_ecuacion.title("Ecuacion de movimiento")
        self.ventana_ecuacion.geometry("500x400")
        self.ventana_ecuacion.configure(background="white")  
        self.ecu= tk.PhotoImage (file='ecuacion de movimiento resorte.png')
        self.imagen_sub=self.ecu.subsample(3)
        self.ecu1 = tk.Label(self.ventana_ecuacion,image=self.imagen_sub,bg="white")
        self.ecu1.place(x=0,y=50,width=500,height=100)
        
        self.label1 = tk.Label(self.ventana_ecuacion, text='Ecuacion de movimiento')
        self.label1.configure(bg="white", fg="black", font=("Courier", 20, "italic"))
        self.label1.place(x=70,y=10,width=360,height=30)
        
        self.label2 = tk.Label(self.ventana_ecuacion, text='Donde:')
        self.label2.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label2.place(x=10,y=180,width=100,height=30)

        self.label3 = tk.Label(self.ventana_ecuacion, text='Amplitud:1.0  ')
        self.label3.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label3.place(x=10,y=220,width=180,height=30)                
                   
        self.label4 = tk.Label(self.ventana_ecuacion, text='Frecuencia:0.996+/-0.005')
        self.label4.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label4.place(x=10,y=260,width=275,height=30)  
        
        self.label5= tk.Label(self.ventana_ecuacion, text='Error de medicion:0.02+/-0.007 ')
        self.label5.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label5.place(x=10,y=300,width=350,height=30)          
        
        self.label6= tk.Label(self.ventana_ecuacion, text='Longitud natural:2             ')
        self.label6.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label6.place(x=10,y=340,width=350,height=30) 
        
        self.quit = tk.Button( self.ventana_ecuacion, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_ecuacion.destroy)
        self.quit.place(x=390,y=370,width=100, height=20)
        
        self.ventana_ecuacion.mainloop()
    
    
        
class pendulo:
    
    def __init__(self, ventanaprincipal):
        
        self.ventana=tk.Toplevel(ventanaprincipal)
        self.interfaz()
        self.labels()
        self.botones()
        self.ventana.mainloop() 
        
    def interfaz(self):
        self.ventana.title("Pendulo simple")
        self.ventana.geometry("660x500")
        self.ventana.configure(background="white")
    def botones(self):
        self.anima = tk.Button(self.ventana, text='Animaciones',fg='black',font=("Courier", 8, "italic"),command=self.class_animapendulo)
        self.anima.place(x=480,y=215,width=170,height=20)
        self.graf = tk.Button(self.ventana, text='Graficas',fg='black',font=("Courier", 8, "italic"), command=self.class_graficapendulo)
        self.graf.place(x=480,y=240,width=170,height=20)
        self.tab_datos = tk.Button(self.ventana, text='Tablas de datos',fg='black',font=("Courier", 8, "italic"),command=self.class_datospendulo)
        self.tab_datos.place(x=480,y=265,width=170,height=20)
        
        
        self.ecu = tk.Button(self.ventana, text='Ecuacion de movimiento',fg='black',font=("Courier", 8, "italic"),command=self.class_ecuacionpendulo)
        self.ecu.place(x=480,y=190,width=170,height=20)
        
        self.car_vid = tk.Button(self.ventana, text='Subir video',fg='black',font=("Courier", 8, "italic"),command=self.open_video)
        self.car_vid.place(x=480,y=165,width=170,height=20)
        self.quit = tk.Button(self.ventana, text="Volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana.destroy)
        self.quit.place(x=555,y=475,width=100, height=20)
    def labels(self):
        self.logo= tk.PhotoImage (file='pendulosimple.gif')
        logotipo = tk.Label(self.ventana,image=self.logo)
        logotipo.place(x=0,y=0,width=500,height=480)
    def class_animapendulo(self):
        Dialogo2=pendulo_animaciones(self.ventana)
    def class_graficapendulo(self):
        Dialogo3=pendulo_graficas(self.ventana)
    def class_datospendulo(self):
        Dialogo3=pendulo_datos(self.ventana)
    def class_ecuacionpendulo(self):
        Dialogo4=ecuacion_pendulo(self.ventana)
    def open_video(self): 
        file = askopenfile(mode ='r', filetypes =[('Python Files', '*.mp4')]) 
        if file is not None: 
            content = file.read() 
            print(content) 


class ecuacion_pendulo:
    def __init__(self,ventanapendulo):
        self.ventana_ecuacion=tk.Toplevel(ventanapendulo)
        self.ventana_ecuacion.title("Ecuacion de movimiento")
        self.ventana_ecuacion.geometry("500x400")
        self.ventana_ecuacion.configure(background="white")  
        self.ecu= tk.PhotoImage (file='ecuacion de movimiento pendulo.png')
        self.imagen_sub=self.ecu.subsample(3)
        self.ecu1 = tk.Label(self.ventana_ecuacion,image=self.imagen_sub,bg="white")
        self.ecu1.place(x=0,y=50,width=500,height=100)
        
        self.label1 = tk.Label(self.ventana_ecuacion, text='Ecuacion de movimiento')
        self.label1.configure(bg="white", fg="black", font=("Courier", 20, "italic"))
        self.label1.place(x=70,y=10,width=360,height=30)
        
        self.label2 = tk.Label(self.ventana_ecuacion, text='Donde:')
        self.label2.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label2.place(x=10,y=180,width=100,height=30)

        self.label3 = tk.Label(self.ventana_ecuacion, text='Amplitud:0.349')
        self.label3.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label3.place(x=10,y=220,width=180,height=30)                
        
        self.label4 = tk.Label(self.ventana_ecuacion, text='Frecuencia:1.783+/-0.263')
        self.label4.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label4.place(x=10,y=260,width=275,height=30)  
        
        self.label5= tk.Label(self.ventana_ecuacion, text='Error de medicion:0.002+/-0.008')
        self.label5.configure(bg="white", fg="black", font=("Courier", 13, "italic"))
        self.label5.place(x=10,y=300,width=350,height=30)          
        
        self.quit = tk.Button( self.ventana_ecuacion, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_ecuacion.destroy)
        self.quit.place(x=390,y=370,width=100, height=20)
        
        self.ventana_ecuacion.mainloop()
        
        
class pendulo_animaciones:
    
    def __init__(self,ventanapendulo):
        self.ventana_animaciones=tk.Toplevel(ventanapendulo)
        self.interfaz()
        self.botones()
        self.ventana_animaciones.mainloop()

    def interfaz(self):
        self.ventana_animaciones.title("Animaciones")
        self.ventana_animaciones.geometry("430x70")
        self.ventana_animaciones.configure(background="white")      
    def botones (self):
        self.anima_teo = tk.Button(self.ventana_animaciones,text="Animacion teorica", fg="black",font=("Courier", 8, "italic"),command=self.animacion_teorica)
        self.anima_teo.place(x=10,y=10,width=200, height=20)
    
        self.anima_exp = tk.Button(self.ventana_animaciones, text="Animacion experimental", fg="black",font=("Courier", 8, "italic"),command=self.animacion_experimental)
        self.anima_exp.place(x=220,y=10,width=200, height=20)
    
        self.quit = tk.Button( self.ventana_animaciones, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_animaciones.destroy)
        self.quit.place(x=165,y=40,width=100, height=20)
    
    def animacion_teorica(self):
        while (video_teo.isOpened()):
          ret, imagen = video_teo.read()
          if ret == True:
            cv2.imshow('video', imagen)
            if cv2.waitKey(30) == ord('s'):
              break
          else: break
        video_1=video_teo.release()
        return video_1      
        
    def animacion_experimental(self):
             
        while (video_exp.isOpened()):
          ret, imagen = video_exp.read()
          if ret == True:
            cv2.imshow('video', imagen)
            if cv2.waitKey(30) == ord('s'):
              break
          else: break
        video_2=video_exp.release()
        return video_2 
    
class pendulo_graficas:
    def __init__(self,ventanapendulo):
        self.ventana_graficas=tk.Toplevel(ventanapendulo)
        self.ventana_graficas.title("Graficas")
        self.ventana_graficas.geometry("1000x410")
        self.ventana_graficas.configure(background="white") 
        
        self.gr_teo= tk.PhotoImage (file='Imagen_teo.png')
        self.gr_teo1 = tk.Label(self.ventana_graficas,image=self.gr_teo,bg="white")
        self.gr_teo1.place(x=0,y=30,width=500,height=350)
        
        self.gr_exp= tk.PhotoImage (file='imagen_exp.gif')
        self.gr_exp1 = tk.Label(self.ventana_graficas,image=self.gr_exp,bg="white")
        self.gr_exp1.place(x=500,y=30,width=500,height=350)
        
        self.label1 = tk.Label(self.ventana_graficas, text='Grafica teorica')
        self.label1.configure(bg="white", fg="black", font=("Courier", 20, "italic"))
        self.label1.place(x=90,y=0,width=320,height=30)
        
        self.label2 = tk.Label(self.ventana_graficas, text='Grafica experimental')
        self.label2.configure(bg="white", fg="black", font=("Courier", 20, "italic"))
        self.label2.place(x=590,y=0,width=320,height=30)
        
        self.quit = tk.Button( self.ventana_graficas, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_graficas.destroy)
        self.quit.place(x=890,y=380,width=100, height=20)
        
        self.ventana_graficas.mainloop()   
        
class pendulo_datos:
    def __init__(self,ventanapendulo):
        self.ventana_datos=tk.Toplevel(ventanapendulo)
        self.ventana_datos.title("Tablas de datos")
        self.ventana_datos.geometry("450x70")
        self.ventana_datos.configure(background="white") 
        
        self.datos_teo = tk.Button(self.ventana_datos,text="Tabla de datos teoricos", fg="black",font=("Courier", 8, "italic"), command=self.open_teo)
        self.datos_teo.place(x=10,y=10,width=210, height=20)
    
        self.datos_exp = tk.Button(self.ventana_datos, text="Tabla de datos experimentales", fg="black",font=("Courier", 8, "italic"),command=self.open_exp)
        self.datos_exp.place(x=230,y=10,width=210, height=20)
    
        self.quit = tk.Button( self.ventana_datos, text="volver", fg="black",font=("Courier", 8, "italic"),command=self.ventana_datos.destroy)
        self.quit.place(x=175,y=40,width=100, height=20)
        
        self.ventana_datos.mainloop()
        
    def open_exp(self):
        
        wb.open_new(r'C:\Users\Sergio Murcia P\datos_exp.txt')
        
    def open_teo(self):
        
        wb.open_new(r'C:\Users\Sergio Murcia P\datos_teo.txt')
      
        
root_principal()


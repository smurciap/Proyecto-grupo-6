# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 00:31:57 2020

@author: Sergio Murcia P
"""

import tkinter as tk
import cv2

video = cv2.VideoCapture('C:/Users/Sergio Murcia P/animation.mp4')

class interfaz(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.botones()

    def botones(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Animacion teorica"
        self.hi_there["command"] = self.animacion_teorica
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="Salir", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def animacion_teorica(self):
        
        while (video.isOpened()):
          ret, imagen = video.read()
          if ret == True:
            cv2.imshow('video', imagen)
            if cv2.waitKey(30) == ord('s'):
              break
          else: break
        video_1=video.release()
        return video_1        
        
        
       

        

root = tk.Tk()
app = interfaz(master=root)
app.mainloop()
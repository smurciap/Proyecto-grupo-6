# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:57:33 2020

@author: Sergio Murcia P
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import math
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

class simulacion:
  def __init__(self,x0,xp0,l,t=0):
    self.anguloi=x0
    self.velanguloi=xp0
    self.longitud=l
    self.omega=math.sqrt(9.81/self.longitud)
    self.tiempoi=t
    self.periodo=(2*math.pi)/self.omega
  def condiciones_iniciales(self):
    omega=math.sqrt(9.81/self.longitud)
    phi=math.atan((-self.velanguloi)/(omega*self.anguloi))-omega*self.tiempoi
    A=(1/omega)*math.sqrt(self.velanguloi*self.velanguloi+(omega*omega)*(self.anguloi*self.anguloi))
    return (phi,A)
  def puntos(self):
    omega=math.sqrt(9.81/self.longitud)
    d=simulacion(self.anguloi,self.velanguloi,self.longitud,self.tiempoi)
    phii,Aa=d.condiciones_iniciales()
    K=np.arange(0,100,0.1)
    P=Aa*np.cos(omega*K+phii)
    return (P,K)
  def posicionx(self):
    d=simulacion(self.anguloi,self.velanguloi,self.longitud,self.tiempoi)
    P,K=d.puntos()
    K1=np.sin(P)*self.longitud
    return (P,K1)
  def posiciony(self):
    d=simulacion(self.anguloi,self.velanguloi,self.longitud,self.tiempoi)
    P,K=d.puntos()
    K2=-np.cos(P)*self.longitud
    return (P,K2)
  def crear_capa(self,step, ax):
    d=simulacion(self.anguloi,self.velanguloi,self.longitud,self.tiempoi)
    P1,K1=d.posicionx()
    P2,K2=d.posiciony()
    ax.cla()
    ax.scatter([0],[0],s=100)
    ax.scatter(K1[step],K2[step],s=100)
    plt.xlim((-5,5))
    plt.ylim((-5,0))

    if K1[step]>0:
      sns.lineplot(np.arange(0,K1[step],0.1),(K2[step]/K1[step])*np.arange(0,K1[step],0.1),ax=ax)
    elif K1[step]<0:
      sns.lineplot(np.arange(K1[step],0,0.1),(K2[step]/K1[step])*np.arange(K1[step],0,0.1),ax=ax)
    elif K1[step]==0:
      sns.lineplot([0],[-self.longitud],ax=ax)
  def animar(self):
    d=simulacion(self.anguloi,self.velanguloi,self.longitud,self.tiempoi)
    fig = plt.figure()
    ax = fig.gca()
    plt.xlim((-5,5))
    plt.ylim((-5,-4.825))
    d.crear_capa(2, ax)
    fig = plt.figure()
    ax = fig.gca()
    animation = FuncAnimation(fig, d.crear_capa, frames=100, fargs=(ax,))
    animation.save('animation.mp4', writer='ffmpeg', fps=20);
    HTML(animation.to_jshtml())
    
d=simulacion(0.18,0,4)
d.animar()

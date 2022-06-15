# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 13:22:41 2022

@author: Álvaro Magdalena 
"""

import numpy as np
import matplotlib.pyplot as plt

#plt.close("all")
def signo(a):
    if a>=0:
        b=1
    elif a<0:
        b=0
    return(b)

matrixaux=np.zeros((450,450))

matrixaux[105:110]=50
# matrixaux[6]=50
matrixaux[130:150]=5
# matrixaux[16]=5
# matrixaux[10]=5
# matrixaux[11]=5
# for i in  range(-225,225):
#     for j in range(-225,225):
#         if 40<=np.sqrt(i**2+j**2)<=80:
#             matrixaux[225+i,225+j]=50
theta=np.linspace(0,90,181)
phi=np.linspace(0,360,361)
dist5=([])
for i in range(len(phi)):           ##vario el angulo "polar"
    # if 0<=phi[i]<=45 or 135<=phi[i]<=225 or 315<=phi[i]<=360:
    #     rmax=abs(int(np.cos(phi[i]*2*np.pi/360)*224))
    #     r=np.linspace(0,rmax,100)
    # elif 45<=phi[i]<=135 or 225<=phi[i]<=315:
    #     rmax=abs(int(np.sin(phi[i]*2*np.pi/360)*224))
    #     r=np.linspace(0,rmax,100)
    r=np.linspace(0,600,700)
    X=([])
    Y=([])
    #for l in range(len(r)):
        # x=int(r[l]*np.cos(phi[i]*2*np.pi/360))
        # y=int(r[l]*np.sin(phi[i]*2*np.pi/360))
        # X.append(x)                 #creo las coordenadas x e y para esa direccion en el plano xy
        # Y.append(y)
    distanciatotalmont5=([])
    for j in range(len(theta)):   ##vario el angulo respecto al eje z
        alturamont=0                ##inicializo la variable q guardará la altura de la montalla
        distanciamont=0             ##inicializo la variable q guardará la cantidad de montaña en esa dirección
        puntoscriticos=([])         ##inicializo el vector q contendra la cantidad de puntos en los que salimos o entramos de la montaña en esa dirección
        puntoscriticosalturas=([])  ##inicializo el vector q contendra la cantidad de puntos en los que salimos o entramos de la montaña en esa dirección
        alturas=([0])               ##inicializo el vector en el q guardaré las alturas de la recta
        X=([])
        Y=([])
        Z=([])
        for k in range(len(r)):            
            x=int(r[k]*np.cos(phi[i]*2*np.pi/360)*np.cos(theta[j]*2*np.pi/360))
            y=int(r[k]*np.sin(phi[i]*2*np.pi/360)*np.cos(theta[j]*2*np.pi/360))
            z=abs(r[k]*np.sin(theta[j]*2*np.pi/360))+matrixaux[225,225]      ##hay que sumar la elevación del centro
            X.append(x)                 #creo las coordenadas x e y para esa direccion en el plano xy
            Y.append(y)
            Z.append(z)
            if (0<=(225+x)<=(len(matrixaux)-1) and 0<=(225+y)<=(len(matrixaux))-1):
                if k==0 or k==1:
                    nada=0
                elif k==len(r)-1:
                    puntoscriticos.append(k)            ##guardamos siempre el último punto
                    puntoscriticosalturas.append(z)                 
                elif signo(matrixaux[225+X[k],225+Y[k]]-Z[k])!=signo(matrixaux[225+X[k-1],225+Y[k-1]]-Z[k-1]) :
                    puntoscriticos.append(k)
                    puntoscriticosalturas.append(z)            ##en el ultimo angulo guarda alturas que por la inclinación no tienen sentido
                alturamont=matrixaux[225+X[k],225+Y[k]]
            else:
                    puntoscriticos.append(k-1)            ##guardamos siempre el último punto
                    puntoscriticosalturas.append(Z[k-1])
                    break
        # if len(puntoscriticos)%2!=0:
        #     for l in range(len(puntoscriticos)//2):
        #         m=l*2
        #         ####aqui voy a calcular la distancia entre los puntos criticos que van seguidos, 
        #         ##que serán los de entrada y salida de la montaña.                
        #         # if l ==len(puntoscriticos)//2-1:
        #         #     # xmont=X[len(X)-1]-X[puntoscriticos[m]]      ##ya no tengo que ponerlo respecto al centro ya que queremos la distancia relativa entre los puntos
        #         #     # ymont=Y[len(X)-1]-Y[puntoscriticos[m]]
        #         #     # zmont=puntoscriticosalturas[len(puntoscriticosalturas)-1]-puntoscriticosalturas[m]
        #         #     frio=1
        #         # else:    
        #         xmont=X[puntoscriticos[m+1]]-X[puntoscriticos[m]]
        #         ymont=Y[puntoscriticos[m+1]]-Y[puntoscriticos[m]]
        #         zmont=Z[puntoscriticos[m+1]]-Z[puntoscriticos[m]]
        #         distanciamont1=np.sqrt(xmont**2+ymont**2+zmont**2)
        #         distanciamont+=distanciamont1
        # else:
        for l in range(len(puntoscriticos)//2):
                ####aqui voy a calcular la distancia entre los puntos criticos que van seguidos, 
                ##que serán los de entrada y salida de la montaña.                
            m=l*2
            xmont=X[puntoscriticos[m+1]]-X[puntoscriticos[m]]
            ymont=Y[puntoscriticos[m+1]]-Y[puntoscriticos[m]]
            zmont=Z[puntoscriticos[m+1]]-Z[puntoscriticos[m]]
            distanciamont1=np.sqrt(xmont**2+ymont**2+zmont**2)
            distanciamont+=distanciamont1
        print(puntoscriticos)
        distanciatotalmont5.append(distanciamont)
    dist5.append(distanciatotalmont5)
    
#%%
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x1=np.zeros((450,450))
y1=np.zeros((450,450))
for i in range(1,450):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    y1[:,i]=i
    x1[i,:]=i
    
ax.plot_surface(X=x1,Y=y1,Z=matrixaux,color="sandybrown")

#%%
dist5=np.array(dist5)
dist5=dist5[:,::-1]
dist5=dist5.T
#%%
fig = plt.figure()
plt.imshow(dist5, extent=(0,360,0,90),cmap="rainbow")
#plt.yticks(range(90))

#plt.ylim(0,90)
#plt.clim(0 ,0.1)
plt.colorbar()
plt.show()
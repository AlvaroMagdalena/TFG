# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:15:59 2022

@author: Álvaro Magdalena 
"""
import numpy as np
import matplotlib.pyplot as plt
import os 
from pathlib import Path

from dted import LatLon, Tile

plt.close("all")

#########################################################
# Make a list with files to be plotted
#path='/Users/jaime/Dropbox/tmp/'
path="/Documentos/Universidad/Física/4º/TFG/Topography/"
# Select dted formatted files
end_of_file='.dt2'
text_in_file=('s35_w069','s35_w070','s35_w071','s36_w069','s36_w070','s36_w071','s37_w069','s37_w070','s37_w071')

#text_in_file='n42_w009'

# File list  
list_path_file = []   
list_file = [] 
for j in range(len(text_in_file)):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(end_of_file) and text_in_file[j] in f]:  
            path_with_filename=os.path.join(dirpath, filename)
            # path with filename
            list_path_file.append(path_with_filename)
            # filename only
            list_file.append(filename)
        list_path_file.sort() 
        list_file.sort() 

    for i in range(len(list_path_file)):
        print(list_path_file[i])
       #print(list_file)

dted_file = Path(list_path_file[0])
tile = Tile(dted_file)
print(len(tile.data))
print(len(list_path_file))
a=np.zeros((len(tile.data)*3,len(tile.data)*3),dtype=int)
##################################################
# Process .dt2 files 
b=2
m=0
for filename_with_path in list_path_file:
    fig = plt.figure()
    print(b,m)

    dted_file = Path(filename_with_path)
    tile = Tile(dted_file)
            #tile = Tile(dted_file, in_memory=False)
        # Put file in a numpy array
            #assert isinstance(tile.data, np.ndarray)
        
        # Latitude and Longitude of corners of map
    print(tile.dsi.south_west_corner, tile.dsi.north_east_corner)
        
        # Maximum and minimum elevation of file
    print(tile.data.max(),tile.data.min())
        
    a[m*len(tile.data):(m+1)*len(tile.data),b*len(tile.data):(b+1)*len(tile.data)]=tile.data.T[::-1]    
        # Plot files 
            #print(tile.data.T[::-1])
    plt.imshow(tile.data.T[::-1], cmap="rainbow")
    plt.clim(0 ,5500)
    plt.colorbar()
    plt.show()
    b-=1
    if (b==(-1)):
        b=2
        m+=1        ##cambio fila al recorrer las columnas
fig = plt.figure()
plt.imshow(a, cmap="rainbow")
plt.clim(0 ,5500)
plt.colorbar()
plt.show()
#%%


fig = plt.figure()
ax5 = fig.add_subplot(projection='3d')
#z=np.array([tile.data[0]])
matrixaux=np.zeros((int((len(tile.data)-1)/80),int((len(tile.data)-1)/80)))
for i in range(3*len(tile.data)-3):
    for j in range(3*len(tile.data)-3):
        if (i+1)%240==0:
            if (j+1)%240==0:
                matrixaux[int(i/240),int(j/240)]=a[i,j]
x6=np.zeros((int((len(tile.data)-1)/80),int((len(tile.data)-1)/80)))
y6=np.zeros((int((len(tile.data)-1)/80),int((len(tile.data)-1)/80)))

## USAR LA SIGUIENTE PÁGINA WEB PARA CALCULAR RÁPIDO

##https://es.planetcalc.com/73/

for i in range(1,int((len(tile.data)-1)/80)):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    ##PROBLEMA
    ##He multiplicado en la línea anterior x2 para que dé como la captura de pantalla, pero no sé como conseguir ese x2
    y6[:,i]=i*4.048178*2    ##multiplico por ese número porque tenemos 45 y la latitud total es 182.168km, 182.168/45=4.048178
    
    x6[i,:]=i*4.942         ##multiplico por ese número porque tenemos 45 y la longitud total es 222.390km, 222.390/45=4.942
ax5.plot_surface(X=x6,Y=y6,Z=matrixaux,color="sandybrown")

#%%


fig = plt.figure()
ax5 = fig.add_subplot(projection='3d')
#z=np.array([tile.data[0]])
matrixaux=np.zeros((len(a),len(a)))
for i in range(10,len(a)-10):
    for j in range(10,len(a)-10):
        matrixaux[i,j]=sum(sum(a[i-10:i+10,j-10:j+1]))/200
matrixaux[0:9,:]=a[0:9,:]
matrixaux[:,0:9]=a[:,0:9]
matrixaux[10794:10803,:]=a[10794:10803,:]
matrixaux[:,10794:10803]=a[:,10794:10803]
x6=np.zeros((len(a),len(a)))
y6=np.zeros((len(a),len(a)))

## USAR LA SIGUIENTE PÁGINA WEB PARA CALCULAR RÁPIDO

##https://es.planetcalc.com/73/

for i in range(1,len(a)):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    ##PROBLEMA
    ##He multiplicado en la línea anterior x2 para que dé como la captura de pantalla, pero no sé como conseguir ese x2
    y6[:,i]=i*0.0168627*2    ##multiplico por ese número porque tenemos 45 y la latitud total es 182.168km, 182.168/10803=0.0168627
    
    x6[i,:]=i*0.020589         ##multiplico por ese número porque tenemos 45 y la longitud total es 222.390km, 222.390/10803=0.020589
ax5.plot_surface(X=x6,Y=y6,Z=matrixaux,color="sandybrown")
#%%

def signo(a):
    if a>=0:
        b=1
    elif a<0:
        b=0
    return(b)

theta=np.linspace(0,90,181)
phi=np.linspace(0,360,361)
dist5=([])
for i in range(len(phi)):           ##vario el angulo "polar en el plano xy"
    r=np.linspace(0,12000,14000)
    X=([])
    Y=([])
    distanciatotalmont5=([])
    for j in range(len(theta)):   ##vario el angulo respecto al eje z
        alturamont=0                ##inicializo la variable q guardará la altura de la montalla
        distanciamont=0             ##inicializo la variable q guardará la cantidad de montaña en esa dirección
        puntoscriticos=([])         ##inicializo el vector q contendra la cantidad de puntos en los que salimos o entramos de la montaña en esa dirección
        puntoscriticosalturas=([])  ##inicializo el vector q contendra la cantidad de puntos en los que salimos o entramos de la montaña en esa dirección
        X=([])
        Y=([])
        XKM=([])
        YKM=([])
        Z=([])
        for k in range(len(r)):   
            xkm=r[k]*np.cos(phi[i]*2*np.pi/360)*np.cos(theta[j]*2*np.pi/360)
            ykm=r[k]*np.sin(phi[i]*2*np.pi/360)*np.cos(theta[j]*2*np.pi/360)
            x=int(xkm/0.020589)
            y=int(ykm/(0.0168627*2))
            z=abs(r[k]*np.sin(theta[j]*2*np.pi/360))+matrixaux[5401,5401]      ##hay que sumar la elevación del centro
            X.append(x)                 #creo las coordenadas x e y para esa direccion en el plano xy
            Y.append(y)
            XKM.append(xkm)
            YKM.append(ykm)
            Z.append(z)
            if (0<=(5401+x)<=(len(matrixaux)-1) and 0<=(5401+y)<=(len(matrixaux))-1):
                if k==0 or k==1:
                    nada=0
                elif k==len(r)-1:
                    puntoscriticos.append(k)            ##guardamos siempre el último punto
                    puntoscriticosalturas.append(z)                 
                elif signo(matrixaux[5401+X[k],5401+Y[k]]-Z[k])!=signo(matrixaux[5401+X[k-1],5041+Y[k-1]]-Z[k-1]) :
                    puntoscriticos.append(k)
                    puntoscriticosalturas.append(z)            ##en el ultimo angulo guarda alturas que por la inclinación no tienen sentido
                alturamont=matrixaux[5401+X[k],5401+Y[k]]
            else:
                    puntoscriticos.append(k-1)            ##guardamos siempre el último punto
                    puntoscriticosalturas.append(Z[k-1])
                    break
        for l in range(len(puntoscriticos)//2):               
            m=l*2
            xmont=XKM[puntoscriticos[m+1]]-XKM[puntoscriticos[m]]
            ymont=YKM[puntoscriticos[m+1]]-YKM[puntoscriticos[m]]
            zmont=Z[puntoscriticos[m+1]]-Z[puntoscriticos[m]]
            distanciamont1=np.sqrt(xmont**2+ymont**2+zmont**2)
            distanciamont+=distanciamont1
        print(puntoscriticos)
        distanciatotalmont5.append(distanciamont)
    dist5.append(distanciatotalmont5)
    
#%%
dist6=np.array(dist5)
#dist6=dist6[:,::-1]
dist6=dist6[::-1,:]
dist6=dist6.T

#%%
fig = plt.figure()
plt.imshow(dist6, extent=(0,360,0,90),cmap="rainbow")
#plt.yticks(range(90))

#plt.ylim(0,90)
plt.clim(0 ,0.1)
plt.colorbar()
plt.show()
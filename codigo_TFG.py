# Parser for DTED (Digital Terrain Elevation Data)
# DTED data obtained from: https://earthexplorer.usgs.gov/
# File extension is .dt2
# Small tutorial on parser available at: https://pythonrepo.com/repo/bbonenfant-dted

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
ax1 = fig.add_subplot(projection='3d')
#z=np.array([tile.data[0]])
matrixaux=np.zeros((int(len(tile.data)/13),int(len(tile.data)/13)))
for i in range(3*len(tile.data)):
    for j in range(3*len(tile.data)):
        if (i+1)%39==0:
            if (j+1)%39==0:
                matrixaux[int(i/39),int(j/39)]=a[i,j]
x2=np.zeros((int(len(tile.data)/13),int(len(tile.data)/13)))
y2=np.zeros((int(len(tile.data)/13),int(len(tile.data)/13)))
for i in range(1,int(len(tile.data)/13)):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    y2[:,i]=i
    x2[i,:]=i      
ax1.plot_surface(X=x2,Y=y2,Z=matrixaux,color="sandybrown")
#%%
fig = plt.figure()
ax2 = fig.add_subplot(projection='3d')
#z=np.array([tile.data[0]])
matrixaux2=np.zeros((int(len(tile.data)/277),int(len(tile.data)/277)))
for i in range(3*len(tile.data)):
    for j in range(3*len(tile.data)):
        if (i+1)%831==0:
            if (j+1)%831==0:
                matrixaux2[int(i/831),int(j/831)]=a[i,j]
x3=np.zeros((int(len(tile.data)/277),int(len(tile.data)/277)))
y3=np.zeros((int(len(tile.data)/277),int(len(tile.data)/277)))
for i in range(1,int(len(tile.data)/277)):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    y3[:,i]=i
    x3[i,:]=i      
ax2.plot_surface(X=x3,Y=y3,Z=matrixaux2,color="sandybrown")
#%%
fig = plt.figure()
ax3 = fig.add_subplot(projection='3d')
#z=np.array([tile.data[0]])
matrixaux3=np.zeros((int((len(tile.data)-1)/30),int((len(tile.data)-1)/30)))
for i in range(3*len(tile.data)-3):
    for j in range(3*len(tile.data)-3):
        if (i+1)%90==0:
            if (j+1)%90==0:
                matrixaux3[int(i/90),int(j/90)]=a[i,j]
x4=np.zeros((int((len(tile.data)-1)/30),int((len(tile.data)-1)/30)))
y4=np.zeros((int((len(tile.data)-1)/30),int((len(tile.data)-1)/30)))
for i in range(1,int((len(tile.data)-1)/30)):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    y4[:,i]=i
    x4[i,:]=i      
ax3.plot_surface(X=x4,Y=y4,Z=matrixaux3,color="sandybrown")
#%%
fig = plt.figure()
ax4 = fig.add_subplot(projection='3d')
#z=np.array([tile.data[0]])
matrixaux4=np.zeros((int((len(tile.data)-1)/50),int((len(tile.data)-1)/50))) 
for i in range(3*len(tile.data)-3):         
    for j in range(3*len(tile.data)-3):
        if (i+1)%150==0:                    
            if (j+1)%150==0:
                matrixaux4[int(i/150),int(j/150)]=a[i,j]
x5=np.zeros((int((len(tile.data)-1)/50),int((len(tile.data)-1)/50)))
y5=np.zeros((int((len(tile.data)-1)/50),int((len(tile.data)-1)/50)))
for i in range(1,int((len(tile.data)-1)/50)):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    y5[:,i]=i
    x5[i,:]=i      
ax4.plot_surface(X=x5,Y=y5,Z=matrixaux4,color="sandybrown")
#%%
####################################
##CREO QUE EL MEJOR
####################################

fig = plt.figure()
ax5 = fig.add_subplot(projection='3d')
#z=np.array([tile.data[0]])
matrixaux5=np.zeros((int((len(tile.data)-1)/80),int((len(tile.data)-1)/80)))
for i in range(3*len(tile.data)-3):
    for j in range(3*len(tile.data)-3):
        if (i+1)%240==0:
            if (j+1)%240==0:
                matrixaux5[int(i/240),int(j/240)]=a[i,j]
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
ax5.plot_surface(X=x6,Y=y6,Z=matrixaux5,color="sandybrown")
#%%
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x1=np.zeros((3*len(tile.data),3*len(tile.data)))
y1=np.zeros((3*len(tile.data),3*len(tile.data)))
for i in range(1,3*len(tile.data)):
    #z=np.vstack([z,tile.data.T[len(tile.data)-i]])
    y1[:,i]=i
    x1[i,:]=i
    
ax.plot_surface(X=x1,Y=y1,Z=a,color="sandybrown")

#%%
#ax.plot_surface(x0,y0,z02,color="b")
#ax.set_xlabel("x")
#ax.set_ylabel("y")
#ax.set_zlabel("z")
#ax.set_title("Agujero de Ellis")


#    for lat in np.arange(-36.,-35.,0.05):
#       for long in np.arange(-70.,-69.,0.05):
#           print(lat,long,tile.get_elevation(LatLon(latitude=lat, longitude=long)))

#%%
##pruebas segunda parte
##los cuadrantes tienen un grado de longitud*un grado de latitud.
##Un grado de longitud=111.1 km (91.17 según la calculadora https://www.tutiempo.net/calcular-distancias.html o si no, usar esta también https://es.planetcalc.com/73/)
##Un grado de latitud=40.000 km/360 grados=111.30 km

##el array tile.data contiene 9 cuadrados con 3601x3601 datos de alturas
##podemos dividir el array en cuadrados de 111.1km/(3601)=0.030852540960844207 km por 111.3km/(3601)=0.030908081088586503 km

##tomamos el punto medio como origen de coordenadas (a[int(len(a)/2),int(len(a)/2)]), que equivaldrá a las coordenadas S36W70

##el ángulo theta mide la inclinación de la trayectoria respecto al plano horizontal y phi gira respecto al eje vertical

##Realmente, las coordenadas que queremos tomar como nuestro centro son:
##latitud_Auger=-35.235937    (equivalentemente 35.235937 South)
##longitud_Auger=-69.249965 (equivalentemente 69.249965 West)

##nuestra región va desde 34-37S 68-71W, por lo que nuestro centro realmente lo habíamos situado en 35.5S 69.5W
theta=np.linspace(0,90,91)
phi=np.linspace(0,360,361)
dist=([])
for i in range(len(phi)):
    if 0<=phi[i]<=45 or 135<=phi[i]<=225 or 315<=phi[i]<=360:
        rmax=abs(int(np.cos(phi[i]*2*np.pi/360)*5401))
        r=np.linspace(0,rmax,7000)
    elif 45<=phi[i]<=135 or 225<=phi[i]<=315:
        rmax=abs(int(np.sin(phi[i]*2*np.pi/360)*5401))
        r=np.linspace(0,rmax,7000)
    # if 0<=phi[i]<=90:
    #     horizontal=1
    #     vertical=1
    # elif 90<=phi[i]<=180:
    #     horizontal=0
    #     vertical=1
    # elif 180<=phi[i]<=270:
    #     horizontal=0
    #     vertical=0
    # elif 270<=phi[i]<=360:
    #     horizontal=1
    #     vertical=0
    X=([])
    Y=([])
    for l in range(len(r)):
        x=int(r[l]*np.cos(phi[i]*2*np.pi/360))
        y=int(r[l]*np.sin(phi[i]*2*np.pi/360))
        X.append(x)
        Y.append(y)
    xmin=0.030852540960844207*np.cos(phi[i]*2*np.pi/360)            ##esto mal
    ymin=0.030908081088586503*np.sin(phi[i]*2*np.pi/360)
    distanciamin=np.sqrt(xmin**2+ymin**2)
    distanciatotalmont=([])
    for j in range(len(theta)):
        alturamont=0
        m=0
        for k in range(len(r)):
            z=abs(r[k]*np.sin(theta[j]*2*np.pi/360))+a[5401,5401] ##hay que sumar la elevación del centro
            if alturamont!=a[5401+X[k],5401+Y[k]]:
                alturamont=a[5401+X[k],5401+Y[k]]
                if z<a[5401+X[k],5401+Y[k]]:
                    m+=distanciamin
        distanciatotalmont.append(m)
    dist.append(distanciatotalmont)
    
#%%

fig = plt.figure()
plt.imshow(np.array(dist).T, cmap="rainbow")
plt.ylim(0,90)
#plt.clim(0 ,0.1)
plt.colorbar()
plt.show()

#%%
##intento desplazar el centro
theta=np.linspace(0,90,91)
phi=np.linspace(0,360,361)
dist2=([])

##comenzamos encontrando el centro en todos nuestros datos, tenemos 9 cuadrados de 3601x3601 datos. 
##originalmente lo teníamos en el medio, en el dato (5402,5402) que equivale al punto 35.5s, 69.5w.
##realmente debería estar en 35.235937 S 69.249965 W. Como recorremos 3 grados en 10803 datos, podemos ver que
##3/10803=0.00027770063871146905 grados por dato. Debemos movernos 35.5-35.235937=0.264063 norte y 69.5-69.249965=0.250035 este.
##esto equivale a 0.264063/0.00027770063871146905=950.891 datos norte y 0.250035/0.00027770063871146905=900.376 datos este.
##por lo que nuestro dato central será [5401-951,5401+900]=[4450,6301] (recordando que el primer dato será el [0,0])

##tengo que descubrir los ángulos con los que choca con las esquinas de nuestra región cuadrada de estudio.
##estos puntos serán en los que un cateto que era constante empiece a variar

##para ello voy a comparar la y para cierto x constante, cuando esta y sea mayor al maximo será que está en la esquina.

##empezamos suponiendo que el x max será 10803-6301=4502 y haciendo que y sea menor que 4450

for i in range(len(phi)):
    if abs(np.tan(phi[i]*2*np.pi/360)*4502)>=4450:
        ang1=phi[i]
        break
for i in range(np.where(phi==ang1)[0][0],len(phi)):
    if abs(4450/np.tan(phi[i]*2*np.pi/360))>=6301:
        ang2=phi[i]
        break
for i in range(np.where(phi==ang2)[0][0],len(phi)):
    if abs(6301*np.tan(phi[i]*2*np.pi/360))>=6353:
        ang3=phi[i]
        break
for i in range(np.where(phi==ang3)[0][0],len(phi)):
    if abs(6353/np.tan(phi[i]*2*np.pi/360))>=4502:
        ang4=phi[i]
        break
for i in range(len(phi)):
    if 0<=phi[i]<=ang1 or ang4<=phi[i]<=360:
        rmax=abs(int(np.cos(phi[i]*2*np.pi/360)*4502))
        r=np.linspace(0,rmax,7000)
    elif ang1<=phi[i]<=ang2:
        rmax=abs(int(np.sin(phi[i]*2*np.pi/360)*4450))
        r=np.linspace(0,rmax,7000)
    elif ang2<=phi[i]<=ang3:
        rmax=abs(int(np.cos(phi[i]*2*np.pi/360)*6301))
        r=np.linspace(0,rmax,7000) 
    elif ang3<=phi[i]<=ang4:
        rmax=abs(int(np.sin(phi[i]*2*np.pi/360)*6353))
        r=np.linspace(0,rmax,7000)         
    X2=([])
    Y2=([])
    for l in range(len(r)):
        x=int(r[l]*np.cos(phi[i]*2*np.pi/360))
        y=int(r[l]*np.sin(phi[i]*2*np.pi/360))
        X2.append(x)
        Y2.append(y)
    if 0<=phi[i]<=45 or 135<=phi[i]<=225 or 315<=phi[i]<=360:
        #xmin=0.030852540960844207
        #ymin=0.030852540960844207*np.tan(phi[i]*2*np.pi/360)
        distanciamin=abs(0.030852540960844207*np.cos(phi[i]*2*np.pi/360))
    elif 45<=phi[i]<=135 or 225<=phi[i]<=315:
        #xmin=np.tan(phi[i]*2*np.pi/360)/0.030908081088586503
        #ymin=0.030908081088586503
        distanciamin=abs(np.sin(phi[i]*2*np.pi/360)*0.030908081088586503)
    #distanciamin=np.sqrt(xmin**2+ymin**2)
    distanciatotalmont2=([])
    for j in range(len(theta)):
        alturamont=0
        m=0
        for k in range(len(r)):
            z=abs(r[k]*np.sin(theta[j]*2*np.pi/360))+a[4450,6301] ##hay que sumar la elevación del centro
            if alturamont!=a[4450+X2[k],6301+Y2[k]]:
                alturamont=a[4450+X2[k],6301+Y2[k]]
                if z<a[4450+X2[k],6301+Y2[k]]:
                    m+=abs(distanciamin*np.sin(theta[j]*2*np.pi/360))
        distanciatotalmont2.append(m)
    dist2.append(distanciatotalmont2)
    
#%%

fig = plt.figure()
plt.imshow(np.array(dist2).T, cmap="rainbow")
plt.ylim(0,90)
#plt.clim(0 ,0.1)
plt.colorbar()
plt.show()

#%%

theta=np.linspace(0,90,91)
phi=np.linspace(0,360,361)
dist3=([])
for i in range(len(phi)):
    if 0<=phi[i]<=45 or 135<=phi[i]<=225 or 315<=phi[i]<=360:
        rmax=abs(int(np.cos(phi[i]*2*np.pi/360)*5401))
        r=np.linspace(0,rmax,7000)
    elif 45<=phi[i]<=135 or 225<=phi[i]<=315:
        rmax=abs(int(np.sin(phi[i]*2*np.pi/360)*5401))
        r=np.linspace(0,rmax,7000)
    X2=([])
    Y2=([])
    for l in range(len(r)):
        x=int(r[l]*np.cos(phi[i]*2*np.pi/360))
        y=int(r[l]*np.sin(phi[i]*2*np.pi/360))
        X2.append(x)
        Y2.append(y)
    if 0<=phi[i]<=45 or 135<=phi[i]<=225 or 315<=phi[i]<=360:
        distanciamin=abs(0.030852540960844207*np.cos(phi[i]*2*np.pi/360))
    elif 45<=phi[i]<=135 or 225<=phi[i]<=315:
        distanciamin=abs(np.sin(phi[i]*2*np.pi/360)*0.030908081088586503)
    distanciatotalmont3=([])
    for j in range(len(theta)):
        alturamont=0
        m=0
        for k in range(len(r)):
            z=abs(r[k]*np.sin(theta[j]*2*np.pi/360))+a[5401,5401] ##hay que sumar la elevación del centro
            if alturamont!=a[5401+X2[k],5401+Y2[k]]:
                alturamont=a[5401+X2[k],5401+Y2[k]]
                if z<a[5401+X2[k],5401+Y2[k]]:
                    m+=abs(distanciamin*np.sin(theta[j]*2*np.pi/360))
        distanciatotalmont3.append(m)
    dist3.append(distanciatotalmont3)

#%%

fig = plt.figure()
plt.imshow(np.array(dist3).T, cmap="rainbow")
plt.ylim(0,90)
#plt.clim(0 ,0.1)
plt.colorbar()
plt.show()

#%%
####################################
##INTENTO OTRO METODO
####################################

##La idea será marcar el punto de entrada y de salida de 
##la montaña y calcular directamente la distancia entre los dos puntos.

def signo(a):
    if a>=0:
        b=1
    elif a<0:
        b=0
    return(b)

theta=np.linspace(0,90,91)
phi=np.linspace(0,360,361)
dist4=([])
for i in range(len(phi)):
    if 0<=phi[i]<=45 or 135<=phi[i]<=225 or 315<=phi[i]<=360:
        rmax=abs(int(np.cos(phi[i]*2*np.pi/360)*22))
        r=np.linspace(0,rmax,100)
    elif 45<=phi[i]<=135 or 225<=phi[i]<=315:
        rmax=abs(int(np.sin(phi[i]*2*np.pi/360)*22))
        r=np.linspace(0,rmax,100)
    X=([])
    Y=([])
    for l in range(len(r)):
        x=int(r[l]*np.cos(phi[i]*2*np.pi/360))
        y=int(r[l]*np.sin(phi[i]*2*np.pi/360))
        X.append(x)
        Y.append(y)
    distanciatotalmont4=([])
    for j in range(len(theta)):
        alturamont=0
        distanciamont=0
        puntoscriticos=([])
        puntoscriticosalturas=([])
        alturas=([100000])
        for k in range(len(r)):
            z=abs(r[k]*np.sin(theta[j]*2*np.pi/360))+matrixaux5[22,22]      ##hay que sumar la elevación del centro
            alturas.append(z)
            if k==len(r)-1:
                puntoscriticosalturas.append(z)    
            elif signo(matrixaux5[22+X[k],22+Y[k]]-z)!=signo(matrixaux5[22+X[k+1],22+Y[k+1]]-alturas[k]) :
                puntoscriticos.append(k)
                puntoscriticosalturas.append(z)            
            alturamont=matrixaux5[22+X[k],22+Y[k]]
        if len(puntoscriticos)%2!=0:
            for l in range(len(puntoscriticosalturas)//2):
                m=l*2
                ####aqui voy a calcular la distancia entre los puntos criticos que van seguidos, 
                ##que serán los de entrada y salida de la montaña.                
                if l ==len(puntoscriticosalturas)//2-1:
                    xmont=X[len(X)-1]-X[puntoscriticos[m]]      ##ya no tengo que ponerlo respecto al centro ya que queremos la distancia relativa entre los puntos
                    ymont=Y[len(X)-1]-Y[puntoscriticos[m]]
                    zmont=puntoscriticosalturas[len(puntoscriticosalturas)-1]-puntoscriticosalturas[m]
                else:    
                    xmont=X[puntoscriticos[m+1]]-X[puntoscriticos[m]]
                    ymont=Y[puntoscriticos[m+1]]-Y[puntoscriticos[m]]
                    zmont=puntoscriticosalturas[m+1]-puntoscriticosalturas[m]
                distanciamont1=np.sqrt(xmont**2+ymont**2+zmont**2)
                distanciamont+=distanciamont1
        else:
            for l in range(len(puntoscriticosalturas)//2):
                ####aqui voy a calcular la distancia entre los puntos criticos que van seguidos, 
                ##que serán los de entrada y salida de la montaña.                
                m=l*2
                xmont=X[puntoscriticos[m+1]]-X[puntoscriticos[m]]
                ymont=Y[puntoscriticos[m+1]]-Y[puntoscriticos[m]]
                zmont=puntoscriticosalturas[m+1]-puntoscriticosalturas[m]
                distanciamont1=np.sqrt(xmont**2+ymont**2+zmont**2)
                distanciamont+=distanciamont1
        distanciatotalmont4.append(distanciamont)
    dist4.append(distanciatotalmont4)
#%%

fig = plt.figure()
plt.imshow(np.array(dist4).T, cmap="rainbow")
plt.ylim(0,90)
#plt.clim(0 ,0.1)
plt.colorbar()
plt.show()

#%%
#from qgis.core import *
#import qgis.utils

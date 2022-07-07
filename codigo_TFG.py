import numpy as np
import matplotlib.pyplot as plt
import os 
from pathlib import Path
from dted import LatLon, Tile

plt.close("all")

path="/Documentos/Universidad/Física/4º/TFG/Topography/" # Directorio donde se encuentran los archivos

# Escribimos los nombres de los archivos con los datos de las alturas
end_of_file='.dt2'
text_in_file=('s35_w069','s35_w070','s35_w071','s36_w069','s36_w070','s36_w071','s37_w069','s37_w070','s37_w071')

# creamos lista con todos los nombres de los archivos
list_path_file = []   
list_file = [] 
for j in range(len(text_in_file)):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(end_of_file) and text_in_file[j] in f]:  
            path_with_filename=os.path.join(dirpath, filename)
            list_path_file.append(path_with_filename)       # directorio con nombre del archivo      
            list_file.append(filename)                      # nombre del archivo
        list_path_file.sort() 
        list_file.sort() 

dted_file = Path(list_path_file[0])         # estas dos líneas las necesitamos solo para crear la matriz a con el tamaño adecuado
tile = Tile(dted_file)

a=np.zeros((len(tile.data)*3,len(tile.data)*3),dtype=int)   # creo la matriz donde guardaré las 9 matrices juntas
b=2
m=0
for filename_with_path in list_path_file:
    fig = plt.figure()

    dted_file = Path(filename_with_path)    
    tile = Tile(dted_file)  # guardamos los datos de cada matriz
        
    a[m*len(tile.data):(m+1)*len(tile.data),b*len(tile.data):(b+1)*len(tile.data)]=tile.data.T[::-1]    # añadimos cada matriz en su posición correcta a la matriz a

    plt.imshow(tile.data.T[::-1], cmap="rainbow")   # imprimo individualmente cada matriz
    plt.xlabel("longitud (U)")
    plt.ylabel("latitud (U)")
    plt.clim(0 ,5500)       # mantenemos una escala constante entre todas las gráficas
    plt.colorbar()
    plt.show()
    b-=1
    if (b==(-1)):
        b=2
        m+=1        # cambio fila al recorrer todas las columnas
        
fig = plt.figure()
plt.imshow(a, cmap="rainbow")
plt.xlabel("longitud (U)")
plt.ylabel("latitud (U)")
plt.clim(0 ,5500)
plt.colorbar()
plt.show()

###############
###SUAVIZADO###
###############

a=a[::-1,:].T   # rotamos la matriz con los datos para tener correctamente la longitud en el eje x y la latitud en el y
asuavizado=np.copy(a)     
   
for i in range(300,len(a)-300):     # suavizamos mucho los puntos en el interior de la matriz
    for j in range(300,len(a)-300):
        asuavizado[i,j]=sum(sum(a[i-300:i+300,j-300:j+300]))/360000
        
for i in range(0,10803):            # suavizamos mucho menos los puntos del exterior de la matriz
    for j in range(40,300):
        asuavizado[i,j]=sum(a[i,j-40:j+40])/80
        asuavizado[i,10803-j]=sum(a[i,10803-j-40:10803-j+40])/80
        asuavizado[j,i]=sum(a[j-40:j+40,i])/80
        asuavizado[10803-j,i]=sum(a[10803-j-40:10803-j+40,i])/80

################################################
###REPRESENTACIÓN 3D SUAVIZADO Y SIN SUAVIZAR###
################################################

xreal=np.zeros((len(a),len(a)))
yreal=np.zeros((len(a),len(a)))
for i in range(1,len(a)):       # creo los ejes con la escala adecuada
    yreal[:,i]=i*0.0308789          # multiplico por ese número porque tenemos 45 y la latitud total es 333,5852km, 333,5852/10803=0.0308789
    xreal[i,:]=i*0.022512944552     # multiplico por ese número porque tenemos 45 y la longitud total es 271,4734km, 271,4734/10803=0.022512944552

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X=xreal,Y=yreal,Z=asuavizado,color="sandybrown")    # representación 3d del suavizado
ax.set_xlabel('longitud (km)')
ax.set_ylabel('latitud (km)')
ax.set_zlabel('Altura (m)')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X=xreal,Y=yreal,Z=a,color="sandybrown")             # representación 3d de los datos originales
ax.set_xlabel('longitud (km)')
ax.set_ylabel('latitud (km)')
ax.set_zlabel('Altura (m)')

##########################################################
###CÁLCULO CANTIDAD DE MONTAÑA ATRAVESADA POR DIRECCIÓN###
##########################################################

def signo(a):   # creo la función que nos dirá si el valor es positivo (1) o negativo (0)
    if a>=0:
        b=1
    elif a<0:
        b=0
    return(b)

theta=np.linspace(0,3,46)      # creo el ángulo de alturas entre 0 y 10 grados
phi=np.linspace(0,360,361)      # creo el ángulo acimutal entre 0 y 360 grados
dist=([])                       # creo la matriz donde guardaré todas las distancias recorridas por el neutrino dentro de la montaña según su dirección
r=np.linspace(0,350000,10000)   # creo el vector que recorrerá la recta de la trayectoria del neutrino, la distancia máxima serán 350 km
for i in range(len(phi)):           # vario el ángulo acimutal
    distanciatotalmont=([])         # creo el vector donde guardaré todas las distancias recorridas por el neutrino dentro de la montaña para ese ángulo acimutal
    for j in range(len(theta)):     # vario el ángulo de alturas
        distanciamont=0             # inicializo la variable que guardará la cantidad de montaña en esa dirección
        puntoscriticos=([])         # inicializo el vector que guardará la cantidad de puntos en los que salimos o entramos de la montaña en esa dirección
        X=([])                      # inicializo el vector que guardará las coordenadas x de los puntos que recorrerá el neutrino
        Y=([])                      # inicializo el vector que guardará las coordenadas y de los puntos que recorrerá el neutrino
        XKM=([])                    # inicializo el vector que guardará las coordenadas x de los puntos que recorrerá el neutrino en km
        YKM=([])                    # inicializo el vector que guardará las coordenadas y de los puntos que recorrerá el neutrino en km
        Z=([])                      # inicializo el vector que guardará las alturas de los puntos que recorrerá el neutrino
        for k in range(len(r)):     # recorro los puntos de la recta
            xkm=r[k]*np.cos(phi[i]*2*np.pi/360)*np.cos(theta[j]*2*np.pi/360)    # calculo la coordenada x (en km) de cada punto
            ykm=r[k]*np.sin(phi[i]*2*np.pi/360)*np.cos(theta[j]*2*np.pi/360)    # calculo la coordenada y (en km) de cada punto
            x=int(xkm/(0.022512944552*1000))
            y=int(ykm/(0.0308789*1000))
            z=abs(r[k]*np.sin(theta[j]*2*np.pi/360))+asuavizado[6302,6352]      # calculo la altura de cada punto, hay que sumar la elevación del observatorio que es el punto de referencia
            X.append(x)
            Y.append(y)
            XKM.append(xkm)
            YKM.append(ykm)
            Z.append(z)
            if (0<=(6302+x)<=(len(asuavizado)-1) and 0<=(6352+y)<=(len(asuavizado))-1): # si el punto de la recta respecto al observatorio está dentro de la región de estudio continuamos con el análisis
                if k==0 or k==1:    # obviamos los dos primeros puntos ya que pueden dar problemas
                    nada=0
                elif k==len(r)-1:   # guardamos siempre el último punto como explicamos en el tfg
                    puntoscriticos.append(k)            
                elif signo(asuavizado[6302+X[k],6352+Y[k]]-Z[k])!=signo(asuavizado[6302+X[k-1],6352+Y[k-1]]-Z[k-1]): #si la diferencia de entre la altura de la recta y la altura de la montaña cambia de signo respecto al punto anterior quiere decir que hemos entrado o salido en la montaña
                    puntoscriticos.append(k)
            else:                   # en el caso de salir de la región de estudio también guardamos el último punto y rompemos el bucle
                    puntoscriticos.append(k-1)            
                    break
        for l in range(len(puntoscriticos)//2):     # recorremos la mitad de los puntos críticos y calculamos la distancia entre ellos dos a dos           
            m=l*2
            xmont=XKM[puntoscriticos[m+1]]-XKM[puntoscriticos[m]]
            ymont=YKM[puntoscriticos[m+1]]-YKM[puntoscriticos[m]]
            zmont=Z[puntoscriticos[m+1]]-Z[puntoscriticos[m]]
            distanciamont1=np.sqrt(xmont**2+ymont**2+zmont**2)
            distanciamont+=distanciamont1           # sumamos todas las distancias ya que pudo haber entrado y salido de varias montañas
        distanciatotalmont.append(distanciamont)    # guardamos la distancia total en el vector de distancias de este ángulo de altura
    dist.append(distanciatotalmont)                 # guardamos el vector de distancias de este ángulo de altura dentro de la matriz que contendrá todas las distancias
    
dist=np.array(dist)     # convertimos a array de numpy y lo rotamos
dist=dist[:,::-1].T

#################################################################
###REPRESENTACIÓN CANTIDAD DE MONTAÑA ATRAVESADA POR DIRECCIÓN###
#################################################################

fig = plt.figure()
plt.imshow(dist, extent=(0,360,0,90),cmap="rainbow")
plt.xlabel("A($^o$)")
plt.ylabel("h($^o$)")
plt.colorbar()
plt.show()

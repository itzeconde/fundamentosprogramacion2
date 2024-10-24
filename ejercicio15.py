'''
pide al usuario dos pares de numeros x1,y2 y x2, y2
 que representen dos puntos en el plano. calcula y muestra la distacia entre ellos'''

x1=input("Cual es el primer numero x:")
x1=int(x1)

y1=input("cual es el primer numero Y: ")
y1=int(y1)

x2=input("cual es el segundo numero x:")
x2=int(x2)

y2=input("Cual es el segundo numero Y:")
y2=int(y2)


difx=x1-x2
dify=y1-y2

difx2=difx*difx

dify2=dify*dify

distancia=(difx2+dify2) ** 1/2

print("la distancia es", distancia)
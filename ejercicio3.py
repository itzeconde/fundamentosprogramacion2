#ejercicio 3
#programa que calcula la hipotenusa de un triangulo rectangulo a partir de sus catetos
#entradas:
#cateto1:int
#cateto2:intt

#salidas:
#hipotenusa

#analisis:se resuelve con el teorema de pitagoras

cateteto1=input("Escribe el cateto 1:")
cateteto1=int(cateteto1)
cateteto2=int(input ('escribe el cateto 2:'))
hipotenusa=cateteto1*cateteto1+cateteto2*cateteto2
hipotenusa=hipotenusa**(1/2)
print('la hipotenusa es:',hipotenusa)
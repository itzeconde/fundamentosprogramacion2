#crear un programa que calcule area y perimetro de un rectangulo
#entradas:
#base:integer
#altura:integer

#salidas
#area:integer
#perimetro:integer

base=input('ingresa la base:')
base=int(base)
altura=input("ingresa la altura:")
altura=int(altura)
area= base*altura
perimetro= (base* altura) * 2
print("el area del rectangulo es", area)
print("El area del rectangulo es",perimetro)

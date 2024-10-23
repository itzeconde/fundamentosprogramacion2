'''programa para invertir un numero'''
num=input("Ingresa un numero de dos cifras: ")
num=int(num)

decena=num // 10
unidad=num % 10

print("el numero invertido es", unidad,decena)
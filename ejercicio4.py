'''Dado 2 numeros mostrar la suma, resta, division y multiplicacion de ambos
entradas:
num1
num2

salidas:
suma, resta multiplicacion, division
'''
numero1 = input('Ingresaq el numero1:')
numero1 = int(numero1)

numero2=input('ingresa el numero 2:')
numero2=int(numero2)

suma = numero1 + numero2
resta=numero1-numero2
division=numero1/numero2
multiplicacion=(numero1*numero2)

print('la suma de los dos numero es:',suma)
print('la resta de los dos numero es',resta)
print('la division de los dos numero es',division)
print('la multiplicacion de los dos numeros es',multiplicacion)
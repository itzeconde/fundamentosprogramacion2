'''escribir un programa que convierta un valor dado en grados fahrenheit a grados celsius
entradas:
grados fahrenheit
salida:
grados celsius
'''
grados = input('Ingresa los grados fahrenheit a covertir:')
grados = int(grados)

celsius= (grados-32)/1.8

print('los grados convertidos a celsius son',celsius)
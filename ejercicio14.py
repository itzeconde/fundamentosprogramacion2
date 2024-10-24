'''
dadas dos variables numericas A y B, que el usuario debe teclear, pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto vale al final'''

numA=input("Escribe la variable numerica A: ")
numA=int(numA)

numB=input("Escribe la variable numerica B : ")
numB=int(numB)

temp=numA
numA=numB
numB=temp

print("el numero es", numA)
print("el numero es ",numB)
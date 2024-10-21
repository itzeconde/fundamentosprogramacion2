'''
cantidad de minutos y muestre a cuantas horas y minutos corresponde

entradas:
minutos
salidas:
minutos totales'''

minutos=input('ingesa el numero de minutos:')
minutos=int(minutos)

horastotal = minutos / 60
minutostotal = minutos % 60

print('las horas y los minutos son:',horastotal, "y" ,+ minutostotal, "minutos")
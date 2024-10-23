'''
entradas:cal1,cal2,cal3,examenfinal,trabajofinal 
salidas:calificacionfinal'''

cal1=input('Ingresa las tres calificaciones: ')
cal1=int(cal1)

cal2=input('calificacion 2: ')
cal2=int(cal2)

cal3=input('calificacion 3 :')
cal3=int(cal3)

examfinal=input('Ingresa la calificacion del examen final: ')
examfinal=int(examfinal)

trabajofinal=input('ingresa la calificacion del trabajo final :')
trabajofinal=int(trabajofinal)

promedio=(cal1+cal2+cal3)/3
parciales=promedio*0.55

promedioexam=examfinal*0.30
promediotrabajo=trabajofinal*0.15

calificacion=parciales+promedioexam+promediotrabajo

print("tu calificacion final es: ",calificacion)
# -*- coding: utf-8 -*-
"""Un alumno desea saber cuál va a ser su promedio general en las tres materias que cursa y cuál va
a ser el promedio que obtendrá en cada una de ellas.
Estas materias se evalúan como se muestra a continuación:
 Matemática. El examen pesa 90 % de la nota, promedio de tareas 10% y se pidieron un total
de tres tareas.
 Física. El examen 80 %, promedio de tareas 20 % y se pidieron dos tareas.
 Química. El examen 85 %, promedio de tareas 15% y se pidieron un total de tres tareas"""

matExamen= input ("Ingrese la nota de su examen de Matematica ")
matTarea1= input("Ingrese la nota de su primer tarea")
matTarea2= input ("Ingrese la nota de su segunda tarea")
matTarea3= input ("Ingrese la nota de su tercer tarea")
proTarea= (matTarea1 + matTarea2 + matTarea3) /3
notaMat= (matExamen * 0.90) + (proTarea * 0.10)
print("Tu nota de Matematica es:",notaMat)
fisExamen= input ("Ingrese la nota de su examen de Fisica")
fisTarea1= input ("Ingrese la nota de su primer tarea")
fisTarea2= input ("Ingrese la nota de su segunda tarea")
proTarea2= (fisTarea1 + fisTarea2) / 2
notaFis= (fisExamen * 0.80) + (proTarea2 * 0.20)
print ("Tu nota de fisica es:",notaFis)
quiExamen= input ("Ingrese la nota de su examen de Quimica")
quiTarea1= input ("Ingrese la nota de su primer tarea")
quiTarea2= input ("Ingrese la nota de su segunda tarea")
quiTarea3= input ("Ingrese la nota de su tercer tarea")
proTarea3= (quiTarea1 + quiTarea2 + quiTarea3) / 3
notaQui= (quiExamen * 0.85) + (proTarea3* 0.15)
print("Tu nota de Quimica es:",notaQui)
proGeneral= (notaMat + notaFis + notaQui) / 3
print("Tu promedio general es: ",proGeneral)

# -*- coding: utf-8 -*-
"""Situación C2
Diseñe un programa capaz de permitir el ingreso de 3 valores, calcular su promedio y que muestre
aquellos valores mayores o iguales al promedio."""
num1= input("Ingrese un primer numero entero")
num2= input("Ingrese un segundo numero entero")
num3= input("Ingrese un tercer numero entero")
promedio= (num1 + num2 + num3)/3
print(promedio)
if (num1>=promedio):
	print("El numero %s es >= a %s" %(num1,promedio))
if (num2>=promedio):
	print("El numero %s es >= a %s" %(num2,promedio))
if (num3>=promedio):
	print("El numero %s es >= a %s" %(num3,promedio))


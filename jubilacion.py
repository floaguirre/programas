# -*- coding: utf-8 -*-
"""El ANSES requiere clasificar a las personas que se jubilan en este año. Existen tres tipos de
jubilaciones por edad, por antigüedad joven y por antigüedad adulta.
Las personas adscriptas a la jubilación por edad deberán tener 60 años o más y una antigüedad en
su empleo de menos de 25 años.
Las personas adscriptas por antigüedad joven deberán tener menos de 60 años y una antigüedad
en su empleo de 25 años o más.
Las de jubilación por antigüedad adulta deben tener 60 años o más y una antigüedad en su empleo
de 25 años o más.
Determinar en qué tipo de jubilación quedara una persona"""
print("Para saber si se puede jubilar este año complete:")
edad= input ("Ingrese su edad")
ant= input("Ingrese la antigüedad en su empleo ")

if (edad>=60) & (ant<25):
	print("Usted esta adscripto para la jubilacion por edad")

elif (edad<60) & (ant>=25):
	print("Usted esta adscripto para la jubilacion por antigüedad joven")


elif (edad>=60) & (ant>=25):
	print("Usted esta adscripto para la jubilacion por antigüedad adulta")
else:
	print("No cumple los requisitos para jubilarse este año")





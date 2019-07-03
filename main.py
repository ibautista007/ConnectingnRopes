#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

ropes = []
num = int(input('Ingrese el numero de cuerdas que conectará:'))
print ('Ingrese el tamaño: ')
for i in range(int(num)):
   n = input("num :")
   ropes.append(int(n))


#ropes = [4,3,2,6]
ropes.sort()


lenght = len(ropes)

if lenght == 1:
 print ("Solo se tiene una cuerda no se puede tomar calor de costo por union")
elif lenght == 2:
 res = 0
 primerd = ropes[0]
 segundod = ropes[1]
 suma = primerd + segundod
 pair = 0
 print ("Total de costo por union: ",suma)
elif lenght == 3:
 res = 0
 primerd = ropes[0]
 segundod = ropes[1]
 suma = primerd + segundod
 pair = 0
 i = 2
  while i < lenght:
   res = suma + ropes[i]
   i +=1
 print ("Total de costo por union ",res)
else:
 res = 0
 primerd = ropes[0]
 segundod = ropes[1]
 suma = primerd + segundod
 pair = 0
 i = 2
  while i < lenght:
   res += suma
   pair = suma + ropes[i]
   suma = pair
   i +=1
 print ("Total de costo por union ",res+suma)

x = len(ropes)

print("Numero de cuerdas unicas",x)

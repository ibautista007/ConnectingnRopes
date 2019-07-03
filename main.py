

ropes = [4,3,2,6] 
ropes.sort()
res = 0
primerd = ropes[0]
segundod = ropes[1]
suma = primerd + segundod
pair = 0
i = 2
lenght = len(ropes)

while i < lenght: 
  res += suma
  pair = suma + ropes[i]
  suma = pair
  i +=1


print ("Total de costo por union ",res + suma)

x = len(ropes)

print("Numero de cuerdas unicas",x)

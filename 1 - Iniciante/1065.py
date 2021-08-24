cont = 0

for e in range(5):
  valor = int(input(""))
  if(valor % 2 == 0):
    cont += 1

print("%d valores pares" % cont)
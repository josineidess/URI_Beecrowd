cont = 0
media = 0

for e in range(6):
  valor = float(input(""))
  if(valor > 0):
    cont += 1
    media += valor

print("%d valores positivos\n%.1f"%(cont,(media/cont)))

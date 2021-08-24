quant = int(input(""))
contin = 0
contout = 0

for e in range(quant):
  valor = int(input(""))
  if(valor >= 10 and valor <= 20):
    contin += 1
  else:
    contout += 1

print("%d in\n%d out"%(contin,contout))

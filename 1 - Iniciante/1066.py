contpar = 0
contimp = 0
contpos = 0
contneg = 0

for e in range(5):
  valor = int(input(""))
  if(valor > 0):
    contpos += 1
  else:
    if(valor != 0):
      contneg += 1
  if(valor % 2 == 0):
    contpar += 1
  else:
    contimp += 1

print("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)"%(contpar,contimp,contpos,contneg))
notas = 0
cont = 0
while(True):
  if(cont == 2):
    break
  while(True):
    nota = float(input())
    if(nota >= 0 and nota <= 10):
      notas += nota
      cont += 1
      break
    else:
      print("nota invalida")

notas = float(notas/2)
print('media = %.2f' % notas)


#URI da 100% Wrong mas não sei porque ainda...

soma = 0
cont = 0
op = 0
while(True):
  while(True):
    nota = float(input())
    if(nota >= 0 and nota <= 10):
      soma += nota
      cont += 1
    else:
      print("nota invalida")
    if(cont == 2):
      soma = float(soma/2)
      print('media = %.2f' % soma)
      soma = 0
      cont = 0
      break
  while(True):
    opcao = int(input("novo calculo (1-sim 2-nao)"))
    if(opcao == 1 or opcao == 2):
      op = opcao
      break
  if(op == 2):
    break


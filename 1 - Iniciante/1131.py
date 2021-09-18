#	Presentation error (5%)

inter = 0
gremio = 0
cont = 0
empates = 0

while(True):
  valores = input().split(' ')
  n1 = int(valores[0])
  n2 = int(valores[1])
  if(n1 != n2):
    if( n1 > n2 ):
      inter += 1
    else:
      gremio += 1
  if(n1 == n2):
    empates += 1
  cont += 1
  opc = int(input("Novo grenal (1-sim 2-nao)\n"))
  if(opc == 2):
    break

print('\n%d grenais' % cont)
print('Inter:%d' % inter)
print('Gremio:%d' % gremio)
print('Empates:%d' % empates)

if(inter > gremio):
  print('Inter venceu mais')
else:
  if(inter == gremio):
    print('Nao houve vencedor')
  else:
    print('Gremio ganhou mais')

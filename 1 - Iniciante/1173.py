vetor = []
valor = int(input())
vetor.append(valor)

for e in range(1,10):
  vetor.append(vetor[e-1] * 2)

for e in range(10):
  print('N[%d] = %d' % (e,vetor[e]))
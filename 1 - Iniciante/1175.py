
vetor= []

for e in range(20):
    vetor.append(int(input()))

final = len(vetor) - 1

for e in range(10):
    aux = vetor[e]
    vetor[e]= vetor[final]
    vetor[final]=aux
    final -=1
    
for e in range(20):
    print('N[%d] = %d' % (e,vetor[e]))

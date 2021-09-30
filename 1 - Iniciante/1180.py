
n = int(input())
vetor = []
linha = input().split(' ')

for e in range(n):
    vetor.append(int(linha[e]))

menor = vetor[0]
pos = 0

for e in range(n):
    if vetor[e] < menor:
        menor = vetor[e]
        pos = e

print('Menor valor: %d' % menor)
print('Posicao: %d' % pos)

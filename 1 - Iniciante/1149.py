valores = input().split(' ')
A = int(valores[0])
B = 0
soma = 0

for e in range(1,len(valores)):
    if(int(valores[e]) > 0):
        B = int(valores[e])
        break

for e in range(A+1):
    soma += e

for e in range(B):
    soma += e

print(soma)

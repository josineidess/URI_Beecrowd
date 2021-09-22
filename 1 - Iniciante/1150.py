
X = int(input())
Z = X - 1
cont = 0
soma = 0

while(True):
    if(Z > X):
        break
    Z = int(input())

for e in range(X,Z):
    soma += e
    cont += 1
    if(soma > Z):
        break
       
print(cont)

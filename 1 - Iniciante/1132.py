n1 = int(input())
n2 = int(input())
minm = min(n1,n2)
maxm = max(n1,n2)
soma = 0

for e in range(minm,maxm+1):
  if(e % 13 != 0):
    soma += e

print(soma)

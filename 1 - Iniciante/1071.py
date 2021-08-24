x = int(input(""))
y = int(input(""))
soma = 0
mx = max(x,y)
mn = min(x,y)

for e in range(mn+1,mx):
  if(e % 2 == 1):
    soma += e

print(soma)
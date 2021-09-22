n = int(input())
x = n - 1
soma = n

for e in range(n-1):
    soma *= x
    x -= 1
    
print(soma)

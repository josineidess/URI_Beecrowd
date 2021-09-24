n = int(input())

for e in range(n):
    p = int(input())
    soma = 0
    for e in range(1,p):
        if(p % e == 0):
            soma += e
    if(soma == p):
        print('%d eh perfeito' % p)
    else:
        print('%d nao eh perfeito' % p)

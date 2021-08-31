
while(True):
    valor = input().split(" ")
    m = int(valor[0])
    n = int(valor[1])
    if(m <= 0 or n <= 0):
        break
    menor = min(n,m)
    maior = max(n,m)
    soma = 0
    for e in range(menor,maior+1):
        print("%d " % e,end="")
        soma += e
    print("Sum=%d" % soma)

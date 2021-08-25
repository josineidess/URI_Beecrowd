maior = 0
pos = 0
for e in range(100):
    valor = int(input(""))
    if(e == 0):
        maior = valor
        pos = e + 1
    else:
        if(valor > maior):
            maior = valor
            pos = e + 1
    
print(maior)
print(pos)

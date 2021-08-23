valores = input().split()
lista = []
lista.append(int(valores[0]))
lista.append(int(valores[1]))
lista.append(int(valores[2]))
nv = sorted(lista)
for e in nv:
    print(e)
print()
for s in lista:
    print(s)
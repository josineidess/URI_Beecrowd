lista1 = input().split()
lista2 = input().split()
vt1 = int(lista1[1]) * float(lista1[2])
vt2 = int(lista2[1]) * float(lista2[2])
print("VALOR A PAGAR: R$ %.2f" % (vt1 + vt2))
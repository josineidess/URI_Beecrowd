valor = input().split()
A = int(valor[0])
B = int(valor[1])
C = int(valor[2])
maiorAB = ((A + B) + abs(A-B))/2
maiorAC = ((A + C) + abs(A-C))/2
maiorBC = ((B + C) + abs(B-C))/2
maior = max(maiorAB,maiorAC,maiorBC)
print("%d eh o maior" % maior)
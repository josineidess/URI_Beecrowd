valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
lista = []
lista.append(a)
lista.append(b)
lista.append(c)
new_lista = sorted(lista)
A = new_lista[2]
B = new_lista[1]
C = new_lista[0]
triangulo = True
if A >= B + C:
    print("NAO FORMA TRIANGULO")
    triangulo = False
if (A**2 == B**2 + C**2) and triangulo == True:
    print("TRIANGULO RETANGULO")
if (A**2 > B**2 + C**2) and triangulo == True:
    print("TRIANGULO OBTUSANGULO")
if (A**2 < B**2 + C**2) and triangulo == True:
    print("TRIANGULO ACUTANGULO")
if (A == B == C) and triangulo == True:
    print("TRIANGULO EQUILATERO")
if (A == B and (C != A)) or (A == C and (B != C)) or (B == C and (A != B)):
    print("TRIANGULO ISOSCELES")

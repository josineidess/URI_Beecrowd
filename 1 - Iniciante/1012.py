pontos = input().split()
A = float(pontos[0])
B = float(pontos[1])
C = float(pontos[2])
Atriangulo = (A * C) / 2
Acirculo = 3.14159 * (C**2)
Atrapezio = ((A + B) * C) / 2
Aquadrado = B**2
Aretangulo = A * B
print("TRIANGULO: %.3f" % Atriangulo)
print("CIRCULO: %.3f" % Acirculo)
print("TRAPEZIO: %.3f" % Atrapezio)
print("QUADRADO: %.3f" % Aquadrado)
print("RETANGULO: %.3f" % Aretangulo)
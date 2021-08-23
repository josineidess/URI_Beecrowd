import math
n = input().split()
a = float(n[0])
b = float(n[1])
c = float(n[2])

delta = (b**2) - (4*a*c)
if(delta > 0):
    x = math.sqrt(delta)
    if(a > 0):
        x1 = (-b + x)/(2*a)
        x2= (-b - x)/(2*a)
        print("R1 = %.5f" % x1)
        print("R2 = %.5f" % x2)
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")

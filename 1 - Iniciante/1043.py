valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
cond1 = b - c < a < b + c
cond2 = a - c < b < a + c
cond3 = b - a < c < b + a
perimetro = ((a + b)*c)/2
if(cond1 and cond2 and cond3):
    print("Perimetro = %2.1f" % (a+b+c))
else:
    print("Area = %2.1f" % perimetro)
    
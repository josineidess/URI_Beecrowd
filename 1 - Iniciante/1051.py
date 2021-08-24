salario = float(input(""))
faixa1 = 0
faixa2 = 0
faixa3 = 0

if(salario - 2000 > 0):
  if(salario > 4500):
    faixa1 = (salario - 4500) * (28/100)
    salario = 4500
  if(salario > 3000):
    faixa2 = (salario - 3000) * (18/100)
    salario = 3000
  if(salario > 2000):
    faixa3 = (salario - 2000) * (8/100)
    salario = 2000
  print("R$ %.2f" % (faixa1+faixa2+faixa3))
else:
  print("Isento")
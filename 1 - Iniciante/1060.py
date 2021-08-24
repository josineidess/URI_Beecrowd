positivos = 0

for e in range(6):
    valor = input("")
    if "." in valor:
        valor = float(valor)
    else:
        valor = int(valor)
    if valor > 0:
        positivos += 1

print("%d valores positivos" % positivos)
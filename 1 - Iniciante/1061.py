#Uri não aceita a solução, mas funciona

day1 = input("")
hora1 = input("")
day2 = input("")
hora2 = input("")
dias = 0
horas = 0
minutos = 0
segundos = 0

hora1 = hora1.split(" : ")
h1 = int(hora1[0])
m1 = int(hora1[1])
s1 = int(hora1[2])

hora2 = hora2.split(" : ")
h2 = int(hora2[0])
m2 = int(hora2[1])
s2 = int(hora2[2])

df = int(day2.split("Dia ")[1]) - int(day1.split("Dia ")[1])

ds = s2 - s1
if(ds >= 0):
  segundos = ds
else:
  segundos = 60 + ds

dm = m2 - m1
if(dm >= 0):
  minutos = dm
else:
  minutos = 60 + dm

dh = h2 - h1
if(dh >= 0):
  horas = dh
else:
  horas = 24 + dh

if(horas > 0 or minutos > 0 or segundos > 0):
  dias = df - 1
else:
  dias = df

print("%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)" % (dias,horas,minutos,segundos))

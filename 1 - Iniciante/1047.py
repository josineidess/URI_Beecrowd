horaIni,minutoIni,horaFin,minutoFin = input().split(" ")
horaIni = int(horaIni)
minutoIni = int(minutoIni)
horaFin = int(horaFin)
minutoFin = int(minutoFin)


minutosf = (horaFin * 60) + minutoFin
minutosI = (horaIni * 60) + minutoIni

minutosT = minutoFin - minutosI
minutosT = abs(minutosT)

if(minutosf <= minutosI):
  minutosT = minutosf + 1440 - minutosI
else:
  minutosT = minutosf - minutosI

horas = minutosT // 60
minutos = minutosT - (horas*60)

print( "O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas,minutos))
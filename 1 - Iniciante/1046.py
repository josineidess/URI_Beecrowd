n = input().split()
i = int(n[0])
f = int(n[1])
if(i > f):
    horas = (24 - i) + f
elif(i == f):
    horas = 24
else:
    horas = f - i
if(1 <= horas <= 24):
    print("O JOGO DUROU %d HORA(S)" % horas)
else:
    print("Você só pode jogar de 1 a 24 horas")
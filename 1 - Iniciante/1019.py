n = int(input())
horas = 0
minutos = 0
segundos = 0
if(n >= 3600):
    horas = n / 3600
    resto = n % 3600
    n = resto
    if(3600 < n >= 60):
        minutos = n / 60
        resto = n % 60
        n = resto
        if(n < 60):
            segundos = n
if(3600 > n >= 60):
    minutos = n // 60
    resto = n % 60
    n = resto
    if(n < 60):
        segundos = n
if(n < 60):
    segundos = n
print("%d:%d:%d" % (horas,minutos,segundos))
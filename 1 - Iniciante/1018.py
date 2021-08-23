n = int(input())
inicial = n
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0
if(n >= 100):
    notas100 = n // 100
    n = n % 100
    if(100 > n >= 50):
        notas50 = n // 50
        n = n % 50
        if(50 > n >= 20):
            notas20 = n // 20
            n = n % 20
            if(20 > n >= 10):
                notas10 = n // 10
                n = n % 10
                if(10 > n >= 5):
                    notas5 = n // 5
                    n = n % 5
                    if(5 > n >= 2):
                        notas2 = n // 2
                        n = n % 2
                        if(2 > n >= 1):
                            notas1 = n

if(100 > n >= 50):
    notas50 = n // 50
    n = n % 50
    if(50 > n >= 20):
        notas20 = n // 20
        n = n % 20
        if(20 > n >= 10):
            notas10 = n // 10
            n = n % 10
            if(10 > n >= 5):
                notas5 = n // 5
                n = n % 5
                if(5 > n >= 2):
                    notas2 = n // 2
                    n = n % 2
                    if(2 > n >= 1):
                        notas1 = n
if(50 > n >= 20):
     notas20 = n // 20
     n = n % 20
     if(20 > n >= 10):
         notas10 = n // 10
         n = n % 10
         if(10 > n >= 5):
             notas5 = n // 5
             n = n % 5
             if(5 > n >= 2):
                 notas2 = n // 2
                 n = n % 2
                 if(2 > n >= 1):
                     notas1 = n
if(20 > n >= 10):
    notas10 = n // 10
    n = n % 10
    if(10 > n >= 5):
        notas5 = n // 5
        n = n % 5
        if(5 > n >= 2):
            notas2 = n // 2
            n = n % 2
            if(2 > n >= 1):
                notas1 = n
if(10 > n >= 5):
    notas5 = n // 5
    n = n % 5
    if(5 > n >= 2):
        notas2 = n // 2
        n = n % 2
        if(2 > n >= 1):
            notas1 = n
    
if(5 > n >= 2):
    notas2 = n // 2
    n = n % 2
    if(2 > n >= 1):
        notas1 = n
if(2 > n >= 1):
    notas1 = n
print(inicial)
print("%d nota(s) de R$ 100,00" % notas100)
print("%d nota(s) de R$ 50,00" % notas50)
print("%d nota(s) de R$ 20,00" % notas20)
print("%d nota(s) de R$ 10,00" % notas10)
print("%d nota(s) de R$ 5,00" % notas5)
print("%d nota(s) de R$ 2,00" % notas2)
print("%d nota(s) de R$ 1,00" % notas1)
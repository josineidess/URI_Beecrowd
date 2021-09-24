n = int(input())

for e in range(n):
    p = int(input())
    eh=False
    for e in range(2,p):
        if(p % e == 0):
            eh = True
            break
    if(eh):
        print('%d nao eh primo' % p)
    else:
        print('%d eh primo' % p)

n = int(input())

valores = [0,1,1]

for e in range(n):
    if(e > 2):
        valores.append(valores[e-1] + valores[e-2])
    if(e != n-1):
        print('%d ' % valores[e],end='')
    else:
        print('%d' % valores[e])

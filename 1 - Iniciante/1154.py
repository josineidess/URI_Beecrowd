soma = 0
cont = 0

while(True):
    i = int(input())
    if(i < 0):
        break
    else:
        soma += i
        cont += 1

print('%.2f' % (soma/cont))

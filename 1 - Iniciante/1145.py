entrada = input().split(' ')
cont = 1

while(cont != int(entrada[1])):
    for e in range(int(entrada[0])):
        if(e != int(entrada[0]) - 1):
            print('%d ' % cont,end='')
        else:
            print('%d' % cont)
        if(cont == int(entrada[1])):
          break
        cont += 1
    

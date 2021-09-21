#Time limit exceeded

while(True):
    val = int(input())
    if(val == 0):
        break
    else:
        for e in range(1,val+1):
            if(e != val):
                print('%d ' % e,end='')
            else:
                print('%d' % e)

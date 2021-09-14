
while(True):
    c = input().split(" ")
    x = int(c[0])
    y = int(c[1])
    
    if(x == 0 or y == 0):
        break
    if(x > 0):
        if(y > 0):
            print("primeiro")
        else:
            print("quarto")
    else:
        if(y < 0):
            print("terceiro")
        else:
            print("segundo")

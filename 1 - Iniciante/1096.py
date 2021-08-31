j = 7
for e in range(1,10):
    if(e % 2 == 1):
        for i in range(3):
            print("I=%d J=%d" % (e,j))
            j -= 1
        j = 7
        

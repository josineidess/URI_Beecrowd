n = int(input())

for e in range(n):
    entrada = input().split(" ")
    n1 = int(entrada[0])
    n2 = int(entrada[1])
    
    if(n2 == 0):
        print("divisao impossivel")
    else:
        print("%.1f" % (n1/n2))

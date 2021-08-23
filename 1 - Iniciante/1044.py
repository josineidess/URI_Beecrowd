n = input().split()
a = int(n[0])
b = int(n[1])
ma = max(a,b)
mi = min(a,b)
if ma % mi == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

e = input().split()
c = int(e[0])
q = int(e[1])
produtos = []
c1 = q * 4.00
c2 = q * 4.50
c3 = q * 5.00
c4 = q * 2.00
c5 = q * 1.50
if c == 1:
    print("Total: R$ %.2f" % c1)
elif c == 2:
     print("Total: R$ %.2f" % c2)
elif c == 3:
     print("Total: R$ %.2f" % c3)
elif c == 4:
     print("Total: R$ %.2f" % c4)
elif c == 5:
     print("Total: R$ %.2f" % c5)
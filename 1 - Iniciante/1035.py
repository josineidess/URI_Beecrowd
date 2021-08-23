n = input().split()
A = int(n[0])
B = int(n[1])
C = int(n[2])
D = int(n[3])
c1 = B > C and D > A
c2 = (C + D) > (A + B)
c3 = (C > 0) and (D > 0)
if c1 and c2 and c3 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
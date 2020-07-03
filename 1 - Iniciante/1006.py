A = float(input(""))
B = float(input(""))
C = float(input(""))
if(A >= 0.0 and A <= 10.0) and (B >= 0.0 and B <= 10.0) and (C >= 0.0 and C <= 10.0):
    A = A * 2
    B = B * 3
    C = C * 5
    media = (A + B + C) / 10
    print("MEDIA = %.1f" % media)
else:
    print("insira uma nota entre 0.0 e 10.0")

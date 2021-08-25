R = 0
C = 0
S = 0

num = int(input(""))

for e in range(num):
    dado = input("")
    if(dado.split(" ")[1] == "C"):
        C += int(dado.split(" ")[0])
    elif(dado.split(" ")[1] == "R"):
        R += int(dado.split(" ")[0])
    elif(dado.split(" ")[1] == "S"):
        S += int(dado.split(" ")[0])

total = R + C + S
print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % C)
print("Total de ratos: %d" % R)
print("Total de sapos: %d" % S)
print("Percentual de coelhos: %.2f %%" % (C * 100 / total))
print("Percentual de ratos: %.2f %%" % (R * 100 / total))
print("Percentual de sapos: %.2f %%" % (S * 100 / total))

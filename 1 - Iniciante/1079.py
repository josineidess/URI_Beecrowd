num = int(input(""))
media = 0
for e in range(num):
    n = input("")
    n1 = float(n.split(" ")[0])
    n2 = float(n.split(" ")[1])
    n3 = float(n.split(" ")[2])
    print("%.1f" % ((n1 * 2 + n2 * 3 + n3 * 5)/10))

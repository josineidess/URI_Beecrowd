num = int(input())
ini = 1
cont = 0
while(True):
  for e in range(3):
    print(ini,end=" ")
    ini += 1
  print("PUM")
  cont += 1
  ini += 1
  if(cont == num):
    break

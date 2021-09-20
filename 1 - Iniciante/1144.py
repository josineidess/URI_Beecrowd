
num = int(input())
cont = 0
ini = 1
for e in range(num):
  print("%d %d %d" % (ini,ini*ini,ini*ini*ini))
  print("%d %d %d" % (ini,(ini*ini)+1,(ini*ini*ini)+1))
  ini += 1

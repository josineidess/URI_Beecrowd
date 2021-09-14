while(True):
   entrada = input("").split(" ")
   v1 = int(entrada[0])
   v2 = int(entrada[1])
   if(v1 == v2):
       break
   if(v1 > v2):
       print("Decrescente")
   else:
       print("Crescente")

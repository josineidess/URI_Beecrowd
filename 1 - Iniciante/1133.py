alcool = 0
gasolina = 0
diesel = 0

while(True):
  cod = int(input(""))
  if(cod == 4):
    break
  else:
    if(cod == 1):
      alcool += 1
    elif(cod == 2):
      gasolina += 1
    elif(cod == 3):
      diesel += 1
    
print("MUITO OBRIGADO")
print("Alcool: %d" % alcool)
print("Gasolina: %d" % gasolina)
print("Diesel: %d" % diesel)

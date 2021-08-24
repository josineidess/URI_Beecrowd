quant = int(input(""))
guarda = ''

for e in range(quant):
  if(e > 0):
    guarda += '\n'
  valor = int(input(""))
  if(valor % 2 == 0):
    if(valor == 0):
      guarda += "NULL"
    else:
      if(valor > 0):
        guarda += "EVEN POSITIVE"
      else:
        guarda += "EVEN NEGATIVE"
  else:
    if(valor > 0):
      guarda += "ODD POSITIVE"
    else:
      guarda += "ODD NEGATIVE"

print(guarda)
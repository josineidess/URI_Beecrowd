nota1 = float(input(""))
nota2 = float(input(""))
if(nota1 >= 0.0 and nota1 <= 10.0) and (nota2 >= 0.0 and nota2 <= 10.0) :
    nota1 = nota1 * 3.5
    nota2 = nota2 * 7.5
    media = (nota1 + nota2) / 11
    print("MEDIA = %.5f" % media)
else:
    print("digite uma nota entre 0.0 e 10.0")

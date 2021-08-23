notas = input().split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1)/10
if media >= 7.0:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    notae = float(input(""))
    notaf = (media + notae) / 2
    print("Nota do exame: %.1f" % notae)
    if notaf >= 5.0:
        print("Aluno aprovado.")
    elif notaf <= 4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f" % notaf)
elif media < 5.0:
    print("Media: %.1f" % media)
    print("Aluno reprovado.")
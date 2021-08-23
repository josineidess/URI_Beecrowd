e = int(input(""))
if e >= 365:
    resto = e % 365
    anos = (e // 365)
    print("%d ano(s)" % anos)
    e = resto
else:
    print("0 ano(s)")
if e >= 30 and e < 365:
    resto = e % 30
    meses = (e // 30)
    print("%d mes(es)" % meses)
    e = meses
else:
    print("0 mes(es)")
if e < 30:
    print("%d dia(s)" % resto)
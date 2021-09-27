vetor = []

for e in range(100):
  vetor.append(float(input()))

for e in range(100):
  if(vetor[e] <= 10):
    print('A[%d] = %.1f' % (e,vetor[e]))


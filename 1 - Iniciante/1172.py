# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor= []

for e in range(10):
    n = int(input())
    vetor.append(n)
    if(vetor[e] <= 0):
        vetor[e] = 1
        
for e in range(10):
    print('X[%d] = %d' % (e,vetor[e]))

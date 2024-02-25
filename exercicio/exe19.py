from random import choice
n1 = input ('primeira aluna: ')
n2 = input ('segunda aluna: ')
n3 = input ('terceira aluna: ')
n4 = input ('quarta aluna: ')
lista = [n1,n2,n3,n4]
escolhida = choice(lista)
print ('a escolhida foi: {}'.format(escolhida))

#sorteiar um nome dentre 4 da lista para fazer algo usando (random.choice)

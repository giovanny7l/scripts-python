from random import randint
from time import sleep
from rich import print
pc = randint(0,5)

print ('-=-' *20)
print ('vou pensar em um numero entre 0 e 5, tente adivinhar...')
print ('-=-' *20)
p = int( input('em qual numero eu pensei?'))
print ('[red]PROCESSANDO...[/]')
sleep(3)
if p==pc:
    print ('Parabens, você adivinhou o numero que eu pensei!')
else:
    print ('Você errou!, eu pensei no numero {} e não no {}'.format(pc, p))


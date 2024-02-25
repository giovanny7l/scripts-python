frase = input ('Digite seu nome').strip()
print ('Analizando seu Nome...')
print ('seu nome com letras maisculas é: {}'.format(frase.upper()))
print ('seu nome com todas as letras minusculas é: {}'.format(frase.lower()))
print ('o seu nome ao todo tem: {} letras'.format(len (frase) - frase.count(' ')))
separa = frase.split()
print ('o primeiro nome é {} e ele tem: {} letras'.format(separa[0], len(separa [0])))






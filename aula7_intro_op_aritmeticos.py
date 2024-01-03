#Exercício
'''A proposta aqui é exebir na tela
[nome] tem [altura em metro] de altura. Pesa [peso] quilos e o seu IMC é'''

nome = 'luiz otávio'
altura = 1.80
peso = 95
imc = peso / (altura * altura)
print (nome,'tem', float(altura), 'de altura.')
print('Pesa', peso, 'quilos e o seu IMC é:')
print (int (imc))

'''Caso eu acho necessário, daí preciso pensar se o código vai ficar mais limpo ou não, posso utilizar a ordem de procedência para fazer meus cálculos. Ex'''
print (' ')
nome = 'Augusto Gonçalves'
altura = 1.80
peso = 80
imc = peso / altura **2

print(nome, 'tem', altura,'de altura')
print('Pesa', peso, 'quilos e o seu IMC é:')
print(int(imc))

#Você pode gerar variáveis e ir pedindo que o programa apenas exiba aa variáveis. EX:

linha1 = f'{nome}, tem {altura} de altura.'
linha2 = f'pesa {peso} quilos e o seu IMC é:'
linha3 = f'{imc: .2f}'

print(linha1)
print(linha2)
print(linha3)
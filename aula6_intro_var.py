#Exercício
nome = 'Augusto'
sobrenome = 'Gonçalves'
idade = 10
ano_nascimento = 1992
maior_idade = idade >= 18
altura_metros = 1.71

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maior de Idade?', maior_idade)
print('Altura em metro:', altura_metros)

#Quando vai utilizar textos a serem exibidos numa variável, sempre colocar o que for txt entre aspas.
"""Outra observação é... Quando for usar termos de comparação, é necessário atribuir essa comparação. No exemplo utilizado foi a idade. Eu queria saber se a pessoa em questão era maior de idade. Então para atribuir essa comparação, dentro da variável 'maior_idade' é preciso colocar a comparação. no exemplo ficou 'maior_idade = idade >= 18. É preciso informar o que será comparado e ainda introduzir um valor para se obter dados.

É impressionante, o como você precisa ser literal para programar. Isso vai complicar minha vida kkkk pq já sou uma pessoa literal

Outra nota importante sobre as variáveis é que é possível inserir contas. Ex"""

ano_nascimento2 = 2024 - idade
print('Ano de Nascimento:', ano_nascimento2)
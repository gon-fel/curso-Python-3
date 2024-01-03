#Introdução ao Tipos de Dados
#str = String = Texto

'''Sempre que você quiser mostrar uma str é preciso colocar a informação entre "aspas". As aspas vai indicar ao interpretador que aquele argumento é uma str.'''
print('Hello World')

#ESCAPE [\ => barra invertida]
#É utilizado para indicar para o interpretado ignorar o próximo caracter. Ex:
print("Augusto \"Gonçalves") # Com o ESCAPE, o caracter que vier após, o interpretador vai considerar como 'str'.

#Caso eu queira que todos os caracteres apareçam como str, basta colocar um 'r' antes das aspas e  o que vier depois das aspas vai aparecer como str.

print(r"\\\\Augusto Gonçalves\\\\")

#Mas para facilitar o código e deixar ele mais bonito [Clear Code], basta mudar as aspas. Se colocar uma aspas "", o que voce quiser que apareça como str tem que ser inserido após as "".

print("///'Vida louca, vida///***'")

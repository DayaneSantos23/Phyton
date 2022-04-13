
#Dicionário
#é uma lista de associação, composta por uma chave (do tipo imutável) e  valores (do tipo mutável)
#é escrita entre chaves

#forma geral
dicionario = {"chave1" : 1, "chave2" : 2, "chave3": 3}
print(dicionario) #{'chave1': 1, 'chave2': 2, 'chave3': 3}

#Outra forma
dicionario = dict() #transforma em dicionário
dicionario["chave1"] = 4
dicionario["chave2"] = 5
dicionario["chave3"] = 6
print(dicionario) #{'chave1': 4, 'chave2': 5, 'chave3': 6}

#metódos 

tel = {"John": 2345, "Peter": 5675, "Vini": 7890}
print(tel) #{'John': 2345, 'Peter': 5675, 'Vini': 7890}

#Adicionar um número à agenda
tel["Paul"] = 1010
print(tel) #{'John': 2345, 'Peter': 5675, 'Vini': 7890, 'Paul': 1010}

#retirar um elemento/telefone da agenda
del tel["John"]
print(tel) #{'Peter': 5675, 'Vini': 7890, 'Paul': 1010}

#método que mostra os itens com suas chaves de um dicionário
print(tel.items()) #([('Peter', 5675), ('Vini', 7890), ('Paul', 1010)])

#método que mostra todas as chaves de um dicionário
print(tel.keys()) #(['Peter', 'Vini', 'Paul'])

#método que mostra todos os valores presentes em um dicionário:
print(tel.values()) #([5675, 7890, 1010])

#metodo para retornar o tamanho da lista (neste caso o número de chaves)
print(len(tel)) #3

#adicionar no dicionário com update
tel.update({"gabriel": "N/a", "Fernando": "N/A"})
print(tel) #{'Peter': 5675, 'Vini': 7890, 'Paul': 1010, 'gabriel': 'N/a', 'Fernando': 'N/A'}


#interação
for x in tel:
    print(x) #para cada item do tel ele vai interar e mostrar no console
#Peter
#Vini
#Paul
#gabriel
#Fernando

for x in tel.values():
    print(x)
#5675
#7890
#1010
#N/a
#N/A

for x in tel.items():
    print(x)
#('Peter', 5675)
#('Vini', 7890)
#('Paul', 1010)
#('gabriel', 'N/a')
#('Fernando', 'N/A')

dic = {}
nome = input("Digite o nome: ")
idade = int(input("Digite a idade:"))
dic[nome] = idade
print(dic)


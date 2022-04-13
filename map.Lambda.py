lista1 = [1,2,3,4]

def multiplicacao(x):
    return x * 2

lista2 = map(multiplicacao, lista1)#map - para cada elemento da minha lista1 o map chama a função multiplicação

print(list(lista2))


###### 

lista3 = list(map(lambda x: x * 2, lista1)) # lambda - cada elemento da minha lista1 coloco dentro do x, então realizo a função que no caso seria x * 2 e ele vai retornar no map e jogo numa lista (list)  (é o mesmo que o map, porém escrito em uma só linha)

print(lista3)

##########

usuarios = [("contato@gmail.com", True),
             ("adm@gmail.com", True),
             ("secretaria@gmail.com", False)]

def getEmail(usuario):
    return usuario[0]

def valido(usuario):
    return usuario[1] == True

print(list(filter(valido, usuarios)))

print(list(map(getEmail, usuarios)))

emails = list(map(getEmail,filter(valido, usuarios)))
print(emails)
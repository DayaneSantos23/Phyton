#tuplas
#O que diferencia uma tupla de uma lista é que a tupla é imutável e está estre parênteses

carro_list = ["Compass","Freemont","Uno"] #lista
carro_tupla = ("Compass","Freemont","Uno") #tupla


carro_list.append("Creta") #['Compass', 'Freemont', 'Uno', 'Creta']
#carro_tupla.append("Ferrari") #ERRO 

print(carro_list)
print(carro_tupla)

print("Creta" in carro_tupla) # "o nome creta está em carro_tupla?" #false



lista = []
for i in range(3): #range : repetir
    lista.append(input("Digite um nome:"))
print(lista)



## for é um tipo de loop

#range = intervalo

for numero in range(6): #começa do zero até o 5
   print(numero)
#0
#1
#2
#3
#4
#5

for numero1 in range(50, 100): #numero1 vai de 50 a 99
    print(numero1) 

#1
#2
#3
#4

for numero2 in range(1,20,2): #começa do 1 e vai até o 19, indo de 2 em 2
    print(numero2)

#1
#3
#5
#7
#9
#11
#13
#15
#17
#19

#######

lista = [1,2,3,4,5]
for item in lista:
    print(item)

#######

frutas1 = ["abacate", 'banana', 'morango']
frutas2 = []

for fruta in frutas1:
    if 'n' in fruta: #se tiver a letra n em fruta , quero que pegue essa fruta e adicione em fruta2
        frutas2.append(fruta) 
print(frutas2) #['banana','morango']

###### Outra maneira de escrever

frutas3 = [fruta for fruta in frutas1 if 'a' in fruta] #se tiver a letra a em fruta , quero que pegue essa fruta e adicione em fruta2
print(frutas3) #['abacate', 'banana', 'morango']

### maneira de verificar o index
index = 0
for fruta in frutas1:
    print(index,fruta)
    index +=1 

#0 abacate
#1 banana
#2 morango

#######Outra maneira

for cont, fruta in enumerate(frutas1):
    print(cont, fruta)

#0 abacate
#1 banana
#2 morango


#####

flagcompra = False
info = 'Compra efetuada com sucesso'

for tentativa in range(3):
    if flagcompra: #se flagcompra for verdadeira, imprimir info
        print(info)
        break
else: #se não
    print("Houve um problema na compra")
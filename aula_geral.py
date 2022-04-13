print("Hello world")
print("marcelo tem" + "25 anos")

nome = "Marcelo"
idade = "35"

print("Meu nome é " + nome + "e tenho idade de " + idade)

texto = f'Nome: {nome} , idade: {idade}'
print(texto)

print(nome.lower()) #marcelo
print(nome.upper()) #MARCELO
print(len(nome)) #7
print(nome[1:4]) #arc
print(nome.count('o')) #1 #quantos letras o tem no mome

email = 'marcelo@corporativo.com.br'
usuario , dominio = email.split("@")

print(usuario) #marcelo
print(dominio) #corporativo.com.br

frase = "Eu amo chocolate"
print(frase.find('amo')) #retorna a posição da palavra

print(frase.replace('amo', 'odeio')) #troca a frase

#variaveis

print(4 + 2)
print(4 + 2.33)
print(2 * 4 + 5)
print(2 * (2 + 6))

i = 5
y = 9
soma = i + y
print(soma)

num_x = str(3) #transformar em string
print(num_x + num_x) #33

num_xx = float(3) #transformar em ponto flutuante
print(num_xx + num_xx) #3.0

print(str(y) + "é um número")

print(max(3,6)) #retorna maior número
print(min(3,6)) #retorna menor número
print(round(12.4)) #arredonda o número

#cidade = input("Digite sua cidade")
#print("A cidade do usuário é:" + cidade)

#num1 = input("Digite o primeiro número")
#num2 = input("Digite o segundo número")
#resultado = int(num1) + int(num2) #transforma em número: int()
#print(resultado)

amigos = ["joão", "Júlia", "Fabiana"]
print(amigos[-2])

amigos[1] = "Silvana"
print(amigos)

amigos.append("Marcio") #adicionar no final da lista
print(amigos)

amigos.insert(2, "MJ") #Adicionar na posição desejada

amigos.remove("joão") #remover da lista
print(amigos)

amigos.pop(1) #remover o item da posição
print(amigos)

numeros = [10, 9, 20, 40, 35]
numeros.sort() # ordenar lista
print(numeros)

# converte cada letra para lista: list()
# converter por espaçoes ou por elementos previamente indicados: split()
#converte lista para string: join()
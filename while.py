#while - enquanto for verdade o seu loop vai ficar executando

a = 10
i = 5 

while i <= a:
    a -= 1
    if a ==7:
        print("sete")
        continue
    print(a)

#9
#8
#sete
#6
#5
#4

b = 10
e = 5 

while e <= b:
    b -= 1
    if b == 7:
        print("sete")
        break
    print(b)


#9
#8
#sete

valor = 100

while valor > 70:
    print(valor)
    valor -= 5

#100
#95
#90
#85
#80
#75

lista = [1,2,9,4,8,5,6]
tamanho = len(lista)
x = 0

while (x < tamanho):
    print(lista[x])
    x += 1

#1
#2
#9
#4
#8
#5
#6

g = 10

while g <= 15:
    print(g)
    g += 1
else:
    print("Chegamos no final do while")

#10
#11
#12
#13
#14
#15
#Chegamos no final do while

pontos = 0
questao = 1

while questao <=3:
    resposta = input("Resposta da questão {questao}")
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    if questao == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questao += 1

print("O aluno teve {pontos} pontos")




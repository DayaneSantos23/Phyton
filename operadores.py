cinco = 5
oito = 8

soma = 5 + 8
print(soma)

subtracao = 7 - 4
print(subtracao)

divisao = 10 / 2
print(divisao)

multiplicao = 10 * 2
print(multiplicao)

modulo = 8 % 2
print(modulo)

num1 = 7
num2 = 4

print(num1 < 8 and num2 < 5) #true

#AND
#falso e verdadeiro = false
#verdadeiro e verdadeiro = verdadeiro
#verdadeiro e falso = false

print(num1 < 6 or num2 < 2) #false

#OR
#falso ou verdadeiro = true
#verdadeiro ou verdadeiro = true
#verdadeiro ou falso = true
#falso ou falso = false

#not 
#torna falso se o resultado for verdadeiro
if not (num1 < 8 and num2 < 6):
    print("Olá entrei no if")


#Operadores de identidade

#is - irá mostrar true no resultado se ambos os operandos forem idênticos
#is not - Ele mostrará True na saída se os operandos forem objetos não idênticos

A = 20
B = 20
C = 22
D = 15
E = [10, 20]
F = [10, 20]

print(A is B) #true
print(A is C) #false
print(E is F) #false    entre listas mesmo que os números sejam iguais o resultado é falso
print(E is not F) # true



#Operadores de associação
#in - isso retornará true se o operando estiver presente na sequência
# Not in - Isso retornará true se o operando não estiver presente na sequência

l = [20, 23, 26, 30]
print(20 in l) #true
print(21 not in l) #true

#Operadores de atribuição

x = 10
x -= 5   #x = x - 5
print(x) #5

x = 10
x *= 5   #x = x * 5
print(x) #50

x = 10
x /= 5   #x = x / 5
print(x) #2.0

x = 10
x %= 5   #x = x % 5
print(x) #0


#Operadores de comparação

x = 10
y = 20

print(x == y) #false
print(x != y) #true
print(x > y) #false
print(x < y) #true
print(x >= y) #false
print(x <= y) #true




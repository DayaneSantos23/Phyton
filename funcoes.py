from wsgiref.validate import validator

################

def teste(v,i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado

a = teste(10,1)
print(f'O resultado é igual a: {a} ')

#########

def boas_vindas(nome, idade):
    print(f'Olá {nome} você tem {str(idade)} anos')

boas_vindas('marcelo', 33) #chama a função

#############3
def teste(v,i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado

a = teste(10,1)
print(a)

###########

def cadastrar(pessoas):
    cpf = input('Digite seu cpf: ')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite seu idade: '))
    pessoas.append((cpf,nome,idade))

def listar(pessoas):
    for pessoa in pessoas:
        cpf,nome,idade = pessoa
        print(f'NOme {nome} e sua idade {idade}')

def exibir_menu():
    print('''\n Escolha uma opção:
    1. Cadastrar pessoa
    2. Listar pessoa
    3. Sair''')

def main():
    pessoas = []
    flag = True
    while flag:
        exibir_menu()
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 1:
                cadastrar(pessoas)
            elif opcao == 2:
                listar(pessoas)
            elif opcao == 3:
                flag = False
            else:
                print("Opção invalida")
        except ValueError:
            print("Favor digitar somente números")


main()



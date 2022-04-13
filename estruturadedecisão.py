x = 4
y = 5


if y > x:
    print("y é maior que x")
else:
    print("y não é maior que x")

####

idade = 40
media_idade = 30

if idade < media_idade: print("A idade é.. que a media")

if idade < media_idade: 
    print("A idade é menor que a media")
elif idade > media_idade:
    print("A idade é maior que a media")
else:
    print("A idade é igual a média")

######

idade1 = 80
idade2 = 70
medianova = 39

if (idade1 < idade2):
    print("Você é mais novo")
    if idade1 < 30:
        print("você está um uma idade excelente")
else: 
    print("Você está bem velhinho")

##########

if idade1 < medianova or idade2 > medianova:
    print("Você se enquadra no perfil da empresa")
else:
    print("Você não se enquadra no perfil")

########

cores = ['amarelo', 'verde', 'azul', 'vermelho']
if 'amarelo' in cores:
    print('Possui')
else:
    print('Não possui')

########

cor_cliente = input('Digite a cor desejada')

if cor_cliente.lower() in cores:
    print('Está')
else:
    print('Não está')

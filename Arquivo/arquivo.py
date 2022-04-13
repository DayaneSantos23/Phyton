# no phyton não precisa importar biblioteca

#Ordem das operações:
#Abra o arquivo
#Execute a operação no arquivo - ler ou gravar
#Feche o arquivo

# função open() - abrir arquivo- recebe três argumentos: nome do arquivo, modo de acesso e codificação (opcional)


# r = abre um arquivo para leitura
# w  = abre um arquivo para escrita. Cria um novo arquivo se não existir ou trunca(apagar) o arquivo se existir
# x = Abre um arquivo para criação exclusiva. Se o arquivo já existir, a operação falhará
# a = Abre um arquivo para anexar no final do arquivo sem trunca-lo. Cria um novo arquivo se ele não existir
# t = Abre no modo de texto (predefinição)

#Abrir
f = open("text.txt") #abre o arquivo com f, escreve open() e adiciona o nome do arquivo
f = open("text.txt", 'w') #adicionado o w mostra que o arquivo tem um modo de escrita

#Ler
with open("arquivo.txt", 'r', encoding='utf-8') as f: #mesma coisa que o f = open(), porém não é necessário fechar o arquivo pois ele fecha sozinho
    print(f.read())

#Sobescrever - apagar arquivo e criar outro
with open("arquivo.txt", 'w', encoding='utf-8') as f:
    f.write("Nova lista")

#Acrescentar
with open("arquivo.txt", 'a', encoding='utf-8') as f:
    f.write("\nNova lista")

#Fechar
f = open("text.txt", encoding='utf-8')
f.close()




try:
    f = open("arquivi.txt", 'r', encoding='utf-8') # se usar f = open() é obrigatório fechar com f = close()
finally:
    f.close()
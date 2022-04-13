
#sobescrever - apaga tudo e reescreve
with open("arquivo/arquivoescrita.txt", 'w', encoding='utf-8') as arquivo: 
   arquivo.write('Nova lista')

#Nova lista

#acrescentar
with open("arquivo/arquivoescrita.txt", 'a', encoding='utf-8') as arquivo: 
   arquivo.write('\nBanana')

#Nova lista
#Banana



with open("arquivo/arquivoleitura.txt", 'r', encoding='utf-8') as f: # r = apenas leitura
    print(f.read())

#Lista
#Maça
#pera
#uva

with open("arquivo/arquivoleitura.txt", 'r', encoding='utf-8') as f: 
    print(f.readlines())

#['Lista\n', 'Maça\n', 'pera\n', 'uva']

with open("arquivo/arquivoleitura.txt", 'r', encoding='utf-8') as f: 
    print(f.readline())

#Lista

with open("arquivo/arquivoleitura.txt", 'r', encoding='utf-8') as f: 
   for linha in f:
       print(linha)

#Lista


#Maça


#pera


#uva
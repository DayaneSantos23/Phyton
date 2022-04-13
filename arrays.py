#Array não é nativo do python por isso tem que fazer import

import array as arr #arr é um apelido que eu criei para simbolizar o array

idades = arr.array("i",[10, 20, 50, 45]) #temos que definir os tipos de dados que serão inseridos lá dentro, que no caso são números inteiros (i)


idades.extend([89,67,66]) #adicionar elementos no array
print(idades)

for x in idades:
    print(x, end=" ") #substituir o pular espaço por ficar na mesma linha

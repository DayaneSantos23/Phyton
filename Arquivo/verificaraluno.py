arquivo = open("arquivo/alunos.txt",'r',encoding='utf-8')

     
for linha in arquivo:
    aluno = linha.split() #split - separa as palavras
    if int(aluno[2]) >= 7:
        print("Aluno Aprovado: " + aluno[0] + " do curso de " + aluno[1] + " tirou nota " + aluno[2])
    else:
        print("Aluno Reprovado: " + aluno[0] + " do curso de " + aluno[1] + " tirou nota " + aluno[2])
    

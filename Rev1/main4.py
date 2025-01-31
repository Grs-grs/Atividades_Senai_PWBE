aluno1,aluno2,aluno3,aluno4,aluno5 = map(int, input("Digite as 5 notas de alunos separados por espaço: ").split())
notas = [aluno1,aluno2,aluno3,aluno4,aluno5]


for i in notas:
    if notas[i] > 5:
        print("O aluno {i} foi aprovado.")
    elif notas[i] > 2.5:
        print("O aluno {i} ficou de recuperação.")
    else:
        print("O aluno {i} ficou reprovado.")



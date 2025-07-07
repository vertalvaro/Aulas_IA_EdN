quant = int(input("Quantos alunos? "))
soma = 0

for i in range(quant):
    nota = float(input("Nota do aluno " + str(i + 1) + ": "))
    soma += nota

media = soma / quant
print("Média da turma:", media)

#informando a nota dos alunos ímpares
soma_i = 0
for i in range(1, 50, 2) :
    print("você está digitando as notas dos alunos ímpares")
    impar = input(f"digite a nota do aluno {i} :")
soma_i = soma_i + impar
media_i = soma_i / 25
#informando a nota dos alunos pares
soma_p = 0
for i in range(2, 51, 2) :
    print("você está digitando a nota dos alunos pares")
    par = input(f"digite a nota do aluno{i} :")
soma_p = soma_p + par
media_p = soma_p / 25

print(f"a média impar foi de {media_i} e a média par foi de {media_p}")
if media_i > media_p :
    print("a média dos alunos ímpares fpi maior.")
elif media_p > media_i :
    print("a média dos alunos pares foi maior.")
else:
    print("a média de ambas são iguais.")

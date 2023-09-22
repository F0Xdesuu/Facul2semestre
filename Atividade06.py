# Inicializa um dicionário vazio para armazenar os dados dos alunos
alunos = {}

# Usando um loop for para ler o nome e a nota de 3 alunos
for i in range(3):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    alunos[nome] = nota

# Calcula a média das notas
soma_notas = sum(alunos.values())
media = soma_notas / len(alunos)

# Exibe a média das notas
print(f"A média das notas dos alunos é: {media}")
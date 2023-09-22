# Definindo as variáveis com informações pessoais
nome = "Mateus Cristiano"
sobrenome = "Razini Biancato"
idade = 10  # Insira sua idade aqui
altura = 1.75  # Insira sua altura em metros aqui
peso = 68.7  # Insira seu peso em quilogramas aqui
e_maior_de_idade = idade >= 18

# Exibindo os resultados
print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Peso:", peso, "quilogramas")

if e_maior_de_idade:
    print("Você é maior de idade.")
else:
    print("Você não é maior de idade.")
# Inicializa uma lista vazia para armazenar os números
numeros = []

# Usando um loop for para ler 5 números inteiros e armazená-los na lista
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

# Usando outro loop for para somar os números na lista
soma = 0
for numero in numeros:
    soma += numero

# Exibe a soma dos números
print(f"A soma dos números digitados é: {soma}")
# Solicita ao usuário que insira o peso em quilogramas e a altura em metros
peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado do IMC
print("Seu Índice de Massa Corporal (IMC) é:", imc)

# Classifica o IMC de acordo com as categorias padrão
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está dentro da faixa saudável.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print("Você está na categoria de obesidade grau I.")
elif 35 <= imc < 39.9:
    print("Você está na categoria de obesidade grau II.")
else:
    print("Você está na categoria de obesidade grau III (obesidade mórbida).")
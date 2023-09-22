# Solicita ao usuário que insira dois valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Verifica qual é o maior valor e o exibe
if valor1 > valor2:
    print("O maior valor é:", valor1)
elif valor2 > valor1:
    print("O maior valor é:", valor2)
else:
    print("Os dois valores são iguais.")
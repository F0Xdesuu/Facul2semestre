# Inicializa uma lista vazia para a lista de compras
lista_de_compras = []

# Função para adicionar um item à lista de compras
def adicionar_item():
    item = input("Digite o nome do item a ser adicionado: ")
    lista_de_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")

# Função para exibir a lista de compras atual
def listar_itens():
    print("\nLista de Compras:")
    for i, item in enumerate(lista_de_compras, start=1):
        print(f"{i}. {item}")

# Função para editar um item na lista de compras
def editar_item():
    listar_itens()
    indice = int(input("Digite o número do item que deseja editar: ")) - 1
    if 0 <= indice < len(lista_de_compras):
        novo_item = input("Digite o novo nome para o item: ")
        lista_de_compras[indice] = novo_item
        print("Item editado com sucesso.")
    else:
        print("Índice inválido. Tente novamente.")

# Função para remover um item da lista de compras
def remover_item():
    listar_itens()
    indice = int(input("Digite o número do item que deseja remover: ")) - 1
    if 0 <= indice < len(lista_de_compras):
        item_removido = lista_de_compras.pop(indice)
        print(f"{item_removido} foi removido da lista de compras.")
    else:
        print("Índice inválido. Tente novamente.")

# Menu principal
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item à lista")
    print("2. Listar itens")
    print("3. Editar item")
    print("4. Remover item")
    print("5. Sair")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        adicionar_item()
    elif opcao == '2':
        listar_itens()
    elif opcao == '3':
        editar_item()
    elif opcao == '4':
        remover_item()
    elif opcao == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
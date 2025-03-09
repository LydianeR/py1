# Dicionário para armazenar os dados
convenios = {}

# Função para adicionar uma pessoa e seu convênio


def adicionar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    convenio = input("Digite o convênio da pessoa: ")
    convenios[nome] = convenio
    print(f"{nome} foi cadastrado(a) com o convênio {convenio}.")

# Função para exibir todas as pessoas cadastradas


def exibir_pessoas():
    if convenios:
        print("\n--- Lista de Pessoas e Convênios ---")
        for nome, convenio in convenios.items():
            print(f"Nome: {nome}, Convênio: {convenio}")
    else:
        print("\nNenhuma pessoa cadastrada.")

# Função para alterar o convênio de uma pessoa


def alterar_convenio():
    nome = input("Digite o nome da pessoa para alterar o convênio: ")
    if nome in convenios:
        novo_convenio = input(f"Digite o novo convênio para {nome}: ")
        convenios[nome] = novo_convenio
        print(f"O convênio de {nome} foi atualizado para {novo_convenio}.")
    else:
        print("Pessoa não encontrada.")

# Função para excluir uma pessoa


def excluir_pessoa():
    nome = input("Digite o nome da pessoa a ser excluída: ")
    if nome in convenios:
        del convenios[nome]
        print(f"{nome} foi removido(a) do sistema.")
    else:
        print("Pessoa não encontrada.")

# Menu principal


def menu():
    while True:
        print("\n--- Controle de Convênios ---")
        print("1. Adicionar Pessoa e Convênio")
        print("2. Exibir Pessoas e Convênios")
        print("3. Alterar Convênio")
        print("4. Excluir Pessoa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_pessoa()
        elif opcao == "2":
            exibir_pessoas()
        elif opcao == "3":
            alterar_convenio()
        elif opcao == "4":
            excluir_pessoa()
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa
menu()

cadastros = []

while True:
    print("1 - Cadastrar pessoa")
    print("2 - Listar cadastros")
    print("3 - Buscar cadastro")
    print("4 - Sair")

    opcao = input("Digite o número de uma opção: ")

    if opcao == "1":
        print("1 - Vamos iniciar o novo cadastro")

    elif opcao == "2":
        print("2 - Esses são os cadastros do sistema")
    
    elif opcao == "3":
        print("3 - qual cadastro deseja buscar")

    elif opcao == "4":
        print("4 - Sair")
        break

    else:
        print("Opção inválida")

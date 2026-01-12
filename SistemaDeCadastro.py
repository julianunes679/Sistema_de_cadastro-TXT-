cadastros = []

while True:
    print("1 - Cadastrar pessoa")
    print("2 - Listar cadastros")
    print("3 - Buscar cadastro")
    print("4 - Sair")
    print("5 - Excluir cadastro")

    opcao = input("Digite o número de uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")

        cadastro = {
            "nome": nome,
            "idade": idade,
            "curso": curso
        }

        cadastros.append(cadastro)

        with open("cadastros.txt", "a") as arquivo:
            arquivo.write(f"{nome},{idade},{curso}\n")

        print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        if len(cadastros) == 0:
            print("Nenhum cadastro encontrado")
        else:
            for cadastro in cadastros:
                print(f"Nome: {cadastro['nome']}")
                print(f"Idade: {cadastro['idade']}")
                print(f"Curso: {cadastro['curso']}")
                print("---------------------------")

    elif opcao == "3":
        nome_buscar = input("Digite o nome do cadastro: ")
        encontrado = False

        for cadastro in cadastros:
            if nome_buscar == cadastro["nome"]:
                print(f"Nome: {cadastro['nome']}")
                print(f"Idade: {cadastro['idade']}")
                print(f"Curso: {cadastro['curso']}")
                print("---------------------------")
                encontrado = True
                break

        if encontrado == False:
            print("Cadastro não localizado!")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    elif opcao == "5":
        nome_excluir = input("Digite o nome do cadastro a excluir: ")
        encontrado = False

        for cadastro in cadastros:
            if cadastro["nome"] == nome_excluir:
                cadastros.remove(cadastro)
                print("Cadastro removido com sucesso!")
                encontrado = True
                break

        if encontrado == False:
            print("Cadastro não encontrado!")

    else:
        print("Opção inválida")

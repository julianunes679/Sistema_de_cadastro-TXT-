cadastros = []

while True:
    print("1 - Cadastrar pessoa")
    print("2 - Listar cadastros")
    print("3 - Buscar cadastro")
    print("4 - Sair")

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
        
        print("Cadastro realizado com sucesso!")


    elif opcao == "2":
        if len(cadastros) == 0:
            print("Nenhum cadastro encontrado")
        else:
            for cadastro in cadastros:
                print (f"nome: {cadastro['nome']}")
                print (f"idade: {cadastro['idade']}")
                print (f"curso: {cadastro['curso']}")
                print ("---------------------------")

    
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
        print("4 - Sair")
        break

    else:
        print("Opção inválida")

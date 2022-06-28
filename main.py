print("Digite uma opção para usar a Agenda: ")
escolha = " "
c = 0
listaAgenda = []

def lin():
    print('-' * 35)

while escolha != "sair":

    escolha = input("1 - Cadastrar | 2 - Pesquisar | 3 - Listar | 4 - Modificar | 5 - Excluir | Ou digite "
                    "'Sair' para encerrar a Agenda\n")


    if escolha == "1":
        print("================== CADASTRAR CONTATO =====================")
        agenda = open("agenda", "w")
        lin()

        numero = input("Digite o número do contato: ")

        contato = {
            "Nome": input("Digite o nome do contato: "),
            "Whatsapp": numero,
            "Email": input("Digite o email do contato: ")
        }

        listaAgenda.append(contato)

        for contato in listaAgenda:
            agenda.write(contato['Nome'])
            agenda.write(contato['Whatsapp'])
            agenda.write(contato['Email'])
            agenda.write("\n")

        agenda.close()

    elif escolha == "2":

        print("=================== PESQUISA =========================")

        numero = input("Digite o número que deseja pesquisar: ")

        for contato in listaAgenda:
            if contato['Whatsapp'] == numero:
                lin()
                print(f'Contato com o número "{contato["Whatsapp"]}":')
                print(f'Nome: {contato["Nome"]}')
                print(f'Whatsapp: {contato["Whatsapp"]}')
                print(f'Email: {contato["Email"]}')
                lin()

    elif escolha == "3":
        print("=================== LISTA DE CONTATOS =========================")
        for i, contato in enumerate(listaAgenda):
            print(f'Nome: {contato["Nome"]}')
            print(f'Whatsapp: {contato["Whatsapp"]}')
            print(f'Email: {contato["Email"]}')
            lin()



    elif escolha == "4":
        print("=================== MODIFICAR CONTATO============================")
        numero = input("Digite o número que deseja pesquisar: ")

        for contato in listaAgenda:
            if contato['Whatsapp'] == numero:
                lin()
                print(f'Contato com o número "{contato["Whatsapp"]}":')
                print(f'Nome: {contato["Nome"]}')
                print(f'Whatsapp: {contato["Whatsapp"]}')
                print(f'Email: {contato["Email"]}')
                lin()
                contato['Nome'] = input("Digite o novo nome do contato: ")
                contato['Whatsapp'] = input("Digite o novo número do contato: ")
                contato['Email'] = input("Digite o novo email do contato: ")
                lin()

                agenda = open("agenda", "w")
                for contato in listaAgenda:
                    agenda.write(contato['Nome'])
                    agenda.write(contato['Whatsapp'])
                    agenda.write(contato['Email'])
                    agenda.write("\n")
                agenda.close()

    elif escolha == "5":
        print("=================== EXCLUIR CONTATO =========================")

        numero = input("Digite o contato que quer excluir (de acordo com seu NÚMERO): ")

        for i, contato in enumerate(listaAgenda):
            if contato['Whatsapp'] == numero:
                del listaAgenda[i]
                print("O contato foi excluído com sucesso.")
                lin()

                agenda = open("agenda", "w")
                for contato in listaAgenda:
                    agenda.write(contato['Nome'])
                    agenda.write(contato['Whatsapp'])
                    agenda.write(contato['Email'])
                    agenda.write("\n")
                agenda.close()


    elif escolha == "sair" or escolha == "Sair":
        print("Obrigado por usar a Agenda")

    else:
        print("Digite uma opção válida.")








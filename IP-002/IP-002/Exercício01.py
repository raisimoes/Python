tarefas = []

def listar_tarefas():
    for tarefa in tarefas:
        print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")

def registrar_tarefa():
    descricao = input("Digite a descrição da tarefa: ").capitalize()
    nova_tarefa = {'id': len(tarefas) + 1, 'descricao': descricao, 'status': '[ ]'}
    tarefas.append(nova_tarefa)
    print("--- Tarefa registrada ---")

def marcar_tarefa_realizada():
    id_tarefa = int(input("Digite o ID da tarefa realizada: "))
    for tarefa in tarefas:
        if tarefa ['id'] == id_tarefa and tarefa['status'] == '[ ]':
            tarefa['status'] = '[x]'
            tarefas.remove(tarefa)
            tarefas.insert(0, tarefa)
            print("--- Tarefa realizada e colocada no início da lista ---")
            return
        print("Tarefa não encontrada ou realizada.")

def editar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que quer editar: "))
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            nova_descricao == input("Digite a nova descrição da tarefa: ").capitalize()
            tarefa['descricao'] = nova_descricao
            print("--- Tarefa editada com sucesso ---")
            return
        print("Tarefa não encontrada.")


while True:
    print("\n ---------- To do List ----------")
    print("1. Listar tarefas")
    print("2. Registrar nova tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("5. Sair")

    opcao = input("Escolhe uma opção: ")
    
    if opcao == '1':
        listar_tarefas()
    elif opcao == '2':
        registrar_tarefa()
    elif opcao == '3':
        marcar_tarefa_realizada()
    elif opcao == '4':
        editar_tarefa()
    elif opcao == '5':
        print("---------- Saindo do aplicativo To do List ----------")
        break
    else:
        print("Opção inválida. Tente novamente.")
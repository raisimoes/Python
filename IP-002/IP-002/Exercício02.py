import json

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
        return tarefas
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo)

def listar_tarefas():
    for tarefa in tarefas:
        print(f"{tarefa['id']}. {tarefa['descricao']} {tarefa['status']}")

def registrar_tarefa():
    descricao = input("Digite a descrição da tarefa: ").capitalize()
    nova_tarefa = {'id': len(tarefas) + 1, 'descricao': descricao, 'status': '[ ]'}
    tarefas.append(nova_tarefa)
    print("Tarefa registrada!!!")

def marcar_tarefa_realizada():
    id_tarefa = int(input("Digite o ID da tarefa que foi realizada: "))
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa and tarefa['status'] == '[ ]':
            tarefa['status'] = '[x]'
            tarefas.remove(tarefa)
            tarefas.insert(0, tarefa)
            print("Tarefa realizada e movida para o início da lista!!!")
            return
    print("Tarefa não encontrada ou já realizada.")

def editar_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja editar: "))
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
            tarefa['descricao'] = nova_descricao
            print("Tarefa editada com sucesso!!!")
            return
    print("Tarefa não encontrada.")

tarefas = carregar_tarefas()

while True:
    print("\n===== ToDoList =====")
    print("1. Listar Tarefas")
    print("2. Registrar Nova Tarefa")
    print("3. Marcar Tarefa como Realizada")
    print("4. Editar Tarefa")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        listar_tarefas()
        
    elif opcao == '2':
        registrar_tarefa()
        salvar_tarefas(tarefas)

    elif opcao == '3':
        marcar_tarefa_realizada()
        salvar_tarefas(tarefas)

    elif opcao == '4':
        editar_tarefa()
        salvar_tarefas(tarefas)

    elif opcao == '5':
        print("Saindo do aplicativo ToDoList. Até logo!")
        salvar_tarefas(tarefas)
        break
    else:
        print("Opção inválida. Tente novamente.")

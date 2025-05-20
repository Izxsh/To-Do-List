import json
import os

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def listar_tarefas(tarefas):
    print("\n Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa adicionada ainda.\n")
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{i}. {status} {tarefa['descricao']}")
    print()

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da nova tarefa: ")
    tarefas.append({"descricao": descricao, "concluida": False})
    salvar_tarefas(tarefas)
    print(" Tarefa adicionada!\n")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        idx = int(input("Digite o número da tarefa concluída: ")) - 1
        tarefas[idx]["concluida"] = True
        salvar_tarefas(tarefas)
        print(" Tarefa marcada como concluída!\n")
    except (ValueError, IndexError):
        print(" Número inválido!\n")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        idx = int(input("Digite o número da tarefa para remover: ")) - 1
        tarefa_removida = tarefas.pop(idx)
        salvar_tarefas(tarefas)
        print(f" Tarefa '{tarefa_removida['descricao']}' removida!\n")
    except (ValueError, IndexError):
        print(" Número inválido!\n")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("===== To-DO list =====")
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Marcar como concluída")
        print("4 - Remover tarefa")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_tarefas(tarefas)
        elif escolha == "2":
            adicionar_tarefa(tarefas)
        elif escolha == "3":
            marcar_concluida(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            print(" Finalizado!")
            break
        else:
            print(" Opção inválida!\n")

if __name__ == "__main__":
    menu()

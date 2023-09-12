from todolist import ListaEncadeada

def main():

    lista = ListaEncadeada()

    # Menu
    while True:
        print("1 - Adicionar uma tarefa")
        print("2 - Excluir uma tarefa")
        print("3 - Alterar uma tarefa")
        print("4 - Listar as tarefas")
        print("0 - Sair")

        try:
            escolha = int(input("Escolha pelo indice: "))
        except:
            print("Valor incorreto, tente novamente!")
            continue

        if escolha == 1:
            valor = input("Digite a descrição da tarefa: ")
            lista.adicionar(valor)

        elif escolha == 2:
            lista.listar()
            indice = int(input("Digite o índice da tarefa que deseja excluir: "))
            lista.excluir(indice)

        elif escolha == 3: 
            lista.listar()
            indice = int(input("Digite o índice da tarefa que deseja alterar: "))
            novo_valor = input("Digite a nova descrição da tarefa: ")
            lista.alterar(indice, novo_valor)

        elif escolha == 4:
            lista.listar()

        elif escolha == 0:
            break

if __name__ == "__main__":
    main()
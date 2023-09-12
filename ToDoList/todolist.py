from nodo import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    # Adiciona no fim
    def adicionar(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = novo
        self.tamanho += 1

    # Exclui pelo índice
    def excluir(self, indice):
        if indice < 0 or indice >= self.tamanho:
            return
        if indice == 0:
            self.inicio = self.inicio.proximo
        else:
            aux = self.inicio
            i = 0
            while i < indice - 1:
                aux = aux.proximo
                i += 1
            aux.proximo = aux.proximo.proximo
        self.tamanho -= 1

    # Altera uma tarefa
    def alterar(self, indice, novo_valor):
        if indice < 0 or indice >= self.tamanho:
            return
        aux = self.inicio
        for i in range(indice):
            aux = aux.proximo
        aux.valor = novo_valor

    # Lista as tarefas
    def listar(self):
        print("-------- TAREFAS -----------")
        if self.inicio == None:
            print("Lista Vazia!")            
        else:    
            aux = self.inicio
            i = 0
            while aux is not None:
                print(f"{i} - {aux.valor}")
                aux = aux.proximo
                i += 1
        print("--------------------------")



# Programa de Lista de Presentes de Casamento

def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar presente")
    print("2. Ver todos os presentes")
    print("3. Remover presente")
    print("4. Sair")

def adicionar_presente(lista):
    presente = input("Digite o nome do presente: ")
    lista.append(presente)
    print(f"{presente} foi adicionado à lista.")

def ver_presentes(lista):
    if lista:
        print("\nLista de Presentes:")
        for i, presente in enumerate(lista, 1):
            print(f"{i}. {presente}")
    else:
        print("A lista de presentes está vazia.")

def remover_presente(lista):
    ver_presentes(lista)
    if lista:
        try:
            indice = int(input("Digite o número do presente a ser removido: "))
            if 0 < indice <= len(lista):
                removido = lista.pop(indice - 1)
                print(f"{removido} foi removido da lista.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    lista_presentes = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_presente(lista_presentes)
        elif escolha == '2':
            ver_presentes(lista_presentes)
        elif escolha == '3':
            remover_presente(lista_presentes)
        elif escolha == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

#if __name__ == "__main__":
    #main()
import random
import time


def merge_sort(lista, mostrar=False, nivel=0):
    if len(lista) > 1:
        meio = len(lista) // 2

        esquerda = lista[:meio]
        direita = lista[meio:]

        if mostrar:
            print("  " * nivel + f"Dividindo: {lista}")

        merge_sort(esquerda, mostrar, nivel + 1)
        merge_sort(direita, mostrar, nivel + 1)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

        if mostrar:
            print("  " * nivel + f"Juntando: {lista}")


def quick_sort(lista, inicio, fim, mostrar=False):
    if inicio < fim:
        pivo = lista[fim]
        i = inicio - 1

        if mostrar:
            print(f"\nArray atual: {lista}")
            print(f"Escolhendo pivô: {pivo}")

        for j in range(inicio, fim):
            if lista[j] <= pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]

                if mostrar:
                    print(f"Troca: {lista}")

        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]

        posicao = i + 1

        if mostrar:
            print(f"Pivô {pivo} posicionado: {lista}")

        quick_sort(lista, inicio, posicao - 1, mostrar)
        quick_sort(lista, posicao + 1, fim, mostrar)


def main():
    print("===== TESTE DE ALGORITMOS DE ORDENACAO =====")

    tamanho = int(input("Digite o tamanho do array: "))

    if tamanho <= 0:
        print("Digite um tamanho maior que zero!")
        return

    lista = [random.randint(0, 100000) for _ in range(tamanho)]

    print("\nArray original:")
    print(lista)

    print("\nEscolha o algoritmo:")
    print("1 - Merge Sort")
    print("2 - Quick Sort")

    opcao = input("Opcao: ")

    print("\nDeseja visualizar o passo a passo?")
    print("1 - Sim")
    print("2 - Nao")

    visualizar = input("Opcao: ")

    mostrar = visualizar == "1"

    lista_ordenada = lista.copy()

    inicio = time.perf_counter()

    if opcao == "1":
        algoritmo = "Merge Sort"
        merge_sort(lista_ordenada, mostrar)

    elif opcao == "2":
        algoritmo = "Quick Sort"
        quick_sort(lista_ordenada, 0, len(lista_ordenada) - 1, mostrar)

    else:
        print("Opcao invalida!")
        return

    fim = time.perf_counter()

    tempo = fim - inicio

    print("\n===== RESULTADO =====")
    print("Algoritmo utilizado:", algoritmo)
    print("Array ordenado:")
    print(lista_ordenada)
    print(f"Tempo de execucao: {tempo:.8f} segundos")


main()

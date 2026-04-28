"""
Exercício: Remover duplicatas
Dificuldade: Fácil
Tópico: Listas

Problema: Dada uma lista, retorne uma nova lista sem elementos repetidos,
mantendo a ordem de aparição.

Exemplos:
    Entrada: [1, 2, 2, 3, 4, 4, 5]
    Saída:   [1, 2, 3, 4, 5]

    Entrada: [1, 1, 1]
    Saída:   [1]

    Entrada: [1, 2, 3]
    Saída:   [1, 2, 3]

    Entrada: []
    Saída:   []
"""

def remove_duplicates(lst: list) -> list:
    new_list = []

    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list

# Manual tests
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
    print(remove_duplicates([1, 1, 1]))               # [1]
    print(remove_duplicates([1, 2, 3]))               # [1, 2, 3]
    print(remove_duplicates([]))                      # []
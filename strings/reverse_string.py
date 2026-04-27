"""
Exercício: Inverter uma string
Dificuldade: Fácil
Tópico: Strings

Problema: Dada uma string, retorne-a invertida sem usar [::-1].

Exemplo:

Entrada: "Python"

Saída: "nohtyP"
"""

def reverse_string(s: str) -> str:
    text = ""

    for i in range(len(s) - 1, -1, -1):
        n = s[i]
        text += n

    return text


# Testes manuais
if __name__ == "__main__":
    print(reverse_string("Python"))  # nohtyP
    print(reverse_string("abcd"))    # dcba
    print(reverse_string(""))        # (vazio)
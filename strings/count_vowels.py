"""
Exercício: Contar vogais
Dificuldade: Fácil
Tópico: Cadeias de caracteres

Problema: Dada cadeia de caracteres, retorne o número de vogais nela.

Considere letras maiúsculas e minúsculas como vogais.

Exemplos:
    Entrada: "Python"
    Saída: 1

    Entrada: "arara"
    Saída: 3

    Entrada: "sky"
    Saída: 0

    Entrada: ""
    Saída: 0
"""

def count_vowels(s: str) -> int:
    s = s.strip().lower()
    vowels = "aeiou"
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1

    return count

# Testes manuais
if __name__ == "__main__":
    print(count_vowels("Python"))  # 1
    print(count_vowels("arara"))   # 3
    print(count_vowels("sky"))     # 0
    print(count_vowels(""))        # 0
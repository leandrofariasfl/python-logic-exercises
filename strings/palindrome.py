"""
Exercício: Verificação de palíndromo
Dificuldade: Fácil
Tópico: Cadeias de caracteres

Problema: Dada cadeia de caracteres, retorne Verdadeiro se ela for um palíndromo, Falso caso contrário.

Um palíndromo é uma palavra que se lê da mesma forma de trás para frente.

Regra: não use [::-1].

Exemplos:
    Input:  "arara"
    Output: True

    Input:  "python"
    Output: False

    Input:  "a"
    Output: True

    Input:  ""
    Output: True
"""
# Minha solução
def is_palindrome(s: str) -> bool:
    chars = []
    s = s.strip().lower()

    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])

    return s == "".join(chars)

# Solução aprendida
def is_palindrome_efficient(s: str) -> bool:
    s = s.strip().lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# Testes manuais
if __name__ == "__main__":
    print(is_palindrome("arara"))   # True
    print(is_palindrome("python"))  # False
    print(is_palindrome("a"))       # True
    print(is_palindrome(""))        # True
    print("__________________________________")
    print(is_palindrome_efficient("arara"))   # True
    print(is_palindrome_efficient("python"))  # False
    print(is_palindrome_efficient("a"))       # True
    print(is_palindrome_efficient(""))        # True
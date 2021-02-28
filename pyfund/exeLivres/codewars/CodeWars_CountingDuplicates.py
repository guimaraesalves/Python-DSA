# Conte o número de duplicados
# Escreva uma função que retornará a contagem de caracteres alfabéticos
# distintos que não diferenciam maiúsculas de minúsculas e dígitos numéricos
# que ocorrem mais de uma vez na string de entrada.
# Pode-se presumir que a string de entrada
# contém apenas letras (maiúsculas e minúsculas) e dígitos numéricos.

# Exemplo
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibilidade" -> 1 # 'i' occurs six times
# "Indivisibilidades" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur



def duplicate_count(text):
    text = text.lower()
    count = {i: text.count(i) for i in set(text)}
    count = sorted(count.values())
    result = 0
    for i in count:
        if i > 1:
            result += 1
    return result

print(duplicate_count('abbAACcatEE'))
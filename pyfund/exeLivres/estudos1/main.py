# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print('-' * 30)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Olá, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Mundo!! Me Ajuda por favor!!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 1 Funções
''' 
1. Crie uma função potencia que receba dois números a e b (base e expoente,
respectivamente) e retorne a elevado a b!
'''

print('-' * 30)
print()
print()
print('1 . FUNÇÕES:')
print()
print('-' * 30)


def potencia(base, expoente):
    resposta = base ** expoente
    return resposta


print('Resposta do Exercício 1: ', potencia(3, 3))
print('-' * 30)

'''
2. Crie uma função que permita a conversão de graus Celsius para Fahrenheit.
'''


def celsius2fahrenheit(graus):
    return 9 / 5.0 * graus + 32


print('Resposta do Exercício 2: ', celsius2fahrenheit(1))
print('-' * 30)

'''
3. Crie uma função numero_par que permita verificar um dado número, x,
passado como parâmetro é um número par.
'''


def numero_par(x):
    if x % 2 == 0:
        return print('Número Par!')
    else:
        return print('Número Impar!')


print('Resposta do Exercício 3:')
numero_par(5.5)
print('-' * 30)

'''
4. Dadas as seguintes funções:
'''


def equacao1(p, q):
    r1 = p + q
    r2 = p - q
    return r1 * r2


def equacao2(r, s):
    return r ** 2 - s ** 2


print('Respostas do Exercício 4: ')
print(equacao1(3, 4))
print(equacao1(4, 3))
print(2 ** equacao2(2, 0))
print(equacao1(0, 2) + equacao2(0, 4))
print(equacao1(9, 99) - equacao2(9, 99))
print('-' * 30)

'''
5. Dadas as seguintes funções:
'''


def numero_par1(x):
    if x % 2 == 0:
        return True
    else:
        return False


def funcaoX(a, b):
    if numero_par1(a):
        return a - b
    else:
        return a - 2 * b


print('Respostas do Exercício 5: ')
print(funcaoX(0, 20))
print(funcaoX(20, 3))
print(funcaoX(3, 20))
print(numero_par1(1) + numero_par1(2))
print(numero_par1(4) * funcaoX(1, funcaoX(2, 3)))
print('-' * 30)

print('2 . DESVIO CONDICIONAL:')
print()
print('-' * 30)
'''
6. Crie uma função em que, dados 3 números como parâmetros, permita 
verificar se a soma de quaisquer par de números gera a soma do terceiro nº:
'''


def verificar_somatoria(a, b, c):
    if a + b == c:
        return str(a) + ' + ' + str(b) + ' = ' + str(c)
    if a + c == b:
        return str(a) + ' + ' + str(c) + ' = ' + str(b)
    if b + c == a:
        return str(b) + ' + ' + str(c) + ' = ' + str(a)


print('Respostas do Exercício 6: ')
print(verificar_somatoria(3, 9, 6))
print('-' * 30)


'''
7. Crie uma função determinar_o_maior_numero que receba dois números
(inteiros ou reais) e retorne o maior valor de ambos os números.
'''
def retorna_o_maior_numero(x, y):
    if x > y:
        return x
    else:
        return y

print('Respostas do Exercício 7: ')
print(retorna_o_maior_numero(3, 5))
print('-' * 30)

'''
8. Crie uma função determinar_maior_numero que receba três números
(inteiros ou reais) e retorne o maior valor dos números.
'''
def determinar_maior_numero(a, b, c):
    if a < b:
        if b < c:
            return c
        else:
            return b
    else:
        if a < c:
            return c
        else:
            return a

print('Respostas do Exercício 8: ')
print(determinar_maior_numero(3, 0, 1))
print('-' * 30)

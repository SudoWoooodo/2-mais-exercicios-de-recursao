


def fatorial(n):
    if n == 0:
        return 1
    
    return n * fatorial(n-1)


def somatorio(n):
    if n == 1:
        return 1

    return n + somatorio(n-1)


def fibo(n):
    if n <= 1:
        return n
    
    return fibo(n-1) + fibo(n-2)


def soma(k, j):
    if j == k:
        return k

    return k + soma(k + 1, j)


def palindromo(s):
    if len(s) == 0:
        return True

    elif len(s) == 1:
        return True

    return s[0] == s[-1] and palindromo(s[1:-1])


def binario(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'

    return binario(n//2) + str(n%2)


def somatorio_array(array):
    if len(array) == 1:
        return array[0]

    return array[0] + somatorio_array(array[1:])


def maior_lista(array):
    if len(array) == 1:
        return array[0]

    a = maior_lista(array[1:])

    return array[0] if array[0] > a else a


def dentro(string, substring):
    if len(substring) == 0:
        return False

    if len(string) < len(substring):
        return False

    if string[:len(substring)] == substring:
        return True

    return  dentro(string[1:], substring)


def quantidade_inteiros(n):
    if n < 1:
        return 0

    return 1 + quantidade_inteiros(n / 10)


def permutacoes(string):
    if len(string) == 1:
        return string

    perm = [] 
    for letter in string:
        resto = ''.join([l for l in string if l != letter])

        for p in permutacoes(resto):
            perm.append(top_letter + p)

    return perm

print(fatorial(4))
print(somatorio(4))
print(fibo(6))
print(soma(5, 10))
print(palindromo('arara'))
print(palindromo('arar'))
print(binario(16))
print(somatorio_array([1,2,3,4]))
print(maior_lista([1, 3, 5, 11, 7, 9]))
print(dentro('perdi meu onibus', 'meu'))
print(dentro('perdi meu onibus', ''))
print(quantidade_inteiros(19642))
print(permutacoes('abc'))



"""
abc
bca
cab
abc
acb
cba
bac

"""
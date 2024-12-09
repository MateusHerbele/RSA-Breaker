import math
import os

'''
Cria uma matriz até o valor de n, e preenche a matriz com True.
Para cada número primo, verifica se é primo e marca todos os múltiplos como False.
Retorna uma lista com os números primos até n.
'''
def crivoEratostenes(n):
    if n < 2:
        return []
    crivo = [True] * (n + 1)
    crivo[0] = crivo[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if crivo[i]:
            for j in range(i * i, n + 1, i):
                crivo[j] = False
    return [i for i in range(2, n + 1) if crivo[i]]


'''
Fatora um número n em seus fatores primos.
Retorna uma lista com os fatores primos de n.
'''
def fatorar(n):
    fatores = []
    for primo in crivoEratostenes(n):
        while n % primo == 0:
            fatores.append(primo)
            n //= primo # Faz a divisão inteira de n por primo
    return fatores

'''
Quebra o valor de n em seus fatores primos p e q.
Retorna p e q.
Caso o número de fatores seja diferente de 2, o valor de n é inválido.
'''
def quebrarPeQ(n):
    fatores = fatorar(n)
    if len(fatores) == 2:
        p = fatores[0]
        q = fatores[1]
        print(f"Valor de P: {p}")
        print(f"Valor de Q: {q}")
        return p, q

    print("Valor de N inválido.")
    exit()

'''
Super simples.
Para cada valor de d, verifica se (d * e) % r == 1.
Caso seja verdade, retorna d.
Nunca chega até r, pois o valor de d é sempre menor que r.
'''
def quebrarD(r, e):
    for d in range(1, r):
        if (d * e) % r == 1:
            return d
    return None

'''
Faz a operação de descriptografar o texto cifrado.
(Cifrado)^d % n
'''
def descriptografar(texto_cifrado, d, n):
    texto_descriptografado = pow(int(texto_cifrado), d) % n 
    return texto_descriptografado

def main():
    texto_cifrado = input("Digite o texto cifrado: ")
    n = int(input("Digite o valor de N associado a chave: "))
    p, q = quebrarPeQ(n)
    r = (p - 1) * (q - 1)
    print(f"Valor de R: {r}")
    e = int(input("Digite o valor de E associado a chave: "))
    d = quebrarD(r, e)
    print(f"Valor de D (Chave Privada): {d}")
    print(f"Texto descriptografado: {descriptografar(texto_cifrado, d, n)}")
    
if __name__ == "__main__":
    main()
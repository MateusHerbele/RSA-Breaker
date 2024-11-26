import math
import os
import sys

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


def fatorar(n):
    fatores = []
    for primo in crivoEratostenes(n):
        while n % primo == 0:
            fatores.append(primo)
            n //= primo
    return fatores

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


def quebrarD(r, e):
    for d in range(1, r):
        if (d * e) % r == 1:
            return d
    return None

def descriptografar(texto_cifrado, d, n):
    with open(texto_cifrado, "r") as arquivo:
        texto = arquivo.read()
    texto_descriptografado = pow(int(texto), d, n)
    with open(os.path.join(os.path.dirname(__file__), "texto_descriptografado.txt"), "w") as arquivo:
        arquivo.write(str(texto_descriptografado))

    return texto_descriptografado
def main():
    texto_cifrado = os.path.join(os.path.dirname(__file__), "texto_cifrado.txt")
    n = int(input("Digite o valor de N associado a chave: "))
    p, q = quebrarPeQ(n)
    e = int(input("Digite o valor de E associado a chave: "))
    r = (p - 1) * (q - 1)
    print(f"Valor de R: {r}")
    d = quebrarD(r, e)
    print(f"Valor de D: {d}")
    texto_descriptografado = descriptografar(texto_cifrado, d, n)
    print(f"Texto descriptografado: {texto_descriptografado}")


if __name__ == "__main__":
    main()
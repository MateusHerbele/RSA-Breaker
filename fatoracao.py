def verifica_primo(p):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(3, p, 2):
        if p % i == 0:
            return False
    return True
    
# n é um produto entre dois primos p e q diferentes entre si e maiores que 1 e menores que 1024
# o maior valor que é 1021 * 1019 = 1040399
n = input("Digite n:\n")
n = int(n)
p = 1
q = 1

for i in range(2, 1024):
    if verifica_primo(i):
        if n % i == 0:
            if p == 1:
                p = i
            else:
                q = i


print("p = ", p)
print("q = ", q)
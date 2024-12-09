# criptografia-T2
Criptografia T2

#  RSA BREAKER

Este trabalho é um **descriptografador RSA** que utiliza conceitos básicos de números primos e aritmética modular para realizar a quebra de chaves privadas RSA, sabendo os valores da chave pública PU = {e, n} e que os primos (p e q) que multiplicados forma n são menores que 1024 bits.

## Estrutura do Código

### 1. `crivoEratostenes(n)`

**Descrição:**
Cria uma lista de números primos até o valor de `n`, utilizando o algoritmo do Crivo de Eratóstenes.

**Funcionamento:**
- Inicializa uma matriz preenchida com `True`.
- Para cada número primo encontrado, marca todos os seus múltiplos como `False`.
- Retorna uma lista contendo apenas os números marcados como primos.

**Entrada:**
- `n`: Limite superior até onde os números primos serão calculados.

**Saída:**
- Lista com números primos até `n`.

---

### 2. `fatorar(n)`

**Descrição:**
Fatora um número `n` em seus fatores primos.

**Funcionamento:**
- Utiliza a lista de números primos gerada pelo `crivoEratostenes`.
- Divide o número `n` pelos primos encontrados até que o quociente seja 1.
- Retorna uma lista com os fatores primos.

**Entrada:**
- `n`: Número a ser fatorado.

**Saída:**
- Lista com os fatores primos de `n`.

---

### 3. `quebrarPeQ(n)`

**Descrição:**
Quebra o valor de `n` em seus dois fatores primos `p` e `q`.

**Funcionamento:**
- Fatora `n` utilizando a função `fatorar`.
- Verifica se o número de fatores primos é exatamente 2.
  - Se sim, retorna os valores de `p` e `q`.
  - Caso contrário, imprime uma mensagem de erro e encerra o programa.

**Entrada:**
- `n`: Número composto utilizado na chave pública RSA.

**Saída:**
- `p`, `q`: Os dois fatores primos de `n`.

---

### 4. `quebrarD(r, e)`

**Descrição:**
Calcula a chave privada `d` para descriptografar o texto cifrado.

**Funcionamento:**
- Para cada valor de `d` entre 1 e `r`, verifica se `(d * e) % r == 1`.
- Retorna o valor de `d` correspondente.

**Entrada:**
- `r`: Valor de `(p - 1) * (q - 1)`.
- `e`: Exponente público da chave RSA.

**Saída:**
- `d`: Exponente privado da chave RSA.

---

### 5. `descriptografar(texto_cifrado, d, n)`

**Descrição:**
Realiza a descriptografia de um texto cifrado utilizando a fórmula `(Cifrado)^d % n`.

**Funcionamento:**
- Eleva o texto cifrado à potência `d` e calcula o módulo `n`.
- Retorna o texto descriptografado.

**Entrada:**
- `texto_cifrado`: Texto cifrado em formato numérico.
- `d`: Chave privada.
- `n`: Número composto da chave pública RSA.

**Saída:**
- Texto descriptografado.

---

### 6. `main()`

**Descrição:**
Função principal que orquestra as etapas de descriptografia.

**Funcionamento:**
1. Recebe o texto cifrado e os valores de `n` e `e` associados à chave pública.
2. Calcula `p` e `q` a partir de `n`.
3. Calcula `r = (p - 1) * (q - 1)`.
4. Determina o valor de `d` (chave privada).
5. Utiliza `d` para descriptografar o texto cifrado.
6. Exibe o texto descriptografado.

**Entrada:**
- Interativa, via `input()` para `texto_cifrado`, `n` e `e`.

**Saída:**
- Texto descriptografado e valores intermediários exibidos no console.

---

## Como Executar
   ```bash
   python3 descriptografador_rsa.py
   ```

---
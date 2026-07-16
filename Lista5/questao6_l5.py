# Soma de dígitos (Etapa 2 — Índice do Presságio)
def soma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)


def obter_soma_ajustada(n):
    s = soma_digitos(n)

    if s < 2:
        return 2

    return s

#verifica se algum resultado já foi calculado
def buscar_memo(memo, n, k, i):

    if i < 0:
        return -1

    if memo[i][0] == n and memo[i][1] == k:
        return memo[i][2]

    return buscar_memo(memo, n, k, i - 1)

#Evita que fique vários valores, se verificou elimina
def limitar_memo(memo):
    if len(memo) > 300:
        memo.pop(0)


# Fatorial Caótico (Etapa 1)
def fato(n, memo_fat):

    valor_salvo = buscar_memo(memo_fat, n, 0, len(memo_fat) - 1)

    if valor_salvo != -1:
        return valor_salvo

    if n <= 1:
        resultado = 1

    elif n % 2 == 0:
        resultado = (n * fato(n // 2, memo_fat)) % 500

    else:
        resultado = (n + fato(n - 1, memo_fat)) % 500

    memo_fat.append([n, 0, resultado])
    limitar_memo(memo_fat)

    return resultado


# Fibonacci Generalizado (Etapa 4)
def fibon(n, k, memo_fib):

    valor_salvo = buscar_memo(memo_fib, n, k, len(memo_fib) - 1)

    if valor_salvo != -1:
        return valor_salvo

    if n == 0:
        resultado = 0

    elif n < k:
        resultado = 1

    else:

        def soma(i):
            if i > k:
                return 0

            return (fibon(n - i, k, memo_fib) + soma(i + 1)) % 500

        resultado = soma(1)

    memo_fib.append([n, k, resultado])
    limitar_memo(memo_fib)

    return resultado

# Primalidade (Etapa 5)
def se_primo(n, divisor=2):

    if n <= 1:
        return 0

    if divisor * divisor > n:
        return 1

    if n % divisor == 0:
        return 0

    return se_primo(n, divisor + 1)


# Formatação
def preencher_zeros(texto):

    if len(texto) >= 3:
        return texto

    return preencher_zeros("0" + texto)


def formatar(numero):
    return preencher_zeros(str(numero))


# Processamento principal
def processar_numero(n, memo_fat, memo_fib):

    sinal = fato(n, memo_fat) % 500

    indice = obter_soma_ajustada(sinal)

    memorias = obter_soma_ajustada(indice)

    eco = fibon(indice, memorias, memo_fib) % 500

    significado = sinal + eco

    if se_primo(significado):
        julgamento = "SEGURO"
    else:
        julgamento = "PERIGOSO"

    print(f"Numero {formatar(n)} | "
        f"Sinal = {formatar(sinal)} | "
        f"Indice = {formatar(indice)} | "
        f"Memorias = {formatar(memorias)} | "
        f"Eco das Luzes = {formatar(eco)} | "
        f"Julgamento: {julgamento}")


# Percorrer lista 
def percorrer_lista(lista, memo_fat, memo_fib, indice=0):

    if indice >= len(lista):
        return

    processar_numero(lista[indice], memo_fat, memo_fib)

    percorrer_lista(lista, memo_fat, memo_fib, indice + 1)


# Converter entrada
def converter_fun(entrada):

    texto = entrada.replace("[", "").replace("]", "")

    def criar_lista(inicio=0):

        pos_virgula = texto.find(",", inicio)

        if pos_virgula == -1:
            return [int(texto[inicio:].strip())]

        atual = int(texto[inicio:pos_virgula].strip())

        return [atual] + criar_lista(pos_virgula + 1)

    return criar_lista()


# código principal
entrada = input()

lista_numeros = converter_fun(entrada)

memo_fat = []
memo_fib = []

percorrer_lista(lista_numeros, memo_fat, memo_fib)
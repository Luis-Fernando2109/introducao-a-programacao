n = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(1, n + 1):
    fatorial = 1
    for j in range(1, i + 1):
        fatorial = fatorial * j
    soma += fatorial

print("A soma dos fatoriais de 1 até", n, "é:", soma)

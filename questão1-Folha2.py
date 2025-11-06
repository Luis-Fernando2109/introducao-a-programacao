numero = input("Digite um número: ")

soma_impares = 0

for digito in numero:
    d = int(digito)
    if d % 2 != 0:
        soma_impares += 1

fatorial = 1
for i in range(1, soma_impares + 1):
    fatorial = fatorial * i

print("Quantidade de dígitos ímpares:", soma_impares)
print("Fatorial dessa quantidade é:", fatorial)

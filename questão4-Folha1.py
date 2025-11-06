maior_peso_masculino=0
nome_pesado_masculino=""

maior_altura_feminina=0
nome_altura_feminina=""

soma_idades=0
quantidade_atletas=0

nome=""
while nome !="@":
    nome = input("Nome do atleta (@ para encerrar): ")
    if nome == "@":
        break

    sexo = input("Sexo (M/F): ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    soma_idades += idade
    quantidade_atletas += 1

    if sexo == "M" or sexo == "m":
        if peso > maior_peso_masculino:
            maior_peso_masculino = peso
            nome_pesado_masculino = nome

    if sexo == "F" or sexo == "f":
        if altura > maior_altura_feminina:
            maior_altura_feminina = altura
            nome_altura_feminina = nome

print("=== RESULTADOS ===")

if nome_pesado_masculino != "":
    print("Atleta masculino com maior peso:", nome_pesado_masculino, "com", maior_peso_masculino, "kg")
else:
    print("Nenhum atleta masculino foi cadastrado.")

if nome_altura_feminina != "":
    print("Atleta feminina com maior altura:", nome_altura_feminina, "com", maior_altura_feminina, "m")
else:
    print("Nenhuma atleta feminina foi cadastrada.")

if quantidade_atletas > 0:
    media_idade = soma_idades / quantidade_atletas
    print("Média de idade dos atletas:", media_idade, "anos")
else:
    print("Nenhum atleta foi cadastrado.")

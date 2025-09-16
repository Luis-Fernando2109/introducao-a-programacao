quant_jogadores = int(input("Digite o número de jogadores: "))
soma_altura = 0
a=0
while a!=quant_jogadores:
    a+=1
    altura = float(input(f"Digite a altura do jogador {a} (em metros): "))
    soma_altura += altura

media = soma_altura / quant_jogadores
print(f"A altura média do time é: {media:.2f} m")


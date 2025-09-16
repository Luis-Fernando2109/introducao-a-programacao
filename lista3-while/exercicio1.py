soma_positivos = 0
quant_negativos = 0
A=0
while A!=20:
    A+=1
    num = int(input(f"Digite o {A}º número: "))
    if num >= 0:
        soma_positivos += num
    else:
        quant_negativos += 1

print("Soma dos números positivos:", soma_positivos)
print("Quantidade de números negativos:", quant_negativos)           
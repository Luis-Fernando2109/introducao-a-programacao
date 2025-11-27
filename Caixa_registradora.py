preço_total = 0
quantidade_produtos = 0
media = 0
mais_caro = 0
compra = 0
preço = 0
while compra!= 1:
    preço = float(input("Preço do produto: "))
    if preço>0:
        preço_total += preço
        quantidade_produtos += 1
        media += preço
        if mais_caro<preço:
            mais_caro=preço
        print("Salvo...")
        a = str(input("Quer continuar? (s/n)"))
        if a== "n" :
            compra = 1
    else:
        print("Digite um valor positivo...")

print("----------------------------------\nFicou no total de:","R$",preço_total)
print("A quantidade de produtos:",quantidade_produtos)
print("A media de preço foi",media/quantidade_produtos)
print("o produto mais caro foi:","R$",mais_caro)


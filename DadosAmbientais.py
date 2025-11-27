temp = 0
temp_max = 0
temp_min = 200000
acima_30 = 0
abaixo_15 = 0
media = 0
N = int(input("Quantas leituras de temperatura serão analisadas? "))
for i in range (1,N+1):
    temp = float(input("Digite a temperatura em C°: "))
    
    if temp>temp_max:
        temp_max=temp
    if temp<temp_min:
        temp_min=temp
    media += temp

    if temp>30:
        acima_30 += 1 

    if temp<15:
        abaixo_15 += 1 

print("A maior temperatura foi:",temp_max)
print("A menor temperatura foi:",temp_min)
print("A media de temperatura foi:",(media/N))
print("A quantidade de temperatura acima de 30:",acima_30)
print("A quantidade de temperatura abaixo de 15:",abaixo_15)


    
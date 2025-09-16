num = int(input("Digite um número para verificar se é primo: "))
if num<=1:
    print("o numero",num,"não é primo")
else:
    divisor=2
    while divisor <= num // 2:
        if num % divisor ==0:
            print("o numero",num,"não é primo")
            break
        divisor +=1
    else:
        print("o numero",num,"é primo")

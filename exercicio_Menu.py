import os
print(">>M E N U   D E   O P E R A Ç Õ E S   M A T E M Á T I C A S<< \n *********************************************************** \n Soma - 1 \n Subtração - 2 \n Multiplicação - 3 \n Divisão - 4 \n Par ou impar - 5 \n Fatorial - 6 \n Primo ou não - 7 \n")
opção=input("Escolha a operação conforme o número indicado ou digite <SAIR> para sair:")
opçãomaiusc=opção.upper()
while opção!="SAIR":
    if opção=="1":
        num1=int(input("digite o 1º número: "))
        num2=int(input("digite o 2º número: "))
        print("o resulado da soma é: ",num1+num2)
    
    if opção=="2":
        num1=int(input("digite o 1º número: "))
        num2=int(input("digite o 2º número: "))
        print("o resulado da subtração é: ",num1-num2)
    
    if opção=="3":
        num1=int(input("digite o 1º número: "))
        num2=int(input("digite o 2º número: "))
        print("o resulado da multiplicação é: ",num1*num2)
    
    if opção=="4":
        num1=int(input("digite o 1º número: "))
        num2=int(input("digite o 2º número: "))
        print("o resulado da divisão é: ",num1/num2)
    
    if opção=="5":
        n=int(input("digite um numero para saber se ele é par ou impar: "))
        if n%2==0:
            print("o número é par.")
        else:
            print("o número é impar.")

    if opção=="6":
        num = int(input("Digite um número para calcular o fatorial: "))
        fatorial = 1
        cont=0
        while cont!=num:
            cont+=1
            fatorial*=cont

        print("o seu numero fatorado é",fatorial)

    if opção=="7":
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

    input("pressione <ENTER> para voltar para o MENU!")
    os.system("cls")
    print(">>M E N U   D E   O P E R A Ç Õ E S   M A T E M Á T I C A S<< \n *********************************************************** \n Soma - 1 \n Subtração - 2 \n Multiplicação - 3 \n Divisão - 4 \n Par ou impar - 5 \n Fatorial - 6 \n Primo ou não - 7 \n")
    opção=input("Escolha a operação conforme o número indicado ou digite <SAIR> para sair:")
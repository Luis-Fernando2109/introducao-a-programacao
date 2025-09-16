maior_media = 0
menor_media = 99
aprovados = 0
reprovados = 0
cont=0
while cont !=10:

    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    media = (n1 + n2 + n3) / 3
    
    
    if media>=6:
        print("este aluno está APROVADO")
        aprovados+=1


    else:
        print("este aluno está REPROVADO")
        reprovados+=1
    
    if media > maior_media:
        maior_media=media


print("a menor media é",menor_media)
print("a maior media é",maior_media)
print("são",aprovados,"alunos aprovados")
print("são",reprovados,"alunos reprovados")
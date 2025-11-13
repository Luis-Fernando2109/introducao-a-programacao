usuario=input("digite o usuário: ")
senha=int(input("digite a senha: "))
if usuario=="admin" and senha==1234:
    print("login bem-sucedido")
else:
    print("a senha ou usuario está incorreta")
